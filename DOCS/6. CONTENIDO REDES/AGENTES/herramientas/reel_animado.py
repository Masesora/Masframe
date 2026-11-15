"""Reel animado de La Clínica de Empresas, sincronizado con una voz.

Uso:
    python3 reel_animado.py <carpeta de la pieza>

Lee assets/reel_spec.json y la voz indicada en él, y genera assets/reel_instagram.mp4 y assets/reel_tiktok.mp4
(1080x1920, 25 fps). Escenas disponibles: titulo, frase, barras_cuenta, barras_meses, pasos, alta, escaner, cierre.
Subtítulos palabra a palabra desde "palabras" (lista de {w, s, e}), con correcciones en "correcciones".
"""
import base64, json, subprocess, sys
from pathlib import Path
from playwright.sync_api import sync_playwright

HERE = Path(__file__).resolve().parent
FPS = 25


def fonts():
    out = []
    for w in (400, 600, 700, 800):
        b = base64.b64encode((HERE / "fonts" / f"montserrat-latin-{w}-normal.woff2").read_bytes()).decode()
        out.append(f"@font-face{{font-family:'Montserrat';font-weight:{w};src:url(data:font/woff2;base64,{b}) format('woff2')}}")
    return "\n".join(out)


PAGE = r"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>
%FONTS%
:root{--navy:#0F1A35;--navy2:#1E3060;--gold:#B89D52;--gold2:#D4B96A;--ok:#2E7D4F;--crit:#B8471F}
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1080px;height:1920px;overflow:hidden;font-family:Montserrat,sans-serif;color:#fff;background:var(--navy)}
#bg{position:absolute;inset:0;background:radial-gradient(900px 800px at 100% 0%,rgba(30,48,96,.95),transparent 70%),radial-gradient(800px 700px at 0% 100%,rgba(30,48,96,.7),transparent 70%),var(--navy)}
#grid{position:absolute;inset:0;opacity:.06;background-image:linear-gradient(rgba(184,157,82,.9) 1px,transparent 1px),linear-gradient(90deg,rgba(184,157,82,.9) 1px,transparent 1px);background-size:60px 60px}
#ecg{position:absolute;left:0;width:1080px;top:1150px;height:110px;opacity:.45}
#ecg path{fill:none;stroke:var(--gold2);stroke-width:5;filter:drop-shadow(0 0 10px rgba(212,185,106,.7))}
#tag{position:absolute;left:90px;top:250px;display:flex;gap:18px;align-items:center}
#tag .pill{background:var(--gold);color:var(--navy);font-weight:800;font-size:26px;letter-spacing:.14em;padding:12px 22px;border-radius:999px}
#tag .txt{font-weight:600;font-size:26px;letter-spacing:.22em;color:var(--gold2);text-transform:uppercase}
.scene{position:absolute;left:90px;right:90px;top:360px;height:770px;display:flex;flex-direction:column;justify-content:center;opacity:0}
h1{font-weight:800;font-size:108px;line-height:1.06}
h2{font-weight:800;font-size:76px;line-height:1.12}
.gold{color:var(--gold2)}
.eyebrow{font-weight:600;font-size:30px;letter-spacing:.26em;color:var(--gold2);text-transform:uppercase;margin-bottom:28px}
.w{display:inline-block;opacity:0;transform:translateY(30px)}
.bars{display:flex;align-items:flex-end;gap:26px;height:420px;margin-top:50px}
.bar{flex:1;border-radius:18px 18px 6px 6px;position:relative;height:0}
.bar span{position:absolute;bottom:-56px;left:0;right:0;text-align:center;font-weight:700;font-size:28px;letter-spacing:.12em;color:rgba(255,255,255,.75);text-transform:uppercase}
.step{display:flex;gap:28px;align-items:center;background:rgba(255,255,255,.06);border:2px solid rgba(184,157,82,.5);border-radius:28px;padding:30px 34px;margin-top:22px;opacity:0;transform:translateX(-40px)}
.step .n{flex:0 0 auto;width:80px;height:80px;border-radius:50%;background:var(--gold);color:var(--navy);font-weight:800;font-size:44px;display:flex;align-items:center;justify-content:center}
.step .t{font-weight:700;font-size:44px;line-height:1.2}
.step .t small{display:block;font-weight:400;font-size:32px;color:rgba(255,255,255,.78);margin-top:6px}
.chip{display:inline-block;border:3px solid var(--gold);color:var(--gold2);font-weight:700;font-size:34px;letter-spacing:.12em;padding:16px 30px;border-radius:999px;margin:14px 14px 0 0;opacity:0}
.go{margin-top:60px;text-align:center;background:var(--gold);color:var(--navy);font-weight:800;font-size:60px;border-radius:999px;padding:36px;opacity:0}
.ill{margin-top:22px;text-align:center;font-weight:600;font-size:30px;letter-spacing:.16em;color:rgba(255,255,255,.65);text-transform:uppercase}
#sub{position:absolute;left:80px;right:80px;top:1270px;height:220px;display:flex;flex-wrap:wrap;align-content:center;justify-content:center;text-align:center;font-weight:700;font-size:50px;line-height:1.25}
#sub .sw{opacity:.35;margin:0 7px}
#sub .sw.on{opacity:1}
#sub .sw.now{color:var(--gold2)}
#brand{position:absolute;left:90px;right:90px;bottom:300px;display:flex;justify-content:space-between;align-items:center}
#brand .wm{font-weight:800;letter-spacing:.12em;font-size:34px}
#brand .wm small{display:block;font-weight:600;font-size:13px;letter-spacing:.42em;color:var(--gold);margin-top:6px}
#brand .hd{font-weight:600;font-size:28px;color:rgba(255,255,255,.7)}
</style></head><body>
<div id="bg"></div><div id="grid"></div>
<svg id="ecg" viewBox="0 0 1080 260"><path id="ecgp" d="M0 130 H300 L340 130 L370 40 L410 230 L450 70 L480 130 H620 L650 130 L680 60 L715 200 L745 130 H1080"/></svg>
<div id="tag"><span class="pill">LA CLÍNICA</span><span class="txt">%TAG%</span></div>
<div id="scenes"></div>
<div id="sub"></div>
<div id="brand"><div class="wm">MASESORA<small>DINAMISMO EMPRESARIAL</small></div><div class="hd">@laclinicadempresas</div></div>
<script>
const SPEC=%SPEC%; const PLAT=%PLAT%;
const clamp=(x,a,b)=>Math.max(a,Math.min(b,x)); const ease=x=>1-Math.pow(1-clamp(x,0,1),3);
const root=document.getElementById('scenes');
function words(txt,cls){return txt.split(' ').map(w=>`<span class="w ${cls||''}">${w}</span>`).join(' ')}
SPEC.escenas.forEach((s,i)=>{
  const d=document.createElement('div'); d.className='scene'; d.id='sc'+i; let h='';
  if(s.eyebrow) h+=`<div class="eyebrow">${s.eyebrow}</div>`;
  if(s.tipo==='titulo') h+=`<h1>${words(s.texto)} ${s.oro?'<br>'+words(s.oro,'gold'):''}</h1>`;
  if(s.tipo==='frase') h+=`<h2>${words(s.texto)} ${s.oro?words(s.oro,'gold'):''}</h2>`;
  if(s.tipo==='barras_cuenta'){h+=`<h2>${words(s.texto)}</h2><div class="bars" style="padding:0 120px"><div class="bar" data-h="1" style="background:var(--gold)"><span>Facturado</span></div><div class="bar" data-h="0.38" style="background:var(--crit)"><span>En la cuenta</span></div></div>`}
  if(s.tipo==='barras_meses'){h+=`<h2>${words(s.texto)}</h2><div class="bars">`+[.9,.35,.75,.2,.95,.45].map((v,k)=>`<div class="bar" data-h="${v}" style="background:${v>.6?'var(--gold)':'rgba(255,255,255,.25)'}"><span>${['E','F','M','A','M','J'][k]}</span></div>`).join('')+`</div>`}
  if(s.tipo==='pasos'||s.tipo==='alta'){h+=`<h2 style="font-size:66px">${words(s.texto)} ${s.oro?words(s.oro,'gold'):''}</h2>`+s.pasos.map((p,k)=>`<div class="step" data-t="${p.t}"><div class="n">${k+1}</div><div class="t">${p.titulo}<small>${p.detalle}</small></div></div>`).join('')}
  if(s.tipo==='escaner'){h+=`<h2>${words(s.texto)} ${s.oro?'<br>'+words(s.oro,'gold'):''}</h2><div>`+s.chips.map(c=>`<span class="chip" data-t="${c.t}">${c.txt}</span>`).join('')+`</div>`}
  if(s.tipo==='cierre'){const c=s[PLAT]; h+=`<h2>${words(s.texto)}</h2><div class="go">${c.boton}</div><div class="ill">${c.debajo}</div>`}
  d.innerHTML=h; root.appendChild(d);
});
const subEl=document.getElementById('sub'); const W=SPEC.palabras;
// subtítulos: grupos de hasta 6 palabras, cortando en pausas
const groups=[];let g=[];W.forEach((w,i)=>{g.push(w);const gap=(W[i+1]?W[i+1].s-w.e:9);if(g.length>=5||gap>0.45||/[.?!,]$/.test(w.w)&&g.length>=3){groups.push(g);g=[]}});if(g.length)groups.push(g);
window.render=function(t){
  SPEC.escenas.forEach((s,i)=>{
    const el=document.getElementById('sc'+i); const fin=(SPEC.escenas[i+1]?SPEC.escenas[i+1].inicio:99);
    const vin=ease((t-s.inicio)/0.35), vout=1-ease((t-(fin-0.25))/0.25);
    const v=t<s.inicio||t>fin?0:Math.min(vin,vout); el.style.opacity=v; el.style.transform=`translateY(${(1-vin)*40}px)`;
    const ws=el.querySelectorAll('.w'); const n=ws.length; const dur=Math.max(0.6,Math.min(s.palabras_hasta?s.palabras_hasta-s.inicio:1.4,2.4));
    ws.forEach((w,k)=>{const p=ease((t-s.inicio-k*dur/n)/0.3); w.style.opacity=p; w.style.transform=`translateY(${(1-p)*30}px)`});
    el.querySelectorAll('.bar').forEach((b,k)=>{const p=ease((t-s.inicio-0.6-k*0.12)/0.6); b.style.height=(p*parseFloat(b.dataset.h)*100)+'%'});
    el.querySelectorAll('.step').forEach(st=>{const p=ease((t-parseFloat(st.dataset.t))/0.4); st.style.opacity=p; st.style.transform=`translateX(${(1-p)*-40}px)`});
    el.querySelectorAll('.chip').forEach(c=>{const p=ease((t-parseFloat(c.dataset.t))/0.3); c.style.opacity=p});
    const go=el.querySelector('.go'); if(go){const p=ease((t-s.inicio-0.8)/0.4); go.style.opacity=p; go.style.transform=`scale(${0.9+0.1*p+0.02*Math.sin(t*5)*p})`}
  });
  // ECG: se dibuja en bucle; en la escena de alta pasa a verde
  const path=document.getElementById('ecgp'); const L=path.getTotalLength(); const ph=(t%2.2)/2.2;
  path.style.strokeDasharray=L; path.style.strokeDashoffset=L*(1-ph);
  const alta=SPEC.escenas.find(s=>s.tipo==='alta'); const inAlta=alta&&t>=alta.inicio&&t<(alta.fin||alta.inicio+6);
  path.style.stroke=inAlta?'#4CC38A':'var(--gold2)';
  // subtítulos
  const cur=groups.find(gr=>t>=gr[0].s-0.15&&t<=gr[gr.length-1].e+0.35)||null;
  subEl.innerHTML=cur?cur.map(w=>`<span class="sw ${t>=w.s?'on':''} ${t>=w.s&&t<=w.e+0.05?'now':''}">${w.w}</span>`).join(''):'';
};
</script></body></html>"""


def build(piece: Path):
    assets = piece / "assets"
    spec = json.loads((assets / "reel_spec.json").read_text())
    voice = assets / spec["voz"]
    dur = spec["duracion"]
    for plat in ("instagram", "tiktok"):
        html = (PAGE.replace("%FONTS%", fonts()).replace("%TAG%", spec.get("etiqueta", ""))
                .replace("%SPEC%", json.dumps(spec, ensure_ascii=False)).replace("%PLAT%", json.dumps(plat)))
        out = assets / f"reel_{plat}.mp4"
        ff = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "image2pipe", "-framerate", str(FPS), "-i", "-",
                               "-i", str(voice), "-map", "0:v", "-map", "1:a", "-c:v", "libx264", "-preset", "veryfast", "-crf", "20",
                               "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "160k", "-af", "loudnorm=I=-14:TP=-1.5:LRA=11",
                               "-t", str(dur), "-movflags", "+faststart", str(out)], stdin=subprocess.PIPE)
        with sync_playwright() as p:
            b = p.chromium.launch(executable_path="/usr/bin/google-chrome" if Path("/usr/bin/google-chrome").exists() else None)
            pg = b.new_page(viewport={"width": 1080, "height": 1920})
            pg.set_content(html); pg.wait_for_timeout(300)
            for f in range(int(dur * FPS)):
                pg.evaluate(f"render({f / FPS})")
                ff.stdin.write(pg.screenshot(type="jpeg", quality=90))
                if f == int(spec.get("portada_t", 1.6) * FPS) and plat == "instagram":
                    pg.screenshot(path=str(assets / "portada.png"))
            b.close()
        ff.stdin.close(); ff.wait()
        print("MP4:", out.name)


if __name__ == "__main__":
    build(Path(sys.argv[1]))
