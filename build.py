# -*- coding: utf-8 -*-
"""Build the KSTS bioenergy site (static HTML) for GitHub Pages."""
import os

SITE = "https://jeeftang.github.io/Energy-saving-Calculation"

BRAND = "KSTS"
BRAND_SUB = "Biogas & Bioenergy"

NAV = [
    ("index.html", "Home"),
    ("biogas-to-power.html", "Biogas to Power"),
    ("biomethane.html", "Biomethane &amp; Bio-CNG"),
    ("equipment.html", "Equipment"),
    ("calculator.html", "Engineering Tools"),
    ("about.html", "About KSTS"),
]

LOGO = """<svg width="34" height="34" viewBox="0 0 34 34" fill="none" aria-hidden="true">
<rect width="34" height="34" rx="9" fill="#0c1a26"/>
<path d="M17 6.5c3.6 2.4 6 6.2 6 10.2 0 3.3-2.7 6-6 6s-6-2.7-6-6c0-4 2.4-7.8 6-10.2Z" fill="#0f7a52"/>
<path d="M17 22.7v4.8M11 14.5h12" stroke="#fff" stroke-width="1.6" stroke-linecap="round" opacity=".85"/>
</svg>"""

FAVICON = ("data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 34 34'>"
           "<rect width='34' height='34' rx='9' fill='%230c1a26'/>"
           "<path d='M17 6.5c3.6 2.4 6 6.2 6 10.2 0 3.3-2.7 6-6 6s-6-2.7-6-6c0-4 2.4-7.8 6-10.2Z' fill='%230f7a52'/></svg>")


def head(title, desc, page):
    items = []
    for href, label in NAV:
        cur = ' aria-current="page"' if href == page else ''
        items.append('<li><a href="%s"%s>%s</a></li>' % (href, cur, label))
    nav = "".join(items)
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{SITE}/{page}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="KSTS K. S. Technical Services — Biogas &amp; Bioenergy">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{SITE}/{page}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0c1a26">
<link rel="stylesheet" href="assets/css/style.css">
<link rel="icon" href="{FAVICON}">
<script src="assets/js/site.js" defer></script>
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"Organization","name":"KSTS K. S. Technical Services","alternateName":"KSTS","url":"{SITE}/","description":"Sabah-based biogas and bioenergy contractor delivering POME biogas power plants, biomethane upgrading and bio-CNG systems in Sabah and Sarawak, with technology partner Zero Carbon Assistant.","address":{{"@type":"PostalAddress","streetAddress":"Kg. Nangoh, NT 083017181 (Lot 2), 34 km Off Jalan Simpang Sapi Nangoh, Labuk-Sugut","addressLocality":"Telupid","addressRegion":"Sabah","addressCountry":"MY"}},"contactPoint":{{"@type":"ContactPoint","telephone":"+60 13-883 3833","email":"k.s.t.s_sabah@hotmail.com","contactType":"sales","availableLanguage":["English","Malay","Chinese"]}}}}</script>
</head>
<body>
<header class="site">
  <div class="wrap nav">
    <a class="brand" href="index.html">{LOGO}<span>{BRAND}<small>{BRAND_SUB}</small></span></a>
    <button class="menu-toggle" id="menuToggle" aria-label="Open menu" aria-expanded="false">&#9776;</button>
    <ul id="navList">{nav}</ul>
    <a class="btn cta" href="contact.html">Request a study</a>
  </div>
</header>
"""


FOOTER = """<footer class="site">
  <div class="wrap">
    <div class="fgrid">
      <div>
        <a class="brand" href="index.html" style="color:#fff">""" + LOGO + f"""<span>{BRAND}<small style="color:#9fb4c0">{BRAND_SUB}</small></span></a>
        <p class="small" style="color:#9fb4c0;margin-top:14px">Biogas power, biomethane upgrading and bio-CNG for palm oil mills and agro-industry in Sabah and Sarawak. Technology partner: ZERO CARBON ASSISTANT, Shanghai.</p>
      </div>
      <div>
        <h4>Solutions</h4>
        <ul>
          <li><a href="biogas-to-power.html">POME biogas to power</a></li>
          <li><a href="biomethane.html">Biomethane &amp; bio-CNG</a></li>
          <li><a href="equipment.html">Equipment &amp; scope</a></li>
          <li><a href="calculator.html">Engineering tools</a></li>
        </ul>
      </div>
      <div>
        <h4>Company</h4>
        <ul>
          <li><a href="about.html">About KSTS</a></li>
          <li><a href="about.html#partner">Local partner profile</a></li>
          <li><a href="contact.html">Contact</a></li>
        </ul>
      </div>
      <div>
        <h4>Contact</h4>
        <ul>
          <li>KSTS K. S. Technical Services<br><span class="small">MPS: R14722/2009</span></li>
          <li>Kg. Nangoh, NT 083017181 (Lot 2),<br>34 km Off Jalan Simpang Sapi Nangoh,<br>Labuk&ndash;Sugut, Telupid, Sabah, Malaysia</li>
          <li><a href="mailto:k.s.t.s_sabah@hotmail.com">k.s.t.s_sabah@hotmail.com</a></li>
          <li><a href="tel:+60138833833">+60 13-883 3833</a></li>
        </ul>
      </div>
    </div>
    <div class="copy">
      <span>&copy; 2026 KSTS K. S. Technical Services. All rights reserved.</span>
      <span>Figures on this site are indicative and subject to site data and formal quotation.</span>
    </div>
  </div>
