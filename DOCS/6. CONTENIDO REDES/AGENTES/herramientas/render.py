"""Renderiza las diapositivas de una pieza a PNG (y, si es un reel, a MP4).

Uso:
    python3 render.py "<carpeta de la pieza>"

La carpeta debe tener assets/slides.html con un <div class="frame" data-name="NN_nombre"> por diapositiva.
Cada frame se exporta a assets/NN_nombre.png con su tamaño real (1080x1350 carrusel/imagen, 1080x1920 reel).
Si existe assets/reel.json ({"segundos": [3,4,...], "plataforma_final": {"instagram": "07_cierre-ig", "tiktok": "07_cierre-tt"}}),
monta assets/reel_instagram.mp4 y assets/reel_tiktok.mp4 y, si hay assets/voz.(m4a|mp3|wav), le pone la voz.
Pantalla dividida y ganchos B/C: ver make_reels (claves "frames", "ganchos" y "clip_zona" de reel.json).
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


def _dur(f: Path) -> float:
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(f)],
                       capture_output=True, text=True, check=True)
    return float(r.stdout.strip())


def make_reels(assets: Path, cfg: dict):
    """Monta los MP4. Claves opcionales de reel.json (pantalla dividida y ganchos, desde el 19 nov):
    "frames": lista ordenada de diapositivas (sin el cierre); si falta, se usan todos los PNG en orden.
    "ganchos": {"B": "01_gancho_B", "C": "01_gancho_C"} -> reel_tiktok_B.mp4 / reel_tiktok_C.mp4 (cambia solo la primera).
    "clip_zona": [x, y, ancho, alto] -> si existe assets/clip.mp4, se encaja ahí (pantalla dividida) y el vídeo dura lo que el clip.
    Audio: voz.(m4a|mp3|wav) > audio del clip > musica.(m4a|wav) > silencio."""
    if "frames" in cfg:
        frames = [assets / f"{n}.png" for n in cfg["frames"]]
    else:
        frames = sorted(p for p in assets.glob("*.png") if not any(p.stem == v for v in cfg["plataforma_final"].values()))
    secs = list(cfg["segundos"])
    voice = next((assets / f"voz.{e}" for e in ("m4a", "mp3", "wav") if (assets / f"voz.{e}").exists()), None)
    music = next((assets / f"musica.{e}" for e in ("m4a", "wav") if (assets / f"musica.{e}").exists()), None)
    clip = assets / "clip.mp4" if cfg.get("clip_zona") and (assets / "clip.mp4").exists() else None
    if clip or (voice and "frames" in cfg):
        k = _dur(clip or voice) / sum(secs)
        secs = [s * k for s in secs]
    total = sum(secs)
    outs = {plat: (frames, last) for plat, last in cfg["plataforma_final"].items()}
    for letra, g in cfg.get("ganchos", {}).items():
        outs[f"tiktok_{letra}"] = ([assets / f"{g}.png"] + frames[1:], cfg["plataforma_final"]["tiktok"])
    for plat, (fr, last) in outs.items():
        seq = fr + [assets / f"{last}.png"]
        with tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False) as lst:
            for img, s in zip(seq, secs):
                lst.write(f"file '{img}'\nduration {s:.3f}\n")
            lst.write(f"file '{seq[-1]}'\n")
        outp = assets / f"reel_{plat}.mp4"
        cmd = ["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", lst.name]
        vf = "[0:v]fps=30,format=yuv420p[v]"
        if clip:
            x, y, w, h = cfg["clip_zona"]
            cmd += ["-i", str(clip)]
            vf = (f"[1:v]scale={w}:{h}:force_original_aspect_ratio=increase,crop={w}:{h},setsar=1[c];"
                  f"[0:v]fps=30[b];[b][c]overlay={x}:{y}:eof_action=pass,format=yuv420p[v]")
        if voice:
            cmd += ["-i", str(voice)]; amap = f"{2 if clip else 1}:a"; desc = "con voz"
        elif clip:
            amap = "1:a?"; desc = "con el audio del clip"
        elif music:
            cmd += ["-i", str(music)]; amap = "1:a"; desc = "con música, sin voz"
        else:
            cmd += ["-f", "lavfi", "-i", "anullsrc=r=44100:cl=stereo"]; amap = "1:a"; desc = "sin voz ni música"
        cmd += ["-filter_complex", vf, "-map", "[v]", "-map", amap, "-c:a", "aac", "-b:a", "160k",
                "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-t", f"{total:.3f}", "-movflags", "+faststart", str(outp)]
        subprocess.run(cmd, check=True)
        os.unlink(lst.name)
        print("MP4:", outp.name, f"({desc})")


if __name__ == "__main__":
    render(Path(sys.argv[1]))
