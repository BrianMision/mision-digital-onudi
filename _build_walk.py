#!/usr/bin/env python3
"""s-how (Version B) v5 — matches Ricardo's sketch:
   TOP BAND: Scan(QR+RFID) -> Tabs(staggered iPhones) -> Sign -> Distribution(Office 100% -> SUBSET Gov, SUBSET Client)
   then a BIG curved arrow sweeps from the Office down to a LARGE Dashboard box at the bottom (app viz, product-agnostic).
   Re-runnable: strips old vB CSS + replaces the how-walk/how-diagram region. Build-once-and-hold + ambient flow; #s-how.in."""
import re, pathlib

def qr_svg(seed0, N, m=4, fill="#0A0F16"):
    g=[[0]*N for _ in range(N)]
    def fnd(r,c,s):
        for i in range(s):
            for j in range(s):
                g[r+i][c+j]=1 if (i in(0,s-1) or j in(0,s-1) or (1<i<s-2 and 1<j<s-2)) else 0
    fs=3 if N<=11 else 7
    fnd(0,0,fs); fnd(0,N-fs,fs); fnd(N-fs,0,fs)
    seed=seed0
    def rnd():
        nonlocal seed; seed=(seed*1103515245+12345)&0x7fffffff; return seed/0x7fffffff
    for r in range(N):
        for c in range(N):
            if (r<fs+1 and c<fs+1) or (r<fs+1 and c>=N-fs-1) or (r>=N-fs-1 and c<fs+1): continue
            g[r][c]=1 if rnd()>0.5 else 0
    rects=''.join(f'<rect x="{c*m}" y="{r*m}" width="{m}" height="{m}"/>' for r in range(N) for c in range(N) if g[r][c])
    return f'<svg viewBox="0 0 {N*m} {N*m}" fill="{fill}" aria-hidden="true">{rects}</svg>'
QR = qr_svg(7, 21, 4)

RFID = ('<svg viewBox="0 0 48 48" fill="none" aria-hidden="true">'
  '<rect x="9" y="20" width="16" height="11" rx="2" fill="#0A0F16"/>'
  '<rect x="12" y="23" width="10" height="2" fill="#fff"/><rect x="12" y="27" width="7" height="2" fill="#fff"/>'
  '<path d="M28 14 A 18 18 0 0 1 28 34" stroke="var(--cyan-deep)" stroke-width="2.4" fill="none" stroke-linecap="round"/>'
  '<path d="M32 10 A 24 24 0 0 1 32 38" stroke="var(--cyan)" stroke-width="2.4" fill="none" stroke-linecap="round" opacity=".7"/>'
  '<path d="M36 6 A 30 30 0 0 1 36 42" stroke="var(--cyan)" stroke-width="2.4" fill="none" stroke-linecap="round" opacity=".4"/></svg>')

