#!/usr/bin/env python3
"""Limpieza de voz para reels de La Clínica de Empresas (cadena v2, DeepFilterNet).

Uso:
  python3 voz.py <entrada (mp4/wav/m4a)> <salida_voz.wav> [--musica musica.wav --mezcla salida_mezcla.wav]
         [--tempo 1.06] [--limpieza 35]

Pasos:
  1. Extrae la voz a 48 kHz mono.
  2. DeepFilterNet (binario `deep-filter`, gratuito y local) quita ruido y reverberación de la sala.
     --limpieza son los dB máximos de reducción: 35 suena natural; 100 es limpieza total.
  3. Ecualización de voz: corte de graves, menos «caja» en 250 Hz, presencia en 3 kHz y aire en 10 kHz.
  4. De-esser, compresión suave, quitar silencios largos y velocidad (--tempo).
  5. Volumen final para redes: -16 LUFS la voz sola y -14 LUFS la mezcla con música
     (la música baja sola cuando hablas, con compresión sidechain).

El binario se descarga de
https://github.com/Rikorose/DeepFilterNet/releases (deep-filter-0.5.6-x86_64-unknown-linux-musl).
Por defecto se busca en ~/dfbin/deep-filter; se puede cambiar con la variable DEEP_FILTER.
"""
import argparse, os, shutil, subprocess, tempfile

DF = os.environ.get("DEEP_FILTER", os.path.expanduser("~/dfbin/deep-filter"))


def run(cmd):
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("entrada"); ap.add_argument("salida")
    ap.add_argument("--musica"); ap.add_argument("--mezcla")
    ap.add_argument("--tempo", type=float, default=1.06)
    ap.add_argument("--limpieza", type=float, default=35)
    a = ap.parse_args()
    tmp = tempfile.mkdtemp()
    raw = os.path.join(tmp, "voz.wav")
    run(["ffmpeg", "-y", "-i", a.entrada, "-vn", "-ac", "1", "-ar", "48000", raw])
    outdir = os.path.join(tmp, "df"); os.makedirs(outdir)
    run([DF, "-D", "-a", str(a.limpieza), "-o", outdir, raw])
    limpio = os.path.join(outdir, "voz.wav")
    filtros = ",".join([
        "highpass=f=80",
        "equalizer=f=250:t=q:w=1.2:g=-3",
        "equalizer=f=3000:t=q:w=1.5:g=2.5",
        "highshelf=f=10000:g=2",
        "deesser=i=0.4",
        "acompressor=threshold=-20dB:ratio=3:attack=10:release=120:makeup=3",
        "silenceremove=stop_periods=-1:stop_duration=0.25:stop_threshold=-42dB",
        f"atempo={a.tempo}",
        "loudnorm=I=-16:TP=-1.5:LRA=7",
        "alimiter=limit=0.9",
    ])
    run(["ffmpeg", "-y", "-i", limpio, "-af", filtros, "-ar", "48000", a.salida])
    if a.musica and a.mezcla:
        fc = ("[1:a]volume=0.35[m];[m][0:a]sidechaincompress=threshold=0.05:ratio=8:attack=20:release=300[md];"
              "[0:a][md]amix=inputs=2:duration=first:normalize=0,loudnorm=I=-14:TP=-1.5[o]")
        run(["ffmpeg", "-y", "-i", a.salida, "-i", a.musica, "-filter_complex", fc, "-map", "[o]",
             "-ar", "48000", a.mezcla])
    shutil.rmtree(tmp)
    print("ok:", a.salida, a.mezcla or "")


if __name__ == "__main__":
    main()
