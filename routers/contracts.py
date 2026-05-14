from fastapi import APIRouter, HTTPException, status
from fastapi.responses import HTMLResponse
from datetime import datetime
from bson import ObjectId
import sys, os

from database.database import get_collection
from models.contract import Contract

# Templates
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from contracts.contrato_template import generar_contrato_html
from contracts.factura_template  import generar_factura_html

router = APIRouter(prefix="/contracts", tags=["contracts"])


# ============================================================
# HELPERS
# ============================================================

async def _get_client(codigo: str) -> dict:
    """Devuelve el documento del cliente o lanza 404."""
    col = get_collection("clients")
    doc = await col.find_one({"codigo": codigo})
    if not doc:
        raise HTTPException(status_code=404, detail=f"Cliente '{codigo}' no encontrado")
    return doc


def _build_datos(doc: dict) -> dict:
    """
    Mapea un documento de clients → datos dict para las plantillas.
    Los campos fiscales se almacenan con PATCH /clients/{codigo}
    desde ContractPaymentForm en el frontend.
    """
    return {
        "codigo":       doc.get("codigo", ""),
        "razon_social": doc.get("razon_social") or doc.get("empresa", ""),
        "cif":          doc.get("cif", ""),
        "representante":doc.get("representante") or doc.get("nombre", ""),
        "cargo":        doc.get("cargo", ""),
        "email":        doc.get("email", ""),
        "telefono":     doc.get("telefono", ""),
        "direccion":    doc.get("direccion", ""),
        "ciudad":       doc.get("ciudad", ""),
        "codigo_postal":doc.get("codigo_postal", ""),
        "plan":         doc.get("plan", "Plan MASFRAME®"),
        "sintomas":     doc.get("sintomas_contratados", []),
        "importe":      float(doc.get("importe", 0)),
        "fecha":        doc.get("fecha_activacion") or datetime.utcnow().strftime("%Y-%m-%d"),
    }


# ============================================================
# 1. GENERAR CONTRATO + FACTURA  (llamar tras pago Stripe)
# ============================================================

@router.post("/generar/{codigo}")
async def generar_documentos(codigo: str, payload: dict = {}):
    """
    Genera y persiste el contrato HTML y la factura HTML para un expediente.

    Body opcional:
      { "stripe_ref": "ch_xxx", "metodo_pago": "Tarjeta de crédito" }

    Guarda en collection 'contracts':
      { codigo, contrato_html, factura_html, generado_en, signed, signed_at }
    """
    doc = await _get_client(codigo)
    datos = 