CSS = r'''
/* BEGIN: s-how walkthrough vB (rollback: delete this block) */
#s-how .how-walk { position: relative; width: 100%; margin: 12px 0 4px; }
#s-how .hw-top { display: flex; align-items: flex-start; justify-content: space-between; gap: 4px; }
#s-how .hw-st { display: flex; flex-direction: column; align-items: center; gap: 11px; position: relative; }
#s-how .hw-cap { text-align: center; line-height: 1.28; }
#s-how .hw-cap b { display: block; font-family: var(--sans-c); font-weight: 600; font-size: 14.5px; color: var(--ink); }
#s-how .hw-cap span { font-family: var(--mono); font-size: 9px; letter-spacing: 0.08em; text-transform: uppercase; color: var(--ink-muted); }

/* iPhone frame (tabs) */
#s-how .iphone { position: relative; width: 104px; height: 200px; border-radius: 23px; background: #0A0F16; padding: 4px; box-shadow: 0 16px 34px rgba(14,23,34,0.28), inset 0 0 0 2px #1c2733, inset 0 0 0 3px #05080d; }
#s-how .iphone .scr { position: relative; width: 100%; height: 100%; background: #FFFFFF; border-radius: 19px; overflow: hidden; }
#s-how .iphone .island { position: absolute; top: 6px; left: 50%; transform: translateX(-50%); width: 34px; height: 10px; background: #05080d; border-radius: 6px; z-index: 5; }
#s-how .scr-top { padding: 14px 10px 6px; font-family: var(--mono); font-size: 7px; letter-spacing: 0.1em; text-transform: uppercase; color: var(--cyan-deep); }
#s-how .scr-title { padding: 0 10px 6px; font-family: var(--sans-c); font-weight: 600; font-size: 11px; color: var(--ink); border-bottom: 1px solid var(--rule); }
#s-how .scr-body { padding: 7px 10px; display: flex; flex-direction: column; gap: 5px; }
#s-how .fld { display: flex; flex-direction: column; gap: 2px; }
#s-how .fld .l { font-family: var(--mono); font-size: 5.5px; letter-spacing: 0.06em; text-transform: uppercase; color: var(--ink-muted); }
#s-how .fld .v { font-family: var(--sans-c); font-size: 8.5px; color: var(--ink); font-weight: 500; }
#s-how .fld .v.ok { color: #22A06D; }
#s-how .fld .bar { height: 4.5px; border-radius: 2px; background: var(--cyan-soft); position: relative; overflow: hidden; }
#s-how .fld .bar::after { content: ""; position: absolute; inset: 0; width: 0; background: linear-gradient(90deg, var(--cyan), var(--cyan-deep)); border-radius: 2px; }
#s-how .tabpips { display:flex; gap:3px; padding: 6px 10px 0; }
#s-how .tabpips i { width:4px; height:4px; border-radius:50%; background: var(--rule-strong); }
#s-how .tabpips i.on { background: var(--cyan-deep); box-shadow:0 0 0 2px var(--cyan-soft); }

/* SCAN: QR + RFID two sources */
#s-how .hw-scan .scan-sources { display:flex; gap:12px; align-items:flex-start; }
#s-how .src { display:flex; flex-direction:column; align-items:center; gap:7px; }
#s-how .src .src-card { width:74px; height:74px; border-radius:12px; background:var(--white); border:1px solid var(--rule-strong); box-shadow:0 8px 20px rgba(36,96,168,0.10); display:flex; align-items:center; justify-content:center; position:relative; padding:9px; }
#s-how .src .src-card.dark { background:#0A0F16; }
#s-how .src .src-card svg { width:100%; height:100%; display:block; }
#s-how .src .src-lbl { font-family:var(--mono); font-size:9px; letter-spacing:0.12em; text-transform:uppercase; color:var(--cyan-deep); font-weight:600; }
#s-how .src .src-scan { position:absolute; left:8px; right:8px; top:10px; height:2px; background:linear-gradient(90deg,transparent,#22C55E,transparent); box-shadow:0 0 8px #22C55E; opacity:0; }
#s-how .scan-or { align-self:center; font-family:var(--mono); font-size:9px; letter-spacing:0.1em; text-transform:uppercase; color:var(--ink-muted); padding-top:26px; }

/* SIGN */
#s-how .sigwrap .iphone { height:200px; }
#s-how .sig-screen { padding:13px 10px; display:flex; flex-direction:column; gap:8px; height:100%; }
#s-how .sig-pad { flex:1; border:1px dashed var(--rule-strong); border-radius:8px; display:flex; align-items:center; justify-content:center; }
#s-how .sig-pad svg { width:78%; height:auto; overflow:visible; }
#s-how .sig-pad path { fill:none; stroke:var(--cyan-deep); stroke-width:2.4; stroke-linecap:round; stroke-linejoin:round; stroke-dasharray:240; stroke-dashoffset:240; }
#s-how .sig-seal { display:flex; align-items:center; gap:6px; font-family:var(--mono); font-size:8px; letter-spacing:0.08em; text-transform:uppercase; color:#22A06D; opacity:0; }
#s-how .sig-seal::before { content:"\2713"; display:inline-flex; align-items:center; justify-content:center; width:13px; height:13px; border-radius:50%; background:#22A06D; color:#fff; font-size:8px; }

/* connectors (top band) */
#s-how .hw-conn { flex: 1 1 auto; height: 2px; min-width: 18px; background: var(--rule); position: relative; align-self: center; margin-top: 92px; }
#s-how .hw-conn::after { content:""; position:absolute; top:-2px; left:0; width:14px; height:6px; border-radius:3px; background: linear-gradient(90deg, transparent, var(--cyan), transparent); opacity:0; }

/* DISTRIBUTION: Office 100% -> SUBSET Gov, SUBSET Client */
#s-how .hw-dist2 { position:relative; width:210px; flex:0 0 auto; }
#s-how .hw-dist2 .blk { display:flex; align-items:center; gap:8px; padding:7px 11px 7px 9px; background:var(--white); border:1px solid var(--rule); border-radius:8px; box-shadow:0 6px 16px rgba(36,96,168,0.10); opacity:0; }
#s-how .hw-dist2 .blk .ic { width:21px; height:21px; flex:0 0 auto; color:var(--cyan-deep); }
#s-how .hw-dist2 .blk .ic svg{ width:100%; height:100%; }
#s-how .hw-dist2 .blk b { font-family:var(--sans-c); font-weight:600; font-size:12.5px; color:var(--ink); }
#s-how .hw-dist2 .blk .tag { margin-left:auto; font-family:var(--mono); font-size:8px; letter-spacing:0.06em; text-transform:uppercase; color:var(--ink-muted); }
#s-how .hw-dist2 .blk.office { border-top:3px solid var(--cyan-deep); margin-bottom:14px; }
#s-how .hw-dist2 .blk.office .tag { color:var(--cyan-deep); font-weight:700; }
#s-how .hw-dist2 .subrow { display:flex; align-items:center; gap:8px; margin:10px 0 0 22px; }
#s-how .hw-dist2 .subrow .sub { font-family:var(--mono); font-size:8px; letter-spacing:0.1em; text-transform:uppercase; color:var(--ink-muted); }
#s-how .hw-dist2 .blk.gov { border-top:3px solid var(--blue); flex:1; }
#s-how .hw-dist2 .blk.gov .ic{ color:var(--blue); }
#s-how .hw-dist2 .blk.sm { padding:6px 10px; }
#s-how .hw-dist2 .dl { position:absolute; left:14px; width:2px; background:var(--rule-strong); opacity:0; transform-origin:top; }
#s-how .hw-dist2 .dl1 { top:46px; height:22px; }
#s-how .hw-dist2 .dl2 { top:98px; height:22px; }

/* BIG curve from Office down to the Dashboard */
#s-how .hw-bigcurve { position:absolute; left:0; right:0; top:118px; height:150px; pointer-events:none; z-index:1; }
#s-how .hw-bigcurve svg { width:100%; height:100%; overflow:visible; }
#s-how .hw-bigcurve path { fill:none; stroke:var(--cyan-deep); stroke-width:2.4; stroke-linecap:round; stroke-dasharray:1000; stroke-dashoffset:1000; }
#s-how .hw-bigcurve .bc-dot { fill:var(--cyan); filter:drop-shadow(0 0 5px var(--cyan)); opacity:0; }

/* DASHBOARD — big box at the bottom (the app visualization, any product) */
#s-how .hw-dashboard { position:relative; margin:128px auto 0; width:84%; max-width:760px; background:var(--white); border:1px solid var(--rule-strong);
  border-radius:14px; box-shadow:0 22px 50px rgba(36,96,168,0.16); padding:16px 20px 18px; opacity:0; transform:scale(.94) translateY(14px); z-index:2; }
#s-how .dash-head { display:flex; align-items:center; gap:10px; margin-bottom:14px; }
#s-how .dash-head .dh-dot { width:8px; height:8px; border-radius:50%; background:#22A06D; box-shadow:0 0 0 3px rgba(34,160,109,.16); }
#s-how .dash-head .dh-t { font-family:var(--sans-c); font-weight:700; font-size:15px; color:var(--ink); }
#s-how .dash-head .dh-products { margin-left:auto; display:flex; gap:8px; align-items:center; }
#s-how .dash-head .dh-products span { font-family:var(--mono); font-size:8.5px; letter-spacing:0.08em; text-transform:uppercase; color:var(--ink-muted); display:flex; align-items:center; gap:5px; }
#s-how .dash-head .dh-products i { width:7px; height:7px; border-radius:2px; background:var(--cyan); display:inline-block; }
#s-how .dash-grid { display:grid; grid-template-columns:auto 1.4fr 1fr; gap:22px; align-items:center; }
#s-how .dg-gauge { width:78px; height:78px; }
#s-how .dg-gauge .gbg { fill:none; stroke:var(--cyan-soft); stroke-width:8; }
#s-how .dg-gauge .garc { fill:none; stroke:var(--cyan-deep); stroke-width:8; stroke-linecap:round; stroke-dasharray:201; stroke-dashoffset:201; transform:rotate(-90deg); transform-origin:40px 40px; }
#s-how .dg-gauge .gtxt { font-family:var(--sans-c); font-weight:700; font-size:16px; fill:var(--ink); }
#s-how .dg-chart { height:74px; position:relative; }
#s-how .dg-chart svg { width:100%; height:100%; overflow:visible; }
#s-how .dg-chart .area { fill:rgba(46,169,230,0.12); opacity:0; }
#s-how .dg-chart .line { fill:none; stroke:var(--cyan-deep); stroke-width:2.4; stroke-dasharray:300; stroke-dashoffset:300; }
#s-how .dg-bars { display:flex; align-items:flex-end; gap:7px; height:74px; }
#s-how .dg-bars i { flex:1; background:linear-gradient(180deg,var(--cyan),var(--cyan-deep)); border-radius:2px 2px 0 0; height:0; }
#s-how .dash-foot { margin-top:13px; padding-top:11px; border-top:1px solid var(--rule); font-family:var(--sans); font-size:12.5px; color:var(--ink-muted); }
#s-how .dash-foot b { color:var(--ink); font-weight:600; }

/* ===== TIMELINE: build ONCE and HOLD (forwards); ambient flow loops. #s-how.in ===== */
#s-how .how-walk .iphone, #s-how .hw-dist2 .blk, #s-how .hw-dashboard, #s-how .src .src-card { opacity:0; }
#s-how.in .src .src-card { animation: hw-in .45s var(--ease-d) both; }
#s-how.in .src.qr .src-card { animation-delay:.1s; }
#s-how.in .src.rfid .src-card { animation-delay:.3s; }
#s-how.in .src .src-scan { animation: hw-srcscan 2.4s ease-in-out .5s infinite; }
#s-how.in .hw-fill .p3 .iphone { animation: hw-in .45s var(--ease-d) .6s forwards; }
#s-how.in .hw-fill .p2 .iphone { animation: hw-in .45s var(--ease-d) .82s forwards; }
#s-how.in .hw-fill .p1 .iphone { animation: hw-in .45s var(--ease-d) 1.04s forwards; }
#s-how.in .hw-fill .bar::after { animation: hw-fill-bar .9s ease 1.3s forwards; }
#s-how.in .hw-fill .v.ok { animation: hw-fade .4s ease 1.5s forwards; }
#s-how.in .hw-sign .iphone { animation: hw-in .45s var(--ease-d) 1.7s forwards; }
#s-how.in .sig-pad path { animation: hw-draw .9s ease 1.95s forwards; }
#s-how.in .sig-seal { animation: hw-fade .4s ease 2.7s forwards; }
#s-how.in .hw-dist2 .blk.office { animation: hw-blkin .45s var(--ease-d) 2.5s forwards; }
#s-how.in .hw-dist2 .dl1 { animation: hw-dl .4s ease 2.85s forwards; }
#s-how.in .hw-dist2 .blk.gov.g1 { animation: hw-blkin .4s var(--ease-d) 3.0s forwards; }
#s-how.in .hw-dist2 .dl2 { animation: hw-dl .4s ease 3.15s forwards; }
#s-how.in .hw-dist2 .blk.gov.g2 { animation: hw-blkin .4s var(--ease-d) 3.3s forwards; }
#s-how.in .hw-bigcurve path { animation: hw-bigdraw 1.1s ease 3.5s forwards; }
#s-how.in .hw-bigcurve .bc-dot { offset-path: path("__BIGPATH__"); animation: hw-bcflow 2.6s linear 5.0s infinite; }
#s-how.in .hw-dashboard { animation: hw-dashpop .6s cubic-bezier(.34,1.56,.64,1) 4.5s forwards; }
#s-how.in .dg-gauge .garc { animation: hw-gauge 1s ease 5.0s forwards; }
#s-how.in .dg-chart .line { animation: hw-draw2 1.1s ease 5.1s forwards; }
#s-how.in .dg-chart .area { animation: hw-fade .6s ease 5.8s forwards; }
#s-how.in .dg-bars i { animation: hw-bar .6s ease 5.2s forwards; }
#s-how.in .dg-bars i:nth-child(1){--bh:48%}#s-how.in .dg-bars i:nth-child(2){--bh:76%}#s-how.in .dg-bars i:nth-child(3){--bh:40%}
#s-how.in .dg-bars i:nth-child(4){--bh:64%}#s-how.in .dg-bars i:nth-child(5){--bh:88%}#s-how.in .dg-bars i:nth-child(6){--bh:56%}
#s-how.in .hw-conn::after { animation: hw-cflow 2s linear 1s infinite; }
@keyframes hw-in { 0%{opacity:0;transform:translateY(14px) scale(.96)} 100%{opacity:1;transform:none} }
@keyframes hw-fade { to{opacity:1} }
@keyframes hw-fill-bar { from{width:0} to{width:76%} }
@keyframes hw-draw { to{stroke-dashoffset:0} }
@keyframes hw-draw2 { to{stroke-dashoffset:0} }
@keyframes hw-blkin { from{opacity:0;transform:translateX(-8px)} to{opacity:1;transform:none} }
@keyframes hw-dl { from{opacity:0;transform:scaleY(0)} to{opacity:1;transform:scaleY(1)} }
@keyframes hw-bigdraw { to{stroke-dashoffset:0} }
@keyframes hw-dashpop { 0%{opacity:0;transform:scale(.94) translateY(14px)} 70%{opacity:1;transform:scale(1.01) translateY(0)} 100%{opacity:1;transform:scale(1) translateY(0)} }
@keyframes hw-gauge { to{stroke-dashoffset:70} }
@keyframes hw-bar { to{height:var(--bh)} }
@keyframes hw-srcscan { 0%{top:10px;opacity:0} 10%{opacity:1} 46%{top:58px;opacity:1} 52%{opacity:0} 53%{top:10px} 100%{top:10px;opacity:0} }
@keyframes hw-cflow { 0%{left:0;opacity:0} 12%{opacity:1} 100%{left:calc(100% - 14px);opacity:0} }
@keyframes hw-bcflow { 0%{offset-distance:0%;opacity:0} 10%{opacity:1} 90%{opacity:1} 100%{offset-distance:100%;opacity:0} }
@media (max-width: 980px){ #s-how .hw-top{flex-wrap:wrap;justify-content:center;gap:22px} #s-how .hw-conn{display:none} #s-how .hw-dashboard{width:100%} }
/* END: s-how walkthrough vB */
'''

