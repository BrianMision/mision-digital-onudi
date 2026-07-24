# Misión Digital · ONUDI deck — Concept Brainstorm

> **Status: IDEAS ONLY. Nothing here is built yet.** This is the captured + classified
> brainstorm from two voice discussions (the product/experience one and the
> deck-architecture / "map of slides" one). Implementation is deferred until we pick
> what makes the cut. Each idea has a tag, the kernel, why it matters, a *deferred*
> build sketch, and open questions.

---

## ★ A — THE CORE CHALLENGE (the thing everything else serves)

**A1 · "Make it one story."**
After 8+ years, the functionality still resists being clustered into a *single* story
that is simultaneously (a) impressive and (b) intelligible to an average first-timer
("for assholes"). In your head it's "two or three different things I want to say." If
*you* can't combine it cleanly, that unresolved tension transmits to the viewer —
subconsciously — through whatever presentation gets made.
- **Why it matters:** This is the root design constraint. The deck's job is to *resolve*
  the multi-thing tension into one spine, then let the branches hang off it.
- **Open Q:** What is the ONE sentence? (Candidate frame below in B.)

**A2 · "Explain it once."**
It is not difficult, but it is not something people invent for themselves. A newcomer
needs the framing exactly once: *"This same flow works for an HVAC unit, a herd of
cattle, or a fleet."* Then they get it.
- **Build sketch (deferred):** one explicit "this could be ___, ___, or ___" beat,
  placed at the moment the abstract flow first appears.

---

## ★ B — NARRATIVE SPINE: the universal 5-step flow

**B1 · The abstract 5 steps (the generic version you sketched).**
1. **Ingest** — "loading, you get load info / data" (the record arrives)
2. **Enrich** — "adding or manipulating the data" (fill it in / edit)
3. **Secure / Approve** — "securing the data… approve" (sign + seal)
4. **Distribute** — "distribute this data" (to the right parties)
5. **Insights** — "data insights" (the dashboard)
- **Maps to what we already have:** the live slide-2 walkthrough is *already this spine* —
  Scan → Tabs → Sign → Distribute → Dashboard. Just relabel against these 5 verbs.
- **Open Q:** keep product words (Scan/Tabs/Sign) or abstract verbs
  (Ingest/Enrich/Secure/Distribute/Insights), or show both?

**B2 · "General one, then an actual one."**
Show the abstract flow AND a concrete instance. Generic = the teaching version; Actual =
the proof it's real (HVAC record with serial, measurements, pass/fail).
- **Build sketch (deferred):** a toggle / second pass that swaps the same 5-step frame
  from abstract labels to a real HVAC record. Same skeleton, two skins.

---

## ★ C — SLIDE-2 WALKTHROUGH: enrich the experience

**C1 · A REAL scannable QR embedded in the deck → the audience does the experience.**
"What if we also have this QR code here? I scan it, and I actually get those tabs on my
phone — this dummy version — and I can swipe through the tabs." Put a live QR on the
slide; scanning loads a dummy record on the *viewer's own phone* with swipeable tabs.
- **Why it matters:** stops being a pitch, becomes a 30-second hands-on demo. This is the
  single highest-impact idea here.
- **Build sketch (deferred):** static dummy record page (name, serial, history, a few
  swipeable tabs), QR points to it, no backend. Mobile-first, read-only.
- **Ties to:** the "Interactively test it" branch in F, and the two-mode QR idea
  (see memory `project_xtrapush_qr_two_modes`).

**C2 · What the QR carries = the time-saver.**
The QR holds **history + all static info + a name + a serial number**. That payload is
*why it saves time* — you scan the thing and its whole identity + past is just there.
- **Build sketch (deferred):** the dummy record leads with Name + Serial, then History,
  then the live tabs.

**C3 · The tabs are "multi, multi usable."**
The tab stack is the reusable core — same tab pattern carries any object's data.

