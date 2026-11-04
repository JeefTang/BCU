# -*- coding: utf-8 -*-
import os
from build3 import write_page, LANGS, SITE
import pages3
import pages_hchp

PAGES = [
    ("index.html", pages3.index,
     {"en": "KSTS — Biogas to Power &amp; Biomethane | Sabah, Malaysia",
      "ms": "KSTS — Biogas ke Kuasa &amp; Biometana | Sabah, Malaysia",
      "zh": "KSTS — 沼气发电与生物天然气 | 马来西亚沙巴"},
     {"en": "POME biogas power plants, biomethane upgrading and bio-CNG for palm oil mills in Sabah and Sarawak. Free engineering calculators.",
      "ms": "Loji kuasa biogas POME, peningkatan biometana dan bio-CNG untuk kilang kelapa sawit di Sabah dan Sarawak. Kalkulator kejuruteraan percuma.",
      "zh": "面向沙巴与砂拉越棕榈油厂的 POME 沼气发电、生物天然气提纯与 Bio-CNG，附五个免费工程计算器。"}),
    ("biogas-to-power.html", pages3.power,
     {"en": "POME Biogas to Power — Engines, Gas Treatment, O&amp;M | KSTS",
      "ms": "Biogas POME ke Kuasa — Enjin, Rawatan Gas, O&amp;M | KSTS",
      "zh": "POME 沼气发电 — 机组、气体净化与运维 | KSTS"},
     {"en": "Covered lagoon to grid-tie: gas capture, desulfurisation, 300 kW–2 MW engines and heat recovery for Malaysian palm oil mills.",
      "ms": "Dari kolam bertutup ke sambungan grid: penangkapan gas, nyahsulfur, enjin 300 kW–2 MW dan pemulihan haba.",
      "zh": "从覆盖塘到并网：沼气收集、脱硫、300 kW–2 MW 机组与余热回收。"}),
    ("biomethane.html", pages3.biomethane,
     {"en": "Biomethane &amp; Bio-CNG Upgrading to 97% CH4 | KSTS",
      "ms": "Peningkatan Biometana &amp; Bio-CNG ke 97% CH4 | KSTS",
      "zh": "生物天然气与 Bio-CNG：提纯至 97% 甲烷 | KSTS"},
     {"en": "Upgrade POME biogas to ≥97% methane for boiler fuel or bio-CNG. PSA, water scrubbing and membrane comparison.",
      "ms": "Tingkatkan biogas POME ke ≥97% metana untuk bahan api dandang atau bio-CNG. Perbandingan PSA, scrubber air dan membran.",
      "zh": "把 POME 沼气提纯至 ≥97% 甲烷，供锅炉或 Bio-CNG。PSA、水洗、膜分离路线对比。"}),
    ("hydrogen-chp.html", pages_hchp.hydrogen,
     {"en": "Hydrogen CHP 7.5–100 kW — Methane Reforming Fuel Cell Cogeneration | KSTS",
      "ms": "CHP Hidrogen 7.5–100 kW — Sel Bahan Api Pembentukan Semula Metana | KSTS",
      "zh": "氢能热电联供 7.5–100 kW — 甲烷重整燃料电池 | KSTS"},
     {"en": "Bottled 97% biomethane reformed to hydrogen on site, converted to power and hot water by a fuel cell: no noise, no NOx, no SOx, no particulates — water is the only by-product. 7.5–100 kW, FOB RM 10,000/kW to Malaysia.",
      "ms": "Biometana 97% dibentuk semula menjadi hidrogen di tapak, ditukar kepada kuasa dan air panas oleh sel bahan api: tiada bunyi, tiada NOx, tiada SOx, tiada zarah — air satu-satunya hasil sampingan. 7.5–100 kW, FOB RM 10,000/kW.",
      "zh": "97% 瓶装生物天然气现场重整制氢，燃料电池同时供电与热水：无噪音、无氮氧化物、无硫氧化物、无粉尘，唯一副产物是水。7.5–100 kW，出口马来西亚 FOB 价 RM 10,000/kW。"}),
    ("equipment.html", pages3.equipment,
     {"en": "Equipment &amp; Scope — Gas Engines, Desulfurisation, Upgrading | KSTS",
      "ms": "Peralatan &amp; Skop — Enjin Gas, Nyahsulfur, Peningkatan | KSTS",
      "zh": "设备与供货范围 — 燃气机组、脱硫、提纯 | KSTS"},
     {"en": "Biogas gensets 300 kW–2 MW, desulfurisation, gas conditioning, flares, heat recovery and upgrading skids with a clear scope matrix.",
      "ms": "Genset biogas 300 kW–2 MW, nyahsulfur, pengkondisian gas, flare, pemulihan haba dan skid peningkatan dengan matriks skop jelas.",
      "zh": "300 kW–2 MW 沼气机组、脱硫、净化、火炬、余热回收与提纯撬，附清晰的供货范围矩阵。"}),
    ("calculator.html", pages3.calculator,
     {"en": "Engineering Calculators — Biogas to Power, Sizing, Biomethane, Economics | KSTS",
      "ms": "Kalkulator Kejuruteraan — Biogas ke Kuasa, Saiz, Biometana, Ekonomi | KSTS",
      "zh": "工程计算器 — 沼气发电、选型、提纯与项目经济性 | KSTS"},
     {"en": "Five free engineering calculators: biogas to electricity and heat, capacity sizing, mill throughput to biogas, upgrading yield and project economics.",
      "ms": "Lima kalkulator kejuruteraan percuma: biogas ke elektrik dan haba, saiz kapasiti, kemampuan kilang ke biogas, hasil peningkatan dan ekonomi projek.",
      "zh": "五个免费工程计算器：沼气发电与余热、容量选型、压榨量产气、提纯收率、项目经济性。"}),
    ("about.html", pages3.about,
     {"en": "About KSTS — Sabah Biogas Contractor &amp; Local Partner",
      "ms": "Tentang KSTS — Kontraktor Biogas Sabah &amp; Rakan Tempatan",
      "zh": "关于 KSTS — 沙巴沼气承包商与本地伙伴"},
     {"en": "KSTS K. S. Technical Services: CIDB-registered, Bumiputera Sabah contractor with DOSH and ECOS registrations.",
      "ms": "KSTS K. S. Technical Services: kontraktor Bumiputera Sabah berdaftar CIDB dengan pendaftaran DOSH dan ECOS.",
      "zh": "KSTS K. S. Technical Services：CIDB 注册、沙巴土著企业，持 DOSH 与 ECOS 资质。"}),
    ("contact.html", pages3.contact,
     {"en": "Contact KSTS — Biogas Project Enquiry, Sabah",
      "ms": "Hubungi KSTS — Pertanyaan Projek Biogas, Sabah",
      "zh": "联系 KSTS — 沼气项目咨询（沙巴）"},
     {"en": "Send mill throughput, pond volume and gas data for a pre-feasibility. KSTS, Telupid, Sabah. Reply within three working days.",
      "ms": "Hantar kemampuan kilang, isipadu kolam dan data gas untuk pra-kelayakan. KSTS, Telupid, Sabah. Balas dalam tiga hari bekerja.",
      "zh": "提交油厂处理量、池塘容积与气量数据，获取预可研。KSTS，沙巴 Telupid，三个工作日内回复。"}),
]