# the big curve path (in the .hw-bigcurve overlay coords, ~ full width x 170). office is top-right, dashboard center-bottom.
BIGPATH = "M880 12 C 980 12, 980 90, 700 95 C 360 100, 470 140, 470 150"

def F(l,v,ok=False,bar=False):
    if bar: return f'<div class="fld"><span class="l">{l}</span><div class="bar"></div></div>'
    return f'<div class="fld"><span class="l">{l}</span><span class="v{" ok" if ok else ""}">{v}</span></div>'
def pips(active): return '<div class="tabpips">'+''.join(f'<i class="{"on" if i==active else ""}"></i>' for i in range(4))+'</div>'
def fillp(num,title,fields,active):
    return (f'<div class="iphone"><div class="island"></div><div class="scr"><div class="scr-top">{num}</div>{pips(active)}'
            f'<div class="scr-title">{title}</div><div class="scr-body">{"".join(fields)}</div></div></div>')
SIG='M6 26 C 20 8, 34 8, 44 22 S 64 38, 78 20 S 104 8, 120 24'
BLD='<svg viewBox="0 0 24 24" fill="none"><path d="M3 21V8l9-5 9 5v13" stroke="currentColor" stroke-width="1.7"/><path d="M9 21v-6h6v6" stroke="currentColor" stroke-width="1.7"/></svg>'
PER='<svg viewBox="0 0 24 24" fill="none"><circle cx="12" cy="8" r="3.4" stroke="currentColor" stroke-width="1.7"/><path d="M5 20c0-3.5 3.1-6 7-6s7 2.5 7 6" stroke="currentColor" stroke-width="1.7"/></svg>'
GOVI='<svg viewBox="0 0 24 24" fill="none"><path d="M3 21h18M5 21V10m4 11V10m6 11V10m4 11V10M12 3l8 5H4l8-5z" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/></svg>'

