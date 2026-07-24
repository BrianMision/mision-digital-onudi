# SESSION HANDOFF — Misión Digital / Maintenanz / XPRNZ
_Updated 2026-06-19 ~14:26 UYT. Read this in full at the start of the new session, alongside the auto-loaded memory index (MEMORY.md)._

## 0 · First moves in the new session
- **Playwright MCP** is configured at user scope and ✔ connected — it loads at session start, so you should have `browser_navigate` / `browser_click` / `browser_snapshot` / computed-style tools. Confirm by navigating a URL.
- Read this file + the memory files it references. Then continue.
- A restyle pass on the demos was mid-flight when this was written; trust the files on disk and **redo design copying as a PORT** (see §4).

## 1 · Projects (what · where · live)
**A. ONUDI pitch deck** (Misión Digital, for UNIDO / Manuel Albaladejo)
- Repo `~/code/mision-digital-onudi/` — `index.html` (ES, root), `index-en.html` (EN), + the 3 demos below.
- LIVE: **https://mision-digital-onudi.pages.dev** (ES `/`, EN `/index-en.html`).
- 14 slides EN+ES, A2 act-rail standard, slide-2 = vertical two-column walkthrough (text-left + flow-island-right) with "Modular tabs" mini-screens + Proven/Belgium slide. See memory `project_mision_digital_onudi_deck`.

**B. The 3 interactive demos** (hosted on the deck site)
- `/experience.html` — MAIN. Navy "AC Unit" header, top white tabs (Asset/History/Work Order/Measure/Sign-off/Reports), swipeable, technician Sign→Seal flow. The deck slide-2 QR points here.
- `/experience-v2.html` — OPTION TWO: abstract 8-tab guide → Done [Customer·Work unit·Installation·Documentation] → To-do [Measurements·Checklist·Materials] → Signature.
- `/experience-v3.html` — GUIDED: Makkie-robot coach walkthrough (spotlight + speech bubble, replayable "?"). Coach hooks: `#coachAsset/#coachChecklist/#coachMeasure/[data-coach-seal]/#coachReports`.

**C. Maintenanz landing page**
- `~/code/maintenanz-landing/index.html` → LIVE **https://maintenanz-landing.pages.dev**. Rebuilt on the real brand (navy/cyan, Makkie mascot, MAINTENANZ wordmark, IBM Plex). See memory `project_maintenanz_landing`.

## 2 · Deploy (Cloudflare Pages) — see memory `project_cloudflare_deploy`
- Account `brian@mision-digital.com`. Creds in `~/.config/maintenanz/cloudflare.env` (chmod 600). wrangler is also OAuth-authed. Projects: `mision-digital-onudi`, `maintenanz-landing`, `xprnz`, `xprnz-ionic`.
- Deck deploy (CLEAN bundle, not the whole repo):
```
cd ~/code/mision-digital-onudi && rm -rf /tmp/onudi-dist && mkdir /tmp/onudi-dist
cp index.html index-en.html experience.html experience-v2.html experience-v3.html /tmp/onudi-dist/
cp -r assets /tmp/onudi-dist/
set -a; source ~/.config/maintenanz/cloudflare.env; set +a
wrangler pages deploy /tmp/onudi-dist --project-name mision-digital-onudi --branch main
```
- Landing: `wrangler pages deploy <dir> --project-name maintenanz-landing --branch main`.
- CF deploys are FULL-SITE snapshots — every file you want kept must be in the bundle.

## 3 · Design system (real Maintenanz/XPRNZ brand)
- **Colors:** cyan `#00ABE9` (light `#14B2EB`), navy `#06364D` (`#1A465B`), orange `#F58817`, amber `#FFC64C`, green `#1FA138`, red `#C6371B`, greys `#575756`/`#ebebeb`/`#f1f1f1`, tints `#EEF8FD`/`#EAF7FC`/`#D5EEFA`.
- **Font:** IBM Plex Sans (+ IBM Plex Mono for labels). NO Inter/Roboto/Clash.
- **Assets:** `assets/xprnz/` — `logo.png` (MAINTENANZ wordmark badge), `xprnz-blue-transparent.png` (XPRNZ badge), `mision-digital-logo.png`, `makkie-new-workorder.png` (blue robot mascot), `daredevil.png`. Plus `assets/logo-blue.svg` (MD), `assets/logo-white.png` (MD white, for navy bg).

