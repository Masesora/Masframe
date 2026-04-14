from fpdf import FPDF
from pathlib import Path
from typing import Optional
from ..onboarding.scanner_schema import ScannerOutput
import re


# ---------------------------------------------------------
# Función para eliminar emojis (evita error latin-1)
# ---------------------------------------------------------
def remove_emojis(text: str) -> str:
    return re.sub(r'[^\x00-\x7F]+', '', text)


# Carpeta donde se guardarán los PDFs generados
REPORTS_DIR = Path(__file__).resolve().parent / "generated_reports"
REPORTS_DIR.mkdir(exist_ok=True)


class ScannerPDF(FPDF):
    """
    Clase extendida para formatear el PDF del Documento 1 MAS.
    """
    def header(self):
        self.set_font("Arial", "B", 16)
        self.set_text_color(30, 36, 68)  # Azul Masesora
        self.cell(0, 10, "Informe Clínico Inicial - MASESORA", ln=True, align="C")
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.set_text_color(120, 120, 120)
        self.cell(0, 10, "© MASESORA - Sistema Clínico Empresarial", align="C")


def generate_scanner_pdf(data: ScannerOutput) -> str:
    """
    Genera el Documento 1 MAS en PDF.
    Devuelve la ruta del archivo generado.
    """

    pdf = ScannerPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)

    # ---------------------------------------------------------
    # 1. Datos generales
    # ---------------------------------------------------------
    pdf.set_font("Arial", "", 12)
    pdf.set_text_color(0, 0, 0)

    pdf.cell(0, 8, f"Empresa: {data.empresa}", ln=True)
    pdf.cell(0, 8, f"Código de activación: {data.codigo}", ln=True)
    pdf.ln(5)

    # ---------------------------------------------------------
    # 2. Especialidades evaluadas
    # ---------------------------------------------------------
    pdf.set_font("Arial", "B", 14)
    pdf.set_text_color(30, 36, 68)
    pdf.cell(0, 10, "Especialidades Evaluadas", ln=True)

    for esp in data.especialidades:
        pdf.ln(4)

        # Título de la especialidad (sin emojis)
        pdf.set_font("Arial", "B", 12)
        pdf.set_text_color(30, 36, 68)
        pdf.cell(
            0,
            8,
            remove_emojis(f"{esp.icon} {esp.nombre} ({esp.score}%) - {esp.categoria}"),
            ln=True
        )

        # Narrativa
        pdf.set_font("Arial", "", 11)
        pdf.set_text_color(0, 0, 0)
        pdf.multi_cell(0, 6, esp.narrativa)

        # Síntomas
        if esp.sintomas:
            pdf.set_font("Arial", "I", 10)
            pdf.set_text_color(80, 80, 80)
            pdf.multi_cell(
                0,
                6,
                "Síntomas detectados: " + ", ".join(esp.sintomas)
            )

    # ---------------------------------------------------------
    # 3. Presupuesto PIE / PRE
    # ---------------------------------------------------------
    pdf.ln(10)
    pdf.set_font("Arial", "B", 14)
    pdf.set_text_color(30, 36, 68)
    pdf.cell(0, 10, "Presupuesto PIE / PRE", ln=True)

    pdf.set_font("Arial", "", 12)
    pdf.set_text_color(0, 0, 0)

    pie = data.presupuesto.PIE
    pre = data.presupuesto.PRE

    pdf.cell(0, 8, f"PIE: {pie if pie is not None else 'No aplica'}", ln=True)
    pdf.cell(0, 8, f"PRE: {pre if pre is not None else 'No aplica'}", ln=True)

    if data.presupuesto.especialidades_incluidas:
        pdf.ln(3)
        pdf.set_font("Arial", "I", 11)
        pdf.set_text_color(80, 80, 80)
        pdf.multi_cell(
            0,
            6,
            "Especialidades incluidas en el presupuesto: " +
            ", ".join(data.presupuesto.especialidades_incluidas)
        )

    # ---------------------------------------------------------
    # 4. Guardar PDF
    # ---------------------------------------------------------
    filename = f"{data.codigo}_scanner.pdf"
    filepath = REPORTS_DIR / filename

    pdf.output(str(filepath))

    return str(filepath)