**C4 · Sign = admin → management handoff.**
The signing step is the third beat; narratively it's where the field/admin work becomes
something management trusts and acts on. Sign = the trust gate.

**C5 · One QR, two readers.**
The same QR can be read by **(a) the tool/app** and **(b) a plain QR reader**. Naming the
two readers separately clarifies *where* each lives, but it also complicates the story —
so it's a "mention, don't dwell" item. (Decide if it earns slide time at all.)

---

## ★ D — THE VOCABULARY PROBLEM (needs a decision)

**D1 · Find a universal word for "device tab."**
On HVAC it's a *device tab*. But cattle aren't devices (you feed them, vaccinate them).
We need one word for *"the nature of the object carrying the data."*
- **Candidates floated:** Product tab · Object tab · Asset tab · (the "thing" tab).
- **Why it matters:** the wrong word silently narrows the product to HVAC. The right word
  is what makes "works for anything" land in one read.
- **Recommendation to decide on:** **"Asset"** is the most universal in industry English
  and already neutral across machines / livestock / fleets. (Decide: Asset vs Object vs
  Product.) — DECISION NEEDED, not yet applied anywhere.

---

## ★ E — THE 30–60 SECOND RULE

**E1 · Whole idea in ≤ 60s, ideally 30s. Shorter is better.**
The experience (and the opening of the deck) must deliver the complete concept inside a
minute. This is a hard budget that governs B, C, and F: if a beat doesn't survive the
60-second cut, it moves to a branch (see F), not the core.

---

## ★ F — DECK ARCHITECTURE: the "map of slides" / lobby directory

**F1 · 13 pages is the point — it is NOT one giant website with this as the core.**
Modular by design: a compact core, and "if you need to know more about X, go to *that*
page." Depth is opt-in, not forced.

**F2 · The first 2–3 sheets tell the WHOLE story.**
Everything after is optional depth. The core is front-loaded; the rest is reference.

**F3 · A page that literally looks like a MAP of slides.**
Core slides in the center, fanning out into labeled branches:
- → **UN / UNIDO alignment** ("learn more about integration with what the U.N. is doing")
- → **Technicals** ("learn more about the technicals")
- → **The interactive experience** ("interactively test it" — the live QR from C1)
- → **FAQs** ("if you have questions, here are FAQs")

**F4 · The office-tower lobby "bells" metaphor (the navigation model).**
You walk into an office tower, see a directory board with every company and a bell for
each. You ring the bell for the one you want and go straight there. The deck should feel
the same: a directory where the viewer self-selects a branch and "rings the bell" to jump
to it.
- **Why it matters:** this is *pull* navigation — the viewer chooses depth — which is the
  structural answer to A1: the core stays one story, the "two or three other things"
  become bells you can ring instead of clutter on the main line.
- **Build sketch (deferred):** a cover/hub slide as a directory; each entry deep-links to
  its section; a persistent way back to the lobby. (This supersedes / merges with the
  earlier A1/A2 side-rail index examples — the "map" is the richer version of that index.)

**F5 · Pull, not push.**
"If you want to know more about this, you can tell them." The presenter answers demand
rather than force-feeding every capability. The bells exist so the asker can self-serve.

---

## ★ G — TIE-INS TO SLIDES WE ALREADY HAVE

**G1 · Field + office work together** ("we have a field and an office, and they work
together") = the existing **System** slide (s7, field+office in sync + real-time
messaging). Reinforce there; don't duplicate on slide 2.

**G2 · The live walkthrough (slide 2)** already embodies B1's spine — it's the
centerpiece the map (F) fans out from.

---

## DECISIONS NEEDED (before any of this gets built)
1. **Universal word** for the object/asset tab (D1): Asset / Object / Product?
2. **Core narrative**: abstract verbs vs product words vs both (B1)?
3. **Live QR experience** (C1): in-scope for this deck, or a branch only?
4. **Map/lobby hub** (F3/F4): replace the planned side-rail index with the map, or do both?
5. **What survives the 60-second core** (E1) vs what becomes a "bell" branch (F4)?

