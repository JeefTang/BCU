# -*- coding: utf-8 -*-
"""Hydrogen CHP page: methane reforming fuel-cell cogeneration, 7.5–100 kW."""
from build3 import L

# ---- locked design basis -------------------------------------------------
KWH_PER_NM3_CH4 = 9.94      # LHV
EFF_E = 42.0                # % electrical, LHV
EFF_H = 43.0                # % recoverable heat, LHV
PRICE_RM_KW = 20000         # indicative budget price to Malaysia, RM/kW
# (kW electrical, fuel input in 0.1 kW, indicative price RM)
MODELS = [
    (7.5, 179, 150000), (10, 238, 200000), (15, 357, 300000), (20, 476, 400000),
    (30, 714, 600000), (50, 1190, 1000000), (75, 1786, 1500000), (100, 2381, 2000000),
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
            "<td class=\"num\">%.1f</td><td class=\"num\">%s</td><td class=\"num\">RM %s</td></tr>"
            % (label, fuel_kw, ch4, heat, "{:,.0f}".format(hot), "{:,.0f}".format(price)))
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
               "Methane reforming plus a fuel cell: the same architecture as Japan's household fuel-cell CHP, scaled to estate housing, resorts, mills and off-grid communities. 97% biomethane is reformed on site into hydrogen and converted to electricity and 60–70 °C hot water — no pipeline, no diesel, no flame at the point of use.",
               "Pembentukan semula metana dengan sel bahan api: seni bina yang sama seperti CHP sel bahan api rumah Jepun, diskalakan untuk perumahan ladang, resort, kilang dan komuniti luar grid. Biometana 97% dibentuk semula di tapak menjadi hidrogen dan ditukar kepada elektrik dan air panas 60–70 °C — tanpa saluran paip, tanpa diesel, tanpa api di tempat penggunaan.",
               "甲烷重整 + 燃料电池：与日本家用燃料电池热电联供同一架构，功率放大到种植园宿舍、度假村、厂区与离网社区。97% 生物天然气现场重整制氢，再转成电与 60–70 ℃ 热水——不用管网、不用柴油、用能端无明火。"),
        k1=L(lang, "Indicative price to Malaysia", "Harga indikatif ke Malaysia", "出口马来西亚参考价"),
        k2=L(lang, "Electrical efficiency (LHV)", "Kecekapan elektrik (LHV)", "发电效率（低热值）"),
        k3=L(lang, "Recoverable heat (LHV)", "Haba boleh pulih (LHV)", "可回收余热（低热值）"),
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
      <div class="stat"><b>RM 20,000</b><span>{s['k1']} · /kW</span></div>
      <div class="stat"><b>42%</b><span>{s['k2']}</span></div>
      <div class="stat"><b>43%</b><span>{s['k3']}</span></div>
      <div class="stat"><b>0.24 Nm³</b><span>{s['k4']}</span></div>
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
      <p class="eyebrow">{L(lang,'Process','Proses','工艺')}</p>
      <h2>{L(lang,'From methane to electrons in five steps','Dari metana ke elektron dalam lima langkah','五步从甲烷到电')}</h2>
    </div>
    <div class="steps" style="grid-template-columns:repeat(5,1fr)">
      <div class="step"><b>{L(lang,'Condition','Kondisi','净化')}</b><span>{L(lang,'Desulphurisation to below 1 ppm H₂S, plus filtration. The reformer catalyst is poisoned by sulphur.','Nyahsulfur di bawah 1 ppm H₂S, serta penapisan. Pemangkin reformer diracuni sulfur.','脱硫到 H₂S 低于 1 ppm，再加过滤。重整催化剂最怕硫。')}</span></div>
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
        'Fuel figures are at rated output, 97% methane, LHV basis. Hot water is at a 50 K rise (20 → 70 °C). Prices are the indicative budget price to Malaysia at RM 20,000 per kW.',
        'Angka bahan api pada output terkadar, 97% metana, asas LHV. Air panas pada kenaikan 50 K (20 → 70 °C). Harga ialah harga bajet indikatif ke Malaysia pada RM 20,000 per kW.',
        '燃料数据为额定出力、97% 甲烷、低热值口径；热水量按温升 50 K（20 → 70 ℃）。价格为出口马来西亚参考预算价，每 kW 2 万马币。')}</p>
    </div>
    <div class="table-wrap">
      <table>
        <thead><tr>
          <th>{L(lang,'Model','Model','机型')}</th>
          <th>{L(lang,'Fuel input (kW)','Input bahan api (kW)','燃料输入（kW）')}</th>
          <th>{L(lang,'CH₄ (Nm³/h)','CH₄ (Nm³/j)','甲烷（Nm³/h）')}</th>
          <th>{L(lang,'Heat (kW)','Haba (kW)','余热（kW）')}</th>
          <th>{L(lang,'Hot water 50 K (L/h)','Air panas 50 K (L/j)','热水 50 K（L/h）')}</th>
          <th>{L(lang,'Indicative price','Harga indikatif','参考价')}</th>
        </tr></thead>
        <tbody>
{rows}
        </tbody>
      </table>
    </div>
    <p class="small" style="margin-top:14px">{L(lang,
      'Basis: methane LHV 9.94 kWh/Nm³; 42% electrical and 43% heat recovery of fuel input; 85% combined. Price excludes SST, local installation, civils, cylinder storage, gas manifold and grid connection — those are quoted per site.',
      'Asas: LHV metana 9.94 kWh/Nm³; 42% elektrik dan 43% pemulihan haba daripada input bahan api; 85% gabungan. Harga tidak termasuk SST, pemasangan tempatan, kerja awam, penyimpanan silinder, manifold gas dan sambungan grid.',
      '口径：甲烷低热值 9.94 kWh/Nm³；发电 42%、余热回收 43%，综合 85%。价格不含 SST、本地安装、土建、气瓶间、汇流排与并网——这些按现场单独报价。')}</p>
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
        <div class="field"><label for="h3_capex">{L(lang,'Price (RM per kW)','Harga (RM per kW)','单价（马币/kW）')}</label><input id="h3_capex" type="number" value="20000" step="500" min="0"></div>
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
          'CO₂ uses 0.60 t/MWh avoided grid emission factor and treats biomethane carbon as short-cycle. At RM 20,000/kW the unit is expensive per kW — it is built for high avoided cost or grant-supported sites, not for displacing a cheap grid tariff.',
          'CO₂ menggunakan faktor pelepasan grid 0.60 t/MWh dan menganggap karbon biometana kitaran pendek. Pada RM 20,000/kW unit ini mahal per kW — ia untuk tapak kos dielakkan tinggi atau bersubsidi.',
          '减排按替代电网 0.60 t/MWh 计，生物天然气碳按短周期处理。RM 20,000/kW 单价不低——它面向高替代成本或有补贴的场景，不是用来替代便宜的电网电价。')}</p>
      </div>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow">{L(lang,'Worked cases','Kes contoh','测算示例')}</p>
      <h2>{L(lang,'One where it pays, one where it does not','Satu yang berbaloi, satu yang tidak','一个划算，一个不划算')}</h2>
    </div>
    <div class="grid-2">
      <article class="card">
        <p class="tag">{L(lang,'Case A · 10 kW, off-grid housing','Kes A · 10 kW, perumahan luar grid','案例 A · 10 kW，离网宿舍')}</p>
        <h3>{L(lang,'Diesel replacement: about 3 years','Ganti diesel: kira-kira 3 tahun','替代柴油：约 3 年')}</h3>
        <p>{L(lang,
          '12 staff houses, 10 kW average, diesel at RM 1.20/kWh avoided. Investment RM 200,000; 68,000 kWh a year at 85% load; fuel 16,300 Nm³ at RM 1.20; O&amp;M RM 6,000. Net about RM 63,000 a year → payback 3.2 years, before any grant.',
          '12 rumah kakitangan, 10 kW purata, diesel RM 1.20/kWh dielakkan. Pelaburan RM 200,000; 68,000 kWh setahun pada beban 85%; bahan api 16,300 Nm³ pada RM 1.20; O&amp;M RM 6,000. Bersih kira-kira RM 63,000 setahun → pulang 3.2 tahun.',
          '12 间员工宿舍，平均 10 kW，替代柴油成本 RM 1.20/kWh。投资 RM 20 万；85% 负荷年发电 68,000 kWh；耗气 16,300 Nm³（RM 1.20）；运维 RM 6,000。年净约 RM 6.3 万 → 回收 3.2 年（未计补贴）。')}</p>
      </article>
      <article class="card">
        <p class="tag">{L(lang,'Case B · 50 kW, grid-connected','Kes B · 50 kW, sambung grid','案例 B · 50 kW，并网')}</p>
        <h3>{L(lang,'Grid tariff: payback beyond the stack life','Tarif grid: pulang melebihi hayat stack','电网电价：回收期超过电堆寿命')}</h3>
        <p>{L(lang,
          'Same unit against a RM 0.45/kWh grid tariff gives about RM 60,000 a year net on RM 1.0 million — 16 years, longer than the 5–8 year stack interval. This is the honest limit of the technology at this price; it needs a heat load with real value, a grant, or a much higher avoided cost.',
          'Unit yang sama berbanding tarif grid RM 0.45/kWh memberi kira-kira RM 60,000 setahun bersih atas RM 1.0 juta — 16 tahun, lebih panjang daripada selang stack 5–8 tahun. Ini had jujur teknologi pada harga ini.',
          '同样一台对标 RM 0.45/kWh 电网电价，投资 RM 100 万、年净约 RM 6 万——回收 16 年，比电堆 5–8 年的更换周期还长。这就是这个价位下的真实边界：要么有真正值钱的热负荷，要么有补贴，要么替代成本足够高。')}</p>
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
        <tr><td><b>{L(lang,'Excluded','Tidak termasuk','不含')}</b></td><td>{L(lang,'SST, freight beyond Malaysian port, civils, cylinder store and manifold, installation, grid connection, permits','SST, tambang melebihi pelabuhan Malaysia, kerja awam, stor silinder dan manifold, pemasangan, sambungan grid, permit','SST、马来西亚港口以外运费、土建、气瓶间与汇流排、安装、并网、许可')}</td></tr>
        <tr><td><b>{L(lang,'Warranty','Waranti','质保')}</b></td><td>{L(lang,'24 months on the unit, 5 years or 25,000 h on the stack, whichever comes first','24 bulan unit, 5 tahun atau 25,000 j pada stack','整机 24 个月；电堆 5 年或 25,000 小时（先到为准）')}</td></tr>
        <tr><td><b>{L(lang,'Lead time','Masa penghantaran','交货期')}</b></td><td>{L(lang,'4–6 months from PO and gas analysis','4–6 bulan dari PO dan analisis gas','收到订单与气质分析后 4–6 个月')}</td></tr>
        <tr><td><b>{L(lang,'Fuel specification','Spesifikasi bahan api','燃料要求')}</b></td><td>{L(lang,'CH₄ ≥ 95%, H₂S &lt; 1 ppm, siloxanes &lt; 0.1 mg/Nm³, no condensate','CH₄ ≥ 95%, H₂S &lt; 1 ppm, siloksan &lt; 0.1 mg/Nm³, tiada kondensat','甲烷 ≥95%，H₂S <1 ppm，硅氧烷 <0.1 mg/Nm³，无冷凝水')}</td></tr>
        <tr><td><b>{L(lang,'Price basis','Asas harga','价格口径')}</b></td><td>{L(lang,'Indicative RM 20,000/kW to Malaysia, valid 90 days, subject to gas analysis and site survey','Indikatif RM 20,000/kW ke Malaysia, sah 90 hari, tertakluk kepada analisis gas dan tinjauan tapak','出口马来西亚参考价 RM 20,000/kW，有效期 90 天，以气质分析与现场勘查为准')}</td></tr>
      </tbody></table></div>
      <div>
        <div class="table-wrap"><table style="min-width:0">
          <thead><tr><th>{L(lang,'Option','Pilihan','方案')}</th><th>{L(lang,'Power','Kuasa','电力')}</th><th>{L(lang,'Heat','Haba','余热')}</th><th>{L(lang,'Noise','Bunyi','噪音')}</th><th>{L(lang,'RM/kW','RM/kW','马币/kW')}</th></tr></thead>
          <tbody>
            <tr><td>{L(lang,'Diesel genset','Genset diesel','柴油机组')}</td><td class="num">—</td><td class="num">{L(lang,'none','tiada','无')}</td><td class="num">{L(lang,'high','tinggi','高')}</td><td class="num">800–1,500</td></tr>
            <tr><td>{L(lang,'Gas engine CHP','CHP enjin gas','燃气机热电联供')}</td><td class="num">35%</td><td class="num">43%</td><td class="num">{L(lang,'medium','sederhana','中')}</td><td class="num">1,800–2,600*</td></tr>
            <tr><td><b>{L(lang,'H₂ fuel-cell CHP','CHP sel bahan api H₂','氢燃料电池热电联供')}</b></td><td class="num"><b>42%</b></td><td class="num"><b>43%</b></td><td class="num">{L(lang,'low','rendah','低')}</td><td class="num"><b>20,000</b></td></tr>
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
      <article class="card"><h3>{L(lang,'Can it run on raw biogas?','Boleh guna biogas mentah?','能直接烧原沼气吗？')}</h3><p>{L(lang,'No. The reformer catalyst needs methane at 95% or better. Raw POME biogas at 55–65% must be upgraded first — which is the same upgrading step that produces the bottled gas.','Tidak. Pemangkin reformer perlukan metana 95% atau lebih. Biogas POME mentah 55–65% mesti ditingkatkan dahulu.','不能。重整催化剂要求甲烷 95% 以上，55–65% 的原沼气必须先提纯——也就是做瓶装气那一步。')}</p></article>
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
