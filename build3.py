# -*- coding: utf-8 -*-
"""Build the trilingual KSTS bioenergy site (EN / BM / 中文) for GitHub Pages."""

import os

SITE = "https://jeeftang.github.io/BCU"
ROOT = os.path.dirname(os.path.abspath(__file__))

LANGS = [("en", "", "English"), ("ms", "ms/", "Bahasa Melayu"), ("zh", "zh/", "中文")]

# short labels used when the header gets tight (default) — full labels only on very wide screens
SHORT = {"en": "EN", "ms": "BM", "zh": "中文"}

NAV = {
    "en": [("index.html", "Home"), ("biogas-to-power.html", "Biogas to Power"),
           ("biomethane.html", "Biomethane"), ("hydrogen-chp.html", "Hydrogen CHP"),
           ("equipment.html", "Equipment"),
           ("calculator.html", "Engineering Tools"), ("about.html", "About KSTS")],
    "ms": [("index.html", "Utama"), ("biogas-to-power.html", "Biogas ke Kuasa"),
           ("biomethane.html", "Biometana"), ("hydrogen-chp.html", "CHP Hidrogen"),
           ("equipment.html", "Peralatan"),
           ("calculator.html", "Alat Kejuruteraan"), ("about.html", "Tentang KSTS")],
    "zh": [("index.html", "首页"), ("biogas-to-power.html", "沼气发电"),
           ("biomethane.html", "生物天然气"), ("hydrogen-chp.html", "氢能热电联供"),
           ("equipment.html", "设备与范围"),
           ("calculator.html", "工程测算工具"), ("about.html", "关于 KSTS")],
}

CTA = {"en": "Request a study", "ms": "Minta kajian", "zh": "申请可行性评估"}
BRAND_SUB = {"en": "Biogas &amp; Bioenergy", "ms": "Biogas &amp; Biotenaga", "zh": "沼气与生物质能源"}

LOGO = """<svg width="34" height="34" viewBox="0 0 34 34" fill="none" aria-hidden="true">
<rect width="34" height="34" rx="9" fill="#0c1a26"/>
<path d="M17 6.5c3.6 2.4 6 6.2 6 10.2 0 3.3-2.7 6-6 6s-6-2.7-6-6c0-4 2.4-7.8 6-10.2Z" fill="#0f7a52"/>
<path d="M17 22.7v4.8M11 14.5h12" stroke="#fff" stroke-width="1.6" stroke-linecap="round" opacity=".85"/>
</svg>"""

FAVICON = ("data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 34 34'>"
           "<rect width='34' height='34' rx='9' fill='%230c1a26'/>"
           "<path d='M17 6.5c3.6 2.4 6 6.2 6 10.2 0 3.3-2.7 6-6 6s-6-2.7-6-6c0-4 2.4-7.8 6-10.2Z' fill='%230f7a52'/></svg>")


def L(lang, en, ms, zh):
    return {"en": en, "ms": ms, "zh": zh}[lang]


def head(lang, page, title, desc):
    prefix = dict((k, p) for k, p, _ in LANGS)[lang]
    asset = "../" if prefix else ""
    nav = "".join(
        '<li><a href="%s"%s>%s</a></li>' % (
            href, ' aria-current="page"' if href == page else "", label)
        for href, label in NAV[lang])
    alts = "".join(
        '<link rel="alternate" hreflang="%s" href="%s/%s%s">' % (
            {"en": "en", "ms": "ms", "zh": "zh"}[code], SITE,
            pre, page if page != "index.html" else "")
        for code, pre, _ in LANGS)
    def lang_link(cur_pre, tgt_pre, page):
        fname = page if page != "index.html" else "index.html"
        if cur_pre == tgt_pre:
            return fname
        if not cur_pre and tgt_pre:
            return tgt_pre + fname
        if cur_pre and not tgt_pre:
            return "../" + fname
        return "../" + tgt_pre + fname
    langs_html = "".join(
        '<a href="%s"%s title="%s" hreflang="%s"><span class="lg-full">%s</span><span class="lg-short">%s</span></a>' % (
            lang_link(prefix, pre, page),
            ' class="on"' if code == lang else "", label, code, label, SHORT[code])
        for code, pre, label in LANGS)
    return """<!doctype html>
<html lang="%s">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%s</title>
<meta name="description" content="%s">
<link rel="canonical" href="%s/%s%s">
%s
<meta property="og:type" content="website">
<meta property="og:site_name" content="KSTS K. S. Technical Services — Biogas &amp; Bioenergy">
<meta property="og:title" content="%s">
<meta property="og:description" content="%s">
<meta name="theme-color" content="#0c1a26">
<link rel="stylesheet" href="%sassets/css/style.css">
<link rel="icon" href="%s">
<script src="%sassets/js/site.js" defer></script>
<script type="application/ld+json">{"@context":"https://schema.org","@type":"Organization","name":"KSTS K. S. Technical Services","url":"%s/","address":{"@type":"PostalAddress","streetAddress":"Kg. Nangoh, NT 083017181 (Lot 2), 34 km Off Jalan Simpang Sapi Nangoh, Labuk-Sugut","addressLocality":"Telupid","addressRegion":"Sabah","addressCountry":"MY"},"contactPoint":{"@type":"ContactPoint","telephone":"+60 13-883 3833","email":"k.s.t.s_sabah@hotmail.com","contactType":"sales"}}</script>
</head>
<body>
<header class="site">
  <div class="wrap nav">
    <a class="brand" href="index.html">%s<span>KSTS<small>%s</small></span></a>
    <div class="lang" role="group" aria-label="Language / Bahasa / 语言">%s</div>
    <button class="menu-toggle" id="menuToggle" aria-label="Menu" aria-expanded="false">&#9776;</button>
    <ul id="navList">%s</ul>
    <a class="btn cta" href="contact.html">%s</a>
  </div>
</header>
""" % ({"en": "en", "ms": "ms", "zh": "zh"}[lang], title, desc, SITE, prefix,
       page if page != "index.html" else "", alts, title, desc, asset, FAVICON, asset,
       SITE, LOGO, BRAND_SUB[lang], langs_html, nav, CTA[lang])