</footer>
</body>
</html>
"""


def write_page(name, title, desc, body):
    html = head(title, desc, name) + body + FOOTER
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), name), "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", name, len(html))


# ---------------------------------------------------------------- index
INDEX = """
<section class="hero">
  <div class="wrap">
    <div class="badge"><i></i> POME biogas &middot; palm biomass &middot; biomethane &middot; Sabah &amp; Sarawak</div>
    <h1>Palm oil mill waste, turned into firm 24/7 power.</h1>
    <p class="lead">KSTS designs, builds and supports biogas power plants and biomethane upgrading systems for palm oil mills and agro-industry across Sabah and Sarawak. We bring the process package, the gas engines and the local statutory know-how &mdash; with our technology partner ZERO CARBON ASSISTANT in Shanghai.</p>
    <div class="hero-actions">
      <a class="btn" href="calculator.html">Size your plant in 30 seconds</a>
      <a class="btn ghost" style="color:#fff;border-color:rgba(255,255,255,.35)" href="contact.html">Send your mill data</a>
    </div>
    <div class="stats">
      <div class="stat"><b>270&ndash;300</b><span>Nm&sup3;/h biogas for a 600 kW set at 60% CH&#8324;</span></div>
      <div class="stat"><b>38&ndash;42%</b><span>Electrical efficiency, gas engine</span></div>
      <div class="stat"><b>&ge;97%</b><span>CH&#8324; biomethane for boilers and bio-CNG</span></div>
      <div class="stat"><b>8,000 h</b><span>Design operating hours per year</span></div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow">What we deliver</p>
      <h2>One contract, from pond cover to grid-tie</h2>
      <p class="lead">Most mills already have the raw material and the pond. What is usually missing is the gas quality control, the engine package and someone accountable for the whole chain. That is the gap we fill.</p>
    </div>
    <div class="grid-3">
      <article class="card prod-card">
        <div>
          <p class="tag">01 &middot; Process</p>
          <h3>Biogas capture &amp; treatment</h3>
          <p>Covered lagoon or CSTR conversion, condensate management, biological plus iron-oxide desulfurisation, chilling and drying, blower and flare station &mdash; sized to the engine&rsquo;s gas specification, not to a catalogue.</p>
        </div>
        <span class="more">See the process &rarr;</span>
      </article>
      <article class="card prod-card">
        <div>
          <p class="tag">02 &middot; Equipment</p>
          <h3>Gas engines 300 kW &ndash; 2 MW</h3>
          <p>Containerised or skid-mounted biogas gensets, 415 V / 50 Hz, parallel-to-grid or island mode, with jacket-water and exhaust heat recovery for the mill&rsquo;s process hot water or boiler feedwater.</p>
        </div>
        <span class="more">Equipment range &rarr;</span>
      </article>
      <article class="card prod-card">
        <div>
          <p class="tag">03 &middot; Delivery</p>
          <h3>EPC, BOO or equipment only</h3>
          <p>Straight equipment supply, full EPC with local civil and mechanical works, or a build-own-operate model where we fund the plant and sell power or gas to the mill under a long-term agreement.</p>
        </div>
        <span class="more">Commercial models &rarr;</span>
      </article>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow">Two ways to monetise the gas</p>
      <h2>Electricity now, biomethane when the boiler matters more</h2>
    </div>
    <div class="grid-2">
      <article class="card">
        <p class="tag">Route A &middot; Power &amp; heat</p>
        <h3>Displace diesel and grid import</h3>
        <p>Many inland Sabah mills run diesel gensets at RM 0.55&ndash;0.75/kWh because the grid is weak or the connection is slow. POME biogas at 60% CH&#8324; can carry a large share of that load at a fraction of the fuel cost, with useful heat as a by-product.</p>
        <ul class="checks">
          <li>Engine electrical output from measured or calculated gas flow</li>
          <li>Heat recovery for boiler feedwater and process hot water</li>
          <li>Island mode or parallel operation with existing diesel sets</li>
        </ul>
        <a class="more" href="biogas-to-power.html" style="color:var(--accent);font-weight:700">Biogas to power &rarr;</a>
      </article>
      <article class="card">
        <p class="tag">Route B &middot; Biomethane</p>
        <h3>Boiler fuel and bio-CNG</h3>
        <p>Where the mill needs boiler fuel more than electricity, POME biogas can be upgraded to &ge;97% CH&#8324; and used in the existing burner, or compressed as bio-CNG and moved by trailer &mdash; a virtual pipeline to sites without a gas grid.</p>
        <ul class="checks">
          <li>PSA, water scrubbing or membrane upgrading</li>
          <li>Compression to 250 bar for tube-trailer delivery</li>
          <li>Burner retrofit support and gas quality guarantees</li>
        </ul>
        <a class="more" href="biomethane.html" style="color:var(--accent);font-weight:700">Biomethane &amp; bio-CNG &rarr;</a>
      </article>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow">Typical design basis</p>
      <h2>What a mill actually gives us</h2>
      <p class="lead">Numbers below are the ranges we use for pre-feasibility. Every project is re-based on measured gas flow and composition for one to two weeks before equipment is sized.</p>
    </div>
    <div class="table-wrap">
      <table>
        <thead><tr><th>Parameter</th><th>Typical range</th><th>Why it matters</th></tr></thead>
        <tbody>
          <tr><td>POME generation</td><td class="num">0.6 &ndash; 0.7 m&sup3; per tonne FFB</td><td>Sets the digester and pond volume</td></tr>
          <tr><td>POME COD</td><td class="num">50 &ndash; 80 g/L</td><td>Determines methane potential per m&sup3;</td></tr>
          <tr><td>Biogas yield (covered lagoon)</td><td class="num">20 &ndash; 28 Nm&sup3; per m&sup3; POME</td><td>The single most uncertain number &mdash; we verify it</td></tr>
          <tr><td>Methane content</td><td class="num">55 &ndash; 65% CH&#8324;</td><td>Drives gas flow per kWh and engine derating</td></tr>
          <tr><td>Hydrogen sulphide</td><td class="num">1,000 &ndash; 4,000 ppm H&#8322;S</td><td>Decides desulfurisation duty and oil change interval</td></tr>
          <tr><td>Engine fuel pressure</td><td class="num">5 &ndash; 15 kPa at inlet</td><td>Blower and gas train design</td></tr>
          <tr><td>Operating hours</td><td class="num">7,000 &ndash; 8,000 h/year</td><td>Revenue and maintenance reserve</td></tr>
        </tbody>
      </table>
    </div>
    <p class="small" style="margin-top:14px">Source: KSTS project experience and published Malaysian POME digestion data. Used for pre-feasibility only &mdash; not a performance guarantee.</p>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow">Engineering tools</p>
      <h2>Check the numbers before you talk to a supplier</h2>
      <p class="lead">Five calculators built on the same formulas we use in proposals. No sign-up, no email capture. Change one input and see what it does to output, heat, gas demand and payback.</p>
    </div>
    <div class="grid-4">
      <article class="card"><p class="tag">Tool 01</p><h3>Gas to power &amp; heat</h3><p>Biogas flow in, electrical and thermal output out.</p><a class="more" href="calculator.html#tool1" style="color:var(--accent);font-weight:700">Open &rarr;</a></article>
      <article class="card"><p class="tag">Tool 02</p><h3>Capacity sizing</h3><p>Target kW in, required gas flow out.</p><a class="more" href="calculator.html#tool2" style="color:var(--accent);font-weight:700">Open &rarr;</a></article>
      <article class="card"><p class="tag">Tool 03</p><h3>Mill to biogas</h3><p>FFB throughput to methane potential.</p><a class="more" href="calculator.html#tool3" style="color:var(--accent);font-weight:700">Open &rarr;</a></article>
      <article class="card"><p class="tag">Tool 04</p><h3>Upgrading yield</h3><p>Raw biogas to &ge;97% biomethane.</p><a class="more" href="calculator.html#tool4" style="color:var(--accent);font-weight:700">Open &rarr;</a></article>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow">Local presence</p>
      <h2>Sabah-based, with the statutory credentials that matter</h2>
      <p class="lead">Biogas plants are not just equipment. They need a DOSH-registered engineer for steam and I.C.E. inspection under FMA 1967, an ECOS-registered electrical energy manager for the efficiency case, and a CIDB contractor for the civil and mechanical works. KSTS holds all three.</p>
    </div>
    <div class="grid-2" style="align-items:center">
      <div class="card">
        <p class="tag">Managing Director</p>
        <h3>Sdr. Leong Kian Sheng (Alvin)</h3>
        <p class="small" style="margin-bottom:14px">B.Eng. Tech (Aust), TMIEAust, InclEM, MMOSTA</p>
        <ul class="checks">
          <li>D.O.S.H Registered Steam &amp; I.C.E. Engineer</li>
          <li>D.O.S.H Registered OSH Coordinator</li>
          <li>ECOS Registered Electrical Energy Manager</li>
          <li>BEM Registered Engineering Technologist &middot; ASEAN Engineering Technologist</li>
          <li>CIDB Registered Contractor &middot; Syarikat Status Bumiputera Sabah</li>
        </ul>
        <a class="btn ghost sm" href="about.html" style="margin-top:8px">Full profile</a>
      </div>
      <div>
        <h3>What that means for a project</h3>
        <p>Permitting and statutory inspection are usually the schedule risk, not the engine. Having the DOSH and ECOS registrations in-house means the plant is designed to the inspection regime from day one, and the paperwork does not become a second project after commissioning.</p>
        <div class="table-wrap" style="margin-top:10px">
          <table style="min-width:0">
            <tbody>
              <tr><td><b>Civil &amp; mechanical</b></td><td>CIDB-registered execution, local labour and plant</td></tr>
              <tr><td><b>Statutory</b></td><td>FMA 1967 steam and I.C.E. inspection services</td></tr>
              <tr><td><b>Energy case</b></td><td>ECOS-registered energy manager reporting</td></tr>
              <tr><td><b>O&amp;M</b></td><td>Local crew, remote support from the factory</td></tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="tight">
  <div class="wrap">
    <div class="band">
      <div>
        <h2>Have a mill, a pond and a diesel bill?</h2>
        <p>Send throughput, pond volume and one week of gas data if you have it. We come back with a capacity, a gas specification and an indicative budget.</p>
      </div>
      <a class="btn light" href="contact.html">Request a pre-feasibility</a>
    </div>
  </div>
