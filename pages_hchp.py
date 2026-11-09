# -*- coding: utf-8 -*-
"""Hydrogen CHP page: methane reforming fuel-cell cogeneration, 7.5–100 kW."""
from build3 import L

# ---- locked design basis -------------------------------------------------
KWH_PER_NM3_CH4 = 9.94      # LHV
EFF_E = 42.0                # % electrical, LHV
EFF_H = 43.0                # % recoverable heat, LHV
PRICE_RM_KW = 10000         # FOB price to Malaysia, RM/kW, installation excluded
PRICE_RM_KW_RAW = 19500     # same, with integrated front-end purification for raw 60% biogas
# (kW electrical, fuel input in 0.1 kW, indicative price RM)
MODELS = [
    (7.5, 179, 75000), (10, 238, 100000), (15, 357, 150000), (20, 476, 200000),
    (30, 714, 300000), (50, 1190, 500000), (75, 1786, 750000), (100, 2381, 1000000),
]


def _rows(lang):
    out = []
    for kw, fuel10, price in MODELS:
        fuel_kw = fuel10 / 10.0
        ch4 = fuel_kw / KWH_PER_NM3_CH4
        heat = kw * EFF_H / EFF_E
        hot = heat * 3600 / (4.18 * 50)  # L/h at ΔT 50 K
        label = ("7.5 kW" if kw == 7.5 else "%d kW" % kw)
        out.append(
            "<tr><td><b>%s</b></td><td class=\"num\">%.1f</td><td class=\"num\">%.2f</td>"
            "<td class=\"num\">%.1f</td><td class=\"num\">%s</td><td class=\"num\">RM %s</td>"
            "<td class=\"num\">RM %s</td></tr>"
            % (label, fuel_kw, ch4, heat, "{:,.0f}".format(hot), "{:,.0f}".format(price),
               "{:,.0f}".format(kw * PRICE_RM_KW_RAW)))
    return "\n".join(out)