## 4 · ⭐ DESIGN-COPY SOP — PORT, don't restyle (the key lesson)
Generative "rebuild in this style" drifts → poor fidelity. To faithfully copy a design:
1. **Port the real source** — use their actual CSS rules + markup + class names, not a paraphrase. We HAVE the source.
2. **Computed-style extraction** — `getComputedStyle()` per element in a real browser → exact px / color / shadow / box-model → replicate.
3. **Token inventory** — `:root` vars + usage counts.
4. **Pixel-diff QA (non-negotiable)** — screenshot original vs copy at the same viewport, diff, iterate to convergence.
5. **Use Playwright MCP interactively** (navigate, inspect, computed styles, screenshots).

**THE REFERENCE SOURCE (we have the actual XPRNZ code):**
- Airport Ionic app: `~/Downloads/xprnz-uy-airport.zip` → `unzip -oq ~/Downloads/xprnz-uy-airport.zip -d /tmp/xprnz-airport`. **Tabs** = `src/components/ionic2-super-tabs/` (super-tabs, TOP placement, sliding cyan indicator). Theme: `src/theme/variables.scss`, `src/app/app.scss`. MD logo: `src/assets/imgs/mision-digital-logo.png`.
- Live web CSS: `https://xprnz.maintenanz.com/hvac/build/main.css` → saved at **`reference/xprnz-main.css`**.
- Screenshots: **`reference/portal_shot.png`**, **`reference/xprnz_portal.png`**.
- XPRNZ live app: `xprnz.maintenanz.com` → **`/hvac/?language=en` loads the app directly (no pin for the overview)**; the gate pin = `222399`.

## 5 · Immediate priority for the new session
**Redo the demos' tabs + components as a faithful PORT** (not a restyle) of the real XPRNZ: lift the actual super-tabs markup/SCSS + `main.css` card/button/header rules, verified by Playwright **pixel-diff** vs `reference/portal_shot.png`. Then finish the **content scrub** across `experience.html` + `-v2` + `-v3`: remove `Hotel Esplendido` + the `Owner · Esplendido Facilities` row, rename `Rooftop Chiller`→`AC Unit`, neutralize `Roof · Block C`. Redeploy.

## 6 · Open / pending / future
- **v3 bot art:** user will provide more Makkie robot images → swap into `experience-v3.html` (the `<img>` is easy to swap).
- **Theme-park virtual demo (PARKED):** navigable "park" of attractions (Home/HVAC, Gym/weight, Pasture/cattle) where you scan a virtual QR → tab record; replaces the free-trial. Full plan in `CONCEPTS-walkthrough-and-map.md`.
- **Concept/ideas doc:** `~/code/mision-digital-onudi/CONCEPTS-walkthrough-and-map.md` — buyer journey, "map of slides"/lobby index, virtual demo world, the universal-word decision (lean "Asset").

## 7 · How we work (preferences / standing rules)
- Parallel subagents, max fan-out, delegate heavy builds — BUT for design copy use PORT + pixel-diff, not generative restyle.
- First line of every non-trivial reply = `⏱ ~range (klaar rond HH:MM UYT)`, time fetched fresh via `TZ='America/Montevideo' date`.
- Deploy on Cloudflare. frontend-design: distinctive, no AI-slop. EN copy: NO em-dashes (commas).
- Memories: `feedback_parallel_orchestration`, `feedback_time_estimate_each_task`, `feedback_frontend_design`, `feedback_fast_iteration_workflows`, `feedback_local_sources_only`.

## 8 · Dev / test
- Screenshots: Playwright MCP now (preferred), or puppeteer at `/tmp/shotdir/node_modules/puppeteer`.
- browser-sync for the deck (restart if needed): `cd ~/code/mision-digital-onudi && npx --no-install browser-sync start --server --index index-en.html --files "*.html, assets/*" --port 3000 --no-open --no-notify`.
- `/tmp` refs (xprnz-airport, xprnz.css, screenshots) may be wiped on reboot — re-unzip the airport zip + re-fetch main.css; the persistent copies live in `reference/`.
