from typing import Tuple, Literal

StatusColor = Literal["rojo", "ambar", "verde"]

# ==========================================================
# MOTOR CLÍNICO UNIVERSAL – FINANZAS S1–S10 IMPLEMENTADO
# ==========================================================

def _finanzas_s1(saldo_total: float, gastos_fijos_mes: float) -> Tuple[float, StatusColor]:
    if gastos_fijos_mes <= 0:
        return 9999, "verde"
    dias_vida = saldo_total / (gastos_fijos_mes / 30.0)
    if dias_vida < 15:
        return dias_vida, "rojo"
    elif dias_vida < 45:
        return dias_vida, "ambar"
    return dias_vida, "verde"


def _finanzas_s2(ventas_mes: float, compras_mes: float) -> Tuple[float, StatusColor]:
    if ventas_mes <= 0:
        return -100.0, "rojo"
    margen = (ventas_mes - compras_mes) / ventas_mes * 100.0
    if margen < 10:
        return margen, "rojo"
    elif margen < 20:
        return margen, "ambar"
    return margen, "verde"


def _finanzas_s3(total_facturado: float, total_cobrado: float) -> Tuple[float, StatusColor]:
    brecha = total_facturado - total_cobrado
    if brecha <= 0:
        return brecha, "verde"
    elif brecha <= 0.2 * total_facturado:
        return brecha, "ambar"
    return brecha, "rojo"


def _finanzas_s4(deuda_clientes: float, venta_mensual: float) -> Tuple[float, StatusColor]:
    if venta_mensual <= 0:
        return 9999.0, "rojo"
    venta_diaria = venta_mensual / 30.0
    dias_espera = deuda_clientes / venta_diaria
    if dias_espera > 90:
        return dias_espera, "rojo"
    elif dias_espera > 45:
        return dias_espera, "ambar"
    return dias_espera, "verde"


def _finanzas_s5(valor_almacen: float, salida_mes: float) -> Tuple[float, StatusColor]:
    if salida_mes <= 0:
        return 999.0, "rojo"
    meses_stock = valor_almacen / salida_mes
    if meses_stock > 6:
        return meses_stock, "rojo"
    elif meses_stock > 3:
        return meses_stock, "ambar"
    return meses_stock, "verde"


def _finanzas_s6(deuda_prov: float, compra_mes: float) -> Tuple[float, StatusColor]:
    if compra_mes <= 0:
        return 0.0, "rojo"
    compra_diaria = compra_mes / 30.0
    dias_aire = deuda_prov / compra_diaria
    if dias_aire < 15:
        return dias_aire, "rojo"
    elif dias_aire < 45:
        return dias_aire, "ambar"
    return dias_aire, "verde"


def _finanzas_s7(beneficio_mes: float, cuota_banco: float) -> Tuple[float, StatusColor]:
    if cuota_banco <= 0:
        return 999.0, "verde"
    ratio = beneficio_mes / cuota_banco
    if ratio < 1:
        return ratio, "rojo"
    elif ratio < 2:
        return ratio, "ambar"
    return ratio, "verde"


def _finanzas_s8(beneficio_producto: float, horas_coste_inv: float) -> Tuple[float, StatusColor]:
    if horas_coste_inv <= 0:
        return 0.0, "rojo"
    roi = beneficio_producto / horas_coste_inv
    if roi < 1:
        return roi, "rojo"
    elif roi < 2:
        return roi, "ambar"
    return roi, "verde"


def _finanzas_s9(presupuesto: float, gasto_real: float) -> Tuple[float, StatusColor]:
    if presupuesto == 0:
        return 0.0, "rojo"
    desviacion = (gasto_real - presupuesto) / presupuesto * 100.0
    if desviacion > 20:
        return desviacion, "rojo"
    elif desviacion > 5:
        return desviacion, "ambar"
    return desviacion, "verde"


def _finanzas_s10(fondo_reserva: float, gasto_estructura_mes: float) -> Tuple[float, StatusColor]:
    if gasto_estructura_mes <= 0:
        return 999.0, "verde"
    meses_tranquilidad = fondo_reserva / gasto_estructura_mes
    if meses_tranquilidad < 1:
        return meses_tranquilidad, "rojo"
    elif meses_tranquilidad < 3:
        return meses_tranquilidad, "ambar"
    return meses_tranquilidad, "verde"

def compute_financial_kpi(short_code, inputs):
    a = inputs.get("a")
    b = inputs.get("b")

    if short_code == "S1": return _finanzas_s1(a, b)
    if short_code == "S2": return _finanzas_s2(a, b)
    if short_code == "S3": return _finanzas_s3(a, b)
    if short_code == "S4": return _finanzas_s4(a, b)
    if short_code == "S5": return _finanzas_s5(a, b)
    if short_code == "S6": return _finanzas_s6(a, b)
    if short_code == "S7": return _finanzas_s7(a, b)
    if short_code == "S8": return _finanzas_s8(a, b)
    if short_code == "S9": return _finanzas_s9(a, b)
    if short_code == "S10": return _finanzas_s10(a, b)

    return None, "ambar"