def footer(lang):
    prefix = dict((k, p) for k, p, _ in LANGS)[lang]
    asset = "../" if prefix else ""
    f = {
        "en": {
            "blurb": "Biogas power, biomethane upgrading and bio-CNG for palm oil mills and agro-industry in Sabah and Sarawak. Technology partner: SINOPEC Dalian Research Institute of Petroleum and Petrochemicals; engineering by a Tsinghua University PhD team.",
            "h_sol": "Solutions", "h_co": "Company", "h_ct": "Contact",
            "l1": "POME biogas to power", "l2": "Biomethane &amp; bio-CNG",
            "l3": "Equipment &amp; scope", "l4": "Engineering tools",
            "l5": "Hydrogen CHP",
            "c1": "About KSTS", "c2": "Local partner profile", "c3": "Contact",
            "copy": "&copy; 2026 KSTS K. S. Technical Services. All rights reserved.",
            "disc": "Figures on this site are indicative and subject to site data and formal quotation.",
        },
        "ms": {
            "blurb": "Kuasa biogas, peningkatan biometana dan bio-CNG untuk kilang kelapa sawit dan industri pertanian di Sabah dan Sarawak. Rakan teknologi: Institut Penyelidikan Petroleum dan Petrokimia Dalian SINOPEC; kejuruteraan oleh pasukan PhD Universiti Tsinghua.",
            "h_sol": "Penyelesaian", "h_co": "Syarikat", "h_ct": "Hubungi",
            "l1": "Biogas POME ke kuasa", "l2": "Biometana &amp; bio-CNG",
            "l3": "Peralatan &amp; skop", "l4": "Alat kejuruteraan",
            "l5": "CHP hidrogen",
            "c1": "Tentang KSTS", "c2": "Profil rakan tempatan", "c3": "Hubungi",
            "copy": "&copy; 2026 KSTS K. S. Technical Services. Hak cipta terpelihara.",
            "disc": "Angka di laman ini adalah indikatif dan tertakluk kepada data tapak dan sebut harga rasmi.",
        },
        "zh": {
            "blurb": "面向沙巴与砂拉越棕榈油厂及农产加工业的沼气发电、生物天然气提纯与 Bio-CNG。技术伙伴：中国石化大连研究院（清华大学博士团队）。",
            "h_sol": "解决方案", "h_co": "公司", "h_ct": "联系",
            "l1": "POME 沼气发电", "l2": "生物天然气 / Bio-CNG",
            "l3": "设备与供货范围", "l4": "工程测算工具",
            "l5": "氢能热电联供",
            "c1": "关于 KSTS", "c2": "本地伙伴简介", "c3": "联系我们",
            "copy": "&copy; 2026 KSTS K. S. Technical Services. 版权所有。",
            "disc": "本页数据均为测算参考值，实际以现场实测数据与正式报价为准。",
        },
    }[lang]
    return """<footer class="site">
  <div class="wrap">
    <div class="fgrid">
      <div>
        <a class="brand" href="index.html" style="color:#fff">%s<span>KSTS<small style="color:#9fb4c0">%s</small></span></a>
        <p class="small" style="color:#9fb4c0;margin-top:14px">%s</p>
      </div>
      <div><h4>%s</h4><ul>
        <li><a href="biogas-to-power.html">%s</a></li>
        <li><a href="biomethane.html">%s</a></li>
        <li><a href="hydrogen-chp.html">%s</a></li>
        <li><a href="equipment.html">%s</a></li>
        <li><a href="calculator.html">%s</a></li>
      </ul></div>
      <div><h4>%s</h4><ul>
        <li><a href="about.html">%s</a></li>
        <li><a href="about.html#partner">%s</a></li>
        <li><a href="contact.html">%s</a></li>
      </ul></div>
      <div><h4>%s</h4><ul>
        <li>KSTS K. S. Technical Services<br><span class="small">MPS: R14722/2009</span></li>
        <li>Kg. Nangoh, NT 083017181 (Lot 2),<br>34 km Off Jalan Simpang Sapi Nangoh,<br>Labuk&ndash;Sugut, Telupid, Sabah, Malaysia</li>
        <li><a href="mailto:k.s.t.s_sabah@hotmail.com">k.s.t.s_sabah@hotmail.com</a></li>
        <li><a href="tel:+60138833833">+60 13-883 3833</a></li>
      </ul></div>
    </div>
    <div class="copy"><span>%s</span><span>%s</span></div>
  </div>
</footer>
</body>
</html>
""" % (LOGO, BRAND_SUB[lang], f["blurb"], f["h_sol"], f["l1"], f["l2"], f["l5"], f["l3"], f["l4"],
       f["h_co"], f["c1"], f["c2"], f["c3"], f["h_ct"], f["copy"], f["disc"])


def write_page(lang, page, title, desc, body):
    prefix = dict((k, p) for k, p, _ in LANGS)[lang]
    outdir = os.path.join(ROOT, prefix) if prefix else ROOT
    os.makedirs(outdir, exist_ok=True)
    path = os.path.join(outdir, page)
    html = head(lang, page, title, desc) + body + footer(lang)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(html)
    print("wrote", os.path.relpath(path, ROOT), len(html))
