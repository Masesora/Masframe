"""Renderiza las diapositivas de una pieza a PNG (y, si es un reel, a MP4).

Uso:
    python3 render.py "<carpeta de la pieza>"

La carpeta debe tener assets/slides.html con un <div class="frame" data-name="NN_nombre"> por diapositiva.
Cada frame se exporta a assets/NN_nombre.png con su tamaño real (1080x1350 carrusel/imagen, 1080x1920 reel).
Si existe assets/reel.json ({"segundos": [3,4,...], "plataforma_final": {"instagram": "07_cierre-ig", "tiktok": "07_cierre-tt"}}),
monta assets/reel_instagram.mp4 y assets/reel_tiktok.mp4 y, si hay assets/voz.(m4a|mp3|wav), le pone la voz.
"""
import base64, json, os, subprocess, sys, tempfile
from pathlib import Path
from playwright.sync_api import sync_playwright

HERE = Path(__file__).resolve().parent


def font_faces():
    css = []
    for w in (400, 500, 600, 700, 800):
        data = base64.b64encode((HERE / "fonts" / f"montserrat-latin-{w}-normal.woff2").read_bytes()).decode()
        css.append(f"@font-face{{font-family:'Montserrat';font-weight:{w};src:url(data:font/woff2;base64,{data}) format('woff2')}}")
    return "\n".join(css)


def build_html(slides_html: str) -> str:
    base = (HERE / "clinica.css").read_text()
    return f"<!DOCTYPE html><html lang='es'><head><meta charset='utf-8'><style>{font_faces()}\n{base}\nbody{{margin:0;background:#05080f}}</style></head><body>{slides_html}</body></html>"


def render(piece: Path):
    assets = piece / "assets"
    html = build_html((assets / "slides.html").read_text())
    out = []
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path="/usr/bin/google-chrome" if Path("/usr/bin/google-chrome").exists() else None)
        page = b.new_page(viewport={"width": 1080, "height": 1920})
        page.set_content(html)
        page.wait_for_timeout(400)
        for el in page.query_selector_all(".frame"):
            name = el.get_attribute("data-name")
            f = assets / f"{name}.png"
            el.screenshot(path=str(f))
            out.append(f)
        b.close()
    print("PNG:", *[o.name for o in out], sep="\n  ")
    cfg = assets / "reel.json"
    if cfg.exists():
        make_reels(assets, json.loads(cfg.read_text()))


def make_reels(assets: Path, cfg: dict):
    frames = sorted(p for p in assets.glob("*.png") if not any(p.stem == v for v in cfg["plataforma_final"].values()))
    secs = cfg["segundos"]
    voice = next((assets / f"voz.{e}" for e in ("m4a", "mp3", "wav") if (assets / f"voz.{e}").exists()), None)
    for plat, last in cfg["plataforma_final"].items():
        seq = frames + [assets / f"{last}.png"]
        with tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False) as lst:
            for img, s in zip(seq, secs):
                lst.write(f"file '{img}'\nduration {s}\n")
            lst.write(f"file '{seq[-1]}'\n")
        outp = assets / f"reel_{plat}.mp4"
        cmd = ["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", lst.name]
        if voice:
            cmd += ["-i", str(voice), "-c:a", "aac", "-b:a", "160k", "-shortest"]
        else:
            cmd += ["-f", "lavfi", "-i", "anullsrc=r=44100:cl=stereo", "-c:a", "aac", "-shortest"]
        cmd += ["-vf", "fps=30,format=yuv420p", "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", str(outp)]
        subprocess.run(cmd, check=True)
        os.unlink(lst.name)
        print("MP4:", outp.name, "(con voz)" if voice else "(sin voz: falta assets/voz.m4a)")


if __name__ == "__main__":
    render(Path(sys.argv[1]))