</section>
"""


# ---------------------------------------------------------------- biogas to power
POWER = """
<section class="page-head">
  <div class="wrap">
    <p class="eyebrow">Biogas to power</p>
    <h1>From the pond to the busbar</h1>
    <p class="lead">A POME biogas power plant is a chain, not a machine. Gas quality at the engine inlet decides whether you get 8,000 hours or 4,000 hours between overhauls. We design the whole chain and take responsibility for the interface.</p>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow">Process chain</p>
      <h2>Six stages, one gas specification</h2>
    </div>
    <div class="steps">
      <div class="step"><b>Capture</b><span>Covered lagoon or CSTR; HDPE/geomembrane cover, condensate traps, gas collection headers.</span></div>
      <div class="step"><b>Buffer</b><span>Gas holder or membrane storage to absorb mill load swings and protect the engine.</span></div>
      <div class="step"><b>Desulfurise</b><span>Biological scrubber for bulk H&#8322;S, iron-oxide or activated carbon polishing.</span></div>
      <div class="step"><b>Condition</b><span>Chilling and coalescing to remove water and siloxane carry-over; blower to engine pressure.</span></div>
      <div class="step"><b>Generate</b><span>Gas engine + alternator, island or parallel; flared safely during trips.</span></div>
      <div class="step"><b>Recover heat</b><span>Jacket water ~90 &deg;C and exhaust to hot water, boiler feedwater or steam.</span></div>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow">Selection</p>
      <h2>Engine size against available gas</h2>
      <p class="lead">At 60% CH&#8324; and 38&ndash;40% electrical efficiency, one cubic metre of biogas carries about 2.2 kWh of electricity. The table shows the gas flow needed at full load.</p>
    </div>
    <div class="table-wrap">
      <table>
        <thead><tr><th>Electrical output</th><th>Biogas at 60% CH&#8324;</th><th>Biogas at 55% CH&#8324;</th><th>Thermal output (recoverable)</th><th>Typical application</th></tr></thead>
        <tbody>
          <tr><td class="num">300 kW</td><td class="num">132 &ndash; 140 Nm&sup3;/h</td><td class="num">144 &ndash; 153 Nm&sup3;/h</td><td class="num">330 &ndash; 390 kW</td><td>Single small mill, 30&ndash;40 t FFB/h</td></tr>
          <tr><td class="num">500 kW</td><td class="num">220 &ndash; 234 Nm&sup3;/h</td><td class="num">240 &ndash; 255 Nm&sup3;/h</td><td class="num">550 &ndash; 650 kW</td><td>Medium mill, 45&ndash;60 t FFB/h</td></tr>
          <tr><td class="num">600 kW</td><td class="num">265 &ndash; 280 Nm&sup3;/h</td><td class="num">289 &ndash; 306 Nm&sup3;/h</td><td class="num">660 &ndash; 780 kW</td><td>Most common single-unit size</td></tr>
          <tr><td class="num">800 kW</td><td class="num">353 &ndash; 373 Nm&sup3;/h</td><td class="num">385 &ndash; 407 Nm&sup3;/h</td><td class="num">880 &ndash; 1,040 kW</td><td>Large mill, 60&ndash;75 t FFB/h</td></tr>
          <tr><td class="num">1,000 kW</td><td class="num">441 &ndash; 466 Nm&sup3;/h</td><td class="num">481 &ndash; 509 Nm&sup3;/h</td><td class="num">1,100 &ndash; 1,300 kW</td><td>Two-mill cluster or group estate</td></tr>
          <tr><td class="num">1,500 kW</td><td class="num">662 &ndash; 699 Nm&sup3;/h</td><td class="num">722 &ndash; 763 Nm&sup3;/h</td><td class="num">1,650 &ndash; 1,950 kW</td><td>Large estate, continuous load</td></tr>
          <tr><td class="num">2,000 kW</td><td class="num">883 &ndash; 932 Nm&sup3;/h</td><td class="num">963 &ndash; 1,017 Nm&sup3;/h</td><td class="num">2,200 &ndash; 2,600 kW</td><td>Multi-mill central plant</td></tr>
        </tbody>
      </table>
    </div>
    <p class="small" style="margin-top:14px">Full-load figures. Running a set below 70% load for long periods causes carbon build-up and shortens the overhaul interval &mdash; size down or split into two units rather than oversize.</p>
  </div>
</section>

