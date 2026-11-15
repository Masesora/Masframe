"""Historia de autodiagnóstico (1080x1920) para La Clínica de Empresas.

Uso: python3 historia.py <carpeta_assets> "<pregunta en blanco>" "<pregunta en oro>" "<opción 1>" "<opción 2>"
Genera <carpeta_assets>/historia.png. Las dos opciones se contestan respondiendo a la historia
(funciona aunque Meta no deje poner el sticker de encuesta desde el ordenador).
"""
import base64
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

HERE = Path(__file__).parent


def font(w):
    return base64.b64encode((HERE / "fonts" / f"montserrat-latin-{w}-normal.woff2").read_bytes()).decode()


def build(assets, q1, q2, o1, o2):
    ff = "".join(f"@font-face{{font-family:M;font-weight:{w};src:url(data:font/woff2;base64,{font(w)})}}" for w in (500, 600, 700, 800))
    html = f"""<html><head><style>{ff}
body{{margin:0;width:1080px;height:1920px;font-family:M;background:radial-gradient(ellipse at 30% 10%,#1E3060,#0F1A35 60%);color:#FAF7F2;position:relative;overflow:hidden}}
.grid{{position:absolute;inset:0;background-image:linear-gradient(rgba(212,185,106,.06) 1px,transparent 1px),linear-gradient(90deg,rgba(212,185,106,.06) 1px,transparent 1px);background-size:60px 60px}}
.tag{{position:absolute;top:250px;left:90px;display:flex;gap:18px;align-items:center}}
.pill{{background:#B89D52;color:#0F1A35;font-weight:800;font-size:28px;letter-spacing:.14em;padding:12px 24px;border-radius:999px}}
.t{{font-weight:600;font-size:28px;letter-spacing:.22em;color:#D4B96A}}
h1{{position:absolute;top:380px;left:90px;right:90px;font-weight:800;font-size:92px;line-height:1.08;margin:0}}
h1 span{{color:#D4B96A}}
.ask{{position:absolute;top:960px;left:90px;right:90px;text-align:center;font-weight:600;font-size:36px;color:rgba(250,247,242,.8)}}
.opts{{position:absolute;top:1040px;left:120px;right:120px;display:flex;flex-direction:column;gap:26px}}
.opt{{background:#FAF7F2;color:#0F1A35;border-radius:28px;padding:30px;font-weight:800;font-size:46px;text-align:center}}
.cta{{position:absolute;bottom:300px;left:90px;right:90px;text-align:center}}
.cta .a{{font-weight:600;font-size:32px;letter-spacing:.16em;color:#D4B96A;text-transform:uppercase}}
.cta .b{{display:inline-block;margin-top:22px;background:#B89D52;color:#0F1A35;font-weight:800;font-size:52px;padding:22px 48px;border-radius:999px}}
.brand{{position:absolute;bottom:150px;left:0;right:0;text-align:center;font-weight:800;font-size:34px;letter-spacing:.3em}}
.brand small{{display:block;font-weight:500;font-size:16px;letter-spacing:.42em;color:#B89D52;margin-top:8px}}
</style></head><body><div class=grid></div>
<div class=tag><div class=pill>LA CLÍNICA</div><div class=t>AUTODIAGNÓSTICO</div></div>
<h1>{q1}<br><span>{q2}</span></h1>
<div class=ask>Contesta a esta historia con tu respuesta</div>
<div class=opts><div class=opt>{o1}</div><div class=opt>{o2}</div></div>
<div class=cta><div class=a>Escáner de Salud Empresarial</div><div class=b>masesora.es</div></div>
<div class=brand>MASESORA<small>DINAMISMO EMPRESARIAL</small></div>
</body></html>"""
    with sync_playwright() as p:
        exe = "/usr/bin/google-chrome" if Path("/usr/bin/google-chrome").exists() else None
        b = p.chromium.launch(executable_path=exe)
        pg = b.new_page(viewport={"width": 1080, "height": 1920})
        pg.set_content(html)
        pg.wait_for_timeout(300)
        pg.screenshot(path=str(Path(assets) / "historia.png"))
        b.close()


if __name__ == "__main__":
    build(*sys.argv[1:6])
