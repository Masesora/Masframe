# Música de fondo original, luminosa y con ritmo (Re mayor, 110 BPM): pulso suave, palmas, arpegio brillante, acordes y bajo.
import numpy as np, wave, sys
SR=48000; BPM=116; dur=float(sys.argv[2]); out=sys.argv[1]
b=60/BPM; N=int(dur*SR)
L=np.zeros(N); R=np.zeros(N); rng=np.random.default_rng(11)
def nf(m): return 440*2**((m-69)/12)
def add(sig,t0,pan=0.0,g=1.0):
    i=int(t0*SR); j=min(N,i+len(sig))
    if i>=N: return
    s=sig[:j-i]*g; L[i:j]+=s*(1-pan); R[i:j]+=s*(1+pan)
def pluck(f,d=0.35):
    t=np.arange(int(d*SR))/SR
    return (np.sin(2*np.pi*f*t)+0.5*np.sin(2*np.pi*2*f*t)*np.exp(-t*18)+0.25*np.sin(2*np.pi*3*f*t)*np.exp(-t*25))*np.exp(-t*9)
def keys(fs,d):
    t=np.arange(int(d*SR))/SR; s=np.zeros_like(t)
    for f in fs:
        for h,a in [(1,1),(2,.45),(3,.2),(4,.1)]: s+=a*np.sin(2*np.pi*f*h*t)*np.exp(-t*(3+h))
    return s*np.minimum(1,t*200)
def kick():
    t=np.arange(int(.22*SR))/SR; return np.sin(2*np.pi*(50+90*np.exp(-t*35))*t)*np.exp(-t*16)
def clap():
    n=int(.18*SR); t=np.arange(n)/SR; x=rng.standard_normal(n)
    x=np.convolve(x,np.ones(6)/6,'same')-np.convolve(x,np.ones(40)/40,'same')
    env=np.exp(-t*28)+0.6*np.exp(-np.maximum(0,t-.012)*30)*(t>.012)
    return x*env
def shaker():
    n=int(.06*SR); x=rng.standard_normal(n); x=np.diff(np.concatenate([[0],x])); return x*np.exp(-np.arange(n)/SR*70)
# G - D - Em - C
prog=[(55,[55,59,62]),(62,[62,66,69]),(64,[64,67,71]),(60,[60,64,67])]
bar=4*b; nbars=int(np.ceil(dur/bar))+1
for k in range(nbars):
    root,ch=prog[k%4]; t0=k*bar
    # bajo en corcheas
    for s in range(8):
        f=nf(root-24); t=np.arange(int(b/2*0.9*SR))/SR
        add(np.sin(2*np.pi*f*t)*np.minimum(1,t*300)*np.exp(-t*4),t0+s*b/2,0,0.20)
    # acordes en contratiempo
    for s in range(4):
        add(keys([nf(m) for m in ch],0.5),t0+s*b+b/2,0.1,0.05)
    # arpegio en semicorcheas
    arp=[ch[0]+12,ch[2]+12,ch[1]+24,ch[2]+12,ch[0]+24,ch[2]+12,ch[1]+12,ch[2]+24]
    for s in range(16):
        add(pluck(nf(arp[s%8]),0.28),t0+s*b/4,(-0.35 if s%2 else 0.35),0.05)
    # percusión
    for s in range(4):
        add(kick(),t0+s*b,0,0.30)
        if s in (1,3): add(clap(),t0+s*b,0,0.10)
    for s in range(8): add(shaker(),t0+s*b/2+b/4,0.3,0.035)
fade=np.ones(N); a=int(0.6*SR); r=int(1.8*SR); fade[:a]=np.linspace(0,1,a); fade[-r:]=np.linspace(1,0,r)
st=np.stack([L*fade,R*fade],1); st/=np.abs(st).max()*1.1
w=wave.open(out,'wb'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((st*32767).astype(np.int16).tobytes()); w.close()
