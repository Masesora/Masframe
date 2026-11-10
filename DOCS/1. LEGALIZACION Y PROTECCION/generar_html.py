#!/usr/bin/env python3
"""Regenera los HTML legales (01-04) desde los .md de DOCS/1. LEGALIZACION Y PROTECCION.

Fuente de verdad: los .md. El HTML conserva cabecera, estilos, barra superior y pie
de cada archivo existente y sustituye solo el cartel de borrador y el cuerpo.

Uso:  python generar_html.py            (desde esta carpeta)
      python generar_html.py --sin-cartel   -> escribe el HTML sin el cartel de borrador
                                               (para las copias publicadas)
"""
import html
import re
import sys
from pathlib import Path

AQUI = Path(__file__).parent
SIN_CARTEL = "--sin-cartel" in sys.argv

CARPETAS = {
    "doc legal Masesora": {"sufijo": "MASESORA", "rutas": "/legal/{}.html"},
    "doc legal Masframe": {"sufijo": "MASFRAME", "rutas": "/legal/{}.html"},
}
DOCS = {
    "01_politica_privacidad": "privacidad",
    "02_aviso_legal": "aviso-legal",
    "03_politica_cookies": "cookies",
    "04_terminos_condiciones": "terminos",
}
DESCRIPCIONES = {
    ("doc legal Masesora", "privacidad"): "Política de Privacidad de Masesora, del diagnóstico Tu Solución y del Escáner de Salud Empresarial.",
    ("doc legal Masesora", "aviso-legal"): "Aviso Legal de Masesora, del diagnóstico Tu Solución y del Escáner de Salud Empresarial.",
    ("doc legal Masesora", "cookies"): "Política de Cookies de Masesora: qué usamos, qué solo si aceptas, y cómo cambiarlo.",
    ("doc legal Masesora", "terminos"): "Términos y Condiciones de Masesora, Tu Solución y el Escáner de Salud Empresarial.",
}


def inline(t):
    t = html.escape(t, quote=False)
    t = re.sub(r"`([^`]+)`", r"<code>\1</code>", t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<![\w*])\*([^*\n]+?)\*(?![\w*])", r"<em>\1</em>", t)
    t = re.sub(r"\[([^\]]+)\]\((https?://[^)]+)\)", r'<a href="\2" target="_blank" rel="noopener">\1</a>', t)
    t = re.sub(r"(?<![\w@\"/=:])([\w.+-]+@[\w-]+(?:\.[\w-]+)+)", r'<a href="mailto:\1">\1</a>', t)
    return t


def cartel(lineas):
    partes = []
    for l in lineas:
        l = l.lstrip(">").strip()
        if not l or l.startswith("**[BORRADOR"):
            continue
        l = inline(l).replace("<strong>", "<em>").replace("</strong>", "</em>")
        partes.append(l)
    return (
        '  <div class="draft-banner">\n'
        "    <strong>Borrador para revisión legal</strong>\n    "
        + "<br><br>".join(partes)
        + "\n  </div>\n\n"
    )


def tabla(filas):
    cab = [c.strip() for c in filas[0].strip().strip("|").split("|")]
    cuerpo = [[c.strip() for c in f.strip().strip("|").split("|")] for f in filas[2:]]
    h = "  <table>\n    <thead><tr>" + "".join(f"<th>{inline(c)}</th>" for c in cab) + "</tr></thead>\n    <tbody>\n"
    for f in cuerpo:
        h += "      <tr>" + "".join(f"<td>{inline(c)}</td>" for c in f) + "</tr>\n"
    return h + "    </tbody>\n  </table>\n"


def cuerpo(md):
    lineas = md.splitlines()
    i, out, meta = 0, "", ""
    # saltar título y cartel inicial
    while i < len(lineas) and not lineas[i].startswith("---"):
        i += 1
    cart = [l for l in lineas[:i] if l.startswith(">")]
    i += 1
    while i < len(lineas):
        l = lineas[i]
        if not l.strip() or l.strip() == "---":
            i += 1
        elif l.startswith("## "):
            out += f"  <h2>{inline(l[3:])}</h2>\n"; i += 1
        elif l.startswith("### "):
            out += f"  <h3>{inline(l[4:])}</h3>\n"; i += 1
        elif l.startswith("|"):
            j = i
            while j < len(lineas) and lineas[j].startswith("|"):
                j += 1
            out += tabla(lineas[i:j]); i = j
        elif re.match(r"^[-*] ", l):
            out += "  <ul>\n"
            while i < len(lineas) and re.match(r"^[-*] ", lineas[i]):
                out += f"    <li>{inline(lineas[i][2:])}</li>\n"; i += 1
            out += "  </ul>\n"
        elif re.match(r"^\d+\. ", l):
            out += "  <ol>\n"
            while i < len(lineas) and re.match(r"^\d+\. ", lineas[i]):
                out += f"    <li>{inline(re.sub(r'^\d+\. ', '', lineas[i]))}</li>\n"; i += 1
            out += "  </ol>\n"
        elif l.startswith("**Fecha de última actualización:**"):
            meta = '  <p class="meta">' + inline(l).replace("<strong>", "").replace("</strong>", "") + "</p>\n"; i += 1
        else:
            par = [l]; i += 1
            while i < len(lineas) and lineas[i].strip() and not re.match(r"^(#|\||[-*] |\d+\. |---|\*\*Fecha)", lineas[i]):
                par.append(lineas[i]); i += 1
            out += f"  <p>{inline(' '.join(par))}</p>\n"
    return cart, out + "\n" + meta


def main():
    for carpeta, cfg in CARPETAS.items():
        for pref, destino in DOCS.items():
            md = (AQUI / carpeta / f"{pref}_{cfg['sufijo']}.md").read_text(encoding="utf-8")
            ruta = AQUI / carpeta / "html" / f"{destino}.html"
            viejo = ruta.read_text(encoding="utf-8")
            crlf = "\r\n" in viejo
            viejo = viejo.replace("\r\n", "\n")
            cart, cuerpo_html = cuerpo(md)
            ini = viejo.index('  <div class="draft-banner">')
            fin = viejo.index("</main>")
            nuevo = viejo[:ini] + ("" if SIN_CARTEL else cartel(cart)) + cuerpo_html + viejo[fin:]
            desc = DESCRIPCIONES.get((carpeta, destino))
            if desc:
                nuevo = re.sub(r'(<meta name="description" content=")[^"]*(")', lambda m: m.group(1) + desc + m.group(2), nuevo, count=1)
            if cfg["rutas"]:
                for otro in DOCS.values():
                    nuevo = nuevo.replace(f'href="/{otro}"', f'href="{cfg["rutas"].format(otro)}"')
            if crlf:
                nuevo = nuevo.replace("\n", "\r\n")
            ruta.write_text(nuevo, encoding="utf-8", newline="")
            print("ok", carpeta, destino)


if __name__ == "__main__":
    main()
