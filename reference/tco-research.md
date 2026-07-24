# TCO Research: HVAC With vs Without Maintenance (15 / 30 years)

**Purpose:** sourced inputs + transparent dollar model for the UNIDO pitch (Maintenanz). Market: Uruguay; EU/US figures used as stated proxies where no Uruguay data exists (user note: cost levels broadly comparable to DE/NL).
**Compiled:** 2026-07-16. **Method:** nominal USD, no discounting, no energy-price escalation (the two roughly offset; see caveats).

**Exchange rates used (BCU interbank, 2026-07-15):** USD 1 = UYU 40.18 · EUR 1 = UYU 46.07 → EUR/USD ≈ 1.147 · GBP/USD ≈ 1.355 (market, 2026-07-15).

---

## 1. Sourced inputs

### 1.1 Lifespan

| Input | Figure | Source | Year | Strength |
|---|---|---|---|---|
| Split/single-package residential AC, median service life | **15 years** | [ASHRAE Equipment Life Expectancy chart](https://www.naturalhandyman.com/iip/infhvac/ASHRAE_Chart_HVAC_Life_Expectancy.pdf) (also [ASHRAE service-life database](https://weblegacy.ashrae.org/publicdatabase/)) | std. ref. | **Strong** (industry standard) |
| AC without maintenance | **10–12 years**; "zero maintenance will, at best, deliver a 10-year lifespan" | [Carrier](https://www.carrier.com/residential/en/us/products/air-conditioners/how-long-do-air-conditioners-last/), [Speer Air](https://speerair.com/maintenance-vs-neglect-the-battle-for-your-acs-life/), [Trane](https://www.trane.com/residential/en/resources/maintenance-tips/air-conditioners/how-long-do-ac-units-last/) | 2024–25 | Medium (manufacturer/trade) |
| AC with annual maintenance | 15–20 years | Carrier / Bryant / Trane (above) | 2024–25 | Medium |
| Gas boiler, typical | **10–15 years** | [Uswitch](https://www.uswitch.com/boilers/guides/how-long-does-a-boiler-last/), [Plumbing Superstore](https://www.plumbingsuperstore.co.uk/help-and-advice/project-guides/heating-and-ventilation/how-long-do-boilers-last/) | 2025 | Medium |
| Boiler: effect of annual service | **adds 5–7 years**; neglect shortens life **30–50%**; well-serviced outlasts neglected by 5–10 yrs | trade consensus ([Endless Energy](https://goendlessenergy.com/blog/boilers/how-long-do-boilers-last-find-out-the-average-lifespan/), [DABONN](https://www.dabonn.com/news/blog/33.html), Uswitch) | 2024–25 | Medium (no gov figure found) |

**Model uses: 15 yrs (maintained) vs 10 yrs (neglected) for both device types** — the mid-point of the claims and consistent with the ASHRAE 15-yr median (median populations include maintained units).

### 1.2 Unit replacement cost (installed)

| Input | Figure | Source | Year | Strength |
|---|---|---|---|---|
| Split AC 12,000 BTU inverter, **Uruguay retail** | **USD 415–639** (Aiwa several models); USD 609 ([Sodimac UY](https://www.sodimac.com.uy/sodimac-uy/product/2467003/aire-acondicionado-12000-btu-inverter-split/2467003/)); UYU 17,990 ≈ USD 448 ([LOi](https://loi.com.uy/electrodomesticos/climatizacion/aires-acondicionados/aire-acondicionado-gold-12000btu-itea12inv)); [Aiwa UY catalog](https://aiwa.com.uy/catalogo/hogar/aires-acondicionados) | 2026 | **Strong** (live listings) |
| Split installation labor, Uruguay | **UYU 2,150–3,400 ≈ USD 54–85** (labor only, by capacity) | [Home Solution UY reference prices](https://homesolution.net/uy/about/preciosreferencia/tecnico-de-aire) | undated | Medium |
| Installation materials (pipe kit, brackets, ducting) | ~USD 100–170 | own estimate (flagged) | — | **Weak** |
| → **Model, UY split installed** | **USD 750** (unit 550 + labor 75 + materials 125) | composite | 2026 | — |
| US single-zone mini-split installed (proxy) | **$2,500–6,000, most ≈ $3,000**; "average 12,000 BTU unit ≈ $3,000" | [HomeAdvisor](https://www.homeadvisor.com/cost/heating-and-cooling/ductless-mini-split-ac/), [Angi](https://www.angi.com/articles/how-much-does-it-cost-install-ductless-mini-split-ac.htm) | 2025 | Strong |
| Gas combi boiler installed, UK | **median £2,300 ≈ $3,100** (2,000 real quotes, Jan–May 2026); typical £2,500–4,000 ≈ $3,400–5,400 | [Heatable](https://heatable.co.uk/new-boilers/advice/new-boiler-costs-explained), [Checkatrade](https://www.checkatrade.com/blog/cost-guides/new-boiler-cost/) | 2026 | **Strong** |
| Gas boiler installed, NL | boiler €800–3,000 + install €800–1,600 → **≈ €2,500–4,000 ≈ $2,900–4,600** | [Zoofy price guides](https://zoofy.nl/en/price-guides/buying-and-installing-boiler/) | 2025 | Medium |
| Gas boiler replacement, US | **$4,000–9,000**; Angi national avg **$5,900** | [HomeAdvisor](https://www.homeadvisor.com/cost/heating-and-cooling/gas-boiler-prices/), [Angi](https://www.angi.com/articles/how-much-does-boiler-installation-cost.htm) | 2025 | Strong |
| → **Model, boiler installed (EU base)** | **USD 3,500** | UK median / NL range | 2025–26 | — |

### 1.3 Annual maintenance cost

| Input | Figure | Source | Year | Strength |
|---|---|---|---|---|
| AC service visit, Uruguay | **UYU 800–1,300 per unit**, recommended 2×/yr; annual plan ≈ half per-visit price | [El Observador](https://www.elobservador.com.uy/nota/-cuanto-cuesta-mantener-el-aire-acondicionado--20189416303) | **2018** | Medium (local but old) |
| AC cleaning/maintenance labor, Uruguay | UYU 600–900 per visit | [Home Solution UY](https://homesolution.net/uy/about/preciosreferencia/tecnico-de-aire) | undated | Medium |
| → **Model, UY AC** | **USD 45/yr** (one professional service ≈ UYU 1,500–1,800 at 2026 prices, owner cleans filters between) | composite | — | — |
| AC tune-up, US (proxy) | $60–200/visit; service contracts **$150–300/yr** | [Angi](https://www.angi.com/articles/ac-service-cost.htm), [HomeAdvisor](https://www.homeadvisor.com/cost/heating-and-cooling/service-maintain-ac-unit/) | 2025–26 | Strong |
| Boiler Wartung, Germany | **€100–250/yr, avg ≈ €130 ≈ $150** | [Enter.de](https://www.enter.de/blog/gasheizung-wartung), [Thermondo](https://www.thermondo.de/info/rat/gas/gasheizung-wartung/), [co2online](https://www.co2online.de/energie-sparen/heizenergie-sparen/heizkosten-sparen/hausbesitzer-heizungswartung/) | 2025 | Strong-ish |
| Boiler onderhoudscontract, NL | basic €90–120/yr; service €130–220/yr; all-in €200–320/yr | [Homedeal](https://www.homedeal.nl/cv-ketel/cv-ketel-onderhoud/), [Werkspot](https://www.werkspot.nl/verwarming/prijzen-kosten/cv-ketel-onderhoud) | 2025–26 | Strong-ish |
| → **Model, boiler** | **USD 150/yr** | DE average / NL mid-contract | 2025 | — |

### 1.4 Repairs

| Input | Figure | Source | Year | Strength |
|---|---|---|---|---|
| HVAC repair, US average | **$350** (range $100–3,000) | [Angi](https://www.angi.com/articles/how-much-hvac-repair-cost.htm) | 2025–26 | Strong |
| Emergency premium | normal $75–150/h vs after-hours **$160–250/h**; call-out fee $50–150; "double or triple" regular rate | Angi / [HomeAdvisor](https://www.homeadvisor.com/cost/heating-and-cooling/repair-an-hvac-system/) / [HomeGuide](https://homeguide.com/costs/hvac-repair-cost) | 2025–26 | Strong |
| Boiler repair, US average | **$425** (typical $190–660) | [HomeAdvisor](https://www.homeadvisor.com/cost/heating-and-cooling/repair-a-boiler/) | 2025 | Strong |
| Reactive vs planned maintenance | reactive costs **3–5×** planned; PM saves **12–18%** vs reactive; PM cuts breakdowns **70–75%** and downtime **35–45%** | [US DOE FEMP O&M Best Practices Guide R3.0](https://www1.eere.energy.gov/femp/pdfs/om_5.pdf), [PNNL O&M](https://www.pnnl.gov/projects/om-best-practices/maintenance-approaches) | std. ref. | **Strong** (US federal) |
| → **Model** | WITHOUT: 1 repair / 5 yrs at emergency-mix price ($150 UY AC / $500 US-EU). WITH: 1 repair / 10 yrs at planned price ($100 UY / $350–425). = only a **50%** breakdown reduction — conservative vs DOE's 70–75% | assumption anchored above | — | — |

### 1.5 Energy

| Input | Figure | Source | Year | Strength |
|---|---|---|---|---|
| Dirty filter (AC) | replacing a dirty filter cuts consumption **5–15%** | US DOE Energy Saver (via [ENERGY STAR maintenance checklist](https://www.energystar.gov/saveathome/heating-cooling/maintenance-checklist), [Entergy](https://www.entergy.com/blog/cost-dirty-air-filters)) | current | **Strong** |
| Dirty condenser coils | up to **+30%** consumption | DOE-attributed, widely cited ([AC Plus](https://acplushvac.com/blog/how-dirty-coils-affect-your-ac-systems-performance/)); same "up to 30%" figure quoted for Uruguay in [El Observador](https://www.elobservador.com.uy/nota/-cuanto-cuesta-mantener-el-aire-acondicionado--20189416303) | — | Medium-strong |
| Refrigerant undercharge | 25% undercharge → **−15% efficiency, −20% capacity**; 12–19% undercharge → −7.6% EER; field data: only **38% of 4,000+ CA systems correctly charged** | [Purdue IRACC study](https://docs.lib.purdue.edu/cgi/viewcontent.cgi?article=2121&context=iracc), [ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0140700712001533), [FSEC](https://publications.energyresearch.ucf.edu/wp-content/uploads/2018/09/FSEC-PF-474-18.pdf) | 2012–18 | **Strong** (peer-reviewed + field) |
| Airflow faults | reduce system efficiency up to **15%** | [ENERGY STAR](https://www.energystar.gov/saveathome/heating-cooling/maintenance-checklist) | current | Strong |
| Unserviced boiler | loses **up to 10%** efficiency (scale/soot); heat-exchanger fouling costs **5–10%+** | [OJ Gas & Heating](https://ojph.co.uk/can-a-boiler-service-reduce-my-energy-bills-and-by-how-much/), [ACHR News](https://www.achrnews.com/articles/133649-optimizing-boiler-performance) | 2016–25 | Medium (trade, not peer-reviewed) |
| → **Model penalties** | **AC neglected: +15%** (conservative composite of filter + coil + charge findings) · **Boiler neglected: +8%** (mid of 5–10%) | composite | — | — |
| Electricity price, Uruguay | Residencial Simple tier 101–600 kWh = **UYU 8.45/kWh + 22% IVA = UYU 10.31 ≈ USD 0.257/kWh** (marginal tier an AC lands in) | [UTE Pliego Tarifario 2026](https://www.ute.com.uy/sites/default/files/docs/Pliego%20Tarifario%20Enero%202026.pdf), [datosUruguay](https://datosuruguay.com/tarifa-electrica/residencial-simple) | 2026 | **Strong** (official) |
| AC consumption, Uruguay | 12,000 BTU: **0.9–1.5 kWh/h**; typical use 6–8 h/day → **140–200 kWh/month in season**; UTE: split heating COP 2.8 = cheapest heating | [Ecool.uy](https://blog.ecool.uy/aire-acondicionado/cuanto-consume-un-aire-acondicionado-de-9000-btu-por-hora-y-por-mes/), [UTE](https://www.ute.com.uy/articulos/la-mejor-opcion-de-calefaccion) | 2026 | Medium |
| → **Model, AC energy** | **900 kWh/yr** (≈6 in-season months × 150 kWh, cooling + heat-pump heating) × $0.257 = **$230/yr** | composite | — | — |
| US home cooling spend (proxy) | national avg **$265/yr** (Southeast $525) | [EIA RECS](https://www.eia.gov/todayinenergy/detail.php?id=36692) | 2015 | Strong but dated → sensitivity uses $300 |
| Annual gas bill, NL | avg **€1,801 ≈ $2,066** (≈1,020–1,110 m³ @ ~€1.33/m³) | [DutchNews](https://www.dutchnews.nl/2025/09/dutch-households-pay-higher-energy-bills-than-their-neighbours/), [Chargee](https://www.chargee.energy/en/blog/661/average-energy-consumption-netherlands-what-is-normal) | 2025 | Medium-strong |
| Annual heating+hot water, DE | **€1,718 ≈ $1,971** (95 m² 2-person apartment, gas) | [Minol heating statistics](https://www.minol.de/en/blog/Statistics-on-heating-cost-accounting-2025-2026/) | 2025 | Strong-ish |
| → **Model, boiler energy** | **$2,000/yr** | NL/DE average | 2025 | — |

---

## 2. Model A — Split AC (12k BTU, Uruguay prices)

**Assumptions:** installed $750 · life 15 yr (with) / 10 yr (without) · maintenance $45/yr · energy $230/yr maintained, +15% neglected (+$34.50/yr) · repairs: with = $10/yr (1×$100 per decade, planned), without = $30/yr (1×$150 per 5 yrs, emergency-mix).

### 30-year horizon

| Line | WITHOUT maintenance | WITH maintenance |
|---|---|---|
| Devices | 3 × $750 (yrs 0, 10, 20) = **$2,250** | 2 × $750 (yrs 0, 15) = **$1,500** |
| Maintenance | $0 | 30 × $45 = **$1,350** |
| Energy | 30 × $264.50 = **$7,935** | 30 × $230.00 = **$6,900** |
| Repairs | 6 × $150 = **$900** | 3 × $100 = **$300** |
| **TOTAL** | **$11,085** | **$10,050** |

**Net savings: $1,035 over 30 years (9.3% of the neglect TCO).**
Self-financing identity (falls out of the inputs): fees $1,350 = avoided 3rd unit $750 + avoided repair premium $600 — an exact wash — so **the entire net saving equals the avoided energy penalty ($1,035)**.

### 15-year horizon

| Line | WITHOUT | WITH |
|---|---|---|
| Devices | 2 × $750 (yrs 0, 10) = $1,500 | 1 × $750 = $750 |
| Maintenance | $0 | 15 × $45 = $675 |
| Energy | 15 × $264.50 = $3,967.50 | 15 × $230 = $3,450 |
| Repairs | 3 × $150 = $450 | 1.5 × $100 = $150 |
| **TOTAL** | **$5,917.50** | **$5,025** |

**Net savings: ≈ $890 simple cash** (≈ $520 if the neglect scenario's half-used 2nd unit gets a $375 residual credit).
**Hypothesis check at 15 yrs: TRUE — 15 years of fees ($675) < the one replacement unit avoided ($750).**

### Sensitivity: same model at EU/US prices (mini-split $3,000 installed, maintenance $150/yr, energy $300/yr, repairs $350/$500)

- 30-yr: WITHOUT $9,000 + $10,350 + $3,000 = **$22,350** vs WITH $6,000 + $4,500 + $9,000 + $1,050 = **$20,550** → **saves $1,800 (8.1%)**.
- 15-yr: WITHOUT $12,675 vs WITH $10,275 → **saves $2,400**; fees $2,250 < avoided unit $3,000. (Simple-cash; boundary artifact makes 15-yr look better than 30-yr — see caveats.)

---

## 3. Model B — Gas boiler (EU prices; boilers are rare in Uruguayan homes, so this model is deliberately EU-grounded)

**Assumptions:** installed $3,500 (UK median £2,300 ≈ $3,100; NL/UK typical range up to $5,400) · life 15/10 yr · maintenance $150/yr · gas $2,000/yr maintained, +8% neglected (+$160/yr) · repairs: with = $42.50/yr (1×$425 per decade), without = $100/yr (1×$500 per 5 yrs, emergency-mix).

### 30-year horizon

| Line | WITHOUT maintenance | WITH maintenance |
|---|---|---|
| Devices | 3 × $3,500 = **$10,500** | 2 × $3,500 = **$7,000** |
| Maintenance | $0 | 30 × $150 = **$4,500** |
| Energy | 30 × $2,160 = **$64,800** | 30 × $2,000 = **$60,000** |
| Repairs | 6 × $500 = **$3,000** | 3 × $425 = **$1,275** |
| **TOTAL** | **$78,300** | **$72,775** |

**Net savings: $5,525 over 30 years (7.1%).**
Non-energy check: fees $4,500 vs avoided boiler $3,500 + avoided repairs $1,725 = $5,225 → **maintenance already pays for itself before counting energy (+$725)**; the avoided gas penalty ($4,800) comes on top.
At **US prices** (boiler $5,900 installed, Angi avg): WITHOUT $85,500 vs WITH $77,575 → **saves $7,925**, and 30 years of fees ($4,500) < the ONE avoided boiler ($5,900) outright.

### 15-year horizon

| Line | WITHOUT | WITH |
|---|---|---|
| Devices | 2 × $3,500 = $7,000 | 1 × $3,500 = $3,500 |
| Maintenance | $0 | 15 × $150 = $2,250 |
| Energy | 15 × $2,160 = $32,400 | 15 × $2,000 = $30,000 |
| Repairs | 3 × $500 = $1,500 | 1.5 × $425 = $637.50 |
| **TOTAL** | **$40,900** | **$36,387.50** |

**Net savings: ≈ $4,510 simple cash** (≈ $2,760 with a $1,750 residual credit for the neglect scenario's half-used 2nd boiler).
**Hypothesis check at 15 yrs: TRUE, comfortably — fees $2,250 vs one avoided boiler $3,500 (1.56× cover).**

---

## 4. Punchlines for the deck (all defensible from the tables)

1. **"Maintenance is self-financing."** Over 30 years, service fees are fully offset by the extra unit you never buy plus the emergency repairs you never pay (AC-UY: $1,350 fees = $750 + $600 exactly; boiler-EU: $4,500 fees vs $5,225 avoided). **The 8–15% energy penalty you avoid is pure profit** — before counting downtime, comfort, warranty and safety.
2. **15-year framing (strongest):** 15 years of maintenance costs less than the single replacement it prevents — AC: $675 vs $750; boiler: $2,250 vs $3,500.
3. **Headline dollars:** 30-yr net savings ≈ **$1,000 per split AC (Uruguay prices)** / **$1,800 (EU-US prices)** and ≈ **$5,500 per gas boiler (EU)** / **$7,900 (US)**. Fleet math for a UNIDO audience: a building with 40 splits ≈ $40–70k saved over 30 yrs; a district with 1,000 boilers ≈ $5.5M.
4. **Energy line:** a neglected AC burns **+15%** electricity (DOE: dirty filter alone 5–15%, dirty coils up to 30%, wrong refrigerant charge −15% efficiency — and 62% of field units are miss-charged); an unserviced boiler burns **up to +10%** gas.
5. **DOE credibility stat:** reactive maintenance costs **3–5×** planned; preventive programs cut breakdowns **70–75%** (our model only assumes 50%).
6. **Safety (boiler, qualitative):** annual service = flue/CO check — the reason UK law mandates annual gas safety checks in rentals; also keeps manufacturer warranties valid.

## 5. Hypothesis verdict (user: "30 yrs of fees ≈ cost of the extra device, más o menos")

- **Boiler: essentially TRUE.** EU: $4,500 fees vs $3,500 device (ratio 1.3 — same ballpark; repairs close the gap). US: fees $4,500 < device $5,900 — true outright.
- **Split AC at Uruguayan hardware prices: NOT true on the device alone at 30 yrs** ($1,350 fees vs $750 device — cheap hardware, cheap labor) — but true the moment avoided repairs are included ($750 + $600 = $1,350, an exact wash). At the 15-yr cut it IS true on the device alone ($675 < $750).
- **Safe formulation for the pitch:** *"Maintenance fees are roughly repaid by avoided replacement and repairs alone; the energy saving — and the safety — come free."*

## 6. Weak points / caveats

1. **Lifespan 15 vs 10 yrs is the load-bearing assumption.** Anchored on ASHRAE's 15-yr median and consistent manufacturer/trade claims (10–12 unmaintained, 15–20 maintained), but there is no controlled study; treat as industry consensus, not measurement.
2. **No discounting, no energy-price escalation** (nominal USD). Discounting shrinks far-future savings; energy inflation grows them — they partially cancel, but a 30-yr undiscounted total overstates present value. For the deck, quote the numbers as nominal totals.
3. **15-yr horizon boundary artifact:** simple-cash counts the neglect scenario's yr-10 replacement in full while its remaining half-life falls outside the window. Residual-adjusted figures are given everywhere; use them if challenged.
4. **Rejected source:** Genz Clima's "Uruguay 2025/26 price guide" (installation UYU 69,000+) is almost certainly mislabeled Argentine pesos — contradicted 20-fold by Home Solution UY (UYU 2,150–3,400 labor). Excluded.
5. **Uruguay maintenance price is thin:** El Observador is 2018 (UYU 800–1,300/visit); Home Solution page is undated. The model's $45/yr assumes ~UYU 1,800 at 2026 prices — conservative (high) vs both sources. MercadoLibre UY blocks direct fetching (HTTP 403), so listing-level service prices could not be pulled.
6. **Boiler +10% efficiency claim is trade-sourced,** not peer-reviewed (unlike the AC-side DOE/Purdue/FSEC evidence, which is solid). Model uses +8% mid-range.
7. **WITHOUT scenario assumes literally $0 spent on care.** Real neglecters still pay occasional gas recharges and cleanings, which would make neglect look worse and maintenance better — the model is conservative in maintenance's favor being understated, not overstated.
8. **Installation-materials cost (USD 100–170) is an own estimate** — the only unsourced input on the AC side.
9. **Boiler model is EU-grounded by design** (gas central heating is rare in Uruguayan homes — supergas/electric/split heating dominate; UTE itself markets the split as the cheapest heater at COP 2.8). Say so on the slide if both models appear side by side.
10. **Not monetized (upside only):** CO/safety risk, voided warranties without annual service, downtime/discomfort during summer failures, refrigerant environmental leakage. All strengthen the case.