def hydrogen(lang):
    asset = "../" if lang != "en" else ""
    s = dict(
        eyebrow=L(lang, "Hydrogen CHP · 7.5–100 kW", "CHP hidrogen · 7.5–100 kW", "氢能热电联供 · 7.5–100 kW"),
        h1=L(lang,
             "Bottled biomethane in, power and hot water out.",
             "Biometana dalam botol masuk, kuasa dan air panas keluar.",
             "瓶装生物天然气进去，电和热水出来。"),
        lead=L(lang,
               "Methane reforming plus a fuel cell: the same architecture as Japan's household fuel-cell CHP, scaled to estate housing, resorts, mills and off-grid communities. Two feeds work: bottled 97% biomethane, or raw 60% biogas taken straight from the mill with an integrated purification front end. Either way the methane is reformed on site into hydrogen and converted to electricity and 60–70 °C hot water — no pipeline, no diesel, no flame at the point of use.",
               "Pembentukan semula metana dengan sel bahan api: seni bina yang sama seperti CHP sel bahan api rumah Jepun, diskalakan untuk perumahan ladang, resort, kilang dan komuniti luar grid. Dua suapan boleh digunakan: biometana 97% dalam botol, atau biogas mentah 60% terus dari kilang dengan bahagian penulenan bersepadu di hadapan. Sama ada cara, metana dibentuk semula di tapak menjadi hidrogen dan ditukar kepada elektrik dan air panas 60–70 °C — tanpa saluran paip, tanpa diesel, tanpa api di tempat penggunaan.",
               "甲烷重整 + 燃料电池：与日本家用燃料电池热电联供同一架构，功率放大到种植园宿舍、度假村、厂区与离网社区。两种进气都能用：瓶装 97% 生物天然气，或者直接从油厂取 60% 原沼气、前端配一体化净化装置。无论哪种，都是现场重整制氢，再转成电与 60–70 ℃ 热水——不用管网、不用柴油、用能端无明火。"),
        k1=L(lang, "FOB price per kW: bottled 97% gas / raw biogas with integrated purification", "Harga FOB per kW: gas botol 97% / biogas mentah dengan penulenan bersepadu", "FOB 单价：瓶装 97% 气 / 带一体化净化的原沼气"),
        k2=L(lang, "Electrical efficiency, guaranteed (LHV)", "Kecekapan elektrik, dijamin (LHV)", "发电效率（厂家保证值·低热值）"),
        k3=L(lang, "Recoverable heat, guaranteed (LHV)", "Haba boleh pulih, dijamin (LHV)", "可回收余热（厂家保证值）"),
        k4=L(lang, "Fuel per kWh sent out", "Bahan api per kWh dihantar", "每度电耗气"),
    )
    rows = _rows(lang)
    return f"""
<section class="page-head">
  <div class="wrap">
    <p class="eyebrow">{s['eyebrow']}</p>
    <h1>{s['h1']}</h1>
    <p class="lead">{s['lead']}</p>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="stats" style="margin-top:0">
      <div class="stat"><b>RM 10,000 / 19,500</b><span>{s['k1']} · /kW</span></div>
      <div class="stat"><b>42%</b><span>{s['k2']}</span></div>
      <div class="stat"><b>43%</b><span>{s['k3']}</span></div>
      <div class="stat"><b>0.24 Nm³</b><span>{s['k4']}</span></div>
    </div>
  </div>
</section>

<section id="emissions">
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow">{L(lang,'Six zeros','Enam sifar','六个没有')}</p>
      <h2>{L(lang,'Nothing leaves this unit but water.','Tiada apa keluar dari unit ini kecuali air.','这台机组排出来的，只有水。')}</h2>
      <p class="lead">{L(lang,
        'No burner, no engine, no flue in the usual sense. This is the strongest reason to choose reforming plus a fuel cell over a diesel or gas engine — and it is measurable at the fence line, not a marketing line.',
        'Tiada pembakar, tiada enjin, tiada cerobong. Ini sebab terkuat memilih pembentukan semula serta sel bahan api berbanding enjin diesel atau gas — dan ia boleh diukur di pagar tapak.',
        '没有燃烧器、没有发动机、没有传统意义的烟囱。这是选重整+燃料电池而不是柴油机或燃气机的最大理由——而且是在围墙外能测出来的，不是宣传话术。')}</p>
    </div>
    <div class="grid-3">
      <article class="card"><p class="tag">01 · {L(lang,'No noise','Tiada bunyi','无噪音')}</p>
        <h3>{L(lang,'No engine, no burner','Tiada enjin, tiada pembakar','没有发动机，也没有燃烧器')}</h3>
        <p>{L(lang,'The only moving parts are a blower and pumps. About 55 dB(A) at one metre — quieter than a normal conversation, so the unit can stand beside staff housing.','Bahagian bergerak hanya blower dan pam. Kira-kira 55 dB(A) pada satu meter — lebih senyap daripada perbualan biasa.','唯一运动部件是风机和水泵。1 米处约 55 dB(A)，比正常交谈还轻，可以直接挨着宿舍放。')}</p></article>
      <article class="card"><p class="tag">02 · {L(lang,'No nitrogen oxides','Tiada nitrogen oksida','无氮氧化物')}</p>
        <h3>NOx = 0</h3>
        <p>{L(lang,'A fuel cell runs at 60–200 °C. With no high-temperature flame, thermal NOx cannot form at all — it is below detection, not merely “low”.','Sel bahan api beroperasi pada 60–200 °C. Tanpa api bersuhu tinggi, NOx terma tidak terbentuk — di bawah pengesanan, bukan sekadar “rendah”.','燃料电池工作在 60–200 ℃，没有高温火焰，热力型 NOx 根本生成不了——是测不出，不是“低”。')}</p></article>
      <article class="card"><p class="tag">03 · {L(lang,'No sulphur oxides','Tiada sulfur oksida','无硫氧化物')}</p>
        <h3>SOx = 0</h3>
        <p>{L(lang,'Gas is desulphurised to below 1 ppm before the reformer. No sulphur enters the process, so none can leave it — no SO₂, no acid smell, no corrosion downstream.','Gas dinyahsulfur di bawah 1 ppm sebelum reformer. Tiada sulfur masuk proses, jadi tiada yang keluar — tiada SO₂, tiada bau asid.','燃气进重整器前先脱硫到 1 ppm 以下。硫不进工艺，就不会从排气出去——没有 SO₂、没有酸味、下游不腐蚀。')}</p></article>
      <article class="card"><p class="tag">04 · {L(lang,'No dust or particulates','Tiada habuk atau zarah','无粉尘颗粒物')}</p>
        <h3>PM = 0</h3>
        <p>{L(lang,'Gas fuel, sealed process, no combustion air and no flue: no particulates, no black smoke, no smell — unlike diesel exhaust, which is a known health hazard.','Bahan api gas, proses tertutup, tiada udara pembakaran dan tiada cerobong: tiada zarah, tiada asap hitam, tiada bau.','气体燃料、全封闭工艺、不引燃烧空气、没有烟囱——没有颗粒物、没有黑烟、没有异味。柴油尾气是公认的健康危害，这里没有。')}</p></article>
      <article class="card"><p class="tag">05 · {L(lang,'Pure water only','Air tulen sahaja','只有纯净水')}</p>
        <h3>H₂O</h3>
        <p>{L(lang,'The electrochemical reaction produces water and heat. The water is clean enough to recover for washing or irrigation instead of discharging it.','Tindak balas elektrokimia menghasilkan air dan haba. Air itu cukup bersih untuk dipulihkan bagi cucian atau pengairan.','电化学反应只生成水和热。水干净到可以回收用于冲洗或灌溉，而不是当废水排掉。')}</p></article>
      <article class="card"><p class="tag">06 · {L(lang,'Near-zero CO₂','CO₂ hampir sifar','少量 CO₂，接近零排放')}</p>
        <h3>CO₂ ≈ 0</h3>
        <p>{L(lang,'The carbon is short-cycle carbon from palm waste, and reforming gives a concentrated CO₂ stream that is far easier to capture than dilute flue gas. This is a path to zero, not just “lower”.','Karbon ialah karbon kitaran pendek daripada sisa sawit, dan pembentukan semula memberi aliran CO₂ pekat yang lebih mudah ditangkap.','碳来自棕榈废料的短周期碳；重整还把 CO₂ 富集成高浓度气流，比稀释烟气好捕集得多——这是通往零排放的路，不只是“更低”。')}</p></article>
    </div>
    <div class="band" style="margin-top:30px">
      <div>
        <h2>{L(lang,'You can hear the difference at the fence line.','Anda boleh dengar bezanya di pagar tapak.','站在围墙外，听得出来，也测得出来。')}</h2>
        <p>{L(lang,'A diesel genset is the exact opposite on all six counts: 95–105 dB(A), NOx, SOx, black smoke and a fuel tank. Ask for the emissions sheet with the quotation.','Genset diesel adalah sebaliknya pada keenam-enam perkara: 95–105 dB(A), NOx, SOx, asap hitam dan tangki bahan api. Minta helaian pelepasan bersama sebut harga.','柴油机组在这六项上正好相反：95–105 dB(A)、NOx、SOx、黑烟，外加一个油罐。要排放清单，随报价一起给。')}</p>
      </div>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow">{L(lang,'Why this fits Malaysia','Mengapa sesuai untuk Malaysia','为什么适合马来西亚')}</p>
      <h2>{L(lang,'The fuel chain already exists — the generator was missing','Rantaian bahan api sudah ada — penjana yang tiada','燃料链已经跑通，缺的是发电端')}</h2>
      <p class="lead">{L(lang,
        'Biogas is already being upgraded to 97% methane and sold in cylinders to households and shops. That means the hard part — gas cleaning, compression and distribution — is solved. What is missing is a quiet, low-maintenance generator that can burn that gas where it is used.',
        'Biogas sudah ditingkatkan kepada 97% metana dan dijual dalam silinder kepada rumah dan kedai. Ini bermakna bahagian sukar — pembersihan gas, pemampatan dan pengedaran — sudah selesai. Yang kurang ialah penjana senyap, penyelenggaraan rendah yang boleh menggunakan gas itu di tempat ia digunakan.',
        '沼气提纯到 97% 甲烷、装瓶卖给居民和商铺，这条链已经跑通了。也就是说最难的净化、压缩、配送环节已经解决，缺的是一个安静、少维护、能就地用掉这瓶气的发电装置。')}</p>
    </div>
    <div class="grid-3">
      <article class="card prod-card"><div>
        <p class="tag">01 · {L(lang,'Fuel','Bahan api','燃料')}</p>
        <h3>{L(lang,'Bottled biomethane, no pipeline','Biometana botol, tanpa paip','瓶装生物天然气，不用管网')}</h3>
        <p>{L(lang,
          'A 50-litre cylinder at 200 bar holds about 10 Nm³ of methane — roughly 99 kWh of fuel, or 10 hours at 10 kW electrical. Cylinders can be swapped like LPG, so there is no gas network to build and no stranded asset if demand moves.',
          'Silinder 50 liter pada 200 bar mengandungi kira-kira 10 Nm³ metana — lebih kurang 99 kWh bahan api, atau 10 jam pada 10 kW elektrik. Silinder boleh ditukar seperti LPG, jadi tiada rangkaian gas untuk dibina.',
          '50 升 200 bar 钢瓶约装 10 Nm³ 甲烷，约 99 kWh 燃料，供 10 kW 机组跑 10 小时。换瓶像换 LPG 一样简单，不用建管网，需求搬走也不留死资产。')}</p>
      </div></article>
      <article class="card prod-card"><div>
        <p class="tag">02 · {L(lang,'Cost','Kos','成本')}</p>
        <h3>{L(lang,'Against diesel, not against the grid','Berbanding diesel, bukan grid','对标柴油，不对标电网')}</h3>
        <p>{L(lang,
          'Off-grid estates, islands and remote resorts in Sabah pay RM 0.90–1.30 per kWh for diesel power once fuel logistics, servicing and downtime are counted. That is the number this unit competes with — not the subsidised grid tariff.',
          'Ladang luar grid, pulau dan resort terpencil di Sabah membayar RM 0.90–1.30 setiap kWh untuk kuasa diesel setelah mengambil kira logistik bahan api, penyelenggaraan dan masa henti. Itulah angka yang disaingi oleh unit ini.',
          '沙巴的离网种植园、岛屿和偏远度假村，算上运油、保养和停机，柴油发电实际成本在 RM 0.90–1.30/kWh。这台机组对标的是这个数，不是补贴后的电网电价。')}</p>
      </div></article>
      <article class="card prod-card"><div>
        <p class="tag">03 · {L(lang,'Heat','Haba','余热')}</p>
        <h3>{L(lang,'Hot water is half the output','Air panas ialah separuh output','一半产出是热水')}</h3>
        <p>{L(lang,
          'A fuel cell makes electricity and heat at the same time: 42% electric, 43% recoverable as 60–70 °C water. Staff housing, kitchens, laundries, sterilisation and hotel hot water all use that heat directly, which is what lifts total efficiency to about 85%.',
          'Sel bahan api menghasilkan elektrik dan haba serentak: 42% elektrik, 43% boleh pulih sebagai air 60–70 °C. Perumahan kakitangan, dapur, dobi, pensterilan dan air panas hotel menggunakan haba itu terus.',
          '燃料电池同时出电和热：42% 电、43% 可回收为 60–70 ℃ 热水。员工宿舍、厨房、洗衣、消毒、酒店热水都能直接消纳，综合效率因此到 85% 左右。')}</p>
      </div></article>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow">{L(lang,'Two feed options','Dua pilihan suapan','两种进气方案')}</p>
      <h2>{L(lang,'Bottled gas, or raw biogas straight from the mill','Gas botol, atau biogas mentah terus dari kilang','瓶装气，或者直接从油厂取原沼气')}</h2>
      <p class="lead">{L(lang,
        'The reformer and fuel cell are the same in both cases. Only the front end changes — and it is built into the same package, not bought as a separate upgrading plant.',
        'Reformer dan sel bahan api sama dalam kedua-dua kes. Hanya bahagian hadapan berubah — dan ia dibina dalam pakej yang sama, bukan dibeli sebagai loji peningkatan berasingan.',
        '两种情况里，重整器和燃料电池是同一套；变的只是前端——而且前端净化就做在同一个机组里，不是另买一套提纯站。')}</p>
    </div>
    <div class="grid-2">
      <article class="card prod-card"><div>
        <p class="tag">A · {L(lang,'Bottled 97% biomethane','Biometana 97% dalam botol','瓶装 97% 生物天然气')}</p>
        <h3>{L(lang,'Lowest investment, fuel bought by the cylinder','Pelaburan terendah, bahan api dibeli ikut silinder','投资最低，燃料按瓶买')}</h3>
        <p>{L(lang,
          'Standard specification. The gas arrives at 200 bar already at 97% methane, so the unit only needs desulphurisation and filtration before the reformer. Nothing to build, nothing to operate upstream — but you pay the bottled-gas price for every Nm³, and you depend on the cylinder supply chain.',
          'Spesifikasi standard. Gas tiba pada 200 bar dan sudah 97% metana, jadi unit hanya perlu nyahsulfur dan penapisan sebelum reformer. Tiada yang perlu dibina atau dikendalikan di huluan — tetapi anda membayar harga gas botol bagi setiap Nm³ dan bergantung pada rantaian bekalan silinder.',
          '标准配置。气到现场就是 200 bar、97% 甲烷，机组只需脱硫和过滤就能进重整器。上游不用建、不用运行——但每一方气都要按瓶装气价付钱，而且依赖钢瓶供应链。')}</p>
        <p class="small"><b>RM 10,000/kW</b> · {L(lang,'FOB, installation excluded','FOB, pemasangan tidak termasuk','FOB 价，不含安装')}</p>
      </div></article>
      <article class="card prod-card"><div>
        <p class="tag">B · {L(lang,'Raw biogas, about 60% CH₄','Biogas mentah, kira-kira 60% CH₄','原沼气，约 60% 甲烷')}</p>
        <h3>{L(lang,'Straight from the palm oil mill — purification built in','Terus dari kilang sawit — penulenan terbina dalam','直接从棕油厂取气——净化装置随机一体化')}</h3>
        <p>{L(lang,
          'Take the biogas directly off the mill pond and skip upgrading, bottling and trucking altogether. An integrated front-end purification module — desulphurisation, CO₂ removal, drying and compression — is supplied as part of our unit and lifts the gas to the ≥95% methane the reformer needs. Higher investment than option A, but the fuel is the mill’s own biogas instead of bought cylinders, and there is no separate upgrading plant to pay for.',
          'Ambil biogas terus dari kolam kilang dan langkaui peningkatan, pembotolan serta pengangkutan. Modul penulenan bersepadu di hadapan — nyahsulfur, penyingkiran CO₂, pengeringan dan pemampatan — dibekalkan sebagai sebahagian unit kami dan menaikkan gas ke ≥95% metana yang diperlukan reformer. Pelaburan lebih tinggi daripada pilihan A, tetapi bahan api ialah biogas kilang sendiri, bukan silinder yang dibeli, dan tiada loji peningkatan berasingan.',
          '直接把油厂厌氧塘的沼气接过来，省掉提纯、装瓶、运输整条链。前端一体化净化模块——脱硫、脱 CO₂、干燥、增压——随我们的机组一起供货，把气质提到重整器需要的 ≥95% 甲烷。投资比方案 A 高，但烧的是油厂自己的沼气，不是买来的瓶装气，也不用另建提纯站。')}</p>
        <p class="small"><b>RM 19,500/kW</b> · {L(lang,'FOB, integrated purification included in the unit','FOB, penulenan bersepadu termasuk dalam unit','FOB 价，一体化净化已含在机组内')}</p>
      </div></article>
    </div>
    <p class="note">{L(lang,
      'Both options use the same reformer and fuel cell; option B simply adds the purification front end inside the same enclosure or skid. The added cost depends on gas flow, H₂S and CO₂ content, so it is quoted per site after a gas analysis — send us your measured flow, methane content and H₂S and we will price both versions side by side.',
      'Kedua-dua pilihan menggunakan reformer dan sel bahan api yang sama; pilihan B hanya menambah bahagian penulenan di hadapan dalam selongsong atau skid yang sama. Kos tambahan bergantung pada aliran gas, kandungan H₂S dan CO₂, jadi ia disebut harga mengikut tapak selepas analisis gas — hantar aliran, kandungan metana dan H₂S yang diukur dan kami akan harga kedua-dua versi bersebelahan.',
      '两种方案的重整器与燃料电池完全一样，方案 B 只是把净化前端做进同一个机柜或撬块。增加多少投资取决于气量、硫化氢和二氧化碳含量，需按气质分析后逐点报价——把实测流量、甲烷含量、硫化氢给我们，两个版本可以并排报价。')}</p>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow">{L(lang,'Process','Proses','工艺')}</p>
      <h2>{L(lang,'From methane to electrons in five steps','Dari metana ke elektron dalam lima langkah','五步从甲烷到电')}</h2>
    </div>
    <div class="steps" style="grid-template-columns:repeat(5,1fr)">
      <div class="step"><b>{L(lang,'Condition','Kondisi','净化')}</b><span>{L(lang,'Desulphurisation to below 1 ppm H₂S, plus filtration. The reformer catalyst is poisoned by sulphur. On raw 60% biogas the same integrated module also strips CO₂ and water.','Nyahsulfur di bawah 1 ppm H₂S, serta penapisan. Pemangkin reformer diracuni sulfur. Pada biogas mentah 60%, modul bersepadu yang sama juga menyingkirkan CO₂ dan air.','脱硫到 H₂S 低于 1 ppm，再加过滤。重整催化剂最怕硫；走 60% 原沼气时，同一个一体化模块还要脱 CO₂ 和脱水。')}</span></div>
      <div class="step"><b>{L(lang,'Reform','Bentuk semula','重整')}</b><span>{L(lang,'Steam reforming at 650–800 °C: CH₄ + H₂O → CO + 3H₂, followed by water-gas shift.','Pembentukan semula stim pada 650–800 °C: CH₄ + H₂O → CO + 3H₂, diikuti anjakan gas air.','650–800 ℃ 蒸汽重整：CH₄ + H₂O → CO + 3H₂，再经水煤气变换。')}</span></div>
      <div class="step"><b>{L(lang,'Purify','Tulenkan','提纯')}</b><span>{L(lang,'PSA or membrane to 99.9% H₂; the off-gas is burned to heat the reformer, which is why efficiency holds.','PSA atau membran ke 99.9% H₂; gas sisa dibakar untuk memanaskan reformer.','PSA 或膜提纯到 99.9% 氢；尾气回烧给重整器供热，效率才守得住。')}</span></div>
      <div class="step"><b>{L(lang,'Convert','Tukar','发电')}</b><span>{L(lang,'PEM fuel cell at 65–75 °C, or PAFC at 160–200 °C for higher-grade heat.','Sel bahan api PEM pada 65–75 °C, atau PAFC pada 160–200 °C untuk haba gred lebih tinggi.','PEM 燃料电池 65–75 ℃；要更高品位余热可选 PAFC（160–200 ℃）。')}</span></div>
      <div class="step"><b>{L(lang,'Deliver','Hantar','供能')}</b><span>{L(lang,'230/400 V AC plus 60–70 °C hot water. Grid-tie or island mode, black-start capable.','AC 230/400 V serta air panas 60–70 °C. Sambungan grid atau mod pulau.','230/400 V 交流电 + 60–70 ℃ 热水；可并网也可孤岛运行，支持黑启动。')}</span></div>
    </div>
    <p class="note">{L(lang,
      'No hydrogen is stored. Hydrogen is made on demand and consumed inside the unit — that is what keeps the safety case simple and avoids a pressure vessel on site.',
      'Tiada hidrogen disimpan. Hidrogen dihasilkan atas permintaan dan digunakan di dalam unit — ini memudahkan keselamatan dan mengelakkan bekas tekanan di tapak.',
      '系统不储氢：氢气按需现制、机内即用，安全评估简单，现场没有高压储氢容器。')}</p>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow">{L(lang,'Range','Julat','机型范围')}</p>
      <h2>{L(lang,'Eight models, 7.5 to 100 kW','Lapan model, 7.5 hingga 100 kW','八个机型，7.5 到 100 kW')}</h2>
      <p class="lead">{L(lang,
        'Fuel figures are at rated output, 97% methane, LHV basis. Hot water is at a 50 K rise (20 → 70 °C). Prices are FOB to Malaysia at RM 10,000 per kW, installation excluded.',
        'Angka bahan api pada output terkadar, 97% metana, asas LHV. Air panas pada kenaikan 50 K (20 → 70 °C). Harga ialah FOB ke Malaysia pada RM 10,000 per kW, pemasangan tidak termasuk.',
        '燃料数据为额定出力、97% 甲烷、低热值口径；热水量按温升 50 K（20 → 70 ℃）。价格为出口马来西亚 FOB 价，每 kW 1 万马币，不含安装。')}</p>
    </div>
    <div class="table-wrap">
      <table>
        <thead><tr>
          <th>{L(lang,'Model','Model','机型')}</th>
          <th>{L(lang,'Fuel input (kW)','Input bahan api (kW)','燃料输入（kW）')}</th>
          <th>{L(lang,'CH₄ (Nm³/h)','CH₄ (Nm³/j)','甲烷（Nm³/h）')}</th>
          <th>{L(lang,'Heat (kW)','Haba (kW)','余热（kW）')}</th>
          <th>{L(lang,'Hot water 50 K (L/h)','Air panas 50 K (L/j)','热水 50 K（L/h）')}</th>
          <th>{L(lang,'Indicative price, bottled gas','Harga indikatif, gas botol','参考价（瓶装气）')}</th>
          <th>{L(lang,'Price, raw biogas with purification','Harga, biogas mentah dengan penulenan','参考价（原沼气含净化）')}</th>
        </tr></thead>
        <tbody>
{rows}
        </tbody>
      </table>
    </div>
    <p class="small" style="margin-top:14px">{L(lang,
      'Minimum order: 10 units per export shipment. Below that we still quote — with a one-off RM 60,000 export engineering and logistics charge and a small-order unit-price uplift; a single 7.5 kW unit shipped on its own spends as much on export overhead as it carries in margin. Units of 30 kW and above, or orders worth RM 300,000 and above, are exempt from the 10-unit minimum. '
      'Basis: methane LHV 9.94 kWh/Nm³; manufacturer-guaranteed 42% electrical and 43% heat recovery at rated output (85% combined) — to be reconfirmed against the guarantee sheet for each model. On raw biogas at 60% CH₄ the raw gas flow is about 1.67× the CH₄ figure, and the integrated purification module is sized to that flow. Prices are FOB Malaysia port, installation excluded: bottled 97% gas at RM 10,000/kW, raw 60% biogas with the integrated purification front end at RM 19,500/kW. Freight, insurance, SST, local installation, civils, cylinder storage, gas manifold and grid connection are excluded and quoted per site.',
      'Pesanan minimum: 10 unit setiap penghantaran eksport. Di bawah itu kami masih memberi sebut harga — dengan caj kejuruteraan dan logistik eksport RM 60,000 sekali serta kenaikan harga unit pesanan kecil; satu unit 7.5 kW yang dihantar bersendirian menghabiskan overhed eksport sebanyak marginnya. Unit 30 kW ke atas, atau pesanan bernilai RM 300,000 ke atas, dikecualikan daripada minimum 10 unit. '
      'Asas: LHV metana 9.94 kWh/Nm³; 42% elektrik dan 43% pemulihan haba dijamin pengeluar pada output terkadar (85% gabungan) — akan disahkan semula dengan helaian jaminan setiap model. Pada biogas mentah 60% CH₄, aliran gas mentah kira-kira 1.67× angka CH₄, dan modul penulenan bersepadu disaiz mengikut aliran itu. Harga FOB pelabuhan Malaysia, pemasangan tidak termasuk: gas botol 97% pada RM 10,000/kW, biogas mentah 60% dengan penulenan bersepadu pada RM 19,500/kW. Tambang, insurans, SST, pemasangan, kerja awam, stor silinder, manifold gas dan sambungan grid tidak termasuk.',
      '最小起订量：出口订单 10 台/单。低于此数仍报价，但加收一次性 RM 60,000 出口工程与物流费用，单价按小批量上浮——单台 7.5 kW 单独发运，出口环节的开销吃掉全部毛利。单机 30 kW 及以上、或订单金额 RM 30 万及以上，不受 10 台起订限制。 '
      '口径：甲烷低热值 9.94 kWh/Nm³；发电 42%、余热回收 43% 为厂家保证值（额定出力、综合 85%）——最终以各机型保证书为准。烧 60% 原沼气时，原气量约为表中甲烷量的 1.67 倍，一体化净化模块按该气量选型。价格为马来西亚港口 FOB，不含安装：瓶装 97% 气 RM 10,000/kW，60% 原沼气配一体化前端净化 RM 19,500/kW。运费、保险、SST、安装、土建、气瓶间、汇流排与并网均不含，按现场单独报价。')}</p>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow">{L(lang,'The unit','Unit','整机')}</p>
      <h2>{L(lang,'One cabinet: reformer, purification, fuel cell, heat recovery','Satu kabinet: reformer, penulenan, sel bahan api, pemulihan haba','一个柜子：重整、净化、燃料电池、余热回收')}</h2>
      <p class="lead">{L(lang,
        'Skid-mounted and factory-tested. Arrives as one enclosure, connects to gas, water and the distribution board — no separate reformer building, no flue, no engine room.',
        'Dipasang pada skid dan diuji di kilang. Tiba sebagai satu kandang, disambung ke gas, air dan papan agihan — tiada bangunan reformer berasingan, tiada cerobong, tiada bilik enjin.',
        '整机撬装、出厂前完成测试。到场就是一个柜体，接燃气、接水、接配电箱就能用——不需要单独的重整房间、不需要烟囱、不需要机房。')}</p>
    </div>
    <div class="gal gal-3">
      <figure><img src="{asset}assets/img/huasen/assembly-skid.jpg" alt="Skid-mounted reforming fuel cell CHP cabinet"><figcaption><b>{L(lang,'Skid-mounted cabinet','Kabinet pada skid','撬装柜')}</b><span>{L(lang,'Reformer, purification, fuel cell and heat recovery in one enclosure.','Reformer, penulenan, sel bahan api dan pemulihan haba dalam satu kandang.','重整、净化、燃料电池与余热回收集成在一个柜体内。')}</span></figcaption></figure>
      <figure><img src="{asset}assets/img/huasen/inside-01.jpg" alt="Inside the CHP cabinet"><figcaption><b>{L(lang,'Inside the cabinet','Di dalam kabinet','柜内')}</b><span>{L(lang,'Stack, gas manifold and control cabinet on the service side.','Stack, manifold gas dan kabinet kawalan di bahagian servis.','电堆、气路歧管与控制柜，保养侧。')}</span></figcaption></figure>
      <figure><img src="{asset}assets/img/huasen/inside-02.jpg" alt="Internal arrangement of the reforming fuel cell unit"><figcaption><b>{L(lang,'Internal arrangement','Susunan dalaman','内部布置')}</b><span>{L(lang,'All serviceable from the front; no specialist lifting gear needed on site.','Semua boleh diservis dari hadapan; tiada alat angkat khas diperlukan di tapak.','全面前保养，现场不需要专用起重工具。')}</span></figcaption></figure>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow">{L(lang,'Small units','Unit kecil','小型机组')}</p>
      <h2>{L(lang,'Home and shop scale, 5 to 10 kW','Skala rumah dan kedai, 5 hingga 10 kW','家庭与商铺规模，5 至 10 kW')}</h2>
      <p class="lead">{L(lang,
        'Compact all-in-one units for a house, a shop lot or a resort block: about 1.8 × 0.6 × 1.4 m for 10 kW, parallelable in blocks for larger loads.',
        'Unit padat semua-dalam-satu untuk rumah, kedai atau blok resort: kira-kira 1.8 × 0.6 × 1.4 m untuk 10 kW, boleh diparallelkan untuk beban lebih besar.',
        '家庭、店铺、度假村客房都能用的一体机：10 kW 约 1.8 × 0.6 × 1.4 m，多台可积木式并联扩容。')}</p>
    </div>
    <div class="gal gal-2">
      <figure><img src="{asset}assets/img/huasen/unit-10kw.jpg" alt="10 kW distributed reforming fuel cell unit"><figcaption><b>{L(lang,'10 kW distributed unit','Unit teragih 10 kW','10 kW 分布式供能装置')}</b><span>{L(lang,'About 1800 × 600 × 1400 mm. 1 m³ of gas gives 5 kWh, plus 60–90 °C hot water.','Kira-kira 1800 × 600 × 1400 mm. 1 m³ gas memberi 5 kWh, serta air panas 60–90 °C.','约 1800 × 600 × 1400 mm。1 m³ 气发 5 kWh，并产 60–90 °C 热水。')}</span></figcaption></figure>
      <figure><img src="{asset}assets/img/huasen/unit-compact.jpg" alt="5 to 10 kW compact all-in-one CHP unit"><figcaption><b>{L(lang,'5–10 kW compact unit','Unit padat 5–10 kW','5–10 kW 一体机')}</b><span>{L(lang,'For a single house or shop; quiet enough to install beside the wall.','Untuk satu rumah atau kedai; cukup senyap untuk dipasang di tepi dinding.','单栋住宅或店铺用，静到可以贴美边墙安装。')}</span></figcaption></figure>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow">{L(lang,'How it works','Cara ia berfungsi','工作原理')}</p>
      <h2>{L(lang,'From methane to electrons, without a flame','Dari metana ke elektron, tanpa api','从甲烷到电子，不靠火焰')}</h2>
      <p class="lead">{L(lang,
        'Three drawings: the system composition, the fuel-cell reaction itself, and a household P&ID showing where the power and the heat actually go.',
        'Tiga lukisan: komposisi sistem, tindak balas sel bahan api itu sendiri, dan P&ID rumah yang menunjukkan ke mana kuasa dan haba pergi.',
        '三张图：系统组成、燃料电池反应本身、以及家庭热电联供 PI 图——看清楚电和热到底去了哪里。')}</p>
    </div>
    <div class="gal gal-3">
      <figure class="diag"><img src="{asset}assets/img/huasen/principle-system.png" alt="Fuel cell system composition"><figcaption><b>{L(lang,'System composition','Komposisi sistem','系统组成')}</b><span>{L(lang,'Gas in, hydrogen at the stack, DC to an inverter, AC out — heat recovered from the stack.','Gas masuk, hidrogen di stack, DC ke inverter, AC keluar — haba dipulihkan dari stack.','气进、堆端制氢、直流过逆变器出交流，堆端余热回收。')}</span></figcaption></figure>
      <figure class="diag"><img src="{asset}assets/img/huasen/principle-fuelcell.png" alt="Fuel cell principle: hydrogen and oxygen to electricity and pure water"><figcaption><b>{L(lang,'Fuel-cell principle','Prinsip sel bahan api','燃料电池原理')}</b><span>{L(lang,'Hydrogen and oxygen react electrochemically; the only product is pure water.','Hidrogen dan oksigen bertindak balas secara elektrokimia; satu-satunya produk ialah air tulen.','氢与氧电化学反应，生成物只有纯水。')}</span></figcaption></figure>
      <figure class="diag"><img src="{asset}assets/img/huasen/diagram-household-pi.png" alt="Household CHP P and ID"><figcaption><b>{L(lang,'Household CHP P&amp;ID','P&amp;ID CHP rumah','家庭热电联供 PI 图')}</b><span>{L(lang,'Power to lighting, fridge, air conditioning, TV and a backup circuit; heat to hot water.','Kuasa ke lampu, peti sejuk, penghawa dingin, TV dan litar sandaran; haba ke air panas.','电供照明、冰箱、空调、电视与备用回路；热供热水。')}</span></figcaption></figure>
    </div>
    <p class="small" style="margin-top:16px">{L(lang,
      'Photos and drawings: Huasen Hydrogen (Anhui) company brochure V1.4. High-resolution originals to be supplied for print use.',
      'Foto dan lukisan: risalah syarikat Huasen Hydrogen (Anhui) V1.4. Imej asal beresolusi tinggi akan dibekalkan untuk kegunaan cetak.',
      '照片与图纸来源：安徽华森氢能公司样册 V1.4。印刷用高清原图待补。')}</p>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow">{L(lang,'Engineering tools','Alat kejuruteraan','工程测算')}</p>
      <h2>{L(lang,'Three calculators — same formulas we quote from','Tiga kalkulator — formula yang sama kami gunakan','三个计算器，与报价同口径')}</h2>
      <p class="lead">{L(lang,
        'Sizing, model selection and project economics. Every assumption is editable; the formulas are the ones used in our pre-feasibility work.',
        'Saiz, pemilihan model dan ekonomi projek. Setiap andaian boleh diubah; formulanya sama seperti kerja pra-kelayakan kami.',
        '选型、机型匹配、项目经济性。所有假设可改，公式与我们的预可研一致。')}</p>
    </div>

    <div class="calc">
      <div class="calc-form">
        <h3 style="margin-top:0">{L(lang,'A · Size and fuel demand','A · Saiz dan keperluan bahan api','A · 容量与燃料需求')}</h3>
        <div class="field"><label for="h1_kw">{L(lang,'Electrical output required (kW)','Output elektrik diperlukan (kW)','目标发电功率（kW）')}</label><input id="h1_kw" type="number" value="50" step="2.5" min="0"></div>
        <div class="field"><label for="h1_eff">{L(lang,'Electrical efficiency (% LHV)','Kecekapan elektrik (% LHV)','发电效率（% 低热值）')}</label><input id="h1_eff" type="number" value="42" step="0.5" min="25" max="60"><div class="hint">{L(lang,'40–45% for reformer + PEM/PAFC at this scale; 50%+ only for large SOFC.','40–45% untuk reformer + PEM/PAFC pada skala ini; 50%+ hanya SOFC besar.','这个功率段重整+燃料电池 40–45%；50% 以上只有大型 SOFC 才谈得上。')}</div></div>
        <div class="field"><label for="h1_heat">{L(lang,'Recoverable heat (% LHV)','Haba boleh pulih (% LHV)','可回收余热（% 低热值）')}</label><input id="h1_heat" type="number" value="43" step="1" min="0" max="60"></div>
        <div class="field"><label for="h1_load">{L(lang,'Average load (%)','Beban purata (%)','平均负荷（%）')}</label><input id="h1_load" type="number" value="85" step="1" min="20" max="100"></div>
        <div class="field"><label for="h1_hours">{L(lang,'Operating hours per year','Jam operasi setahun','年运行小时')}</label><input id="h1_hours" type="number" value="8000" step="100" min="0" max="8760"></div>
      </div>
      <div class="calc-out">
        <h3>{L(lang,'Fuel and output','Bahan api dan output','燃料与产出')}</h3>
        <div class="out-grid">
          <div class="kv hl"><span>{L(lang,'Fuel energy input','Tenaga bahan api masuk','燃料输入能量')}</span><b id="h1_fuel">—</b></div>
          <div class="kv hl"><span>{L(lang,'Methane at full load','Metana beban penuh','满负荷甲烷')}</span><b id="h1_ch4">—</b></div>
          <div class="kv"><span>{L(lang,'Methane per day','Metana sehari','日耗甲烷')}</span><b id="h1_day">—</b></div>
          <div class="kv"><span>{L(lang,'Methane per year','Metana setahun','年耗甲烷')}</span><b id="h1_year">—</b></div>
          <div class="kv"><span>{L(lang,'Cylinders per day (10 Nm³)','Silinder sehari (10 Nm³)','日耗钢瓶（10 Nm³）')}</span><b id="h1_cyl">—</b></div>
          <div class="kv"><span>{L(lang,'Heat output','Output haba','余热功率')}</span><b id="h1_heatkw">—</b></div>
          <div class="kv"><span>{L(lang,'Hot water at 50 K rise','Air panas kenaikan 50 K','热水（温升 50 K）')}</span><b id="h1_hot">—</b></div>
          <div class="kv"><span>{L(lang,'Annual generation','Penjanaan tahunan','年发电量')}</span><b id="h1_gen">—</b></div>
          <div class="kv"><span>{L(lang,'Annual heat','Haba tahunan','年供热量')}</span><b id="h1_heatyr">—</b></div>
          <div class="kv"><span>{L(lang,'Combined efficiency','Kecekapan gabungan','综合效率')}</span><b id="h1_total">—</b></div>
        </div>
        <div class="warn" id="h1_warn"></div>
      </div>
    </div>

    <div class="calc" style="margin-top:26px">
      <div class="calc-form">
        <h3 style="margin-top:0">{L(lang,'B · Match the model to the load','B · Padankan model dengan beban','B · 机型与负荷匹配')}</h3>
        <div class="field"><label for="h2_need">{L(lang,'Load to carry (kW)','Beban untuk ditanggung (kW)','需要承担的负荷（kW）')}</label><input id="h2_need" type="number" value="35" step="1" min="0"></div>
        <div class="field"><label for="h2_ch4">{L(lang,'Biomethane available (Nm³/h)','Biometana tersedia (Nm³/j)','可用生物天然气（Nm³/h）')}</label><input id="h2_ch4" type="number" value="10" step="0.5" min="0"><div class="hint">{L(lang,'Set 0 if you only want the model for a load.','Tetapkan 0 jika hanya mahu model untuk beban.','只看负荷选型可填 0。')}</div></div>
        <div class="field"><label for="h2_load">{L(lang,'Expected average load (%)','Beban purata dijangka (%)','预计平均负荷（%）')}</label><input id="h2_load" type="number" value="85" step="1" min="20" max="100"></div>
      </div>
      <div class="calc-out">
        <h3>{L(lang,'Recommended unit','Unit disyorkan','推荐机型')}</h3>
        <div class="out-grid">
          <div class="kv hl"><span>{L(lang,'Model','Model','机型')}</span><b id="h2_model">—</b></div>
          <div class="kv hl"><span>{L(lang,'Indicative price','Harga indikatif','参考价')}</span><b id="h2_price">—</b></div>
          <div class="kv"><span>{L(lang,'Electrical output','Output elektrik','发电功率')}</span><b id="h2_kw">—</b></div>
          <div class="kv"><span>{L(lang,'Methane needed','Metana diperlukan','需甲烷')}</span><b id="h2_needgas">—</b></div>
          <div class="kv"><span>{L(lang,'Fuel coverage','Liputan bahan api','气量覆盖')}</span><b id="h2_cover">—</b></div>
          <div class="kv"><span>{L(lang,'Heat output','Output haba','余热功率')}</span><b id="h2_heat">—</b></div>
          <div class="kv"><span>{L(lang,'Annual generation','Penjanaan tahunan','年发电量')}</span><b id="h2_gen">—</b></div>
        </div>
        <div class="warn" id="h2_warn"></div>
      </div>
    </div>

    <div class="calc" style="margin-top:26px">
      <div class="calc-form">
        <h3 style="margin-top:0">{L(lang,'C · Project economics','C · Ekonomi projek','C · 项目经济性')}</h3>
        <div class="field"><label for="h3_kw">{L(lang,'Unit size (kW)','Saiz unit (kW)','机组功率（kW）')}</label><input id="h3_kw" type="number" value="50" step="2.5" min="0"></div>
        <div class="field"><label for="h3_capex">{L(lang,'Price (RM per kW)','Harga (RM per kW)','单价（马币/kW）')}</label><input id="h3_capex" type="number" value="10000" step="500" min="0"><div class="hint">{L(lang,'RM 10,000 for bottled 97% gas; RM 19,500 for raw 60% biogas with integrated purification.','RM 10,000 untuk gas botol 97%; RM 19,500 untuk biogas mentah 60% dengan penulenan bersepadu.','瓶装 97% 气用 10,000；60% 原沼气带一体化净化用 19,500。')}</div></div>
        <div class="field"><label for="h3_om">{L(lang,'O&amp;M (% of capex per year)','O&amp;M (% capex setahun)','运维（占投资 %/年）')}</label><input id="h3_om" type="number" value="3" step="0.5" min="0" max="12"><div class="hint">{L(lang,'Service contract plus stack provision. Stack replacement is the big item — 25–35% of unit price every 5–8 years.','Kontrak servis serta peruntukan stack. Penggantian stack ialah item besar — 25–35% harga unit setiap 5–8 tahun.','含服务合同与电堆计提。电堆更换是大项：每 5–8 年约机组价的 25–35%。')}</div></div>
        <div class="field"><label for="h3_gas">{L(lang,'Biomethane price (RM/Nm³)','Harga biometana (RM/Nm³)','生物天然气价（马币/Nm³）')}</label><input id="h3_gas" type="number" value="1.20" step="0.05" min="0"></div>
        <div class="field"><label for="h3_tariff">{L(lang,'Avoided electricity cost (RM/kWh)','Kos elektrik dielakkan (RM/kWh)','替代电价（马币/kWh）')}</label><input id="h3_tariff" type="number" value="0.45" step="0.05" min="0"><div class="hint">{L(lang,'Grid tariff 0.40–0.50; off-grid diesel 0.90–1.30. Use the cost you actually avoid.','Tarif grid 0.40–0.50; diesel luar grid 0.90–1.30. Guna kos yang benar-benar dielakkan.','电网 0.40–0.50；离网柴油 0.90–1.30。填你真实省下的成本。')}</div></div>
        <div class="field"><label for="h3_heat">{L(lang,'Value of heat (RM/kWh)','Nilai haba (RM/kWh)','热价（马币/kWh）')}</label><input id="h3_heat" type="number" value="0.10" step="0.01" min="0"><div class="hint">{L(lang,'Set 0 if there is no year-round hot-water demand.','Tetapkan 0 jika tiada permintaan air panas sepanjang tahun.','没有全年热水负荷就填 0。')}</div></div>
        <div class="field"><label for="h3_load">{L(lang,'Average load (%)','Beban purata (%)','平均负荷（%）')}</label><input id="h3_load" type="number" value="85" step="1" min="20" max="100"></div>
        <div class="field"><label for="h3_hours">{L(lang,'Operating hours per year','Jam operasi setahun','年运行小时')}</label><input id="h3_hours" type="number" value="8000" step="100" min="0" max="8760"></div>
        <div class="field"><label for="h3_life">{L(lang,'Evaluation period (years)','Tempoh penilaian (tahun)','评价期（年）')}</label><input id="h3_life" type="number" value="10" step="1" min="1" max="25"></div>
        <div class="field"><label for="h3_disc">{L(lang,'Discount rate (%)','Kadar diskaun (%)','折现率（%）')}</label><input id="h3_disc" type="number" value="8" step="0.5" min="0" max="30"></div>
      </div>
      <div class="calc-out">
        <h3>{L(lang,'Results (RM)','Keputusan (RM)','结果（马币）')}</h3>
        <div class="out-grid">
          <div class="kv hl"><span>{L(lang,'Total investment','Jumlah pelaburan','总投资')}</span><b id="h3_inv">—</b></div>
          <div class="kv hl"><span>{L(lang,'Net annual benefit','Manfaat tahunan bersih','年净收益')}</span><b id="h3_net">—</b></div>
          <div class="kv hl"><span>{L(lang,'Simple payback','Tempoh pulang mudah','静态回收期')}</span><b id="h3_pb">—</b></div>
          <div class="kv"><span>{L(lang,'Electricity revenue','Hasil elektrik','电费收益')}</span><b id="h3_rev_e">—</b></div>
          <div class="kv"><span>{L(lang,'Heat revenue','Hasil haba','热收益')}</span><b id="h3_rev_h">—</b></div>
          <div class="kv"><span>{L(lang,'Fuel cost','Kos bahan api','燃料成本')}</span><b id="h3_cost_g">—</b></div>
          <div class="kv"><span>{L(lang,'O&amp;M cost','Kos O&amp;M','运维成本')}</span><b id="h3_cost_om">—</b></div>
          <div class="kv"><span>{L(lang,'NPV','NPV','净现值')}</span><b id="h3_npv">—</b></div>
          <div class="kv"><span>{L(lang,'IRR','IRR','内部收益率')}</span><b id="h3_irr">—</b></div>
          <div class="kv"><span>{L(lang,'LCOE','LCOE','平准化度电成本')}</span><b id="h3_lcoe">—</b></div>
          <div class="kv"><span>{L(lang,'CO₂ avoided vs grid','CO₂ dielakkan vs grid','较电网减排')}</span><b id="h3_co2">—</b></div>
        </div>
        <div class="warn" id="h3_warn"></div>
        <p class="note">{L(lang,
          'CO₂ uses 0.60 t/MWh avoided grid emission factor and treats biomethane carbon as short-cycle. At RM 10,000/kW FOB the unit is competitive where power costs RM 0.60/kWh or more, or where the heat replaces LPG or diesel. Against a subsidised grid tariff with bought gas it is still marginal — check the numbers rather than the brochure.',
          'CO₂ menggunakan faktor pelepasan grid 0.60 t/MWh dan menganggap karbon biometana kitaran pendek. Pada RM 10,000/kW FOB unit ini berdaya saing jika kos kuasa RM 0.60/kWh atau lebih, atau jika haba menggantikan LPG atau diesel. Berbanding tarif grid bersubsidi dengan gas dibeli, ia masih marginal.',
          '减排按替代电网 0.60 t/MWh 计，生物天然气碳按短周期处理。RM 10,000/kW FOB 这个价位，在电价 ≥0.60 马币/kWh，或余热替代 LPG/柴油的场合有竞争力；如果对着补贴电价、气还要外购，仍然只是勉强——看数字，别只看宣传册。')}</p>
      </div>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow">{L(lang,'Worked cases','Kes contoh','测算示例')}</p>
      <h2>{L(lang,'One strong case, one marginal','Satu kes kukuh, satu marginal','一个很划算，一个刚刚够')}</h2>
    </div>
    <div class="grid-2">
      <article class="card">
        <p class="tag">{L(lang,'Case A · 10 kW, off-grid housing','Kes A · 10 kW, perumahan luar grid','案例 A · 10 kW，离网宿舍')}</p>
        <h3>{L(lang,'Diesel replacement: about 1.5 years','Ganti diesel: kira-kira 1.5 tahun','替代柴油：约 1.5 年')}</h3>
        <p>{L(lang,
          '12 staff houses, 10 kW average, diesel at RM 1.20/kWh avoided. Investment RM 100,000 FOB plus installation; 68,000 kWh a year at 85% load; fuel 16,300 Nm³ at RM 1.20; O&amp;M RM 3,000. Net about RM 66,000 a year → payback 1.5 years, before any grant.',
          '12 rumah kakitangan, 10 kW purata, diesel RM 1.20/kWh dielakkan. Pelaburan RM 100,000 FOB serta pemasangan; 68,000 kWh setahun pada beban 85%; bahan api 16,300 Nm³ pada RM 1.20; O&amp;M RM 3,000. Bersih kira-kira RM 66,000 setahun → pulang 1.5 tahun.',
          '12 间员工宿舍，平均 10 kW，替代柴油成本 RM 1.20/kWh。设备 FOB RM 10 万，另加安装；85% 负荷年发电 68,000 kWh；耗气 16,300 Nm³（RM 1.20）；运维 RM 3,000。年净约 RM 6.6 万 → 回收 1.5 年（未计补贴）。')}</p>
      </article>
      <article class="card">
        <p class="tag">{L(lang,'Case B · 50 kW, grid-connected','Kes B · 50 kW, sambung grid','案例 B · 50 kW，并网')}</p>
        <h3>{L(lang,'Grid tariff: about seven years','Tarif grid: kira-kira tujuh tahun','电网电价：约 7 年')}</h3>
        <p>{L(lang,
          'Same 50 kW unit against a RM 0.45/kWh grid tariff: RM 500,000 FOB, about RM 75,000 a year net — 6.7 years, inside a 10-year life but only just clearing an 8% hurdle, and only if the 43% heat is genuinely used. Remove the heat revenue and it stops working.',
          'Unit 50 kW yang sama berbanding tarif grid RM 0.45/kWh: RM 500,000 FOB, kira-kira RM 75,000 setahun bersih — 6.7 tahun, dalam hayat 10 tahun tetapi hanya hampir melepasi halangan 8%, dan hanya jika haba 43% benar-benar digunakan.',
          '同样 50 kW 对标 RM 0.45/kWh 电网电价：FOB RM 50 万，年净约 RM 7.5 万——回收 6.7 年，在 10 年寿命内，但只是刚刚跨过 8% 的门槛，而且 43% 的余热必须真的用掉。余热收益一拿掉，这个账就不成立。')}</p>
      </article>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow">{L(lang,'Scope &amp; terms','Skop &amp; terma','范围与条款')}</p>
      <h2>{L(lang,'What the price covers','Apa yang diliputi harga','价格包含什么')}</h2>
    </div>
    <div class="grid-2">
      <div class="table-wrap"><table style="min-width:0"><tbody>
        <tr><td><b>{L(lang,'Included','Termasuk','包含')}</b></td><td>{L(lang,'Reformer, shift reactor, H₂ purification, fuel-cell stack, inverter, heat exchanger, controls, enclosure','Reformer, reaktor anjakan, penulenan H₂, stack sel bahan api, penyongsang, penukar haba, kawalan, selongsong','重整器、变换反应器、氢气提纯、电堆、逆变器、换热器、控制系统、机柜')}</td></tr>
        <tr><td><b>{L(lang,'Optional','Pilihan','选配')}</b></td><td>{L(lang,'Integrated front-end purification for raw biogas feed — desulphurisation, CO₂ removal, drying and compression inside the same package, priced per site','Penulenan bersepadu di hadapan untuk suapan biogas mentah — nyahsulfur, penyingkiran CO₂, pengeringan dan pemampatan dalam pakej yang sama, harga mengikut tapak','原沼气进气用的一体化前端净化——脱硫、脱 CO₂、干燥、增压做进同一机组，按现场单独报价')}</td></tr>
        <tr><td><b>{L(lang,'Excluded','Tidak termasuk','不含')}</b></td><td>{L(lang,'SST, freight beyond Malaysian port, civils, cylinder store and manifold, installation, grid connection, permits','SST, tambang melebihi pelabuhan Malaysia, kerja awam, stor silinder dan manifold, pemasangan, sambungan grid, permit','SST、马来西亚港口以外运费、土建、气瓶间与汇流排、安装、并网、许可')}</td></tr>
        <tr><td><b>{L(lang,'Warranty','Waranti','质保')}</b></td><td>{L(lang,'24 months on the unit, 5 years or 25,000 h on the stack, whichever comes first','24 bulan unit, 5 tahun atau 25,000 j pada stack','整机 24 个月；电堆 5 年或 25,000 小时（先到为准）')}</td></tr>
        <tr><td><b>{L(lang,'Lead time','Masa penghantaran','交货期')}</b></td><td>{L(lang,'4–6 months from PO and gas analysis','4–6 bulan dari PO dan analisis gas','收到订单与气质分析后 4–6 个月')}</td></tr>
        <tr><td><b>{L(lang,'Fuel specification','Spesifikasi bahan api','燃料要求')}</b></td><td>{L(lang,'CH₄ ≥ 95%, H₂S &lt; 1 ppm, siloxanes &lt; 0.1 mg/Nm³, no condensate','CH₄ ≥ 95%, H₂S &lt; 1 ppm, siloksan &lt; 0.1 mg/Nm³, tiada kondensat','甲烷 ≥95%，H₂S <1 ppm，硅氧烷 <0.1 mg/Nm³，无冷凝水')}</td></tr>
        <tr><td><b>{L(lang,'Price basis','Asas harga','价格口径')}</b></td><td>{L(lang,'Bottled-gas version: FOB RM 10,000/kW, installation excluded, valid 90 days, minimum 10 units per export order (units of 30 kW and above, or orders worth RM 300,000 and above, are exempt). Orders below 10 units are quoted at RM 12,500/kW plus a one-off RM 60,000 export engineering and logistics charge. Raw-biogas version with the integrated purification front end: quoted per site. Both subject to gas analysis and site survey.','Versi gas botol: FOB RM 10,000/kW, pemasangan tidak termasuk, sah 90 hari, minimum 10 unit setiap pesanan eksport (unit 30 kW ke atas, atau pesanan bernilai RM 300,000 ke atas, dikecualikan). Pesanan kurang 10 unit disebut pada RM 12,500/kW serta caj kejuruteraan dan logistik eksport RM 60,000 sekali. Versi biogas mentah dengan penulenan bersepadu: disebut harga mengikut tapak. Kedua-duanya tertakluk kepada analisis gas dan tinjauan tapak.','瓶装气版：FOB 价 RM 10,000/kW，不含安装，有效期 90 天，出口起订量 10 台/单（单机 ≥30 kW 或订单 ≥RM 30 万豁免）；不足 10 台按 RM 12,500/kW 并加收一次性 RM 60,000 出口工程与物流费用；带前端净化的一体化原沼气版：按现场单独报价。两者均以气质分析与现场勘查为准。')}</td></tr>
      </tbody></table></div>
      <div>
        <div class="table-wrap"><table style="min-width:0">
          <thead><tr><th>{L(lang,'Option','Pilihan','方案')}</th><th>{L(lang,'Power','Kuasa','电力')}</th><th>{L(lang,'Heat','Haba','余热')}</th><th>{L(lang,'Noise','Bunyi','噪音')}</th><th>{L(lang,'RM/kW','RM/kW','马币/kW')}</th></tr></thead>
          <tbody>
            <tr><td>{L(lang,'Diesel genset','Genset diesel','柴油机组')}</td><td class="num">—</td><td class="num">{L(lang,'none','tiada','无')}</td><td class="num">{L(lang,'high','tinggi','高')}</td><td class="num">800–1,500</td></tr>
            <tr><td>{L(lang,'Gas engine CHP','CHP enjin gas','燃气机热电联供')}</td><td class="num">35%</td><td class="num">43%</td><td class="num">{L(lang,'medium','sederhana','中')}</td><td class="num">1,800–2,600*</td></tr>
            <tr><td><b>{L(lang,'H₂ fuel-cell CHP','CHP sel bahan api H₂','氢燃料电池热电联供')}</b></td><td class="num"><b>42%</b></td><td class="num"><b>43%</b></td><td class="num">{L(lang,'low','rendah','低')}</td><td class="num"><b>10,000 / 19,500</b></td></tr>
            <tr><td><b>NOx · SOx · {L(lang,'dust','habuk','粉尘')}</b></td><td class="num">{L(lang,'high','tinggi','高')}</td><td class="num">{L(lang,'low','rendah','低')}</td><td class="num"><b>{L(lang,'none','tiada','无')}</b></td><td class="num">{L(lang,'none','tiada','无')}</td></tr>
            <tr><td>{L(lang,'Solar + battery','Solar + bateri','光伏 + 储能')}</td><td class="num">—</td><td class="num">{L(lang,'none','tiada','无')}</td><td class="num">{L(lang,'none','tiada','无')}</td><td class="num">3,000–5,000</td></tr>
          </tbody>
        </table></div>
        <p class="small" style="margin-top:12px">{L(lang,
          '* Gas-engine CHP is the 500–1,000 kW class; it has no model below 100 kW. The fuel-cell unit is the only option in this range that gives quiet, flame-free power with usable heat at 7.5 kW upwards.',
          '* CHP enjin gas ialah kelas 500–1,000 kW; tiada model bawah 100 kW. Unit sel bahan api satu-satunya pilihan dalam julat ini.',
          '* 燃气机热电联供是 500–1,000 kW 级，100 kW 以下没有机型。这个功率段要安静、无明火、还能出可用余热的，只有燃料电池这一条路。')}</p>
      </div>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="sec-head"><p class="eyebrow">FAQ</p><h2>{L(lang,'Questions we get asked','Soalan yang sering ditanya','常被问到的问题')}</h2></div>
    <div class="grid-2">
      <article class="card"><h3>{L(lang,'Can it run on raw biogas?','Boleh guna biogas mentah?','能直接烧原沼气吗？')}</h3><p>{L(lang,'Yes — with the integrated purification front end. Raw POME biogas at about 60% methane is desulphurised, stripped of CO₂, dried and compressed inside the same package, then fed to the reformer at ≥95% CH₄. The reformer itself still needs concentrated methane; what changes is that we do the upgrading in the unit instead of you buying bottled gas. Investment is higher than the bottled-gas version and is quoted per site on gas flow, H₂S and CO₂.','Ya — dengan bahagian penulenan bersepadu di hadapan. Biogas POME mentah kira-kira 60% metana dinyahsulfur, disingkirkan CO₂, dikeringkan dan dimampatkan dalam pakej yang sama, kemudian disuap ke reformer pada ≥95% CH₄. Reformer tetap perlukan metana pekat; bezanya kita buat peningkatan dalam unit, bukan anda membeli gas botol. Pelaburan lebih tinggi daripada versi gas botol dan disebut harga mengikut tapak berdasarkan aliran gas, H₂S dan CO₂.','能——但要配前端一体化净化装置。约 60% 甲烷的 POME 原沼气，在同一机组内完成脱硫、脱 CO₂、干燥和增压，再以 ≥95% 甲烷送进重整器。重整器本身仍然要浓甲烷，变的是：提纯在我们机组里做，而不是你去买瓶装气。投资比瓶装气版本高，具体按气量、硫化氢和二氧化碳逐点报价。')}</p></article>
      <article class="card"><h3>{L(lang,'Is hydrogen stored on site?','Adakah hidrogen disimpan?','现场储氢吗？')}</h3><p>{L(lang,'No. Hydrogen is produced on demand and consumed inside the unit within seconds. There is no hydrogen vessel, no high-pressure storage and no delivery of hydrogen.','Tidak. Hidrogen dihasilkan atas permintaan dan digunakan dalam unit.','不储。氢气按需产生、机内秒级用完，没有储氢罐、没有高压储氢、也不需要外购氢。')}</p></article>
      <article class="card"><h3>{L(lang,'What maintenance does it need?','Penyelenggaraan apa?','维护要做什么？')}</h3><p>{L(lang,'Annual service, reformer catalyst every 3–5 years, fuel-cell stack every 5–8 years (25–35% of unit price). Budget 3% of capex a year and you will not be surprised.','Servis tahunan, pemangkin reformer setiap 3–5 tahun, stack setiap 5–8 tahun (25–35% harga unit). Belanjawan 3% capex setahun.','年度保养；重整催化剂 3–5 年一换；电堆 5–8 年一换（机组价 25–35%）。按投资 3%/年计提就不会被吓到。')}</p></article>
      <article class="card"><h3>{L(lang,'Can several units run together?','Boleh beberapa unit bersama?','能多台并联吗？')}</h3><p>{L(lang,'Yes. Units parallel on the AC side up to 1 MW, and a failed unit only takes its share of the load offline — which is why we prefer 2 × 50 kW to 1 × 100 kW where the budget allows.','Boleh. Unit selari di sebelah AC hingga 1 MW.','可以。交流侧可并机到 1 MW；单台故障只掉它那一份负荷——所以预算允许时我们更愿意 2×50 kW 而不是 1×100 kW。')}</p></article>
    </div>
    <p class="small" style="margin-top:18px">{L(lang,
      'All figures on this page are indicative engineering estimates for pre-feasibility. Formal quotation requires gas analysis, load profile and site survey.',
      'Semua angka adalah anggaran kejuruteraan indikatif untuk pra-kelayakan. Sebut harga rasmi memerlukan analisis gas, profil beban dan tinjauan tapak.',
      '本页所有数据均为预可研阶段的工程估算。正式报价需气质分析、负荷曲线与现场勘查。')}</p>
  </div>
</section>
<script src="{asset}assets/js/hchp.js"></script>
"""