for fname, fn, titles, descs in PAGES:
    for lang, prefix, _ in LANGS:
        write_page(lang, fname, titles[lang], descs[lang], fn(lang))

# 404 pages
for lang, prefix, _ in LANGS:
    from build3 import L
    body = ('<section class="page-head"><div class="wrap"><p class="eyebrow">404</p>'
            + "<h1>" + L(lang, "Page not found", "Halaman tidak dijumpai", "页面不存在") + "</h1>"
            + '<p class="lead">' + L(lang, "The page you asked for does not exist.", "Halaman yang diminta tidak wujud.", "你访问的页面不存在。") + "</p>"
            + '<p style="margin-top:22px"><a class="btn" href="index.html">' + L(lang, "Back to home", "Kembali ke utama", "返回首页") + "</a>"
            + ' <a class="btn ghost" href="../index.html" style="margin-left:8px">English</a>'
            + ' <a class="btn ghost" href="../ms/index.html" style="margin-left:8px">Bahasa Melayu</a>'
            + ' <a class="btn ghost" href="../zh/index.html" style="margin-left:8px">中文</a></p>'
            + '<p class="small" style="margin-top:18px">' + L(lang, "Check the address — our site lives at jeeftang.github.io/BCU/ (capital letters).", "Semak alamat — laman kami di jeeftang.github.io/BCU/ (huruf besar).", "请检查网址——本站地址为 jeeftang.github.io/BCU/（注意大写）。") + "</p></div></section>")
    write_page(lang, "404.html", "404 | KSTS", "404", body)

# sitemap with hreflang alternates
lines = ['<?xml version="1.0" encoding="UTF-8"?>',
         '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">']
for fname, *_ in PAGES:
    for lang, prefix, _ in LANGS:
        loc = SITE + "/" + prefix + ("" if fname == "index.html" else fname)
        lines.append("  <url>")
        lines.append("    <loc>%s</loc>" % loc)
        for l2, p2, _ in LANGS:
            alt = SITE + "/" + p2 + ("" if fname == "index.html" else fname)
            lines.append('    <xhtml:link rel="alternate" hreflang="%s" href="%s"/>' % ({"en":"en","ms":"ms","zh":"zh"}[l2], alt))
        lines.append("    <changefreq>monthly</changefreq><priority>%s</priority>" % ("1.0" if fname == "index.html" else "0.8"))
        lines.append("  </url>")
lines.append("</urlset>")
open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "sitemap.xml"), "w", encoding="utf-8").write("\n".join(lines) + "\n")

open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "robots.txt"), "w", encoding="utf-8").write(
    "User-agent: *\nAllow: /\nSitemap: %s/sitemap.xml\n" % SITE)
print("done")