<section>
  <div class="wrap grid-2" style="gap:44px;align-items:start">
    <div>
      <p class="eyebrow">Gas specification</p>
      <h2>What the engine will accept</h2>
      <p>These limits are the basis of our warranty discussions with the engine supplier. If your gas cannot meet them, the treatment scope changes &mdash; we would rather say so before the order than after.</p>
      <div class="table-wrap">
        <table style="min-width:0">
          <tbody>
            <tr><td>Methane content</td><td class="num">&ge; 50% (design 55&ndash;65%)</td></tr>
            <tr><td>H&#8322;S at engine inlet</td><td class="num">&le; 200 ppm, target &le; 100 ppm</td></tr>
            <tr><td>Water dew point</td><td class="num">&le; 10 &deg;C above ambient at pressure</td></tr>
            <tr><td>Gas temperature</td><td class="num">&le; 40 &deg;C</td></tr>
            <tr><td>Inlet pressure</td><td class="num">5&ndash;15 kPa, stable within &plusmn;1 kPa</td></tr>
            <tr><td>Particulates / oil</td><td class="num">Essentially free; coalescing filter fitted</td></tr>
            <tr><td>Pressure fluctuation</td><td class="num">&le; 10% per minute</td></tr>
          </tbody>
        </table>
      </div>
      <div class="callout" style="margin-top:22px">
        <p><b>The most common mistake:</b> accepting raw POME gas at 2,000&ndash;4,000 ppm H&#8322;S. It halves the lube-oil life, doubles the maintenance cost, and the saving is invisible until the first overhaul. Desulfurisation is not optional.</p>
      </div>
    </div>
    <div>
      <p class="eyebrow">Economics</p>
      <h2>What O&amp;M really costs</h2>
      <p>For a 600 kW set at 8,000 h/year, gas after scrubbing at 60% CH&#8324;:</p>
      <div class="table-wrap">
        <table style="min-width:0">
          <thead><tr><th>Item</th><th>RM/kWh</th></tr></thead>
          <tbody>
            <tr><td>Lube oil, filters, spark plugs</td><td class="num">0.014</td></tr>
            <tr><td>Routine service labour</td><td class="num">0.012</td></tr>
            <tr><td>Top / major overhaul reserve</td><td class="num">0.016</td></tr>
            <tr><td>Polishing desulfurisation media</td><td class="num">0.005</td></tr>
            <tr><td>Spares, insurance, misc.</td><td class="num">0.008</td></tr>
            <tr><td><b>Total</b></td><td class="num"><b>0.055</b></td></tr>
          </tbody>
        </table>
      </div>
      <p class="small" style="margin-top:12px">Range RM 0.048&ndash;0.058/kWh (&asymp; USD 0.011&ndash;0.014/kWh). Full-service O&amp;M contract including overhauls: RM 0.065&ndash;0.085/kWh. Excludes digester/pond O&amp;M and the upgrading section, if fitted.</p>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow">Commercial models</p>
      <h2>Three ways to structure the project</h2>
    </div>
    <div class="grid-3">
      <article class="card"><p class="tag">Model 1</p><h3>Equipment supply</h3><p>Genset, gas train, control panel, heat recovery. Client or their contractor handles civils and balance of plant. Lowest entry cost, most interfaces on the client side.</p></article>
      <article class="card"><p class="tag">Model 2</p><h3>EPC turnkey</h3><p>Single contract from pond cover to grid-tie, with local civil and mechanical works executed by KSTS under CIDB registration and commissioning witnessed by DOSH.</p></article>
      <article class="card"><p class="tag">Model 3</p><h3>BOO / shared savings</h3><p>We fund and own the plant, the mill buys power or gas at a discount to its current cost. No capital outlay for the mill; the return comes from the spread over the contract term.</p></article>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow">Before we quote</p>
      <h2>Seven pieces of data we need</h2>
      <p class="lead">With these we can produce a defensible capacity and budget. Without them, any number is a guess with a decimal point.</p>
    </div>
    <div class="grid-2">
      <ul class="checks">
        <li>FFB throughput, t/h and operating days per year</li>
        <li>POME pond: number of stages, total volume, HRT, whether covered</li>
        <li>Measured biogas flow and composition (CH&#8324;, CO&#8322;, H&#8322;S, temperature)</li>
      </ul>
      <ul class="checks">
        <li>Electricity tariff or diesel consumption and price</li>
        <li>Grid connection status and transformer capacity</li>
        <li>Boiler fuel, steam demand and pressure, if heat or biomethane is the target</li>
        <li>Load profile: base load, peaks, night shift</li>
      </ul>
    </div>
    <div class="band" style="margin-top:28px">
      <div><h2>Send the data, get a capacity</h2><p>We reply with a gas balance, a recommended unit size and an indicative budget &mdash; normally within three working days.</p></div>
      <a class="btn light" href="contact.html">Contact KSTS</a>
    </div>
  </div>
</section>
"""


# ---------------------------------------------------------------- biomethane
BIOMETHANE = """
<section class="page-head">
  <div class="wrap">
    <p class="eyebrow">Biomethane &amp; bio-CNG</p>
    <h1>Biogas upgraded to boiler-grade gas</h1>
    <p class="lead">If the mill&rsquo;s boiler runs on diesel, LPG or natural gas, the fastest payback is often not electricity &mdash; it is replacing that fuel with biomethane at &ge;97% CH&#8324;, produced on site from the same POME.</p>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-head"><p class="eyebrow">Process</p><h2>From 60% to 97% in five steps</h2></div>
    <div class="steps" style="grid-template-columns:repeat(5,1fr)">
      <div class="step"><b>Desulfurise</b><span>Biological plus iron oxide to protect the upgrading media and the compressor.</span></div>
      <div class="step"><b>Compress</b><span>To the pressure required by the selected separation technology.</span></div>
      <div class="step"><b>Dry</b><span>Refrigerated dryer and coalescing filters; no free water into the sorbent.</span></div>
      <div class="step"><b>Separate CO&#8322;</b><span>PSA, water scrubbing or membrane &mdash; selected on gas volume and site constraints.</span></div>
      <div class="step"><b>Deliver</b><span>Odorise and send to the burner, or compress to 250 bar for tube-trailer bio-CNG.</span></div>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow">Technology selection</p>
      <h2>PSA, water scrubbing or membrane</h2>
      <p class="lead">There is no universal best choice. It depends on gas volume, required purity, power cost and how much space you have next to the mill.</p>
    </div>
    <div class="table-wrap">
      <table>
        <thead><tr><th>&nbsp;</th><th>PSA</th><th>Water scrubbing</th><th>Membrane</th></tr></thead>
        <tbody>
          <tr><td><b>Typical CH&#8324; purity</b></td><td class="num">96&ndash;98%</td><td class="num">97&ndash;99%</td><td class="num">96&ndash;98% (two-stage)</td></tr>
          <tr><td><b>Methane recovery</b></td><td class="num">95&ndash;98%</td><td class="num">98&ndash;99%</td><td class="num">96&ndash;99%</td></tr>
          <tr><td><b>Power demand</b></td><td class="num">0.25&ndash;0.30 kWh/Nm&sup3;</td><td class="num">0.20&ndash;0.30 kWh/Nm&sup3;</td><td class="num">0.20&ndash;0.28 kWh/Nm&sup3;</td></tr>
          <tr><td><b>Footprint</b></td><td class="num">Medium</td><td class="num">Large (water loop)</td><td class="num">Small</td></tr>
          <tr><td><b>Water demand</b></td><td class="num">Low</td><td class="num">High unless looped</td><td class="num">Very low</td></tr>
          <tr><td><b>Best fit</b></td><td class="num">200&ndash;1,500 Nm&sup3;/h, dry sites</td><td class="num">Large plants, stable operation</td><td class="num">Small/medium, skid-mounted</td></tr>
          <tr><td><b>Sensitivity to H&#8322;S</b></td><td class="num">High</td><td class="num">Medium</td><td class="num">Low</td></tr>
        </tbody>
      </table>
    </div>
    <p class="small" style="margin-top:14px">Figures are typical ranges from supplier data and our own projects. Actual performance depends on feed gas composition, pressure and operating regime.</p>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-head"><p class="eyebrow">Output</p><h2>What 500 Nm&sup3;/h of raw biogas becomes</h2></div>
    <div class="grid-2">
      <div class="table-wrap">
        <table style="min-width:0">
          <tbody>
            <tr><td>Raw biogas in</td><td class="num">500 Nm&sup3;/h at 60% CH&#8324;</td></tr>
            <tr><td>Methane in</td><td class="num">300 Nm&sup3;/h</td></tr>
            <tr><td>Upgrading recovery (97%)</td><td class="num">291 Nm&sup3; CH&#8324;/h</td></tr>
            <tr><td>Product at 97% CH&#8324;</td><td class="num">&asymp; 300 Nm&sup3;/h</td></tr>
            <tr><td>Product energy</td><td class="num">&asymp; 2,890 kW (LHV)</td></tr>
            <tr><td>CO&#8322; removed</td><td class="num">&asymp; 209 Nm&sup3;/h</td></tr>
            <tr><td>Upgrading power</td><td class="num">&asymp; 125&ndash;150 kW</td></tr>
          </tbody>
        </table>
      </div>
      <div>
        <h3>Gas quality we guarantee</h3>
        <ul class="checks">
          <li>CH&#8324; &ge; 97% (adjustable to 96&ndash;99%)</li>
          <li>CO&#8322; &le; 2&ndash;3%</li>
          <li>H&#8322;S &le; 5 ppm after polishing</li>
          <li>Water dew point &le; &minus;40 &deg;C at pressure</li>
          <li>O&#8322; &le; 0.5%</li>
          <li>Calorific value compatible with the existing burner after nozzle/jet change</li>
        </ul>
        <div class="callout"><p><b>Burner retrofit is part of the scope.</b> A biomethane burner needs a different gas train, orifice and flame-detection setup from diesel or LPG. We coordinate that with the boiler supplier rather than leaving it to the mill.</p></div>
      </div>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="sec-head"><p class="eyebrow">Bio-CNG</p><h2>When there is no pipeline, build a virtual one</h2><p class="lead">Compressed biomethane at 250 bar in tube trailers moves gas to estates, factories or refuelling points without a pipeline. For remote Sabah and Sarawak sites this is often the only practical route to market.</p></div>
    <div class="grid-3">
      <article class="card"><p class="tag">Step 1</p><h3>Compression</h3><p>Multi-stage compression from upgrading pressure to 250 bar, with inter-stage drying and gas cooling.</p></article>
      <article class="card"><p class="tag">Step 2</p><h3>Storage &amp; loading</h3><p>Stationary cascade storage plus a loading arm for tube trailers; metering and custody-transfer records.</p></article>
      <article class="card"><p class="tag">Step 3</p><h3>Off-site use</h3><p>Pressure reduction skid at the receiving site, or a daughter-station arrangement for fleet refuelling.</p></article>
    </div>
  </div>
</section>
"""


# ---------------------------------------------------------------- equipment
EQUIPMENT = """
<section class="page-head">
  <div class="wrap">
    <p class="eyebrow">Equipment &amp; scope</p>
    <h1>What we supply, and what we do not</h1>
    <p class="lead">Clear scope boundaries are the cheapest risk control on a biogas project. Below is the standard battery limit for a power plant and for an upgrading plant, and who does what.</p>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-head"><p class="eyebrow">Gas engines</p><h2>Biogas gensets, 300 kW to 2 MW</h2><p class="lead">Chinese-manufactured gas engines from a proven production line, configured for POME biogas, at roughly 40&ndash;45% of the landed price of a European equivalent in the same class.</p></div>
    <div class="table-wrap">
      <table>
        <thead><tr><th>Model class</th><th>Electrical output</th><th>Fuel</th><th>Electrical efficiency</th><th>Heat recovery</th><th>Voltage</th></tr></thead>
        <tbody>
          <tr><td class="num">300 kW</td><td class="num">300 kW / 375 kVA</td><td>Biogas &ge; 50% CH&#8324;</td><td class="num">36&ndash;38%</td><td class="num">&asymp; 330 kW</td><td>415 V / 50 Hz</td></tr>
          <tr><td class="num">500 kW</td><td class="num">500 kW / 625 kVA</td><td>Biogas &ge; 50% CH&#8324;</td><td class="num">37&ndash;39%</td><td class="num">&asymp; 560 kW</td><td>415 V / 50 Hz</td></tr>
          <tr><td class="num">600 kW</td><td class="num">600 kW / 750 kVA</td><td>Biogas &ge; 50% CH&#8324;</td><td class="num">37&ndash;39%</td><td class="num">&asymp; 680 kW</td><td>415 V / 50 Hz</td></tr>
          <tr><td class="num">800 kW</td><td class="num">800 kW / 1,000 kVA</td><td>Biogas &ge; 50% CH&#8324;</td><td class="num">38&ndash;40%</td><td class="num">&asymp; 900 kW</td><td>415 V / 50 Hz</td></tr>
          <tr><td class="num">1,000 kW</td><td class="num">1,000 kW / 1,250 kVA</td><td>Biogas &ge; 50% CH&#8324;</td><td class="num">38&ndash;40%</td><td class="num">&asymp; 1,150 kW</td><td>415 V / 50 Hz</td></tr>
          <tr><td class="num">1,500 kW</td><td class="num">1,500 kW / 1,875 kVA</td><td>Biogas &ge; 50% CH&#8324;</td><td class="num">39&ndash;41%</td><td class="num">&asymp; 1,700 kW</td><td>415 V / 50 Hz</td></tr>
          <tr><td class="num">2,000 kW</td><td class="num">2,000 kW / 2,500 kVA</td><td>Biogas &ge; 50% CH&#8324;</td><td class="num">39&ndash;42%</td><td class="num">&asymp; 2,300 kW</td><td>11 kV option</td></tr>
        </tbody>
      </table>
    </div>
    <p class="small" style="margin-top:14px">Efficiency and heat recovery are indicative at full load with 60% CH&#8324;. Final selection is based on site gas data. Containerised units available from 300 kW to 1.5 MW.</p>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="sec-head"><p class="eyebrow">Balance of plant</p><h2>The parts between the pond and the engine</h2></div>
    <div class="grid-3">
      <article class="card"><p class="tag">Capture</p><h3>Pond cover &amp; gas collection</h3><p>HDPE or geomembrane cover, gas collection headers, condensate traps, pressure relief and inspection hatches. Retrofittable to existing covered lagoons.</p></article>
      <article class="card"><p class="tag">Desulfurisation</p><h3>Biological + iron oxide</h3><p>Biological trickling filter for bulk H&#8322;S removal, followed by iron-oxide or activated-carbon polishing vessels in duty/standby arrangement.</p></article>
      <article class="card"><p class="tag">Conditioning</p><h3>Chiller, blower, filters</h3><p>Refrigerated dryer, coalescing filters, Roots blower with VFD, flame arrestor, gas train with shut-off and relief valves.</p></article>
      <article class="card"><p class="tag">Storage</p><h3>Gas holder</h3><p>Membrane or double-membrane holder to buffer mill load swings and keep the engine off the trip line during upstream upsets.</p></article>
      <article class="card"><p class="tag">Safety</p><h3>Flare &amp; gas detection</h3><p>Enclosed or open flare sized for full gas flow, CH&#8324;/H&#8322;S detection, emergency shutdown logic and explosion-proof instrumentation in the gas area.</p></article>
      <article class="card"><p class="tag">Heat</p><h3>Heat recovery</h3><p>Exhaust gas heat exchanger and jacket-water circuit producing hot water at 85&ndash;95 &deg;C, or steam via an exhaust boiler where the mill needs it.</p></article>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-head"><p class="eyebrow">Scope matrix</p><h2>Who does what</h2><p class="lead">For a typical EPC project. Equipment-only supply moves the middle column to the client or their contractor.</p></div>
    <div class="table-wrap">
      <table>
        <thead><tr><th>Work package</th><th>KSTS / technology partner</th><th>Client</th><th>Notes</th></tr></thead>
        <tbody>
          <tr><td>Process design &amp; gas balance</td><td>Yes</td><td>Data supply</td><td>Mass and energy balance, P&amp;ID, GA drawings</td></tr>
          <tr><td>Pond cover / digester</td><td>Design &amp; supply</td><td>Site access, earthworks</td><td>Existing pond condition survey first</td></tr>
          <tr><td>Gas treatment &amp; gas train</td><td>Yes</td><td>&mdash;</td><td>Battery limit: engine inlet flange</td></tr>
          <tr><td>Genset &amp; control panel</td><td>Yes</td><td>&mdash;</td><td>Including protection and synchronising</td></tr>
          <tr><td>Civil foundations &amp; buildings</td><td>Execution (CIDB)</td><td>Approvals</td><td>Local subcontractors under KSTS</td></tr>
          <tr><td>Electrical reticulation</td><td>Execution</td><td>Transformer / grid interface</td><td>415 V works; HV by utility or client</td></tr>
          <tr><td>Erection &amp; commissioning</td><td>Yes</td><td>Utilities, fuel, water</td><td>DOSH witness during commissioning</td></tr>
          <tr><td>O&amp;M</td><td>Option</td><td>Site crew</td><td>Full contract or advisory</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="sec-head"><p class="eyebrow">Upgrading plant</p><h2>Biomethane package</h2></div>
    <div class="grid-2">
      <ul class="checks">
        <li>Feed compression and pre-treatment skid</li>
        <li>PSA / water scrubber / membrane separation skid</li>
        <li>Polishing, odorisation and custody metering</li>
        <li>250 bar compression, cascade storage and loading arm (bio-CNG option)</li>
      </ul>
      <ul class="checks">
        <li>Burner retrofit coordination for the existing boiler</li>
        <li>Gas quality analyser with continuous logging</li>
        <li>PLC + SCADA with remote access for factory support</li>
        <li>Operator training and spares package</li>
      </ul>
    </div>
  </div>
</section>
"""


# ---------------------------------------------------------------- calculator
CALCULATOR = """
<section class="page-head">
  <div class="wrap">
    <p class="eyebrow">Engineering tools</p>
    <h1>Five calculators, no sign-up</h1>
    <p class="lead">These are the same formulas we use in pre-feasibility work. They are deliberately transparent: every assumption is shown, and you can change it. Use them to challenge a supplier&rsquo;s numbers &mdash; including ours.</p>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="tabs" id="tabs">
      <button class="tab-btn active" data-tab="tool1">1 &middot; Gas to power &amp; heat</button>
      <button class="tab-btn" data-tab="tool2">2 &middot; Capacity sizing</button>
      <button class="tab-btn" data-tab="tool3">3 &middot; Mill to biogas</button>
      <button class="tab-btn" data-tab="tool4">4 &middot; Upgrading yield</button>
      <button class="tab-btn" data-tab="tool5">5 &middot; Project economics</button>
    </div>

    <!-- ---------------- tool 1 -->
    <div class="tab-panel active" id="tool1">
      <div class="tool-head">
        <div><p class="eyebrow">Tool 01</p><h2>Biogas flow &rarr; electricity and heat</h2></div>
        <div class="tool-actions">
          <button class="btn ghost sm" onclick="window.print()">Print / save as PDF</button>
          <button class="btn sm" onclick="copySummary('tool1')">Copy summary</button>
        </div>
      </div>
      <div class="calc">
        <div class="calc-form">
          <div class="field"><label for="t1_flow">Biogas flow available (Nm&sup3;/h)</label><input id="t1_flow" type="number" value="300" step="1" min="0"><div class="hint">Normal cubic metres per hour at 0 &deg;C, 101.3 kPa.</div></div>
          <div class="field"><label for="t1_ch4">Methane content (%)</label><input id="t1_ch4" type="number" value="60" step="0.5" min="40" max="99"><div class="hint">POME biogas is typically 55&ndash;65%.</div></div>
          <div class="field"><label for="t1_eff">Electrical efficiency (%)</label><input id="t1_eff" type="number" value="38" step="0.5" min="20" max="45"><div class="hint">Chinese gas engines 36&ndash;40%; premium European 40&ndash;43%.</div></div>
          <div class="field"><label for="t1_heat">Recoverable heat (% of fuel energy)</label><input id="t1_heat" type="number" value="43" step="1" min="0" max="60"><div class="hint">Jacket water + exhaust, typically 40&ndash;45%.</div></div>
          <div class="field"><label for="t1_hours">Operating hours per year</label><input id="t1_hours" type="number" value="8000" step="100" min="0" max="8760"></div>
          <div class="field"><label for="t1_load">Average load factor (%)</label><input id="t1_load" type="number" value="85" step="1" min="10" max="100"></div>
        </div>
        <div class="calc-out">
          <h3>Results</h3>
          <div class="out-grid" id="t1_out">
            <div class="kv hl"><span>Electrical output at full load</span><b id="t1_kw">—</b></div>
            <div class="kv hl"><span>Recoverable heat</span><b id="t1_heatkw">—</b></div>
            <div class="kv"><span>Fuel energy input</span><b id="t1_energy">—</b></div>
            <div class="kv"><span>Total efficiency (power + heat)</span><b id="t1_total">—</b></div>
            <div class="kv"><span>Biogas per kWh generated</span><b id="t1_gas_kwh">—</b></div>
            <div class="kv"><span>Annual generation</span><b id="t1_year_kwh">—</b></div>
            <div class="kv"><span>Annual heat delivered</span><b id="t1_year_heat">—</b></div>
            <div class="kv"><span>Diesel avoided</span><b id="t1_diesel">—</b></div>
          </div>
          <div class="warn" id="t1_warn"></div>
          <p class="note">LHV of methane taken as 9.94 kWh/Nm&sup3; (35.8 MJ/Nm&sup3;). Typical diesel genset at 35% efficiency and 2.68 kg CO&#8322;/litre used for the avoided-fuel figure.</p>
        </div>
      </div>
    </div>

    <!-- ---------------- tool 2 -->
    <div class="tab-panel" id="tool2">
      <div class="tool-head">
        <div><p class="eyebrow">Tool 02</p><h2>Target output &rarr; gas demand</h2></div>
        <div class="tool-actions">
          <button class="btn ghost sm" onclick="window.print()">Print / save as PDF</button>
          <button class="btn sm" onclick="copySummary('tool2')">Copy summary</button>
        </div>
      </div>
      <div class="calc">
        <div class="calc-form">
          <div class="field"><label for="t2_kw">Target electrical output (kW)</label><input id="t2_kw" type="number" value="600" step="10" min="0"></div>
          <div class="field"><label for="t2_ch4">Methane content (%)</label><input id="t2_ch4" type="number" value="60" step="0.5" min="40" max="99"></div>
          <div class="field"><label for="t2_eff">Electrical efficiency (%)</label><input id="t2_eff" type="number" value="38" step="0.5" min="20" max="45"></div>
          <div class="field"><label for="t2_load">Average load factor (%)</label><input id="t2_load" type="number" value="85" step="1" min="10" max="100"><div class="hint">Gas demand is calculated at full load; average consumption scales with load.</div></div>
        </div>
        <div class="calc-out">
          <h3>Gas demand</h3>
          <div class="out-grid">
            <div class="kv hl"><span>Biogas at full load</span><b id="t2_flow">—</b></div>
            <div class="kv hl"><span>Biogas per day at full load</span><b id="t2_day">—</b></div>
            <div class="kv"><span>Average consumption at load factor</span><b id="t2_avg">—</b></div>
            <div class="kv"><span>Methane flow</span><b id="t2_ch4flow">—</b></div>
            <div class="kv"><span>Fuel energy input</span><b id="t2_energy">—</b></div>
            <div class="kv"><span>Annual biogas</span><b id="t2_year">—</b></div>
          </div>
          <div class="warn" id="t2_warn"></div>
          <p class="note">Use this to test whether a supplier&rsquo;s engine is matched to your measured gas flow. A 600 kW set on 200 Nm&sup3;/h of biogas will run below 70% load and cost more to maintain.</p>
        </div>
      </div>
    </div>

    <!-- ---------------- tool 3 -->
    <div class="tab-panel" id="tool3">
      <div class="tool-head">
        <div><p class="eyebrow">Tool 03</p><h2>Mill throughput &rarr; biogas potential</h2></div>
        <div class="tool-actions">
          <button class="btn ghost sm" onclick="window.print()">Print / save as PDF</button>
          <button class="btn sm" onclick="copySummary('tool3')">Copy summary</button>
        </div>
      </div>
      <div class="calc">
        <div class="calc-form">
          <div class="field"><label for="t3_ffb">FFB throughput (t/h)</label><input id="t3_ffb" type="number" value="60" step="1" min="0"></div>
          <div class="field"><label for="t3_pome">POME generated (m&sup3; per t FFB)</label><input id="t3_pome" type="number" value="0.65" step="0.05" min="0.2" max="1.2"></div>
          <div class="field"><label for="t3_yield">Biogas yield (Nm&sup3; per m&sup3; POME)</label><input id="t3_yield" type="number" value="24" step="1" min="5" max="40"><div class="hint">Covered lagoon 20&ndash;28; well-mixed CSTR can reach 30+.</div></div>
          <div class="field"><label for="t3_ch4">Methane content (%)</label><input id="t3_ch4" type="number" value="60" step="0.5" min="40" max="99"></div>
          <div class="field"><label for="t3_capture">Capture efficiency (%)</label><input id="t3_capture" type="number" value="85" step="1" min="30" max="100"><div class="hint">Share of generated biogas actually collected and delivered.</div></div>
          <div class="field"><label for="t3_eff">Electrical efficiency (%)</label><input id="t3_eff" type="number" value="38" step="0.5" min="20" max="45"></div>
        </div>
        <div class="calc-out">
          <h3>Biogas &amp; power potential</h3>
          <div class="out-grid">
            <div class="kv"><span>POME produced</span><b id="t3_pome_day">—</b></div>
            <div class="kv hl"><span>Biogas generated</span><b id="t3_gas_day">—</b></div>
            <div class="kv hl"><span>Biogas available to engine</span><b id="t3_gas_h">—</b></div>
            <div class="kv"><span>Methane available</span><b id="t3_ch4_h">—</b></div>
            <div class="kv"><span>Electrical potential</span><b id="t3_kw">—</b></div>
            <div class="kv"><span>Annual generation (8,000 h)</span><b id="t3_mwh">—</b></div>
          </div>
          <div class="warn" id="t3_warn"></div>
          <p class="note">Assumes continuous 24-hour POME production from the stated throughput. Real mills have shifts and stoppages &mdash; use the measured pond inflow where available. This is a screening number, not a design basis.</p>
        </div>
      </div>
    </div>

    <!-- ---------------- tool 4 -->
    <div class="tab-panel" id="tool4">
      <div class="tool-head">
        <div><p class="eyebrow">Tool 04</p><h2>Raw biogas &rarr; biomethane yield</h2></div>
        <div class="tool-actions">
          <button class="btn ghost sm" onclick="window.print()">Print / save as PDF</button>
          <button class="btn sm" onclick="copySummary('tool4')">Copy summary</button>
        </div>
      </div>
      <div class="calc">
        <div class="calc-form">
          <div class="field"><label for="t4_flow">Raw biogas flow (Nm&sup3;/h)</label><input id="t4_flow" type="number" value="500" step="10" min="0"></div>
          <div class="field"><label for="t4_ch4">Methane content in (%)</label><input id="t4_ch4" type="number" value="60" step="0.5" min="40" max="80"></div>
          <div class="field"><label for="t4_rec">Methane recovery (%)</label><input id="t4_rec" type="number" value="97" step="0.5" min="80" max="100"><div class="hint">PSA 95&ndash;98, membrane 96&ndash;99, water scrubber 98&ndash;99.</div></div>
          <div class="field"><label for="t4_purity">Product purity (% CH&#8324;)</label><input id="t4_purity" type="number" value="97" step="0.5" min="90" max="99.9"></div>
          <div class="field"><label for="t4_power">Upgrading power (kWh/Nm&sup3; raw)</label><input id="t4_power" type="number" value="0.27" step="0.01" min="0.05" max="0.6"></div>
        </div>
        <div class="calc-out">
          <h3>Upgrading output</h3>
          <div class="out-grid">
            <div class="kv"><span>Methane entering</span><b id="t4_ch4in">—</b></div>
            <div class="kv hl"><span>Biomethane product</span><b id="t4_product">—</b></div>
            <div class="kv"><span>Methane in product</span><b id="t4_ch4out">—</b></div>
            <div class="kv"><span>Methane loss (tail gas)</span><b id="t4_loss">—</b></div>
            <div class="kv"><span>CO&#8322; removed</span><b id="t4_co2">—</b></div>
            <div class="kv hl"><span>Product energy (LHV)</span><b id="t4_mw">—</b></div>
            <div class="kv"><span>Upgrading power demand</span><b id="t4_kw">—</b></div>
            <div class="kv"><span>Diesel equivalent</span><b id="t4_diesel">—</b></div>
          </div>
          <p class="note">Product flow = CH&#8324; in &times; recovery &divide; purity. Diesel equivalence at 35.8 MJ/L LHV. Boiler replacement also needs a burner/gas-train retrofit &mdash; see the biomethane page.</p>
        </div>
      </div>
    </div>

    <!-- ---------------- tool 5 -->
    <div class="tab-panel" id="tool5">
      <div class="tool-head">
        <div><p class="eyebrow">Tool 05</p><h2>Project economics</h2></div>
        <div class="tool-actions">
          <button class="btn ghost sm" onclick="window.print()">Print / save as PDF</button>
          <button class="btn sm" onclick="copySummary('tool5')">Copy summary</button>
        </div>
      </div>
      <div class="calc">
        <div class="calc-form">
          <div class="field"><label for="t5_kw">Plant capacity (kW)</label><input id="t5_kw" type="number" value="600" step="10" min="0"></div>
          <div class="field"><label for="t5_capex">Turnkey capex (USD per kW)</label><input id="t5_capex" type="number" value="2200" step="50" min="0"><div class="hint">Engine-only package &asymp; USD 350&ndash;450/kW; full plant with civils, gas treatment and grid connection typically USD 1,500&ndash;2,500/kW.</div></div>
          <div class="field"><label for="t5_cur">Currency</label>
            <select id="t5_cur"><option value="MYR">MYR (Malaysia)</option><option value="IDR">IDR (Indonesia)</option><option value="USD">USD</option></select>
          </div>
          <div class="field"><label for="t5_tariff">Value of electricity (<span id="t5_curlabel">RM</span>/kWh)</label><input id="t5_tariff" type="number" value="0.65" step="0.01" min="0"><div class="hint">Displaced diesel in inland Sabah: RM 0.55&ndash;0.75. Grid import: RM 0.40&ndash;0.50. Indonesia: USD 0.07&ndash;0.10.</div></div>
          <div class="field"><label for="t5_use">Share of output that displaces bought power (%)</label><input id="t5_use" type="number" value="75" step="5" min="0" max="100"><div class="hint">Only self-consumed kWh carry the full displaced-fuel value. Export or unused capacity earns less or nothing.</div></div>
          <div class="field"><label for="t5_fx">Exchange rate (local units per USD)</label><input id="t5_fx" type="number" value="4.2" step="0.01" min="1"></div>
          <div class="field"><label for="t5_hours">Operating hours per year</label><input id="t5_hours" type="number" value="8000" step="100" min="0" max="8760"></div>
          <div class="field"><label for="t5_om">Variable O&amp;M (USD/kWh)</label><input id="t5_om" type="number" value="0.013" step="0.001" min="0"></div>
          <div class="field"><label for="t5_omfix">Fixed O&amp;M (USD/year)</label><input id="t5_omfix" type="number" value="15000" step="1000" min="0"><div class="hint">Local crew, insurance, admin. Excludes major overhaul reserve if included above.</div></div>
          <div class="field"><label for="t5_disc">Discount rate (%)</label><input id="t5_disc" type="number" value="8" step="0.5" min="0" max="30"></div>
        </div>
        <div class="calc-out">
          <h3>Financial summary</h3>
          <div class="out-grid">
            <div class="kv"><span>Total capex</span><b id="t5_total_capex">—</b></div>
            <div class="kv"><span>Annual generation</span><b id="t5_gen">—</b></div>
            <div class="kv hl"><span>Annual revenue</span><b id="t5_rev">—</b></div>
            <div class="kv"><span>Annual O&amp;M</span><b id="t5_opex">—</b></div>
            <div class="kv hl"><span>Net annual cash flow</span><b id="t5_net">—</b></div>
            <div class="kv hl"><span>Simple payback</span><b id="t5_payback">—</b></div>
            <div class="kv"><span>10-year net (undiscounted)</span><b id="t5_cum10">—</b></div>
            <div class="kv"><span>NPV @ discount rate</span><b id="t5_npv">—</b></div>
            <div class="kv"><span>IRR (10 years)</span><b id="t5_irr">—</b></div>
            <div class="kv"><span>LCOE</span><b id="t5_lcoe">—</b></div>
          </div>
          <div class="warn" id="t5_warn"></div>
          <p class="note">Revenue assumes the plant is paid the stated value for every kWh generated. Capex excludes financing costs, land and any grid upgrade charged by the utility. No escalation or degradation applied &mdash; a screening model, not a bankable one.</p>
        </div>
      </div>
    </div>

    <div class="assume" style="margin-top:28px">
      <b>Method &amp; constants.</b> Methane LHV 35.8 MJ/Nm&sup3; = 9.94 kWh/Nm&sup3;. Biogas energy = flow &times; CH&#8324; fraction &times; 9.94. Electrical output = fuel energy &times; electrical efficiency. Recoverable heat = fuel energy &times; heat recovery fraction. 1 tonne of diesel-equivalent taken as 35.8 GJ. All results are indicative; equipment guarantees are issued only against measured site data.
      <br><br>
      <b>Why we publish the formulas.</b> Most supplier calculators hide the assumptions. Ours are visible because a biogas project is decided on gas quality and operating hours, not on a polished number.
    </div>
  </div>
</section>
<script src="assets/js/calc.js"></script>
"""


# ---------------------------------------------------------------- about
ABOUT = """
<section class="page-head">
  <div class="wrap">
    <p class="eyebrow">About KSTS</p>
    <h1>A Sabah contractor with the right registrations &mdash; and a factory behind it</h1>
    <p class="lead">KSTS K. S. Technical Services is a CIDB-registered, Bumiputera-owned technical services company based in Telupid, Sabah. We deliver biogas and bioenergy projects for the palm oil and agro-industrial sector in Sabah and Sarawak, with process and equipment support from ZERO CARBON ASSISTANT in Shanghai.</p>
  </div>
</section>

<section>
  <div class="wrap grid-2" style="gap:48px;align-items:start">
    <div>
      <p class="eyebrow">The company</p>
      <h2>What KSTS does</h2>
      <p>Founded to serve the estates and mills of the Labuk&ndash;Sugut and Telupid belt, KSTS works across civil, mechanical and electrical scope, and holds the statutory registrations that a biogas plant needs before it can legally run.</p>
      <ul class="checks">
        <li>Agricultural, building, civil and mechanical works</li>
        <li>I.C.E. and steam engineering visitation services under FMA 1967</li>
        <li>Energy management, project management and technical solutions</li>
        <li>Land transportation services</li>
        <li>Drone aerial surveying and agricultural spraying</li>
      </ul>
      <div class="table-wrap" style="margin-top:22px">
        <table style="min-width:0">
          <tbody>
            <tr><td>Registered name</td><td>KSTS K. S. TECHNICAL SERVICES</td></tr>
            <tr><td>Registration</td><td>MPS: R14722/2009</td></tr>
            <tr><td>Status</td><td>Syarikat Status Bumiputera Sabah &middot; CIDB Registered Contractor</td></tr>
            <tr><td>Base</td><td>Kg. Nangoh, Telupid, Sabah, Malaysia</td></tr>
            <tr><td>Coverage</td><td>Sabah and Sarawak</td></tr>
          </tbody>
        </table>
      </div>
    </div>
    <div>
      <p class="eyebrow">Managing Director</p>
      <h2>Sdr. Leong Kian Sheng</h2>
      <p class="small" style="margin-bottom:16px">Known as Alvin &middot; B.Eng. Tech (Aust), TMIEAust, InclEM, MMOSTA</p>
      <p>Alvin is a mechanical engineering technologist who has spent his career on the plant floor of the palm oil and process industries &mdash; inspection, energy management, and project delivery. He is the person who signs off that a plant is safe to operate, not just that it was delivered.</p>
      <div class="card" style="margin-top:18px">
        <h3 style="font-size:17px">Registrations</h3>
        <ul class="checks" style="margin-bottom:0">
          <li>D.O.S.H Registered Steam &amp; I.C.E. Engineer</li>
          <li>D.O.S.H Registered OSH Coordinator</li>
          <li>BEM Registered Engineering Technologist</li>
          <li>ASEAN Engineering Technologist</li>
          <li>ECOS Registered Electrical Energy Manager</li>
          <li>CAAM Certified Remote Pilot (B) &amp; AGRI (2)</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="alt" id="partner">
  <div class="wrap">
    <div class="sec-head"><p class="eyebrow">Technology partner</p><h2>ZERO CARBON ASSISTANT, Shanghai</h2><p class="lead">The engineering, gas engines and upgrading equipment come from a Chinese manufacturer with an export track record in pumps, energy systems and gas power. KSTS is the in-country partner: site data, permitting, civil works, installation, statutory inspection and operations.</p></div>
    <div class="table-wrap">
      <table>
        <thead><tr><th>Function</th><th>KSTS (Malaysia)</th><th>ZERO CARBON ASSISTANT (China)</th></tr></thead>
        <tbody>
          <tr><td>Site survey &amp; gas measurement</td><td>Yes</td><td>Test protocol and interpretation</td></tr>
          <tr><td>Process design &amp; gas balance</td><td>Review</td><td>Yes</td></tr>
          <tr><td>Equipment manufacture</td><td>&mdash;</td><td>Yes</td></tr>
          <tr><td>Civil / mechanical execution</td><td>Yes (CIDB)</td><td>Supervision</td></tr>
          <tr><td>Commissioning &amp; DOSH witness</td><td>Yes</td><td>Engineer on site</td></tr>
          <tr><td>Operations &amp; maintenance</td><td>Yes</td><td>Remote diagnostics, spares</td></tr>
          <tr><td>Commercial contracting</td><td>Malaysian entity</td><td>Equipment supply</td></tr>
        </tbody>
      </table>
    </div>
    <div class="grid-3" style="margin-top:30px">
      <div class="card"><p class="tag">Why it matters</p><h3>One accountable chain</h3><p>Gas quality, engine warranty and civil works are usually three contracts with three excuses. Here they meet at one interface.</p></div>
      <div class="card"><p class="tag">Why it matters</p><h3>Local statutory knowledge</h3><p>FMA 1967 inspections, DOSH registration and ECOS reporting are handled by the same team that designed the plant.</p></div>
      <div class="card"><p class="tag">Why it matters</p><h3>Factory-backed pricing</h3><p>Direct supply from the production line, at roughly 40&ndash;45% of European equipment pricing in the same class.</p></div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-head"><p class="eyebrow">How we work</p><h2>Four steps, no surprises</h2></div>
    <div class="grid-4">
      <div class="card"><p class="tag">Step 1</p><h3>Data</h3><p>Throughput, pond volume, one to two weeks of gas flow and composition, tariff and load profile.</p></div>
      <div class="card"><p class="tag">Step 2</p><h3>Pre-feasibility</h3><p>Gas balance, recommended capacity, indicative capex and opex, payback range. Free of charge.</p></div>
      <div class="card"><p class="tag">Step 3</p><h3>Engineering</h3><p>P&amp;ID, GA drawings, equipment selection, firm quotation, and the commercial model that fits.</p></div>
      <div class="card"><p class="tag">Step 4</p><h3>Delivery</h3><p>Supply, install, commission, DOSH witness, operator training, then O&amp;M if required.</p></div>
    </div>
  </div>
</section>
"""


# ---------------------------------------------------------------- contact
CONTACT = """
<section class="page-head">
  <div class="wrap">
    <p class="eyebrow">Contact</p>
    <h1>Send mill data, get a capacity</h1>
    <p class="lead">The fastest route to a useful answer is measured gas data. If you do not have it yet, send throughput and pond volume &mdash; we will tell you what to measure and for how long.</p>
  </div>
</section>

<section>
  <div class="wrap grid-2" style="gap:56px;align-items:start">
    <div>
      <form class="enquiry" action="https://formsubmit.co/k.s.t.s_sabah@hotmail.com" method="POST">
        <input type="hidden" name="_subject" value="Website enquiry — KSTS bioenergy">
        <input type="hidden" name="_captcha" value="false">
        <div><label class="small" for="name">Name</label><input id="name" name="name" required></div>
        <div><label class="small" for="company">Company / mill</label><input id="company" name="company"></div>
        <div><label class="small" for="email">Email</label><input id="email" name="email" type="email" required></div>
        <div><label class="small" for="phone">Phone / WhatsApp</label><input id="phone" name="phone"></div>
        <div class="full"><label class="small" for="site">Site data</label><textarea id="site" name="site" placeholder="FFB throughput t/h · operating days · POME pond stages and volume · measured biogas Nm³/h and CH₄ % · H₂S ppm · electricity tariff or diesel price · grid status · boiler fuel and steam demand"></textarea></div>
        <div class="full"><label class="small" for="interest">Interest</label>
          <select id="interest" name="interest">
            <option>Biogas to power (electricity and heat)</option>
            <option>Biomethane for boiler fuel</option>
            <option>Bio-CNG / virtual pipeline</option>
            <option>Equipment supply only</option>
            <option>BOO / shared savings</option>
          </select>
        </div>
        <div class="full"><button class="btn" type="submit">Send enquiry</button></div>
      </form>
      <p class="small" style="margin-top:14px">The form is delivered by email. Prefer to write directly? <a href="mailto:k.s.t.s_sabah@hotmail.com">k.s.t.s_sabah@hotmail.com</a></p>
    </div>
    <div>
      <div class="card">
        <h3>Malaysia &mdash; KSTS</h3>
        <div class="kv" style="color:var(--ink);border-color:var(--line)"><span class="muted">Contact</span><b>Sdr. Leong Kian Sheng (Alvin)</b></div>
        <div class="kv" style="color:var(--ink);border-color:var(--line)"><span class="muted">Email</span><b><a href="mailto:k.s.t.s_sabah@hotmail.com">k.s.t.s_sabah@hotmail.com</a></b></div>
        <div class="kv" style="color:var(--ink);border-color:var(--line)"><span class="muted">Phone</span><b><a href="tel:+60138833833">+60 13-883 3833</a></b></div>
        <div class="kv" style="color:var(--ink);border:0"><span class="muted">Address</span><b style="font-weight:600;text-align:right">Kg. Nangoh, NT 083017181 (Lot 2),<br>34 km Off Jalan Simpang Sapi Nangoh,<br>Labuk&ndash;Sugut, Telupid, Sabah</b></div>
      </div>
      <div class="card" style="margin-top:20px">
        <h3>What happens next</h3>
        <ul class="checks">
          <li>We review the data and reply within three working days</li>
          <li>You get a gas balance, a recommended capacity and an indicative budget</li>
          <li>If a site visit is needed for gas measurement, we say so up front</li>
        </ul>
      </div>
      <div class="card" style="margin-top:20px">
        <h3>Trade terms</h3>
        <p class="small" style="margin:0">Quotations in USD or MYR. English documentation, GA drawings, test reports and O&amp;M manuals supplied with every plant. Equipment shipped CIF Kota Kinabalu or Sandakan, or delivered to site.</p>
      </div>
    </div>
  </div>
</section>
"""


def main():
    write_page("index.html",
               "KSTS — Biogas to Power &amp; Biomethane | Sabah, Malaysia",
               "KSTS builds POME biogas power plants, biomethane upgrading and bio-CNG systems for palm oil mills in Sabah and Sarawak. Free engineering calculators for gas-to-power, sizing and project economics.",
               INDEX)
    write_page("biogas-to-power.html",
               "POME Biogas to Power — Engines, Gas Treatment, O&amp;M | KSTS",
               "Covered lagoon to grid-tie: biogas capture, desulfurisation, gas conditioning, 300 kW–2 MW gas engines and heat recovery for Malaysian palm oil mills.",
               POWER)
    write_page("biomethane.html",
               "Biomethane &amp; Bio-CNG Upgrading to 97% CH4 | KSTS",
               "Upgrade POME biogas to ≥97% methane for boiler fuel or bio-CNG. PSA, water scrubbing and membrane comparison, gas quality guarantees and virtual pipeline delivery.",
               BIOMETHANE)
    write_page("equipment.html",
               "Equipment &amp; Scope — Gas Engines, Desulfurisation, Upgrading | KSTS",
               "Biogas gensets 300 kW–2 MW, biological and iron-oxide desulfurisation, gas conditioning, flares, heat recovery and biomethane skids. Clear battery limits and scope matrix.",
               EQUIPMENT)
    write_page("calculator.html",
               "Engineering Calculators — Biogas to Power, Sizing, Biomethane, Economics | KSTS",
               "Five free engineering calculators: biogas to electricity and heat, capacity sizing, mill throughput to biogas potential, biomethane upgrading yield and project economics.",
               CALCULATOR)
    write_page("about.html",
               "About KSTS — Sabah Biogas Contractor &amp; Local Partner",
               "KSTS K. S. Technical Services: CIDB-registered, Bumiputera Sabah contractor with DOSH steam and I.C.E. registration, ECOS energy manager and technology partner Zero Carbon Assistant.",
               ABOUT)
    write_page("contact.html",
               "Contact KSTS — Biogas Project Enquiry, Sabah",
               "Send mill throughput, pond volume and gas data for a pre-feasibility. KSTS, Telupid, Sabah. Response within three working days.",
               CONTACT)

    # 404
    body404 = """<section class="page-head"><div class="wrap"><p class="eyebrow">404</p><h1>Page not found</h1><p class="lead">The page you asked for does not exist. Try the biogas power page, the biomethane page, or the calculators.</p><p style="margin-top:22px"><a class="btn" href="index.html">Back to home</a></p></div></section>"""
    write_page("404.html", "Page not found | KSTS", "Page not found.", body404)

    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
        for href, _ in NAV:
            f.write(f"  <url><loc>{SITE}/{href}</loc><changefreq>monthly</changefreq><priority>{'1.0' if href=='index.html' else '0.8'}</priority></url>\n")
        f.write("</urlset>\n")

    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "robots.txt"), "w", encoding="utf-8") as f:
        f.write(f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")


if __name__ == "__main__":
    main()
