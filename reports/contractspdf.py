from fpdf import FPDF
from pathlib import Path
from typing import Dict

REPORTS_DIR = Path(__file__).resolve().parent / "generated_contracts"
REPORTS_DIR.mkdir(exist_ok=True)


class ContractPDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 16)
        self.set_text_color(30, 36, 68)
        self.cell(0, 10, "Contrato Clínico Empresarial MASFRAME®", ln=True, align="C")
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.set_text_color(120, 120, 120)
        self.cell(0, 10, "© MASESORA - Sistema Clínico Empresarial", align="C")


def generate_contract_pdf(contract: Dict) -> str:
    pdf = ContractPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)

    pdf.set_font("Arial", "", 12)
    pdf.set_text_color(0, 0, 0)

    pdf.cell(0, 8, f"Empresa: {contract['empresa']}", ln=True)
    pdf.cell(0, 8, f"Código: {contract['codigo']}", ln=True)
    pdf.cell(0, 8, f"Plan: {contract['plan']}", ln=True)
    pdf.cell(0, 8, f"Segmento: {contract['segment']}", ln=True)
    pdf.cell(0, 8, f"Precio: {contract['price'] if contract['price'] is not None else 'A medida'} €", ln=True)
    pdf.ln(5)

    pdf.set_font("Arial", "B", 13)
    pdf.set_text_color(30, 36, 68)
    pdf.cell(0, 8, "Especialidades incluidas:", ln=True)

    pdf.set_font("Arial", "", 11)
    pdf.set_text_color(0, 0, 0)
    for esp in contract["specialties"]:
        pdf.cell(0, 6, f"- {esp}", ln=True)

    if contract.get("guarantee"):
        pdf.ln(5)
        pdf.set_font("Arial", "B", 13)
        pdf.set_text_color(30, 36, 68)
        pdf.cell(0, 8, contract["guarantee"]["title"], ln=True)

        pdf.set_font("Arial", "", 10)
        pdf.set_text_color(0, 0, 0)
        pdf.multi_cell(0, 6, contract["guarantee"]["summary"])

    filename = f"{contract['codigo']}_contract.pdf"
    filepath = REPORTS_DIR / filename
    pdf.output(str(filepath))

    return str(filepath)