---

## ★ H — THE BUYER JOURNEY (the labeling spine for the page + index)

Phases a visitor moves through when buying an app (differs by product — "a stereo vs matches"):
1. **Awareness** — "What does it do? Does it solve my problem?" Hunting for answers.
2. **Consideration** — features, what I get, how it works → decide buy / not.
3. **Decision / Purchase.**
4. **Onboarding.**
5. **Retention.**
- **Use these as the LABELING + GROUPING system** for the landing page sections AND the deck index/branches (ties to F map-of-slides / lobby bells). This is the "way to label / make it coherent" the user is reaching for.
- Map: Awareness → hero + problem + "what it is"; Consideration → how-it-works, benefits, use-cases, **the virtual demo (try it)**, proof, FAQ, pricing; Decision → CTAs + transparent pricing; Onboarding/Retention → post-sale (the QR sticker kit, setup, the live dashboard).
- The **virtual demo is the centerpiece of Consideration** (and seeds Awareness).

## ★ I — THE VIRTUAL DEMO WORLD = a "theme park of attractions" (the big idea — replaces the free trial)

**Why a normal trial/demo fails for us:** the product's backbone is a PHYSICAL QR sticker. With no sticker on a real asset there's nothing to scan, so a trial/demo account is hollow, and shipping stickers to every tire-kicker doesn't scale. A standard SaaS trial does not fit.
**The insight:** give them the QR *virtually*. Build a navigable environment on the website — a **theme park with attractions**, each attraction an illustrative application of the app, "a showroom / store of the applications." The visitor walks up to an asset, "scans" its virtual QR, and gets the exact tab record. Full scan-and-see experience, no physical sticker, no account. It IS the demo/trial, already on the site. "As good as the real thing — it's just: walk up, scan, see what you get."
**Attractions (each one proves "any asset"):**
- 🏠 **Home** — an HVAC / heating unit
- 🏋️ **Gym** — a weight machine / rack (XtraPush tie-in)
- 🐄 **Pasture / field** — cattle (livestock record)
- (extensible: a fleet vehicle, a building — each new attraction = another vertical proven)
**Why it fits everything above:** lives in Awareness→Consideration; lets them *experience* before buying; reuses `experience.html`'s tab UI as the "what you get" payload; zero trial-account friction; teaches the core scan gesture by keeping a visible QR + scan animation in every attraction.

## ★ J — HOW TO BUILD THE PARK (design approach)

Web app, no native. Fidelity, cheapest → richest:
1. **Illustrated interactive scenes (RECOMMENDED v1):** stylized isometric/illustrated attraction scenes (Home, Gym, Pasture) with a clickable hotspot on each asset → a phone-scan overlay (reticle + scan line) → opens the tab record (reuse `experience.html`). A small park "map"/selector to pick an attraction. Pure HTML/CSS/SVG + light JS. Cheap, fast, on-brand, reuses what we built. "Wouldn't be that hard to develop."
2. **360° panorama** per attraction (rendered/photo) with hotspots — more immersive, more art.
3. **Lightweight 3D** (`three.js` / `<model-viewer>`) — actually walk a room and click objects — more wow, more dev.
4. **Interactive video** (the "click on it" walkthrough described) — pre-rendered tour with clickable moments — polished but rigid.
**Recommendation:** ship (1) as v1; keep the tab payload = existing `experience.html`; evolve to 3D/panorama later for "wow." Architecture: `experience.html` stays the record payload; add `park.html` (or `/demo`) = attraction selector + scenes; each hotspot opens the record seeded with that asset's fixtures (HVAC / gym / cattle). Same host. Becomes the landing page's upgraded "Try the live demo" target.

**Decision needed:** build the park v1 now? which fidelity (illustrated scenes recommended)? Which attractions for v1 (Home + Gym + Pasture)?
