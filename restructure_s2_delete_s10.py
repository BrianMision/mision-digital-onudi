#!/usr/bin/env python3
"""Major restructure:
1. Delete s10 zoom-out slide entirely.
2. Rewrite s2 with NEW quote (Lima Declaration) + clear product info + compact zoom mini-visual.
3. Update counters to /13.
"""
import re, pathlib

# ============================================================
# 1. Delete s10
# ============================================================
def delete_s10(text):
    pattern = re.compile(r'(<!--\s*10\s*·.*?-->\s*\n)?<section class="slide alt" id="s10".*?</section>\s*\n?', re.DOTALL)
    new_text, n = pattern.subn('', text)
    return new_text, n

# ============================================================
# 2. Rewrite s2 — new quote + product clarity + mini zoom visual
# ============================================================

S2_EN_NEW = '''<!-- 2 · THE PURPOSE — Product intro + Lima quote + compact zoom visual -->
<section class="slide alt" id="s2" data-label="The Product" aria-label="The Product">
  <style>
    #s2 .s2-grid { display: grid; grid-template-columns: 1.1fr 1fr; gap: 56px; align-items: start; }
    #s2 .s2-quote { padding-right: 8px; border-right: 1px solid var(--rule); }
    #s2 .s2-quote-mark { font-family: var(--serif, var(--sans-c)); font-weight: 300; font-size: 64px; color: var(--cyan-deep); line-height: 0.7; margin-bottom: 8px; }
    #s2 .s2-quote-text { font-family: var(--sans-c); font-weight: 500; font-size: clamp(22px, 2vw, 30px); line-height: 1.32; color: var(--ink); letter-spacing: -0.005em; max-width: 36ch; }
    #s2 .s2-quote-cite { margin-top: 22px; font-family: var(--sans); font-size: 14px; line-height: 1.55; color: var(--ink-muted); max-width: 38ch; }
    #s2 .s2-quote-cite::before { content: "— "; color: var(--cyan-deep); font-weight: 600; }
    #s2 .s2-quote-cite i { font-style: italic; color: var(--ink); }
    #s2 .s2-product { padding-left: 8px; }
    #s2 .s2-product-h { font-family: var(--sans-c); font-weight: 600; font-size: clamp(28px, 3.2vw, 44px); line-height: 1.1; color: var(--ink); letter-spacing: -0.01em; margin-bottom: 22px; }
    #s2 .s2-product-h .em { color: var(--cyan-deep); }
    #s2 .s2-product-body { font-family: var(--sans); font-size: 17px; line-height: 1.62; color: var(--ink-body); max-width: 52ch; margin-bottom: 24px; }
    #s2 .s2-product-body b { color: var(--ink); font-weight: 600; }
    #s2 .s2-bullets { list-style: none; padding: 0; margin: 0 0 28px; display: flex; flex-direction: column; gap: 9px; }
    #s2 .s2-bullets li { display: grid; grid-template-columns: 18px 1fr; gap: 12px; align-items: baseline; font-family: var(--sans); font-size: 14.5px; line-height: 1.5; color: var(--ink-body); }
    #s2 .s2-bullets li::before { content: ""; width: 6px; height: 6px; border-radius: 50%; background: var(--cyan-deep); transform: translateY(8px); }
    #s2 .s2-bullets li b { color: var(--ink); font-weight: 600; }
    #s2 .s2-zoom { margin-top: 32px; padding-top: 22px; border-top: 1px solid var(--rule); }
    #s2 .s2-zoom-h { font-family: var(--mono); font-size: 10px; letter-spacing: 0.22em; text-transform: uppercase; color: var(--cyan-deep); margin-bottom: 14px; }
    #s2 .s2-zoom-stage { display: grid; grid-template-columns: 1fr 18px 1fr 18px 1fr; align-items: center; gap: 12px; }
    #s2 .s2-zoom-step { display: flex; flex-direction: column; align-items: center; gap: 10px; }
    #s2 .s2-zoom-vis {
      width: 100%; max-width: 130px; height: 54px;
      display: flex; align-items: end; justify-content: center; gap: 4px;
      padding: 8px; border: 1px solid var(--rule);
      border-radius: 3px; background: var(--white); position: relative;
      box-shadow: 0 4px 12px rgba(36,96,168,0.06);
    }
    #s2 .s2-zoom-vis--field { gap: 5px; }
    #s2 .s2-zoom-vis--field span { width: 4px; height: 4px; border-radius: 50%; background: var(--cyan); box-shadow: 0 0 4px rgba(46,169,230,0.4); }
    #s2 .s2-zoom-vis--office span { width: 9px; height: 9px; background: linear-gradient(135deg, var(--cyan), var(--cyan-deep)); border-radius: 1px; }
    #s2 .s2-zoom-vis--sector { padding: 8px 10px; align-items: end; gap: 3px; }
    #s2 .s2-zoom-vis--sector span { flex: 1; background: linear-gradient(180deg, var(--cyan), var(--cyan-deep)); border-radius: 1px 1px 0 0; }
    #s2 .s2-zoom-label { text-align: center; line-height: 1.45; }
    #s2 .s2-zoom-label b { display: block; color: var(--ink); font-family: var(--sans-c); font-size: 13px; font-weight: 600; margin-bottom: 2px; }
    #s2 .s2-zoom-label span { display: block; font-family: var(--mono); font-size: 9.5px; letter-spacing: 0.12em; text-transform: uppercase; color: var(--ink-muted); }
    #s2 .s2-zoom-arrow { font-family: var(--sans-c); color: var(--cyan-deep); font-size: 18px; font-weight: 300; text-align: center; }
    @media (max-width: 900px) {
      #s2 .s2-grid { grid-template-columns: 1fr; gap: 36px; }
      #s2 .s2-quote { border-right: none; border-bottom: 1px solid var(--rule); padding-bottom: 24px; padding-right: 0; }
      #s2 .s2-zoom-stage { grid-template-columns: 1fr; gap: 16px; }
      #s2 .s2-zoom-arrow { display: none; }
    }
  </style>
  <div class="slide-inner">
    <div class="kicker r-up">The Product</div>
    <div class="s2-grid">
      <div class="s2-quote r-up" data-delay style="--d:.1s;">
        <div class="s2-quote-mark">"</div>
        <div class="s2-quote-text">Inclusive and sustainable industrial development is the principal driver of sustainable development.</div>
        <div class="s2-quote-cite"><i>Lima Declaration</i>, UNIDO, 2013, reaffirmed 2015</div>
      </div>
      <div class="s2-product r-up" data-delay style="--d:.35s;">
        <h2 class="s2-product-h">We make that development <span class="em">verifiable</span>.</h2>
        <p class="s2-product-body">Misión Digital turns the act of work into <b>signed evidence</b>. One QR per work order, eight tabs in one view, every signature stamps a record that an auditor can read.</p>
        <ul class="s2-bullets">
          <li><span><b>One QR</b> per piece of equipment, per work order.</span></li>
          <li><span><b>Eight tabs</b> for the eight things every job needs: customer, scope, equipment, docs, measurements, verification, intervention, signature.</span></li>
          <li><span><b>One signed record,</b> rolled up across the field, the office, and the sector.</span></li>
        </ul>
        <div class="s2-zoom">
          <div class="s2-zoom-h">The same record, at three altitudes</div>
          <div class="s2-zoom-stage">
            <div class="s2-zoom-step">
              <div class="s2-zoom-vis s2-zoom-vis--field"><span></span><span></span><span></span></div>
              <div class="s2-zoom-label"><b>Field</b><span>one signed act</span></div>
            </div>
            <span class="s2-zoom-arrow">→</span>
            <div class="s2-zoom-step">
              <div class="s2-zoom-vis s2-zoom-vis--office"><span></span><span></span><span></span><span></span></div>
              <div class="s2-zoom-label"><b>Office</b><span>bundled orders</span></div>
            </div>
            <span class="s2-zoom-arrow">→</span>
            <div class="s2-zoom-step">
              <div class="s2-zoom-vis s2-zoom-vis--sector"><span style="height:55%"></span><span style="height:78%"></span><span style="height:45%"></span><span style="height:90%"></span><span style="height:60%"></span></div>
              <div class="s2-zoom-label"><b>Sector</b><span>industry pattern</span></div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>'''

