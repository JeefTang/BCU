# BCU — Biogas Comprehensive Utilization

Trilingual (English / Bahasa Melayu / 中文) marketing and engineering-tools site for **KSTS K. S. Technical Services** (MPS: R14722/2009, Telupid, Sabah) covering POME biogas power, biomethane upgrading and bio-CNG. Technology partner: **ZERO CARBON ASSISTANT** (Shanghai).

Live: https://jeeftang.github.io/BCU/

## Structure
| Path | Content |
|---|---|
| `/` | English (canonical) |
| `/ms/` | Bahasa Melayu |
| `/zh/` | 中文 |
| `assets/js/calc.js` | Five calculators, pure front-end, no dependencies |
| `build3.py`, `pages3.py`, `build_all.py` | Generator — `python3 build_all.py` rebuilds all three languages |

## Calculators
1. Gas → power &amp; heat
2. Target kW → gas demand
3. Mill throughput → biogas potential
4. Raw biogas → biomethane yield
5. Project economics (payback, NPV, IRR, LCOE)

Constants: CH₄ LHV 35.8 MJ/Nm³ = 9.94 kWh/Nm³; diesel 9.94 kWh/L, 2.68 kg CO₂/L.

## Deploy
GitHub Pages, branch `main`, root. Content pushed through the GitHub Contents API.