def build(lang):
    en = lang=='en'
    T = dict(
        SCAN='Scan' if en else 'Escanear', SCANs='QR or RFID on the asset' if en else 'QR o RFID en el activo',
        TABS='Tabs' if en else 'Pestañas', TABSs='it fills itself' if en else 'se llena solo',
        SIGN='Sign' if en else 'Firmar', SIGNs='sealed' if en else 'sellado',
        DIST='Distribute' if en else 'Distribuir', DISTs='reports to each party' if en else 'reportes a cada parte',
        OFFICE='Office' if en else 'Oficina', GOV='Government' if en else 'Gobierno', CLIENT='Client' if en else 'Cliente',
        SUB='Subset' if en else 'Subconjunto', P='100%',
        DASH='Dashboard' if en else 'Tablero',
        DASHfoot=('One visualization for any product, a heating unit, a herd of cattle, a fleet.' if en
                  else 'Una visualización para cualquier producto: una caldera, un rodeo, una flota.'))
    if en:
        p1=fillp('Tab · Measurements','Measurements',[F('Pressure','',bar=True),F('Flow','',bar=True),F('Inlet','23.4°C'),F('Status','Pass',ok=True)],3)
        p2=fillp('Tab · Work order','WO-2026-0418',[F('Customer','Hotel Esplendido'),F('Equipment','HVAC-12B'),F('Time','14:02',ok=True)],1)
        p3=fillp('Tab · Asset','Asset record',[F('Owner','Esplendido S.A.'),F('Site','Rooftop')],0)
    else:
        p1=fillp('Pestaña · Medidas','Medidas',[F('Presión','',bar=True),F('Caudal','',bar=True),F('Entrada','23.4°C'),F('Estado','OK',ok=True)],3)
        p2=fillp('Pestaña · Orden','OT-2026-0418',[F('Cliente','Hotel Esplendido'),F('Equipo','HVAC-12B'),F('Hora','14:02',ok=True)],1)
        p3=fillp('Pestaña · Activo','Registro del activo',[F('Dueño','Esplendido S.A.'),F('Sitio','Azotea')],0)

    scan=(f'<div class="hw-st hw-scan"><div class="scan-sources">'
      f'<div class="src qr"><div class="src-card">{QR}<div class="src-scan"></div></div><span class="src-lbl">QR</span></div>'
      f'<div class="scan-or">{"or" if en else "o"}</div>'
      f'<div class="src rfid"><div class="src-card">{RFID}<div class="src-scan"></div></div><span class="src-lbl">RFID</span></div>'
      f'</div><div class="hw-cap"><b>{T["SCAN"]}</b><span>{T["SCANs"]}</span></div></div>')
    fill=(f'<div class="hw-st hw-fill"><div class="stack" style="position:relative;width:236px;height:208px">'
      f'<div class="p3" style="position:absolute;top:6px;left:0;transform:scale(.88) rotate(-4deg);transform-origin:bottom left;z-index:1">{p3}</div>'
      f'<div class="p2" style="position:absolute;top:6px;left:62px;transform:scale(.94) rotate(-2deg);transform-origin:bottom left;z-index:2">{p2}</div>'
      f'<div class="p1" style="position:absolute;top:6px;left:128px;transform:rotate(1.5deg);z-index:3">{p1}</div>'
      f'</div><div class="hw-cap"><b>{T["TABS"]}</b><span>{T["TABSs"]}</span></div></div>')
    sign=(f'<div class="hw-st hw-sign sigwrap"><div class="iphone"><div class="island"></div><div class="scr"><div class="sig-screen">'
      f'<div class="scr-top">Tab · Signature</div><div class="sig-pad"><svg viewBox="0 0 126 36"><path d="{SIG}"/></svg></div>'
      f'<div class="sig-seal">{T["SIGNs"]}</div></div></div></div><div class="hw-cap"><b>{T["SIGN"]}</b><span>{T["SIGNs"]}</span></div></div>')
    dist=(f'<div class="hw-st hw-dist2">'
      f'<span class="dl dl1"></span><span class="dl dl2"></span>'
      f'<div class="blk office"><span class="ic">{BLD}</span><b>{T["OFFICE"]}</b><span class="tag">{T["P"]}</span></div>'
      f'<div class="subrow"><span class="sub">{T["SUB"]}</span><div class="blk gov g1"><span class="ic">{GOVI}</span><b>{T["GOV"]}</b></div></div>'
      f'<div class="subrow"><span class="sub">{T["SUB"]}</span><div class="blk gov g2"><span class="ic">{PER}</span><b>{T["CLIENT"]}</b></div></div>'
      f'<div class="hw-cap" style="margin-top:14px"><b>{T["DIST"]}</b><span>{T["DISTs"]}</span></div></div>')
    bigcurve=(f'<div class="hw-bigcurve"><svg viewBox="0 0 1000 170" preserveAspectRatio="none">'
      f'<defs><marker id="bc-arrow" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="var(--cyan-deep)"/></marker></defs>'
      f'<path d="{BIGPATH}" marker-end="url(#bc-arrow)"/><circle class="bc-dot" r="4"/></svg></div>')
    dash=(f'<div class="hw-dashboard"><div class="dash-head"><span class="dh-dot"></span><span class="dh-t">{T["DASH"]}</span>'
      f'<span class="dh-products"><span><i></i>{"HVAC" if en else "HVAC"}</span><span><i></i>{"Cattle" if en else "Ganado"}</span><span><i></i>XtraPush</span></span></div>'
      f'<div class="dash-grid">'
      f'<svg class="dg-gauge" viewBox="0 0 80 80"><circle class="gbg" cx="40" cy="40" r="32"/><circle class="garc" cx="40" cy="40" r="32"/><text class="gtxt" x="40" y="46" text-anchor="middle">68%</text></svg>'
      f'<div class="dg-chart"><svg viewBox="0 0 200 74" preserveAspectRatio="none"><path class="area" d="M0 60 L30 48 L60 54 L95 30 L130 38 L170 16 L200 22 L200 74 L0 74 Z"/><path class="line" d="M0 60 L30 48 L60 54 L95 30 L130 38 L170 16 L200 22"/></svg></div>'
      f'<div class="dg-bars"><i></i><i></i><i></i><i></i><i></i><i></i></div>'
      f'</div><div class="dash-foot"><b>{T["DASH"]}.</b> {T["DASHfoot"]}</div></div>')
    return (f'<div class="how-walk" aria-hidden="true">'
            f'<div class="hw-top">{scan}<div class="hw-conn"></div>{fill}<div class="hw-conn"></div>{sign}<div class="hw-conn"></div>{dist}</div>'
            f'{bigcurve}{dash}</div>')

CSS_OUT = CSS.replace('__BIGPATH__', BIGPATH)
region = re.compile(r'<div class="how-(?:walk|diagram)"[^>]*>.*?\n  </div>\n</section>', re.DOTALL)
oldcss = re.compile(r'/\* BEGIN: s-how walkthrough vB.*?/\* END: s-how walkthrough vB \*/\n?', re.DOTALL)
# also strip the old standalone scan CSS blocks if present
oldscan = re.compile(r'/\* --- Scan[^\n]*--- \*/.*?(?=/\* |\n#s-how |</style>)', re.DOTALL)
for path,lang in [('/Users/frankheijckers/code/mision-digital-onudi/index-en.html','en'),
                  ('/Users/frankheijckers/code/mision-digital-onudi/index.html','es')]:
    p=pathlib.Path(path); t=p.read_text()
    t=oldcss.sub('', t)
    t=oldscan.sub('', t)
    t2,n=region.subn(build(lang)+'\n  </div>\n</section>', t, count=1)
    assert n==1, f'region {n} in {path}'
    se=t2.find('</style>'); t2=t2[:se]+CSS_OUT+t2[se:]
    p.write_text(t2); print(f'  {path}: v5 (sketch framework) applied')