S2_ES_NEW = '''<!-- 2 · EL PRODUCTO — Intro de producto + cita de Lima + zoom compacto -->
<section class="slide alt" id="s2" data-label="El Producto" aria-label="El Producto">
  <style>
    #s2 .s2-grid { display: grid; grid-template-columns: 1.1fr 1fr; gap: 56px; align-items: start; }
    #s2 .s2-quote { padding-right: 8px; border-right: 1px solid var(--rule); }
    #s2 .s2-quote-mark { font-family: var(--serif, var(--sans-c)); font-weight: 300; font-size: 64px; color: var(--cyan-deep); line-height: 0.7; margin-bottom: 8px; }
    #s2 .s2-quote-text { font-family: var(--sans-c); font-weight: 500; font-size: clamp(22px, 2vw, 30px); line-height: 1.32; color: var(--ink); letter-spacing: -0.005em; max-width: 36ch; }
    #s2 .s2-quote-cite { margin-top: 22px; font-family: var(--sans); font-size: 14px; line-height: 1.55; color: var(--ink-muted); max-width: 38ch; }
    #s2 .s2-quote-cite::before { content: "— "; color: var(--cyan-deep); font-weight: 600; }
    #s2 .s2-quote-cite i { font-style: italic; color: var(--ink); }
    #s2 .s2-product { padding-left: 8px; }
    #s2 .s2-product-h { font-family: var(--sans-c); font-weight: 600; font-size: clamp(28px, 3.2vw, 44px); line-height: 1.1; color: var(--ink); letter-spacing: -0.01em; margin-bottom: 22px; }
    #s2 .s2-product-h .em { color: var(--cyan-deep); }
    #s2 .s2-product-body { font-family: var(--sans); font-size: 17px; line-height: 1.62; color: var(--ink-body); max-width: 52ch; margin-bottom: 24px; }
    #s2 .s2-product-body b { color: var(--ink); font-weight: 600; }
    #s2 .s2-bullets { list-style: none; padding: 0; margin: 0 0 28px; display: flex; flex-direction: column; gap: 9px; }
    #s2 .s2-bullets li { display: grid; grid-template-columns: 18px 1fr; gap: 12px; align-items: baseline; font-family: var(--sans); font-size: 14.5px; line-height: 1.5; color: var(--ink-body); }
    #s2 .s2-bullets li::before { content: ""; width: 6px; height: 6px; border-radius: 50%; background: var(--cyan-deep); transform: translateY(8px); }
    #s2 .s2-bullets li b { color: var(--ink); font-weight: 600; }
    #s2 .s2-zoom { margin-top: 32px; padding-top: 22px; border-top: 1px solid var(--rule); }
    #s2 .s2-zoom-h { font-family: var(--mono); font-size: 10px; letter-spacing: 0.22em; text-transform: uppercase; color: var(--cyan-deep); margin-bottom: 14px; }
    #s2 .s2-zoom-stage { display: grid; grid-template-columns: 1fr 18px 1fr 18px 1fr; align-items: center; gap: 12px; }
    #s2 .s2-zoom-step { display: flex; flex-direction: column; align-items: center; gap: 10px; }
    #s2 .s2-zoom-vis {
      width: 100%; max-width: 130px; height: 54px;
      display: flex; align-items: end; justify-content: center; gap: 4px;
      padding: 8px; border: 1px solid var(--rule);
      border-radius: 3px; background: var(--white); position: relative;
      box-shadow: 0 4px 12px rgba(36,96,168,0.06);
    }
    #s2 .s2-zoom-vis--field { gap: 5px; }
    #s2 .s2-zoom-vis--field span { width: 4px; height: 4px; border-radius: 50%; background: var(--cyan); box-shadow: 0 0 4px rgba(46,169,230,0.4); }
    #s2 .s2-zoom-vis--office span { width: 9px; height: 9px; background: linear-gradient(135deg, var(--cyan), var(--cyan-deep)); border-radius: 1px; }
    #s2 .s2-zoom-vis--sector { padding: 8px 10px; align-items: end; gap: 3px; }
    #s2 .s2-zoom-vis--sector span { flex: 1; background: linear-gradient(180deg, var(--cyan), var(--cyan-deep)); border-radius: 1px 1px 0 0; }
    #s2 .s2-zoom-label { text-align: center; line-height: 1.45; }
    #s2 .s2-zoom-label b { display: block; color: var(--ink); font-family: var(--sans-c); font-size: 13px; font-weight: 600; margin-bottom: 2px; }
    #s2 .s2-zoom-label span { display: block; font-family: var(--mono); font-size: 9.5px; letter-spacing: 0.12em; text-transform: uppercase; color: var(--ink-muted); }
    #s2 .s2-zoom-arrow { font-family: var(--sans-c); color: var(--cyan-deep); font-size: 18px; font-weight: 300; text-align: center; }
    @media (max-width: 900px) {
      #s2 .s2-grid { grid-template-columns: 1fr; gap: 36px; }
      #s2 .s2-quote { border-right: none; border-bottom: 1px solid var(--rule); padding-bottom: 24px; padding-right: 0; }
      #s2 .s2-zoom-stage { grid-template-columns: 1fr; gap: 16px; }
      #s2 .s2-zoom-arrow { display: none; }
    }
  </style>
  <div class="slide-inner">
    <div class="kicker r-up">El Producto</div>
    <div class="s2-grid">
      <div class="s2-quote r-up" data-delay style="--d:.1s;">
        <div class="s2-quote-mark">"</div>
        <div class="s2-quote-text">El desarrollo industrial inclusivo y sostenible es el principal motor del desarrollo sostenible.</div>
        <div class="s2-quote-cite"><i>Declaración de Lima</i>, ONUDI, 2013, reafirmada en 2015</div>
      </div>
      <div class="s2-product r-up" data-delay style="--d:.35s;">
        <h2 class="s2-product-h">Nosotros lo hacemos <span class="em">verificable</span>.</h2>
        <p class="s2-product-body">Misión Digital convierte el acto de trabajo en <b>evidencia firmada</b>. Un QR por orden de trabajo, ocho pestañas en una sola vista, cada firma sella un registro que un auditor puede leer.</p>
        <ul class="s2-bullets">
          <li><span><b>Un QR</b> por cada equipo, por cada orden de trabajo.</span></li>
          <li><span><b>Ocho pestañas</b> para las ocho cosas que toda intervención necesita: cliente, alcance, equipo, documentos, medidas, verificación, intervención, firma.</span></li>
          <li><span><b>Un registro firmado,</b> agregado a través del campo, la oficina y el sector.</span></li>
        </ul>
        <div class="s2-zoom">
          <div class="s2-zoom-h">El mismo registro, a tres altitudes</div>
          <div class="s2-zoom-stage">
            <div class="s2-zoom-step">
              <div class="s2-zoom-vis s2-zoom-vis--field"><span></span><span></span><span></span></div>
              <div class="s2-zoom-label"><b>Campo</b><span>un acto firmado</span></div>
            </div>
            <span class="s2-zoom-arrow">→</span>
            <div class="s2-zoom-step">
              <div class="s2-zoom-vis s2-zoom-vis--office"><span></span><span></span><span></span><span></span></div>
              <div class="s2-zoom-label"><b>Oficina</b><span>órdenes agrupadas</span></div>
            </div>
            <span class="s2-zoom-arrow">→</span>
            <div class="s2-zoom-step">
              <div class="s2-zoom-vis s2-zoom-vis--sector"><span style="height:55%"></span><span style="height:78%"></span><span style="height:45%"></span><span style="height:90%"></span><span style="height:60%"></span></div>
              <div class="s2-zoom-label"><b>Sector</b><span>patrón industrial</span></div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>'''

# ============================================================
# Apply
# ============================================================

def apply(path, is_en):
    p = pathlib.Path(path)
    txt = p.read_text()

    # 1. Delete s10
    txt, n10 = delete_s10(txt)
    print(f'  s10 deleted: {n10}')

    # 2. Rewrite s2
    s2_pattern = re.compile(r'<!-- 2 ·.*?</section>', re.DOTALL)
    new_s2 = S2_EN_NEW if is_en else S2_ES_NEW
    txt, n2 = s2_pattern.subn(new_s2, txt, count=1)
    print(f'  s2 rewritten: {n2}')

    # 3. Update counter to /13
    txt = re.sub(
        r'(<div class="counter"><span class="now" id="now">01</span> / )\d+',
        r'\g<1>13',
        txt
    )

    p.write_text(txt)
    print(f'  ✓ wrote {path}')

print('=== EN ===')
apply('/Users/frankheijckers/code/mision-digital-onudi/index-en.html', True)
print('=== ES ===')
apply('/Users/frankheijckers/code/mision-digital-onudi/index.html', False)
