# Música de fondo original (sintetizada aquí, sin derechos de terceros): pad cálido + arpegio suave + bajo + pulso ligero.
import numpy as np, wave, sys
SR=48000; BPM=96; dur=float(sys.argv[2]); out=sys.argv[1]
beat=60/BPM; N=int(dur*SR); t=np.arange(N)/SR
def note(m): return 440*2**((m-69)/12)
# Progresión Am - F - C - G (2 compases de 4 tiempos cada acorde)
chords=[[57,60,64],[53,57,60],[48,52,55],[55,59,62]]
bar=4*beat; L=np.zeros(N); R=np.zeros(N)
def env(n,a,r):
    e=np.ones(n); a=int(a*SR); r=int(r*SR)
    e[:a]=np.linspace(0,1,a); e[-r:]*=np.linspace(1,0,r); return e
k=0; pos=0.0
while pos<dur:
    ch=chords[k%4]; seg=2*bar; i0=int(pos*SR); i1=min(N,int((pos+seg)*SR)); n=i1-i0
    if n<=0: break
    tt=np.arange(n)/SR
    pad=np.zeros(n)
    for m in ch+[ch[0]+12]:
        f=note(m)
        for d in (-0.12,0.0,0.12):  # desafinado suave
            ph=2*np.pi*f*(1+d/100)*tt
            pad+= (np.sin(ph)+0.25*np.sin(2*ph)+0.08*np.sin(3*ph))
    pad*=env(n,1.2,1.2)*0.035
    bass=np.sin(2*np.pi*note(ch[0]-12)*tt)*0.09*env(n,0.3,0.8)
    L[i0:i1]+=pad+bass; R[i0:i1]+=pad*0.92+bass
    # arpegio en corcheas
    arp=[ch[0]+12,ch[1]+12,ch[2]+12,ch[1]+12]
    steps=int(seg/(beat/2))
    for s in range(steps):
        j0=i0+int(s*beat/2*SR); ln=int(0.45*SR)
        if j0+ln>N: break
        f=note(arp[s%4]); tt2=np.arange(ln)/SR
        pl=(np.sin(2*np.pi*f*tt2)+0.3*np.sin(4*np.pi*f*tt2))*np.exp(-tt2*7)*0.028
        pan=0.35 if s%2 else -0.35
        L[j0:j0+ln]+=pl*(1-pan); R[j0:j0+ln]+=pl*(1+pan)
    # pulso suave (bombo blando) en 1 y 3, tic en contratiempos
    for b in range(int(seg/beat)):
        j0=i0+int(b*beat*SR)
        if b%2==0:
            ln=int(0.25*SR); tt3=np.arange(ln)/SR
            if j0+ln<=N:
                kick=np.sin(2*np.pi*(55+60*np.exp(-tt3*30))*tt3)*np.exp(-tt3*14)*0.12
                L[j0:j0+ln]+=kick; R[j0:j0+ln]+=kick
        j1=j0+int(beat/2*SR); ln=int(0.05*SR)
        if j1+ln<=N:
            hh=np.random.default_rng(b+k).standard_normal(ln)*np.exp(-np.arange(ln)/SR*90)*0.012
            hh=np.diff(np.concatenate([[0],hh]))  # más agudo
            L[j1:j1+ln]+=hh; R[j1:j1+ln]+=hh
    pos+=seg; k+=1
fade=env(N,1.5,2.5); L*=fade; R*=fade
st=np.stack([L,R],1); st/=np.abs(st).max()*1.15
w=wave.open(out,'wb'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
w.writeframes((st*32767).astype(np.int16).tobytes()); w.close()
