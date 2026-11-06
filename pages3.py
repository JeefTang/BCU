# -*- coding: utf-8 -*-
"""Page bodies for the trilingual KSTS site."""
from build3 import L


def index(lang):
    asset = "../" if lang != "en" else ""
    s = dict(
        badge=L(lang,
                "POME biogas · palm biomass · biomethane · Sabah &amp; Sarawak",
                "Biogas POME · biojisim sawit · biometana · Sabah &amp; Sarawak",
                "POME 沼气 · 棕榈生物质 · 生物天然气 · 沙巴与砂拉越"),
        h1=L(lang,
             "Palm oil mill waste, turned into firm 24/7 power.",
             "Sisa kilang kelapa sawit, menjadi kuasa 24 jam.",
             "把棕榈油厂的废料，变成 24 小时稳定电力。"),
        lead=L(lang,
               "KSTS designs, builds and supports biogas power plants and biomethane upgrading systems for palm oil mills across Sabah and Sarawak — with technology from SINOPEC Dalian Research Institute of Petroleum and Petrochemicals, and engineers from a Tsinghua University PhD team.",
               "KSTS merekabentuk, membina dan menyokong loji kuasa biogas serta sistem peningkatan biometana untuk kilang kelapa sawit di Sabah dan Sarawak — dengan teknologi daripada Institut Penyelidikan Petroleum dan Petrokimia Dalian SINOPEC, dan jurutera daripada pasukan PhD Universiti Tsinghua.",
               "KSTS 为沙巴与砂拉越的棕榈油厂设计、建设并运维沼气发电站与生物天然气提纯系统，技术伙伴为中国石化大连研究院，技术工程师来自清华大学博士团队。"),
        b1=L(lang, "Size your plant in 30 seconds", "Kira kapasiti loji dalam 30 saat", "30 秒算出你的电站规模"),
        b2=L(lang, "Send your mill data", "Hantar data kilang", "提交油厂数据"),
        s1=L(lang, "Nm³/h biogas for a 600 kW set at 60% CH₄", "Nm³/j biogas untuk set 600 kW pada 60% CH₄", "600 kW 机组所需沼气量（60% 甲烷）"),
        s2=L(lang, "Electrical efficiency, gas engine", "Kecekapan elektrik enjin gas", "燃气机发电效率"),
        s3=L(lang, "CH₄ biomethane for boilers and bio-CNG", "CH₄ biometana untuk dandang dan bio-CNG", "锅炉与 Bio-CNG 所需甲烷纯度"),
        s4=L(lang, "Design operating hours per year", "Jam operasi reka bentuk setahun", "年设计运行小时"),
    )
    return f"""
<section class="press-top" style="padding:22px 0 6px">
  <div class="wrap">
    <figure style="margin:0">
      <img src="{asset}assets/img/press-iem-sabah-cpd-2026-zh.jpg" alt="Chinese-language press report on the IEM Sabah Branch CPD talk on palm oil mill biomass, Asia Times Sabah edition, 23 August 2026" loading="eager" style="width:100%;max-width:900px;margin:0 auto;border:1px solid var(--line);border-radius:12px;box-shadow:0 10px 30px rgba(12,26,38,.10)">
      <figcaption class="small" style="max-width:900px;margin:10px auto 0;text-align:center">{L(lang,
        'In the news — Asia Times (Sabah edition), 23 August 2026: palm oil mill waste turned into green energy.',
        'Dalam berita — Asia Times (edisi Sabah), 23 Ogos 2026: sisa kilang kelapa sawit menjadi tenaga hijau.',
        '媒体报道：《亚洲时报》沙巴新闻 A10 版，2026 年 8 月 23 日——《棕油废料变绿能》。')}</figcaption>
    </figure>
  </div>
</section>

<section class="hero">
  <div class="wrap">
    <div class="badge"><i></i> {s['badge']}</div>
    <h1>{s['h1']}</h1>
    <p class="lead">{s['lead']}</p>
    <div class="hero-actions">
      <a class="btn" href="calculator.html">{s['b1']}</a>
      <a class="btn ghost" style="color:#fff;border-color:rgba(255,255,255,.35)" href="contact.html">{s['b2']}</a>
    </div>
    <div class="stats">
      <div class="stat"><b>270–300</b><span>{s['s1']}</span></div>
      <div class="stat"><b>38–42%</b><span>{s['s2']}</span></div>
      <div class="stat"><b>≥97%</b><span>{s['s3']}</span></div>
      <div class="stat"><b>8,000 h</b><span>{s['s4']}</span></div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow">{L(lang,'What we deliver','Apa yang kami berikan','我们交付什么')}</p>
      <h2>{L(lang,'One contract, from pond cover to grid-tie','Satu kontrak, dari penutup kolam hingga sambungan grid','一份合同，从池塘覆盖到并网')}</h2>
      <p class="lead">{L(lang,
        'Most mills already have the raw material and the pond. What is missing is gas quality control, the engine package and one party accountable for the whole chain.',
        'Kebanyakan kilang sudah mempunyai bahan mentah dan kolam. Yang kurang ialah kawalan kualiti gas, pakej enjin dan satu pihak yang bertanggungjawab atas seluruh rantaian.',
        '大多数油厂已有原料和池塘，缺的是气体质量控制、机组成套，以及一个对全链条负责的人。')}</p>
    </div>
    <div class="grid-3">
      <article class="card prod-card"><div>
        <p class="tag">01 · {L(lang,'Process','Proses','工艺')}</p>
        <h3>{L(lang,'Biogas capture &amp; treatment','Penangkapan &amp; rawatan biogas','沼气收集与净化')}</h3>
        <p>{L(lang,
          'Covered lagoon or CSTR, condensate management, biological plus iron-oxide desulfurisation, chilling, drying, blower and flare — sized to the engine specification.',
          'Kolam bertutup atau CSTR, pengurusan kondensat, penyahsulfuran biologi dan oksida besi, penyejukan, pengeringan, blower dan flare — mengikut spesifikasi enjin.',
          '覆盖式厌氧塘或 CSTR、冷凝水管理、生物法加氧化铁脱硫、降温干燥、风机与火炬——按机组进气规范设计。')}</p>
      </div></article>
      <article class="card prod-card"><div>
        <p class="tag">02 · {L(lang,'Equipment','Peralatan','设备')}</p>
        <h3>{L(lang,'Gas engines 300 kW – 2 MW','Enjin gas 300 kW – 2 MW','燃气发电机组 300 kW – 2 MW')}</h3>
        <p>{L(lang,
          'Containerised or skid-mounted biogas gensets, 415 V / 50 Hz, island or parallel operation, with jacket-water and exhaust heat recovery.',
          'Genset biogas dalam kontena atau skid, 415 V / 50 Hz, mod pulau atau selari, dengan pemulihan haba air jaket dan ekzos.',
          '集装箱式或撬装沼气机组，415V/50Hz，孤岛或并网运行，带缸套水与烟气余热回收。')}</p>
      </div></article>
      <article class="card prod-card"><div>
        <p class="tag">03 · {L(lang,'Delivery','Pelaksanaan','交付')}</p>
        <h3>{L(lang,'EPC, BOO or equipment only','EPC, BOO atau peralatan sahaja','EPC、BOO 或仅设备供应')}</h3>
        <p>{L(lang,
          'Straight equipment supply, full EPC with local civil and mechanical works, or build-own-operate where we fund the plant and sell power or gas to the mill.',
          'Bekalan peralatan, EPC penuh dengan kerja awam dan mekanikal tempatan, atau bina-miliki-kendali di mana kami membiayai loji dan menjual kuasa atau gas kepada kilang.',
          '纯设备供货、含本地土建机装的 EPC 总包，或我方投资建站的 BOO——按折扣价向油厂售电或售气。')}</p>
      </div></article>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow">{L(lang,'Two ways to monetise the gas','Dua cara menjana nilai daripada gas','两条变现路径')}</p>
      <h2>{L(lang,'Electricity now, biomethane when the boiler matters more','Elektrik dahulu, biometana bila dandang lebih penting','先发电，锅炉更重要时改做生物天然气')}</h2>
    </div>
    <div class="grid-2">
      <article class="card">
        <p class="tag">{L(lang,'Route A · Power &amp; heat','Laluan A · Kuasa &amp; haba','路线 A · 电与热')}</p>
        <h3>{L(lang,'Displace diesel and grid import','Ganti diesel dan import grid','替代柴油与市电')}</h3>
        <p>{L(lang,
          'Inland Sabah mills often run diesel gensets at RM 0.55–0.75/kWh. POME biogas at 60% CH₄ can carry a large share of that load, with useful heat as a by-product.',
          'Kilang di pedalaman Sabah sering menggunakan genset diesel pada RM 0.55–0.75/kWh. Biogas POME pada 60% CH₄ boleh menampung sebahagian besar beban itu, dengan haba berguna sebagai hasil sampingan.',
          '沙巴内陆油厂多用柴油机组，电价 RM 0.55–0.75/kWh。60% 甲烷的 POME 沼气可承担大部分负荷，余热还能回收利用。')}</p>
        <a class="more" href="biogas-to-power.html" style="color:var(--accent);font-weight:700">{L(lang,'Biogas to power →','Biogas ke kuasa →','沼气发电 →')}</a>
      </article>
      <article class="card">
        <p class="tag">{L(lang,'Route B · Biomethane','Laluan B · Biometana','路线 B · 生物天然气')}</p>
        <h3>{L(lang,'Boiler fuel and bio-CNG','Bahan api dandang dan bio-CNG','锅炉燃料与 Bio-CNG')}</h3>
        <p>{L(lang,
          'Where the mill needs boiler fuel more than electricity, biogas can be upgraded to ≥97% CH₄ for the existing burner, or compressed as bio-CNG and moved by trailer.',
          'Jika kilang lebih memerlukan bahan api dandang, biogas boleh ditingkatkan kepada ≥97% CH₄ untuk pembakar sedia ada, atau dimampatkan sebagai bio-CNG dan dihantar dengan treler.',
          '若油厂更需要锅炉燃料，可提纯至 ≥97% 甲烷直接供现有燃烧器，或压缩成 Bio-CNG 用槽车外运。')}</p>
        <a class="more" href="biomethane.html" style="color:var(--accent);font-weight:700">{L(lang,'Biomethane &amp; bio-CNG →','Biometana &amp; bio-CNG →','生物天然气 / Bio-CNG →')}</a>
      </article>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow">{L(lang,'Typical design basis','Asas reka bentuk biasa','典型设计基础数据')}</p>
      <h2>{L(lang,'What a mill actually gives us','Apa yang kilang sebenarnya berikan','油厂实际能提供什么')}</h2>
      <p class="lead">{L(lang,
        'These are the ranges we use for pre-feasibility. Every project is re-based on one to two weeks of measured gas flow and composition.',
        'Ini julat yang kami gunakan untuk pra-kelayakan. Setiap projek dinilai semula berdasarkan satu hingga dua minggu data aliran dan komposisi gas sebenar.',
        '以下是我们做预可研的取值区间。每个项目都要用 1–2 周实测气量与气质重新校核。')}</p>
    </div>
    <div class="table-wrap">
      <table>
        <thead><tr>
          <th>{L(lang,'Parameter','Parameter','参数')}</th>
          <th>{L(lang,'Typical range','Julat biasa','典型范围')}</th>
          <th>{L(lang,'Why it matters','Mengapa penting','为什么重要')}</th>
        </tr></thead>
        <tbody>
          <tr><td>{L(lang,'POME generation','Penjanaan POME','POME 产生量')}</td><td class="num">0.6 – 0.7 m³ / t FFB</td><td>{L(lang,'Sets the pond and digester volume','Menentukan isipadu kolam dan pencerna','决定池塘与厌氧罐容积')}</td></tr>
          <tr><td>{L(lang,'POME COD','COD POME','POME 的 COD')}</td><td class="num">50 – 80 g/L</td><td>{L(lang,'Methane potential per m³','Potensi metana per m³','决定每立方米产甲烷潜力')}</td></tr>
          <tr><td>{L(lang,'Biogas yield (covered lagoon)','Hasil biogas (kolam bertutup)','沼气产率（覆盖塘）')}</td><td class="num">20 – 28 Nm³ / m³ POME</td><td>{L(lang,'The most uncertain number — we verify it','Angka paling tidak pasti — kami sahkan','最不确定的一项，必须实测')}</td></tr>
          <tr><td>{L(lang,'Methane content','Kandungan metana','甲烷含量')}</td><td class="num">55 – 65% CH₄</td><td>{L(lang,'Drives gas flow per kWh','Menentukan aliran gas per kWh','决定每度电耗气量')}</td></tr>
          <tr><td>{L(lang,'Hydrogen sulphide','Hidrogen sulfida','硫化氢')}</td><td class="num">1,000 – 4,000 ppm H₂S</td><td>{L(lang,'Decides desulfurisation duty','Menentukan beban penyahsulfuran','决定脱硫负荷')}</td></tr>
          <tr><td>{L(lang,'Operating hours','Jam operasi','年运行小时')}</td><td class="num">7,000 – 8,000 h/year</td><td>{L(lang,'Revenue and maintenance reserve','Hasil dan rizab penyelenggaraan','决定收益与检修准备金')}</td></tr>
        </tbody>
      </table>
    </div>
    <p class="small" style="margin-top:14px">{L(lang,
      'KSTS project experience and published Malaysian POME data. Pre-feasibility only — not a performance guarantee.',
      'Pengalaman projek KSTS dan data POME Malaysia yang diterbitkan. Untuk pra-kelayakan sahaja — bukan jaminan prestasi.',
      '来源：KSTS 项目经验与马来西亚公开的 POME 数据。仅作预可研，不构成性能保证。')}</p>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow">{L(lang,'Engineering tools','Alat kejuruteraan','工程测算工具')}</p>
      <h2>{L(lang,'Check the numbers before you talk to a supplier','Semak angka sebelum berjumpa pembekal','和供应商谈之前，先自己算一遍')}</h2>
      <p class="lead">{L(lang,
        'Five calculators built on the formulas we use in proposals. No sign-up, no email capture.',
        'Lima kalkulator berdasarkan formula yang kami gunakan dalam cadangan. Tanpa pendaftaran, tanpa tangkapan e-mel.',
        '五个计算器，公式与我们的方案一致。无需注册，不留邮箱。')}</p>
    </div>
    <div class="grid-4">
      <article class="card"><p class="tag">{L(lang,'Tool 01','Alat 01','工具 01')}</p><h3>{L(lang,'Gas to power &amp; heat','Gas ke kuasa &amp; haba','气量 → 电与热')}</h3><p>{L(lang,'Biogas flow in, electrical and thermal output out.','Aliran biogas masuk, output elektrik dan haba keluar.','输入沼气流量，输出电功率与热功率。')}</p><a class="more" href="calculator.html#tool1" style="color:var(--accent);font-weight:700">{L(lang,'Open →','Buka →','打开 →')}</a></article>
      <article class="card"><p class="tag">{L(lang,'Tool 02','Alat 02','工具 02')}</p><h3>{L(lang,'Capacity sizing','Saiz kapasiti','容量选型')}</h3><p>{L(lang,'Target kW in, required gas flow out.','Sasaran kW masuk, keperluan aliran gas keluar.','输入目标功率，反推所需气量。')}</p><a class="more" href="calculator.html#tool2" style="color:var(--accent);font-weight:700">{L(lang,'Open →','Buka →','打开 →')}</a></article>
      <article class="card"><p class="tag">{L(lang,'Tool 03','Alat 03','工具 03')}</p><h3>{L(lang,'Mill to biogas','Kilang ke biogas','压榨量 → 沼气')}</h3><p>{L(lang,'FFB throughput to methane potential.','Kemampuan FFB ke potensi metana.','从 FFB 处理量推算甲烷潜力。')}</p><a class="more" href="calculator.html#tool3" style="color:var(--accent);font-weight:700">{L(lang,'Open →','Buka →','打开 →')}</a></article>
      <article class="card"><p class="tag">{L(lang,'Tool 04','Alat 04','工具 04')}</p><h3>{L(lang,'Upgrading yield','Hasil peningkatan','提纯收率')}</h3><p>{L(lang,'Raw biogas to ≥97% biomethane.','Biogas mentah ke biometana ≥97%.','原沼气提纯到 ≥97% 生物天然气。')}</p><a class="more" href="calculator.html#tool4" style="color:var(--accent);font-weight:700">{L(lang,'Open →','Buka →','打开 →')}</a></article>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow">{L(lang,'Local presence','Kehadiran tempatan','本地落地能力')}</p>
      <h2>{L(lang,'Sabah-based, with the statutory credentials that matter','Berpangkalan di Sabah, dengan kelayakan berkanun','沙巴本地公司，具备关键法定资质')}</h2>
      <p class="lead">{L(lang,
        'A biogas plant needs a DOSH-registered engineer for steam and I.C.E. inspection under FMA 1967, an ECOS-registered energy manager, and a CIDB contractor. KSTS holds all three.',
        'Loji biogas memerlukan jurutera berdaftar DOSH untuk pemeriksaan stim dan I.C.E. di bawah FMA 1967, pengurus tenaga berdaftar ECOS, dan kontraktor CIDB. KSTS memiliki ketiga-tiganya.',
        '沼气站需要 DOSH 注册的蒸汽与内燃机检验工程师（FMA 1967）、ECOS 注册电能管理师，以及 CIDB 注册承包商。KSTS 三者齐备。')}</p>
    </div>
    <div class="grid-2" style="align-items:center">
      <div class="card">
        <p class="tag">{L(lang,'Managing Director','Pengarah Urusan','董事总经理')}</p>
        <h3>Sdr. Leong Kian Sheng (Alvin)</h3>
        <p class="small" style="margin-bottom:14px">B.E.Tech (Mech) · Eng Tech (BEM) · MIEM · AMIMechE · MMOSTA</p>
        <ul class="checks">
          <li>{L(lang,'DOSH Registered 2nd Grade Steam Engineer','Jurutera Stim Gred 2 Berdaftar DOSH','DOSH 注册二级蒸汽工程师')}</li>
          <li>{L(lang,'DOSH Registered 2nd Grade I.C.E. Engineer','Jurutera I.C.E. Gred 2 Berdaftar DOSH','DOSH 注册二级内燃机工程师')}</li>
          <li>{L(lang,'DOSH Certified OSH Coordinator','Penyelaras OSH Bertauliah DOSH','DOSH 认证职业安全健康协调员')}</li>
          <li>{L(lang,'ECOS Registered Electrical Energy Manager','Pengurus Tenaga Elektrik Berdaftar ECOS','ECOS 注册电能管理师')}</li>
          <li>{L(lang,'BEM Registered Engineering Technologist (Manufacturing)','Teknolog Kejuruteraan Berdaftar BEM (Pembuatan)','BEM 注册工程技术师（制造）')}</li>
          <li>{L(lang,'AER Registered ASEAN Engineering Technologist','Teknolog Kejuruteraan ASEAN Berdaftar AER','AER 注册东盟工程技术师')}</li>
          <li>{L(lang,'IEM Corporate Member No. 35532 · AMIMechE · MMOSTA','Ahli Korporat IEM No. 35532 · AMIMechE · MMOSTA','IEM 正式会员 35532 · AMIMechE · MMOSTA')}</li>
          <li>{L(lang,'CIDB Green Card Holder · IRWS Professional Engineer','Pemegang Kad Hijau CIDB · Jurutera Profesional IRWS','CIDB 绿卡 · IRWS 专业工程师')}</li>
          <li>{L(lang,'CIDB Registered Contractor · Bumiputera Sabah','Kontraktor Berdaftar CIDB · Bumiputera Sabah','CIDB 注册承包商 · 沙巴土著企业')}</li>
        </ul>
        <a class="btn ghost sm" href="about.html" style="margin-top:8px">{L(lang,'Full profile','Profil penuh','完整简介')}</a>
      </div>
      <div>
        <h3>{L(lang,'What that means for a project','Apa maksudnya untuk projek','这对项目意味着什么')}</h3>
        <p>{L(lang,
          'Permitting and statutory inspection are usually the schedule risk, not the engine. Having DOSH and ECOS registrations in-house means the plant is designed to the inspection regime from day one.',
          'Kebenaran dan pemeriksaan berkanun biasanya menjadi risiko jadual, bukan enjin. Pendaftaran DOSH dan ECOS dalaman bermakna loji direkabentuk mengikut rejim pemeriksaan sejak hari pertama.',
          '进度风险通常在审批与法定检验，而不是机组。DOSH 与 ECOS 资质在自家手上，意味着从第一天就按检验要求设计。')}</p>
        <div class="table-wrap" style="margin-top:10px">
          <table style="min-width:0"><tbody>
            <tr><td><b>{L(lang,'Civil &amp; mechanical','Awam &amp; mekanikal','土建与机装')}</b></td><td>{L(lang,'CIDB-registered execution, local labour and plant','Pelaksanaan berdaftar CIDB, buruh dan loji tempatan','CIDB 资质施工，本地人力与机具')}</td></tr>
            <tr><td><b>{L(lang,'Statutory','Berkanun','法定检验')}</b></td><td>{L(lang,'FMA 1967 steam and I.C.E. inspection','Pemeriksaan stim dan I.C.E. FMA 1967','FMA 1967 蒸汽与内燃机检验')}</td></tr>
            <tr><td><b>{L(lang,'Energy case','Kes tenaga','能耗论证')}</b></td><td>{L(lang,'ECOS-registered energy manager reporting','Laporan pengurus tenaga berdaftar ECOS','ECOS 注册管理师出具报告')}</td></tr>
            <tr><td><b>O&amp;M</b></td><td>{L(lang,'Local crew, remote support from the factory','Krew tempatan, sokongan jauh dari kilang','本地班组，工厂远程支持')}</td></tr>
          </tbody></table>
        </div>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="wrap grid-2" style="gap:44px;align-items:center">
    <figure style="margin:0">
      <img src="{asset}assets/img/press-iem-sabah-cpd-2026.jpg" alt="Report on the IEM Sabah Branch CPD talk on palm oil mill biomass presented by Alvin Leong" loading="lazy" style="border:1px solid var(--line);border-radius:12px;box-shadow:0 10px 30px rgba(12,26,38,.10)">
      <figcaption class="small" style="margin-top:12px">{L(lang,
        'Report on the IEM Sabah Branch CPD talk, Kota Kinabalu.',
        'Laporan ceramah CPD IEM Cawangan Sabah, Kota Kinabalu.',
        'IEM 沙巴分会 CPD 讲座报道，亚庇。')}</figcaption>
      <img src="{asset}assets/img/press-iem-sabah-cpd-2026-zh.jpg" alt="Chinese-language report on the IEM Sabah Branch CPD talk, Asia Times Sabah edition, 23 August 2026" loading="lazy" style="margin-top:22px;border:1px solid var(--line);border-radius:12px;box-shadow:0 10px 30px rgba(12,26,38,.10)">
      <figcaption class="small" style="margin-top:12px">{L(lang,
        'Chinese-language report, Asia Times (Sabah edition), 23 August 2026.',
        'Laporan bahasa Cina, Asia Times (edisi Sabah), 23 Ogos 2026.',
        '中文报道：《亚洲时报》沙巴新闻 A10 版，2026 年 8 月 23 日。')}</figcaption>
    </figure>
    <div>
      <p class="eyebrow">{L(lang,'In the news','Dalam berita','媒体报道')}</p>
      <h2>{L(lang,
        'Invited to speak at the Institution of Engineers Malaysia, Sabah Branch',
        'Dijemput berucap di Institution of Engineers Malaysia, Cawangan Sabah',
        '受邀在马来西亚工程师学会沙巴分会主讲')}</h2>
      <p>{L(lang,
        'Alvin Leong presented “Transforming Palm Oil Mill Biomass Wastes” at the IEM Sabah Branch CPD talk in Kota Kinabalu — cogeneration and Bio-CNG from palm kernel shells, palm fibre and POME.',
        'Alvin Leong membentangkan “Transforming Palm Oil Mill Biomass Wastes” pada ceramah CPD IEM Cawangan Sabah di Kota Kinabalu — kogenerasi dan Bio-CNG daripada tempurung isirung sawit, gentian sawit dan POME.',
        'Alvin Leong 在亚庇的 IEM 沙巴分会 CPD 讲座主讲《Transforming Palm Oil Mill Biomass Wastes》——棕仁壳、棕纤维与 POME 的热电联产与 Bio-CNG。')}</p>
      <p>{L(lang,
        'Sabah has 129 active palm oil mills producing an estimated 25.75 million tonnes of biomass a year.',
        'Sabah mempunyai 129 kilang kelapa sawit aktif yang menghasilkan kira-kira 25.75 juta tan biomas setahun.',
        '沙巴现有 129 家运营中的棕榈油厂，每年产生约 2,575 万吨生物质。')}</p>
      <a class="btn ghost sm" href="about.html#press">{L(lang,'Read more','Baca lagi','了解更多')}</a>
    </div>
  </div>
</section>

<section class="tight">
  <div class="wrap">
    <div class="band">
      <div>
        <h2>{L(lang,'Have a mill, a pond and a diesel bill?','Ada kilang, kolam dan bil diesel?','有油厂、有池塘、有柴油账单？')}</h2>
        <p>{L(lang,
          'Send throughput, pond volume and one week of gas data if you have it. We come back with a capacity, a gas specification and a budget.',
          'Hantar kemampuan, isipadu kolam dan data gas seminggu jika ada. Kami balas dengan kapasiti, spesifikasi gas dan bajet.',
          '把处理量、池塘容积和一周气量数据发来，我们给出容量、气质要求与预算。')}</p>
      </div>
      <a class="btn light" href="contact.html">{L(lang,'Request a pre-feasibility','Minta pra-kelayakan','申请预可研')}</a>
    </div>
  </div>
</section>
"""


def power(lang):
    return f"""
<section class="page-head">
  <div class="wrap">
    <p class="eyebrow">{L(lang,'Biogas to power','Biogas ke kuasa','沼气发电')}</p>
    <h1>{L(lang,'From the pond to the busbar','Dari kolam ke busbar','从池塘到母线')}</h1>
    <p class="lead">{L(lang,
      'A POME biogas plant is a chain, not a machine. Gas quality at the engine inlet decides whether you get 8,000 hours or 4,000 hours between overhauls.',
      'Loji biogas POME ialah satu rantaian, bukan satu mesin. Kualiti gas di salur masuk enjin menentukan sama ada anda mendapat 8,000 atau 4,000 jam antara baik pulih.',
      'POME 沼气站是一条链，不是一台机器。机组进气质量决定你两次大修之间是 8000 小时还是 4000 小时。')}</p>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-head"><p class="eyebrow">{L(lang,'Process chain','Rantaian proses','工艺链')}</p>
    <h2>{L(lang,'Six stages, one gas specification','Enam peringkat, satu spesifikasi gas','六个环节，一套气质标准')}</h2></div>
    <div class="steps">
      <div class="step"><b>{L(lang,'Capture','Tangkap','收集')}</b><span>{L(lang,'Covered lagoon or CSTR; cover, condensate traps, collection headers.','Kolam bertutup atau CSTR; penutup, perangkap kondensat, header pengumpulan.','覆盖塘或 CSTR；覆盖膜、冷凝水收集、集气总管。')}</span></div>
      <div class="step"><b>{L(lang,'Buffer','Penampan','缓冲')}</b><span>{L(lang,'Gas holder to absorb mill load swings.','Penyimpan gas untuk menyerap turun naik beban kilang.','储气柜吸收油厂负荷波动。')}</span></div>
      <div class="step"><b>{L(lang,'Desulfurise','Nyahsulfur','脱硫')}</b><span>{L(lang,'Biological scrubber plus iron-oxide polishing.','Scrubber biologi serta penggilap oksida besi.','生物脱硫塔 ＋ 氧化铁精脱。')}</span></div>
      <div class="step"><b>{L(lang,'Condition','Kondisi','净化')}</b><span>{L(lang,'Chilling, coalescing, blower to engine pressure.','Penyejukan, penggabungan, blower ke tekanan enjin.','降温、除水除油，风机送至机组压力。')}</span></div>
      <div class="step"><b>{L(lang,'Generate','Jana','发电')}</b><span>{L(lang,'Gas engine and alternator, island or parallel.','Enjin gas dan penjana, pulau atau selari.','燃气机与发电机，孤岛或并网。')}</span></div>
      <div class="step"><b>{L(lang,'Recover heat','Pulih haba','余热回收')}</b><span>{L(lang,'Jacket water ~90 °C and exhaust to hot water or steam.','Air jaket ~90 °C dan ekzos ke air panas atau stim.','缸套水约 90°C 与烟气，产热水或蒸汽。')}</span></div>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="sec-head"><p class="eyebrow">{L(lang,'Selection','Pemilihan','选型')}</p>
      <h2>{L(lang,'Engine size against available gas','Saiz enjin berbanding gas tersedia','机组容量与可用气量')}</h2>
      <p class="lead">{L(lang,
        'At 60% CH₄ and 38–40% electrical efficiency, one cubic metre of biogas carries about 2.2 kWh of electricity.',
        'Pada 60% CH₄ dan kecekapan elektrik 38–40%, satu meter padu biogas menghasilkan kira-kira 2.2 kWh elektrik.',
        '在 60% 甲烷、38–40% 发电效率下，1 立方米沼气约可发 2.2 度电。')}</p>
    </div>
    <div class="table-wrap">
      <table>
        <thead><tr><th>{L(lang,'Electrical output','Output elektrik','发电功率')}</th><th>{L(lang,'Gas at 60% CH₄','Gas pada 60% CH₄','60% 甲烷所需气量')}</th><th>{L(lang,'Gas at 55% CH₄','Gas pada 55% CH₄','55% 甲烷所需气量')}</th><th>{L(lang,'Recoverable heat','Haba boleh pulih','可回收热量')}</th></tr></thead>
        <tbody>
          <tr><td class="num">300 kW</td><td class="num">132 – 140 Nm³/h</td><td class="num">144 – 153 Nm³/h</td><td class="num">330 – 390 kW</td></tr>
          <tr><td class="num">500 kW</td><td class="num">220 – 234 Nm³/h</td><td class="num">240 – 255 Nm³/h</td><td class="num">550 – 650 kW</td></tr>
          <tr><td class="num">600 kW</td><td class="num">265 – 280 Nm³/h</td><td class="num">289 – 306 Nm³/h</td><td class="num">660 – 780 kW</td></tr>
          <tr><td class="num">800 kW</td><td class="num">353 – 373 Nm³/h</td><td class="num">385 – 407 Nm³/h</td><td class="num">880 – 1,040 kW</td></tr>
          <tr><td class="num">1,000 kW</td><td class="num">441 – 466 Nm³/h</td><td class="num">481 – 509 Nm³/h</td><td class="num">1,100 – 1,300 kW</td></tr>
          <tr><td class="num">1,500 kW</td><td class="num">662 – 699 Nm³/h</td><td class="num">722 – 763 Nm³/h</td><td class="num">1,650 – 1,950 kW</td></tr>
          <tr><td class="num">2,000 kW</td><td class="num">883 – 932 Nm³/h</td><td class="num">963 – 1,017 Nm³/h</td><td class="num">2,200 – 2,600 kW</td></tr>
        </tbody>
      </table>
    </div>
    <p class="small" style="margin-top:14px">{L(lang,
      'Full-load figures. Running below 70% load for long periods causes carbon build-up and shortens the overhaul interval — size down or split into two units.',
      'Angka beban penuh. Beroperasi di bawah 70% beban untuk jangka panjang menyebabkan pengumpulan karbon dan memendekkan selang baik pulih — pilih saiz lebih kecil atau dua unit.',
      '满负荷数据。长期低于 70% 负荷运行会积碳、缩短大修周期——宁可选小一号或拆成两台。')}</p>
  </div>
</section>

<section>
  <div class="wrap grid-2" style="gap:44px;align-items:start">
    <div>
      <p class="eyebrow">{L(lang,'Gas specification','Spesifikasi gas','进气规范')}</p>
      <h2>{L(lang,'What the engine will accept','Apa yang enjin terima','机组能接受什么气')}</h2>
      <p>{L(lang,
        'These limits are the basis of our warranty discussion with the engine supplier. If your gas cannot meet them, the treatment scope changes — we would rather say so before the order.',
        'Had ini menjadi asas perbincangan waranti dengan pembekal enjin. Jika gas anda tidak memenuhi, skop rawatan berubah — lebih baik kami nyatakan sebelum pesanan.',
        '这些限值是我们与机组厂谈质保的基础。如果气质达不到，处理范围就要变——这话最好在订单前说。')}</p>
      <div class="table-wrap"><table style="min-width:0"><tbody>
        <tr><td>{L(lang,'Methane content','Kandungan metana','甲烷含量')}</td><td class="num">≥ 50% (design 55–65%)</td></tr>
        <tr><td>{L(lang,'H₂S at engine inlet','H₂S di salur masuk enjin','机组入口 H₂S')}</td><td class="num">≤ 200 ppm, target ≤ 100</td></tr>
        <tr><td>{L(lang,'Water dew point','Titik embun air','水露点')}</td><td class="num">≤ 10 °C above ambient</td></tr>
        <tr><td>{L(lang,'Gas temperature','Suhu gas','气体温度')}</td><td class="num">≤ 40 °C</td></tr>
        <tr><td>{L(lang,'Inlet pressure','Tekanan masuk','进气压力')}</td><td class="num">5–15 kPa, ±1 kPa</td></tr>
        <tr><td>{L(lang,'Pressure fluctuation','Turun naik tekanan','压力波动')}</td><td class="num">≤ 10% per minute</td></tr>
      </tbody></table></div>
      <div class="callout" style="margin-top:22px"><p><b>{L(lang,'The most common mistake:','Kesilapan paling biasa:','最常见的错误：')}</b> {L(lang,
        'accepting raw POME gas at 2,000–4,000 ppm H₂S. It halves lube-oil life and doubles maintenance cost, invisibly, until the first overhaul.',
        'menerima gas POME mentah pada 2,000–4,000 ppm H₂S. Ia memendekkan hayat minyak pelincir separuh dan menggandakan kos penyelenggaraan, tanpa disedari sehingga baik pulih pertama.',
        '直接接受 2000–4000 ppm 硫化氢的原气。机油寿命腰斩、维护成本翻倍，直到第一次大修才发现。')}</p></div>
    </div>
    <div>
      <p class="eyebrow">{L(lang,'Economics','Ekonomi','经济性')}</p>
      <h2>{L(lang,'What O&amp;M really costs','Kos O&amp;M sebenar','运维到底多少钱')}</h2>
      <p>{L(lang,'600 kW at 8,000 h/year, gas at 60% CH₄ after scrubbing:','600 kW pada 8,000 jam/tahun, gas 60% CH₄ selepas nyahsulfur:','600 kW、年运行 8000 小时、脱硫后 60% 甲烷：')}</p>
      <div class="table-wrap"><table style="min-width:0">
        <thead><tr><th>{L(lang,'Item','Item','项目')}</th><th>RM/kWh</th></tr></thead>
        <tbody>
          <tr><td>{L(lang,'Oil, filters, spark plugs','Minyak, penapis, palam pencucuh','机油、三滤、火花塞')}</td><td class="num">0.014</td></tr>
          <tr><td>{L(lang,'Routine service labour','Buruh servis rutin','日常保养人工')}</td><td class="num">0.012</td></tr>
          <tr><td>{L(lang,'Overhaul reserve','Rizab baik pulih','小修/大修准备金')}</td><td class="num">0.016</td></tr>
          <tr><td>{L(lang,'Desulfurisation media','Media nyahsulfur','脱硫剂')}</td><td class="num">0.005</td></tr>
          <tr><td>{L(lang,'Spares, insurance, misc.','Alat ganti, insurans, lain-lain','备件、保险、杂费')}</td><td class="num">0.008</td></tr>
          <tr><td><b>{L(lang,'Total','Jumlah','合计')}</b></td><td class="num"><b>0.055</b></td></tr>
        </tbody></table></div>
      <p class="small" style="margin-top:12px">{L(lang,
        'Range RM 0.048–0.058/kWh (≈ USD 0.011–0.014/kWh). Full-service O&M incl. overhauls: RM 0.065–0.085/kWh. Excludes pond O&M and upgrading.',
        'Julat RM 0.048–0.058/kWh (≈ USD 0.011–0.014/kWh). Kontrak O&M penuh termasuk baik pulih: RM 0.065–0.085/kWh. Tidak termasuk O&M kolam dan peningkatan gas.',
        '区间 RM 0.048–0.058/kWh（约 USD 0.011–0.014/kWh）。全包运维（含大修）RM 0.065–0.085/kWh。不含池塘运维与提纯段。')}</p>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="sec-head"><p class="eyebrow">{L(lang,'Commercial models','Model komersial','商业模式')}</p><h2>{L(lang,'Three ways to structure the project','Tiga cara menyusun projek','三种项目结构')}</h2></div>
    <div class="grid-3">
      <article class="card"><p class="tag">{L(lang,'Model 1','Model 1','模式 1')}</p><h3>{L(lang,'Equipment supply','Bekalan peralatan','设备供货')}</h3><p>{L(lang,
        'Genset, gas train, panel and heat recovery. Civils and balance of plant by the client or their contractor.',
        'Genset, gas train, panel dan pemulihan haba. Kerja awam oleh pelanggan atau kontraktor mereka.',
        '机组、气路、控制柜与余热回收。土建与配套由客户或其承包商负责。')}</p></article>
      <article class="card"><p class="tag">{L(lang,'Model 2','Model 2','模式 2')}</p><h3>{L(lang,'EPC turnkey','EPC turnkey','EPC 总包')}</h3><p>{L(lang,
        'Single contract from pond cover to grid-tie, with local works under CIDB registration and DOSH-witnessed commissioning.',
        'Satu kontrak dari penutup kolam hingga sambungan grid, kerja tempatan di bawah CIDB dan pentauliahan disaksikan DOSH.',
        '从覆盖塘到并网一份合同，本地施工由 CIDB 资质承接，DOSH 见证调试。')}</p></article>
      <article class="card"><p class="tag">{L(lang,'Model 3','Model 3','模式 3')}</p><h3>{L(lang,'BOO / shared savings','BOO / perkongsian penjimatan','BOO / 合同能源管理')}</h3><p>{L(lang,
        'We fund and own the plant; the mill buys power or gas at a discount to its current cost.',
        'Kami membiayai dan memiliki loji; kilang membeli kuasa atau gas pada harga diskaun berbanding kos semasa.',
        '我方投资建站并持有，油厂按低于现价的折扣购电或购气。')}</p></article>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-head"><p class="eyebrow">{L(lang,'Before we quote','Sebelum sebut harga','报价前')}</p>
      <h2>{L(lang,'Seven pieces of data we need','Tujuh data yang kami perlukan','我们需要七项数据')}</h2></div>
    <div class="grid-2">
      <ul class="checks">
        <li>{L(lang,'FFB throughput t/h and operating days','Kemampuan FFB t/j dan hari operasi','FFB 处理量 t/h 与年运行天数')}</li>
        <li>{L(lang,'POME pond: stages, volume, HRT, covered or not','Kolam POME: peringkat, isipadu, HRT, bertutup atau tidak','POME 池塘：级数、容积、HRT、是否覆盖')}</li>
        <li>{L(lang,'Measured biogas flow and composition','Aliran dan komposisi biogas yang diukur','实测沼气流量与成分')}</li>
      </ul>
      <ul class="checks">
        <li>{L(lang,'Electricity tariff or diesel consumption and price','Tarif elektrik atau penggunaan dan harga diesel','电价，或柴油耗量与单价')}</li>
        <li>{L(lang,'Grid connection status and transformer capacity','Status sambungan grid dan kapasiti transformer','并网条件与变压器容量')}</li>
        <li>{L(lang,'Boiler fuel, steam demand and pressure','Bahan api dandang, keperluan stim dan tekanan','锅炉燃料、蒸汽量与压力')}</li>
        <li>{L(lang,'Load profile: base load, peaks, night shift','Profil beban: beban asas, puncak, syif malam','负荷曲线：基荷、峰值、夜班')}</li>
      </ul>
    </div>
    <div class="band" style="margin-top:28px">
      <div><h2>{L(lang,'Send the data, get a capacity','Hantar data, dapat kapasiti','发数据，给容量')}</h2><p>{L(lang,'We reply with a gas balance, a unit size and an indicative budget within three working days.','Kami balas dengan imbangan gas, saiz unit dan bajet indikatif dalam tiga hari bekerja.','三个工作日内回复气量平衡、机组选型与预算区间。')}</p></div>
      <a class="btn light" href="contact.html">{L(lang,'Contact KSTS','Hubungi KSTS','联系 KSTS')}</a>
    </div>
  </div>
</section>
"""


def biomethane(lang):
    return f"""
<section class="page-head">
  <div class="wrap">
    <p class="eyebrow">{L(lang,'Biomethane &amp; bio-CNG','Biometana &amp; bio-CNG','生物天然气与 Bio-CNG')}</p>
    <h1>{L(lang,'Biogas upgraded to boiler-grade gas','Biogas ditingkatkan ke gred dandang','把沼气提纯到锅炉级燃气')}</h1>
    <p class="lead">{L(lang,
      'If the mill boiler runs on diesel, LPG or natural gas, the fastest payback is often not electricity — it is replacing that fuel with biomethane at ≥97% CH₄, produced on site.',
      'Jika dandang kilang menggunakan diesel, LPG atau gas asli, pulangan terpantas sering bukan elektrik — tetapi menggantikan bahan api itu dengan biometana ≥97% CH₄ yang dihasilkan di tapak.',
      '如果油厂锅炉烧柴油、LPG 或天然气，回本最快的往往不是发电，而是用现场生产的 ≥97% 甲烷替代那部分燃料。')}</p>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-head"><p class="eyebrow">{L(lang,'Process','Proses','工艺')}</p><h2>{L(lang,'From 60% to 97% in five steps','Dari 60% ke 97% dalam lima langkah','五步从 60% 提到 97%')}</h2></div>
    <div class="steps" style="grid-template-columns:repeat(5,1fr)">
      <div class="step"><b>{L(lang,'Desulfurise','Nyahsulfur','脱硫')}</b><span>{L(lang,'Biological plus iron oxide to protect media and compressor.','Biologi serta oksida besi untuk melindungi media dan pemampat.','生物法加氧化铁，保护吸附剂与压缩机。')}</span></div>
      <div class="step"><b>{L(lang,'Compress','Mampat','增压')}</b><span>{L(lang,'To the pressure required by the separation step.','Ke tekanan yang diperlukan oleh langkah pemisahan.','升到分离工艺所需压力。')}</span></div>
      <div class="step"><b>{L(lang,'Dry','Kering','干燥')}</b><span>{L(lang,'Refrigerated dryer and coalescing filters.','Pengering penyejukan dan penapis penggabungan.','冷冻式干燥机与聚结过滤器。')}</span></div>
      <div class="step"><b>{L(lang,'Remove CO₂','Buang CO₂','脱碳')}</b><span>{L(lang,'PSA, water scrubbing or membrane.','PSA, scrubber air atau membran.','PSA、水洗或膜分离。')}</span></div>
      <div class="step"><b>{L(lang,'Deliver','Hantar','外送')}</b><span>{L(lang,'To the burner, or 250 bar for tube-trailer bio-CNG.','Ke pembakar, atau 250 bar untuk bio-CNG treler.','送燃烧器，或 250 bar 装槽车做 Bio-CNG。')}</span></div>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="sec-head"><p class="eyebrow">{L(lang,'Technology selection','Pemilihan teknologi','技术路线选择')}</p>
      <h2>{L(lang,'PSA, water scrubbing or membrane','PSA, scrubber air atau membran','PSA、水洗、膜分离怎么选')}</h2>
      <p class="lead">{L(lang,
        'There is no universal best choice. It depends on gas volume, required purity, power cost and available space.',
        'Tiada pilihan terbaik sejagat. Ia bergantung kepada isipadu gas, ketulenan diperlukan, kos kuasa dan ruang tersedia.',
        '没有放之四海皆准的答案，取决于气量、纯度要求、电价与场地。')}</p>
    </div>
    <div class="table-wrap">
      <table>
        <thead><tr><th>&nbsp;</th><th>PSA</th><th>{L(lang,'Water scrubbing','Scrubber air','水洗')}</th><th>{L(lang,'Membrane','Membran','膜分离')}</th></tr></thead>
        <tbody>
          <tr><td><b>{L(lang,'CH₄ purity','Ketulenan CH₄','甲烷纯度')}</b></td><td class="num">96–98%</td><td class="num">97–99%</td><td class="num">96–98%</td></tr>
          <tr><td><b>{L(lang,'Methane recovery','Pemulihan metana','甲烷回收率')}</b></td><td class="num">95–98%</td><td class="num">98–99%</td><td class="num">96–99%</td></tr>
          <tr><td><b>{L(lang,'Power demand','Keperluan kuasa','电耗')}</b></td><td class="num">0.25–0.30 kWh/Nm³</td><td class="num">0.20–0.30</td><td class="num">0.20–0.28</td></tr>
          <tr><td><b>{L(lang,'Footprint','Ruang','占地')}</b></td><td class="num">{L(lang,'Medium','Sederhana','中')}</td><td class="num">{L(lang,'Large','Besar','大')}</td><td class="num">{L(lang,'Small','Kecil','小')}</td></tr>
          <tr><td><b>{L(lang,'Best fit','Padanan terbaik','适用场景')}</b></td><td class="num">200–1,500 Nm³/h</td><td class="num">{L(lang,'Large plants','Loji besar','大型站')}</td><td class="num">{L(lang,'Small/medium, skid','Kecil/sederhana, skid','中小型、撬装')}</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-head"><p class="eyebrow">{L(lang,'Output','Output','产出')}</p><h2>{L(lang,'What 500 Nm³/h of raw biogas becomes','Apa jadi kepada 500 Nm³/j biogas mentah','500 Nm³/h 原气能出多少产品')}</h2></div>
    <div class="grid-2">
      <div class="table-wrap"><table style="min-width:0"><tbody>
        <tr><td>{L(lang,'Raw biogas in','Biogas mentah masuk','原沼气输入')}</td><td class="num">500 Nm³/h @ 60% CH₄</td></tr>
        <tr><td>{L(lang,'Methane in','Metana masuk','甲烷输入')}</td><td class="num">300 Nm³/h</td></tr>
        <tr><td>{L(lang,'Recovery (97%)','Pemulihan (97%)','回收率 97%')}</td><td class="num">291 Nm³/h</td></tr>
        <tr><td>{L(lang,'Product at 97% CH₄','Produk pada 97% CH₄','97% 甲烷产品')}</td><td class="num">≈ 300 Nm³/h</td></tr>
        <tr><td>{L(lang,'Product energy','Tenaga produk','产品热值')}</td><td class="num">≈ 2,890 kW (LHV)</td></tr>
        <tr><td>{L(lang,'Upgrading power','Kuasa peningkatan','提纯电耗')}</td><td class="num">≈ 125–150 kW</td></tr>
      </tbody></table></div>
      <div>
        <h3>{L(lang,'Gas quality we guarantee','Kualiti gas yang kami jamin','我们保证的气质')}</h3>
        <ul class="checks">
          <li>CH₄ ≥ 97% ({L(lang,'adjustable 96–99%','boleh laras 96–99%','可调 96–99%')})</li>
          <li>CO₂ ≤ 2–3%</li>
          <li>H₂S ≤ 5 ppm</li>
          <li>{L(lang,'Water dew point ≤ −40 °C at pressure','Titik embun air ≤ −40 °C pada tekanan','带压下露点 ≤ −40°C')}</li>
          <li>O₂ ≤ 0.5%</li>
        </ul>
        <div class="callout"><p><b>{L(lang,'Burner retrofit is part of the scope.','Retrofit pembakar adalah sebahagian skop.','燃烧器改造在范围内。')}</b> {L(lang,
          'A biomethane burner needs a different gas train, orifice and flame detection from diesel or LPG — we coordinate that with the boiler supplier.',
          'Pembakar biometana memerlukan gas train, orifis dan pengesanan nyalaan berbeza daripada diesel — kami selaraskan dengan pembekal dandang.',
          '燃生物天然气的燃烧器，气路、喷嘴与火焰检测都与柴油/LPG 不同，我们负责与锅炉厂对接。')}</p></div>
      </div>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="sec-head"><p class="eyebrow">Bio-CNG</p><h2>{L(lang,'When there is no pipeline, build a virtual one','Bila tiada saluran paip, bina secara maya','没有管网，就建一条虚拟管网')}</h2>
      <p class="lead">{L(lang,
        'Compressed biomethane at 250 bar in tube trailers moves gas to estates, factories or refuelling points. For remote Sabah and Sarawak sites this is often the only route to market.',
        'Biometana termampat pada 250 bar dalam treler tiub menghantar gas ke estet, kilang atau pusat pengisian. Bagi tapak terpencil di Sabah dan Sarawak, ini selalunya satu-satunya laluan pasaran.',
        '250 bar 压缩生物天然气用管束槽车运到庄园、工厂或加气点。对沙巴与砂拉越的偏远站点，这常是唯一出路。')}</p></div>
    <div class="grid-3">
      <article class="card"><p class="tag">1</p><h3>{L(lang,'Compression','Pemampatan','压缩')}</h3><p>{L(lang,'Multi-stage to 250 bar with inter-stage drying and cooling.','Berbilang peringkat ke 250 bar dengan pengeringan dan penyejukan antara peringkat.','多级压缩至 250 bar，级间干燥冷却。')}</p></article>
      <article class="card"><p class="tag">2</p><h3>{L(lang,'Storage &amp; loading','Penyimpanan &amp; pemuatan','储气与装车')}</h3><p>{L(lang,'Cascade storage, loading arm, custody metering.','Penyimpanan kaskad, lengan pemuatan, pemeteran.','级联储气、装车臂、交接计量。')}</p></article>
      <article class="card"><p class="tag">3</p><h3>{L(lang,'Off-site use','Penggunaan luar tapak','异地使用')}</h3><p>{L(lang,'Pressure reduction skid or daughter station for fleets.','Skid penurunan tekanan atau stesen anak untuk fleet.','减压撬，或为车队做子站。')}</p></article>
    </div>
  </div>
</section>
"""


def equipment(lang):
    return f"""
<section class="page-head">
  <div class="wrap">
    <p class="eyebrow">{L(lang,'Equipment &amp; scope','Peralatan &amp; skop','设备与供货范围')}</p>
    <h1>{L(lang,'What we supply, and what we do not','Apa kami bekalkan, dan apa yang tidak','我们供什么，不供什么')}</h1>
    <p class="lead">{L(lang,
      'Clear scope boundaries are the cheapest risk control on a biogas project. Below is the standard battery limit for a power plant and an upgrading plant.',
      'Sempadan skop yang jelas ialah kawalan risiko termurah dalam projek biogas. Di bawah ialah had standard untuk loji kuasa dan loji peningkatan.',
      '把供货边界写清楚，是沼气项目最便宜的风险控制。以下是电站与提纯站的标准界限。')}</p>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-head"><p class="eyebrow">{L(lang,'Gas engines','Enjin gas','燃气机组')}</p><h2>{L(lang,'Biogas gensets, 300 kW to 2 MW','Genset biogas, 300 kW hingga 2 MW','沼气发电机组 300 kW – 2 MW')}</h2>
      <p class="lead">{L(lang,
        'Chinese-manufactured gas engines from a proven production line, configured for POME biogas, typically 25–35% below the landed price of a European equivalent for 600–800 kW units.',
        'Enjin gas buatan China daripada barisan pengeluaran yang terbukti, dikonfigurasi untuk biogas POME, biasanya 25–35% lebih rendah daripada harga rakan Eropah bagi unit 600–800 kW.',
        '国产成熟产线燃气机，按 POME 沼气配置，600–800 kW 机型到岸价通常比同级欧洲机组低 25–35%。')}</p></div>
    <div class="table-wrap">
      <table>
        <thead><tr><th>{L(lang,'Model class','Kelas model','机型')}</th><th>{L(lang,'Output','Output','功率')}</th><th>{L(lang,'Electrical efficiency','Kecekapan elektrik','发电效率')}</th><th>{L(lang,'Heat recovery','Pemulihan haba','余热回收')}</th><th>{L(lang,'Voltage','Voltan','电压')}</th></tr></thead>
        <tbody>
          <tr><td class="num">300 kW</td><td class="num">300 kW / 375 kVA</td><td class="num">36–38%</td><td class="num">≈ 330 kW</td><td>415 V / 50 Hz</td></tr>
          <tr><td class="num">500 kW</td><td class="num">500 kW / 625 kVA</td><td class="num">35.2%</td><td class="num">≈ 560 kW</td><td>415 V / 50 Hz</td></tr>
          <tr><td class="num">600 kW</td><td class="num">600 kW / 750 kVA</td><td class="num">35.1%</td><td class="num">≈ 680 kW</td><td>415 V / 50 Hz</td></tr>
          <tr><td class="num">700 kW</td><td class="num">700 kW / 875 kVA</td><td class="num">35.2%</td><td class="num">≈ 790 kW</td><td>415 V / 50 Hz</td></tr>
          <tr><td class="num">800 kW</td><td class="num">800 kW / 1,000 kVA</td><td class="num">≈ 35.2%</td><td class="num">≈ 900 kW</td><td>415 V / 50 Hz</td></tr>
          <tr><td class="num">1,000 kW</td><td class="num">1,000 kW / 1,250 kVA</td><td class="num">35.2%</td><td class="num">≈ 1,150 kW</td><td>415 V / 50 Hz</td></tr>
          <tr><td class="num">1,500 kW</td><td class="num">1,500 kW / 1,875 kVA</td><td class="num">39–41%</td><td class="num">≈ 1,700 kW</td><td>415 V / 50 Hz</td></tr>
          <tr><td class="num">2,000 kW</td><td class="num">2,000 kW / 2,500 kVA</td><td class="num">39–42%</td><td class="num">≈ 2,300 kW</td><td>11 kV {L(lang,'option','pilihan','可选')}</td></tr>
        </tbody>
      </table>
    </div>
    <p class="small" style="margin-top:14px">{L(lang,
      'Indicative at full load with 60% CH₄. Final selection based on site gas data. Containerised from 300 kW to 1.5 MW.',
      'Indikatif pada beban penuh dengan 60% CH₄. Pemilihan akhir berdasarkan data gas tapak. Kontena dari 300 kW hingga 1.5 MW.',
      '60% 甲烷满负荷下的参考值，最终按现场气样选型。300 kW–1.5 MW 可做集装箱式。')}</p>
    <p class="small" style="margin-top:8px">{L(lang,
      'Electrical efficiency is taken from the manufacturer gas consumption data below (≈3.50 kWh per Nm³ CH₄), which is lower than the 38–40% sometimes quoted for Chinese units.',
      'Kecekapan elektrik diambil daripada data penggunaan gas pengeluar di bawah (≈3.50 kWh per Nm³ CH₄), lebih rendah daripada 38–40% yang kadangkala disebut.',
      '发电效率取自下方厂家实测气耗（≈3.50 kWh/Nm³ 甲烷），低于市面上常说的 38–40% 国产机组口径。')}</p>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-head"><p class="eyebrow">{L(lang,'Fuel gas','Gas bahan api','气质与气耗')}</p><h2>{L(lang,'What the engine needs at the inlet flange','Apa yang enjin perlukan di flan masuk','机组进口法兰需要什么')}</h2>
      <p class="lead">{L(lang,
        'All values measured 1 m upstream of the gas pressure regulating valve. Outside these limits the engine is derated and warranty conditions change.',
        'Semua nilai diukur 1 m di hadapan injap pengatur tekanan gas. Di luar had ini enjin akan dikurangkan kuasa dan syarat waranti berubah.',
        '以下数值均在机组燃气调压阀前 1 m 处测量。超出限值会降功率并影响质保条款。')}</p></div>
    <div class="table-wrap">
      <table>
        <thead><tr><th>{L(lang,'Parameter','Parameter','参数')}</th><th>{L(lang,'Requirement','Keperluan','要求')}</th><th>{L(lang,'Why','Sebab','原因')}</th></tr></thead>
        <tbody>
          <tr><td>{L(lang,'Gas temperature','Suhu gas','沼气温度')}</td><td class="num">10 – 35 °C</td><td>{L(lang,'Condensation and knock control','Kawalan kondensasi dan ketukan','防冷凝与爆震')}</td></tr>
          <tr><td>{L(lang,'Gas pressure','Tekanan gas','进气压力')}</td><td class="num">3 – 10 kPa(g); ramp ≤ 1 kPa/min</td><td>{L(lang,'Stable mixing at the gas train','Pencampuran stabil pada kereta gas','燃气混合稳定')}</td></tr>
          <tr><td>{L(lang,'Dust','Habuk','粉尘')}</td><td class="num">≤ 5 μm; ≤ 10 mg/Nm³</td><td>{L(lang,'Valve and piston ring wear','Kehausan injap dan cincin piston','阀门与活塞环磨损')}</td></tr>
          <tr><td>H₂S</td><td class="num">≤ 50 mg/Nm³</td><td>{L(lang,'Acid corrosion of lube oil and liners','Kakisan asid pada minyak pelincir dan liner','润滑油与缸套酸腐蚀')}</td></tr>
          <tr><td>{L(lang,'Gas humidity','Kelembapan gas','气体湿度')}</td><td class="num">≤ 70% RH</td><td>{L(lang,'No free water in the gas train','Tiada air bebas dalam kereta gas','燃气系统不析水')}</td></tr>
          <tr><td>{L(lang,'Condensate','Kondensat','冷凝水')}</td><td>{L(lang,'None at lowest ambient temperature','Tiada pada suhu ambien terendah','最低环境温度下不产生')}</td><td>{L(lang,'Cold-start and winter operation','Mula sejuk dan operasi musim hujan','冷启动与低温工况')}</td></tr>
          <tr><td>NH₃</td><td class="num">≤ 40 mg/Nm³</td><td>{L(lang,'Formation of ammonium sulphates','Pembentukan ammonium sulfat','生成硫酸铵盐')}</td></tr>
          <tr><td>{L(lang,'Siloxanes','Siloksan','硅氧烷')}</td><td class="num">≤ 10 mg/Nm³</td><td>{L(lang,'Abrasive silica deposits on valves and plugs','Mendapan silika pada injap dan palam','阀件与火花塞积二氧化硅')}</td></tr>
          <tr><td>CH₄</td><td class="num">≥ 45% by volume; ramp ≤ 2%/min</td><td>{L(lang,'Stable combustion, no lean-burn trips','Pembakaran stabil, tiada hentian lean-burn','燃烧稳定，避免稀薄燃烧停机')}</td></tr>
        </tbody>
      </table>
    </div>
    <div class="sec-head" style="margin-top:44px"><p class="eyebrow">{L(lang,'Gas consumption','Penggunaan gas','气耗')}</p><h3>{L(lang,'Pure methane demand by rating','Permintaan metana tulen mengikut saiz','各功率段纯甲烷耗量')}</h3></div>
    <div class="table-wrap">
      <table>
        <thead><tr><th>{L(lang,'Rating','Saiz','功率')}</th><th>{L(lang,'CH₄ (Nm³/h)','CH₄ (Nm³/j)','纯甲烷（Nm³/h）')}</th><th>{L(lang,'Raw biogas at 45%','Biogas mentah pada 45%','原气 @45%')}</th><th>{L(lang,'at 55%','pada 55%','@55%')}</th><th>{L(lang,'at 60%','pada 60%','@60%')}</th><th>{L(lang,'kWh per Nm³ CH₄','kWh per Nm³ CH₄','每方甲烷发电')}</th></tr></thead>
        <tbody>
          <tr><td class="num">500 kW</td><td class="num">142</td><td class="num">316 Nm³/h</td><td class="num">258 Nm³/h</td><td class="num">237 Nm³/h</td><td class="num">3.52 kWh</td></tr>
          <tr><td class="num">600 kW</td><td class="num">172</td><td class="num">382 Nm³/h</td><td class="num">313 Nm³/h</td><td class="num">287 Nm³/h</td><td class="num">3.49 kWh</td></tr>
          <tr><td class="num">700 kW</td><td class="num">200</td><td class="num">444 Nm³/h</td><td class="num">364 Nm³/h</td><td class="num">333 Nm³/h</td><td class="num">3.50 kWh</td></tr>
          <tr><td class="num">1,000 kW</td><td class="num">286</td><td class="num">636 Nm³/h</td><td class="num">520 Nm³/h</td><td class="num">477 Nm³/h</td><td class="num">3.50 kWh</td></tr>
        </tbody>
      </table>
    </div>
    <p class="small" style="margin-top:14px">{L(lang,
      'Manufacturer data: 142 / 172 / 200 / 286 Nm³ CH₄ per hour for 500 / 600 / 700 / 1,000 kW, i.e. ≈ 0.286 Nm³ CH₄ per kWh. Long-term output on variable biogas runs at 90–100% of rating, so annual energy should be modelled at 90% load.',
      'Data pengeluar: 142 / 172 / 200 / 286 Nm³ CH₄ sejam bagi 500 / 600 / 700 / 1,000 kW, iaitu ≈ 0.286 Nm³ CH₄ per kWh. Output jangka panjang pada biogas berubah ialah 90–100% daripada saiz, jadi tenaga tahunan patut dimodelkan pada beban 90%.',
      '厂家实测：500 / 600 / 700 / 1,000 kW 分别对应 142 / 172 / 200 / 286 Nm³ 纯甲烷每小时，即每度电约 0.286 Nm³ 甲烷。沼气波动下长期出力为额定值的 90–100%，年发电量宜按 90% 负荷建模。')}</p>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="sec-head"><p class="eyebrow">{L(lang,'Balance of plant','Baki loji','配套系统')}</p><h2>{L(lang,'The parts between the pond and the engine','Bahagian antara kolam dan enjin','从池塘到机组之间的东西')}</h2></div>
    <div class="grid-3">
      <article class="card"><p class="tag">{L(lang,'Capture','Tangkap','收集')}</p><h3>{L(lang,'Pond cover &amp; gas collection','Penutup kolam &amp; pengumpulan gas','覆盖与集气')}</h3><p>{L(lang,'HDPE or geomembrane cover, headers, condensate traps, relief and hatches.','Penutup HDPE atau geomembran, header, perangkap kondensat, relief dan hatch.','HDPE 或土工膜覆盖、集气总管、冷凝水罐、泄压与检修口。')}</p></article>
      <article class="card"><p class="tag">{L(lang,'Desulfurisation','Nyahsulfur','脱硫')}</p><h3>{L(lang,'Biological + iron oxide','Biologi + oksida besi','生物法 ＋ 氧化铁')}</h3><p>{L(lang,'Trickling filter for bulk H₂S, polishing vessels in duty/standby.','Penapis titisan untuk H₂S pukal, vesel penggilap tugas/siap sedia.','滴滤塔除大量硫化氢，精脱罐一用一备。')}</p></article>
      <article class="card"><p class="tag">{L(lang,'Conditioning','Pengkondisian','净化')}</p><h3>{L(lang,'Chiller, blower, filters','Penyejuk, blower, penapis','冷干机、风机、过滤器')}</h3><p>{L(lang,'Refrigerated dryer, coalescing filters, Roots blower with VFD, flame arrestor.','Pengering penyejukan, penapis penggabungan, blower Roots dengan VFD, penahan api.','冷冻干燥、聚结过滤、变频罗茨风机、阻火器。')}</p></article>
      <article class="card"><p class="tag">{L(lang,'Storage','Penyimpanan','储存')}</p><h3>{L(lang,'Gas holder','Penyimpan gas','储气柜')}</h3><p>{L(lang,'Membrane holder to buffer mill swings and protect the engine.','Penyimpan membran untuk menampan turun naik kilang dan melindungi enjin.','膜式储气柜缓冲波动，保护机组。')}</p></article>
      <article class="card"><p class="tag">{L(lang,'Safety','Keselamatan','安全')}</p><h3>{L(lang,'Flare &amp; gas detection','Flare &amp; pengesanan gas','火炬与气体检测')}</h3><p>{L(lang,'Full-flow flare, CH₄/H₂S detection, ESD logic, Ex-rated instruments.','Flare aliran penuh, pengesanan CH₄/H₂S, logik ESD, instrumen berkadaran Ex.','全流量火炬、甲烷与硫化氢检测、紧急停车逻辑、防爆仪表。')}</p></article>
      <article class="card"><p class="tag">{L(lang,'Heat','Haba','余热')}</p><h3>{L(lang,'Heat recovery','Pemulihan haba','余热回收')}</h3><p>{L(lang,'Exhaust exchanger and jacket circuit to 85–95 °C hot water, or steam.','Penukar ekzos dan litar jaket ke air panas 85–95 °C, atau stim.','烟气换热器与缸套水回路，产 85–95°C 热水或蒸汽。')}</p></article>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-head"><p class="eyebrow">{L(lang,'Scope matrix · biogas plant &amp; upgrading','Matriks skop · loji biogas &amp; peningkatan','范围矩阵 · 沼气电站与提纯站')}</p><h2>{L(lang,'Who does what','Siapa buat apa','谁做什么')}</h2></div>
    <div class="table-wrap">
      <table>
        <thead><tr><th>{L(lang,'Work package','Pakej kerja','工作包')}</th><th>KSTS / {L(lang,'technology partner','rakan teknologi','技术方')}</th><th>{L(lang,'Client','Pelanggan','客户')}</th><th>{L(lang,'Notes','Nota','说明')}</th></tr></thead>
        <tbody>
          <tr><td>{L(lang,'Process design &amp; gas balance','Reka proses &amp; imbangan gas','工艺设计与气量平衡')}</td><td>{L(lang,'Yes','Ya','是')}</td><td>{L(lang,'Data supply','Bekal data','提供数据')}</td><td>P&amp;ID, GA, {L(lang,'mass balance','imbangan jisim','物料平衡')}</td></tr>
          <tr><td>{L(lang,'Pond cover / digester','Penutup kolam / pencerna','池塘覆盖 / 厌氧罐')}</td><td>{L(lang,'Design &amp; supply','Reka &amp; bekal','设计供货')}</td><td>{L(lang,'Site access, earthworks','Akses tapak, kerja tanah','场地与土方')}</td><td>{L(lang,'Pond survey first','Tinjauan kolam dahulu','先做池塘勘察')}</td></tr>
          <tr><td>{L(lang,'Gas treatment &amp; gas train','Rawatan gas &amp; gas train','气体净化与气路')}</td><td>{L(lang,'Yes','Ya','是')}</td><td>—</td><td>{L(lang,'Battery limit: engine inlet','Had: salur masuk enjin','界限：机组入口法兰')}</td></tr>
          <tr><td>{L(lang,'Genset &amp; control panel','Genset &amp; panel kawalan','机组与控制柜')}</td><td>{L(lang,'Yes','Ya','是')}</td><td>—</td><td>{L(lang,'Protection and synchronising','Perlindungan dan penyegerakan','保护与同期')}</td></tr>
          <tr><td>{L(lang,'Civil foundations','Asas awam','土建基础')}</td><td>{L(lang,'Execution (CIDB)','Pelaksanaan (CIDB)','施工（CIDB）')}</td><td>{L(lang,'Approvals','Kelulusan','审批')}</td><td>{L(lang,'Local subcontractors','Subkontraktor tempatan','本地分包')}</td></tr>
          <tr><td>{L(lang,'Electrical reticulation','Rangkaian elektrik','电气敷设')}</td><td>{L(lang,'Execution','Pelaksanaan','施工')}</td><td>{L(lang,'Transformer / grid','Transformer / grid','变压器与并网')}</td><td>415 V; HV {L(lang,'by utility','oleh utiliti','由供电局')}</td></tr>
          <tr><td>{L(lang,'Erection &amp; commissioning','Pemasangan &amp; pentauliahan','安装与调试')}</td><td>{L(lang,'Yes','Ya','是')}</td><td>{L(lang,'Utilities','Utiliti','水电')}</td><td>{L(lang,'DOSH witness','Saksi DOSH','DOSH 见证')}</td></tr>
          <tr><td>O&amp;M</td><td>{L(lang,'Option','Pilihan','可选')}</td><td>{L(lang,'Site crew','Krew tapak','现场班组')}</td><td>{L(lang,'Full contract or advisory','Kontrak penuh atau nasihat','全包或顾问')}</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-head"><p class="eyebrow">{L(lang,'Hydrogen CHP','CHP Hidrogen','氢能热电联供')}</p><h2>{L(lang,'Methane-reforming fuel cell CHP, 7.5 kW to 100 kW','CHP sel bahan api pembentukan semula metana, 7.5 kW hingga 100 kW','甲烷重整制氢热电联供 7.5 kW – 100 kW')}</h2>
      <p class="lead">{L(lang,
        'Bottled 97% biomethane — or raw 60% biogas taken straight from the mill with an integrated purification front end — is reformed to hydrogen on site, then converted by a fuel cell into power and 60–70 °C hot water: no flame, no NOx, no SOx, no particulates. Water is the only by-product. FOB RM 10,000/kW for the bottled-gas version, installation excluded; the raw-biogas version is quoted per site.',
        'Biometana 97% dalam botol — atau biogas mentah 60% terus dari kilang dengan penulenan bersepadu di hadapan — dibentuk semula kepada hidrogen di tapak, kemudian ditukar oleh sel bahan api kepada kuasa dan air panas 60–70 °C: tiada api, tiada NOx, tiada SOx, tiada zarah. Air ialah satu-satunya hasil sampingan. FOB RM 10,000/kW untuk versi gas botol, tidak termasuk pemasangan; versi biogas mentah disebut harga mengikut tapak.',
        '瓶装 97% 生物天然气——或者直接从油厂取 60% 原沼气、前端配一体化净化装置——现场重整制氢，燃料电池同时供电与 60–70 ℃ 热水：无明火、无氮氧化物、无硫氧化物、无粉尘，唯一副产物是水。瓶装气版 FOB 价 RM 10,000/kW；带一体化净化的原沼气版 FOB 价 RM 19,500/kW，均不含安装。')}</p></div>
    <div class="table-wrap">
      <table>
        <thead><tr><th>{L(lang,'Model','Model','机型')}</th><th>{L(lang,'Fuel input (kW)','Input bahan api (kW)','燃料输入（kW）')}</th><th>{L(lang,'CH₄ (Nm³/h)','CH₄ (Nm³/j)','甲烷（Nm³/h）')}</th><th>{L(lang,'Heat recovery (kW)','Pemulihan haba (kW)','余热（kW）')}</th><th>{L(lang,'Hot water, 50 K rise (L/h)','Air panas, kenaikan 50 K (L/j)','热水 50 K（L/h）')}</th><th>{L(lang,'Indicative price','Harga indikatif','参考价')}</th></tr></thead>
        <tbody>
          <tr><td class="num">7.5 kW</td><td class="num">17.9</td><td class="num">1.80</td><td class="num">7.7</td><td class="num">132</td><td class="num">RM 75,000</td></tr>
          <tr><td class="num">10 kW</td><td class="num">23.8</td><td class="num">2.39</td><td class="num">10.2</td><td class="num">176</td><td class="num">RM 100,000</td></tr>
          <tr><td class="num">15 kW</td><td class="num">35.7</td><td class="num">3.59</td><td class="num">15.4</td><td class="num">265</td><td class="num">RM 150,000</td></tr>
          <tr><td class="num">20 kW</td><td class="num">47.6</td><td class="num">4.79</td><td class="num">20.5</td><td class="num">353</td><td class="num">RM 200,000</td></tr>
          <tr><td class="num">30 kW</td><td class="num">71.4</td><td class="num">7.18</td><td class="num">30.7</td><td class="num">529</td><td class="num">RM 300,000</td></tr>
          <tr><td class="num">50 kW</td><td class="num">119.0</td><td class="num">11.97</td><td class="num">51.2</td><td class="num">882</td><td class="num">RM 500,000</td></tr>
          <tr><td class="num">75 kW</td><td class="num">178.6</td><td class="num">17.97</td><td class="num">76.8</td><td class="num">1,323</td><td class="num">RM 750,000</td></tr>
          <tr><td class="num">100 kW</td><td class="num">238.1</td><td class="num">23.95</td><td class="num">102.4</td><td class="num">1,763</td><td class="num">RM 1,000,000</td></tr>
        </tbody>
      </table>
    </div>
    <p class="small" style="margin-top:14px">{L(lang,
      'Basis: methane LHV 9.94 kWh/Nm³; 42% electrical and 43% recoverable heat are manufacturer guaranteed values at rated output (85% overall). Indicative FOB price to a Malaysian port, excluding freight, insurance, SST, installation, civil works, cylinder room, manifold and grid connection: RM 10,000/kW on bottled 97% gas, RM 19,500/kW on raw 60% biogas with integrated purification.',
      'Asas: LHV metana 9.94 kWh/Nm³; 42% elektrik dan 43% haba boleh pulih ialah nilai dijamin pengeluar pada output terkadar (85% keseluruhan). Harga FOB indikatif ke pelabuhan Malaysia, tidak termasuk tambang, insurans, SST, pemasangan, kerja awam, bilik silinder, manifold dan sambungan grid: RM 10,000/kW pada gas botol 97%, RM 19,500/kW pada biogas mentah 60% dengan penulenan bersepadu.',
      '口径：甲烷低热值 9.94 kWh/Nm³；发电 42%、余热回收 43% 为厂家保证值（额定出力、综合 85%）。参考价为马来西亚港口 FOB，不含运费、保险、SST、安装、土建、气瓶间、汇流排与并网：瓶装 97% 气 RM 10,000/kW，60% 原沼气配一体化净化 RM 19,500/kW。')}</p>
    <div class="sec-head" style="margin-top:44px"><p class="eyebrow">{L(lang,'Feed gas','Gas suapan','进气条件')}</p><h3>{L(lang,'What the reformer needs','Apa yang pemangkin pembentukan perlukan','重整器进口需要什么')}</h3></div>
    <div class="table-wrap">
      <table>
        <thead><tr><th>{L(lang,'Parameter','Parameter','参数')}</th><th>{L(lang,'Requirement','Keperluan','要求')}</th><th>{L(lang,'Why','Sebab','原因')}</th></tr></thead>
        <tbody>
          <tr><td>CH₄</td><td class="num">≥ 95% by volume</td><td>{L(lang,'Reforming catalyst needs a concentrated methane feed','Pemangkin pembentukan perlukan suapan metana pekat','重整催化剂要求甲烷浓度')}</td></tr>
          <tr><td>H₂S</td><td class="num">&lt; 1 ppm</td><td>{L(lang,'Sulphur poisons the reforming catalyst and the stack','Sulfur meracuni pemangkin dan sel','硫使重整催化剂与电堆中毒')}</td></tr>
          <tr><td>{L(lang,'Siloxanes','Siloksan','硅氧烷')}</td><td class="num">&lt; 0.1 mg/Nm³</td><td>{L(lang,'Silica deposits on catalyst and electrodes','Mendapan silika pada pemangkin dan elektrod','二氧化硅沉积在催化剂与电极上')}</td></tr>
          <tr><td>{L(lang,'Condensate','Kondensat','冷凝水')}</td><td>{L(lang,'None','Tiada','无')}</td><td>{L(lang,'Free water damages the catalyst bed','Air bebas merosakkan katil pemangkin','游离水损坏催化剂床层')}</td></tr>
          <tr><td>{L(lang,'Supply','Bekalan','供气方式')}</td><td>{L(lang,'Bottled 97% gas at 200 bar via a manifold, or raw biogas at 55–65% through the integrated purification module','Gas botol 97% pada 200 bar melalui manifold, atau biogas mentah 55–65% melalui modul penulenan bersepadu','瓶装 97% 气经汇流排 200 bar，或 55–65% 原沼气经一体化净化模块')}</td><td>{L(lang,'No pipeline and no on-site hydrogen storage','Tiada saluran paip dan tiada penyimpanan hidrogen di tapak','不用管网，现场不储氢')}</td></tr>
          <tr><td>{L(lang,'Raw biogas option','Pilihan biogas mentah','原沼气方案')}</td><td>{L(lang,'Desulphurisation, CO₂ removal, drying and compression inside the same package','Nyahsulfur, penyingkiran CO₂, pengeringan dan pemampatan dalam pakej yang sama','脱硫、脱 CO₂、干燥、增压，全部在同一机组内')}</td><td>{L(lang,'No separate upgrading plant and no bottled gas needed; investment higher than the bottled-gas version','Tiada loji peningkatan berasingan dan tiada gas botol; pelaburan lebih tinggi daripada versi gas botol','不需要另建提纯站，也不用买瓶装气；投资高于瓶装气版')}</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="sec-head"><p class="eyebrow">{L(lang,'Supply scope','Skop bekalan','供货范围')}</p><h2>{L(lang,'What the CHP price includes','Apa yang termasuk dalam harga CHP','热电联供的价格包含什么')}</h2></div>
    <div class="table-wrap">
      <table>
        <thead><tr><th>{L(lang,'Item','Item','项目')}</th><th>{L(lang,'Content','Kandungan','内容')}</th></tr></thead>
        <tbody>
          <tr><td><b>{L(lang,'Included','Termasuk','包含')}</b></td><td>{L(lang,'Reformer, shift reactor, hydrogen purification, fuel cell stack, inverter, heat exchangers, control system, enclosure','Pembentuk semula, reaktor shift, penulenan hidrogen, timbunan sel bahan api, penyongsang, penukar haba, sistem kawalan, selongsong','重整器、变换反应器、氢气提纯、电堆、逆变器、换热器、控制系统、机柜')}</td></tr>
          <tr><td><b>{L(lang,'Optional','Pilihan','选配')}</b></td><td>{L(lang,'Integrated front-end purification for raw biogas feed — desulphurisation, CO₂ removal, drying and compression inside the same package, priced per site','Penulenan bersepadu di hadapan untuk suapan biogas mentah — nyahsulfur, penyingkiran CO₂, pengeringan dan pemampatan dalam pakej yang sama, harga mengikut tapak','原沼气进气用的一体化前端净化——脱硫、脱 CO₂、干燥、增压做进同一机组，按现场单独报价')}</td></tr>
          <tr><td><b>{L(lang,'Excluded','Tidak termasuk','不含')}</b></td><td>{L(lang,'SST, freight beyond a Malaysian port, civil works, cylinder room and manifold, installation, grid connection, permits','SST, tambang melebihi pelabuhan Malaysia, kerja awam, bilik silinder dan manifold, pemasangan, sambungan grid, permit','SST、马来西亚港口以外运费、土建、气瓶间与汇流排、安装、并网、许可')}</td></tr>
          <tr><td><b>{L(lang,'Warranty','Waranti','质保')}</b></td><td>{L(lang,'24 months on the unit; stack 5 years or 25,000 hours, whichever comes first','24 bulan untuk unit; timbunan 5 tahun atau 25,000 jam, mana yang dahulu','整机 24 个月；电堆 5 年或 25,000 小时（先到为准）')}</td></tr>
          <tr><td><b>{L(lang,'Delivery','Penghantaran','交货期')}</b></td><td>{L(lang,'4–6 months from order and gas analysis','4–6 bulan dari pesanan dan analisis gas','收到订单与气质分析后 4–6 个月')}</td></tr>
          <tr><td><b>{L(lang,'Price basis','Asas harga','价格口径')}</b></td><td>{L(lang,'Bottled-gas version FOB RM 10,000/kW; raw-biogas version with integrated purification FOB RM 19,500/kW. Both installation excluded, valid 90 days, subject to gas analysis and site survey.','Versi gas botol FOB RM 10,000/kW; versi biogas mentah dengan penulenan bersepadu FOB RM 19,500/kW. Kedua-duanya pemasangan tidak termasuk, sah 90 hari, tertakluk kepada analisis gas dan tinjauan tapak.','瓶装气版 FOB 价 RM 10,000/kW；带一体化净化的原沼气版 FOB 价 RM 19,500/kW。两者均不含安装，有效期 90 天，以气质分析与现场勘查为准。')}</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-head"><p class="eyebrow">{L(lang,'Scope matrix · hydrogen CHP','Matriks skop · CHP hidrogen','范围矩阵 · 氢能热电联供')}</p><h2>{L(lang,'Who does what','Siapa buat apa','谁做什么')}</h2></div>
    <div class="table-wrap">
      <table>
        <thead><tr><th>{L(lang,'Work package','Pakej kerja','工作包')}</th><th>KSTS / {L(lang,'technology partner','rakan teknologi','技术方')}</th><th>{L(lang,'Client','Pelanggan','客户')}</th><th>{L(lang,'Notes','Nota','说明')}</th></tr></thead>
        <tbody>
          <tr><td>{L(lang,'Sizing &amp; load matching','Saiz &amp; padanan beban','选型与负荷匹配')}</td><td>{L(lang,'Yes','Ya','是')}</td><td>{L(lang,'Load profile','Profil beban','负荷曲线')}</td><td>{L(lang,'Sized on the heat and power demand','Mengikut permintaan haba dan kuasa','按热电需求定容')}</td></tr>
          <tr><td>{L(lang,'Fuel chain: upgrading, bottling, manifold — or raw biogas with integrated purification','Rantaian bahan api: peningkatan, pembotolan, manifold — atau biogas mentah dengan penulenan bersepadu','燃料链：提纯、装瓶、汇流排——或原沼气配一体化净化')}</td><td>{L(lang,'Design &amp; supply','Reka &amp; bekal','设计供货')}</td><td>{L(lang,'Cylinder yard / pond gas tapping point','Halaman silinder / titik ambilan gas kolam','瓶组场地 / 池顶取气点')}</td><td>CH₄ ≥ 95% {L(lang,'at reformer inlet','di salur masuk reformer','重整器进口')}, H₂S &lt; 1 ppm</td></tr>
          <tr><td>{L(lang,'CHP unit &amp; control panel','Unit CHP &amp; panel kawalan','机组与控制柜')}</td><td>{L(lang,'Yes','Ya','是')}</td><td>—</td><td>{L(lang,'Battery limit: gas inlet and AC terminals','Had: salur masuk gas dan terminal AC','界限：燃气接口与交流出线端子')}</td></tr>
          <tr><td>{L(lang,'Civil foundations &amp; enclosure','Asas awam &amp; selongsong','土建基础与机房')}</td><td>{L(lang,'Execution (CIDB)','Pelaksanaan (CIDB)','施工（CIDB）')}</td><td>{L(lang,'Approvals','Kelulusan','审批')}</td><td>{L(lang,'Local subcontractors','Subkontraktor tempatan','本地分包')}</td></tr>
          <tr><td>{L(lang,'Electrical &amp; grid connection','Elektrik &amp; sambungan grid','电气与并网')}</td><td>{L(lang,'Execution','Pelaksanaan','施工')}</td><td>{L(lang,'Transformer / utility','Transformer / utiliti','变压器与供电局')}</td><td>230/400 V; {L(lang,'HV by utility','HV oleh utiliti','高压由供电局')}</td></tr>
          <tr><td>{L(lang,'Erection &amp; commissioning','Pemasangan &amp; pentauliahan','安装与调试')}</td><td>{L(lang,'Separate quotation','Sebut harga berasingan','另行报价')}</td><td>{L(lang,'Utilities &amp; access','Utiliti &amp; akses','水电与场地')}</td><td>{L(lang,'Not included in the FOB price','Tidak termasuk dalam harga FOB','不含在 FOB 价内')}</td></tr>
          <tr><td>O&amp;M</td><td>{L(lang,'Option','Pilihan','可选')}</td><td>{L(lang,'Site crew','Krew tapak','现场班组')}</td><td>{L(lang,'Includes stack replacement planning','Termasuk perancangan penggantian timbunan','含电堆更换计划')}</td></tr>
          <tr><td>{L(lang,'Permits &amp; SST','Permit &amp; SST','许可与 SST')}</td><td>{L(lang,'Assist','Bantu','协助')}</td><td>{L(lang,'Applicant of record','Pemohon berdaftar','申报主体')}</td><td>{L(lang,'Per Malaysian regulations','Mengikut peraturan Malaysia','按马来西亚法规')}</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</section>
"""


def calculator(lang):
    asset = "../" if lang != "en" else ""
    print_btn = L(lang, 'Print / save as PDF', 'Cetak / simpan PDF', '打印 / 存为 PDF')
    copy_btn = L(lang, 'Copy summary', 'Salin ringkasan', '复制结果')
    return f"""
<section class="page-head">
  <div class="wrap">
    <p class="eyebrow">{L(lang,'Engineering tools','Alat kejuruteraan','工程测算工具')}</p>
    <h1>{L(lang,'Five calculators, no sign-up','Lima kalkulator, tanpa pendaftaran','五个计算器，不用注册')}</h1>
    <p class="lead">{L(lang,
      'These are the formulas we use in pre-feasibility work. They are deliberately transparent: every assumption is shown and you can change it. Use them to challenge a supplier’s numbers — including ours.',
      'Ini formula yang kami gunakan dalam kerja pra-kelayakan. Ia sengaja telus: setiap andaian dipaparkan dan boleh diubah. Gunakan untuk menyemak angka pembekal — termasuk kami.',
      '这些公式与我们的预可研一致，所有假设都摊开、可改。用它去质疑供应商的数字——包括我们的。')}</p>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-head"><p class="eyebrow">{L(lang,'Selection at a glance','Pemilihan sekilas pandang','选型速查')}</p><h2>{L(lang,'Pick the model from the gas you measured','Pilih model daripada gas yang anda ukur','用实测气量直接定机型')}</h2>
      <p class="lead">{L(lang,
        'Enter the raw biogas flow and methane content from your own measurement. The selector returns the largest unit that runs on that gas at full load, plus the gas it needs and what it generates in a year.',
        'Masukkan aliran biogas mentah dan kandungan metana daripada pengukuran anda sendiri. Pemilih memberi unit terbesar yang boleh beroperasi pada gas itu dengan beban penuh, serta keperluan gas dan penjanaan setahun.',
        '输入你现场实测的原沼气流量与甲烷含量，直接给出能满负荷运行的最大机型、对应需气量与年发电量。')}</p></div>
    <div class="calc">
      <div class="calc-form">
        <div class="field"><label for="q_flow">{L(lang,'Measured raw biogas (Nm³/h)','Biogas mentah diukur (Nm³/j)','实测原沼气量（Nm³/h）')}</label><input id="q_flow" type="number" value="400" step="10" min="0"><div class="hint">{L(lang,'Average over one to two weeks, not a peak reading.','Purata satu hingga dua minggu, bukan bacaan puncak.','取一到两周平均值，不要用峰值。')}</div></div>
        <div class="field"><label for="q_ch4">{L(lang,'Methane content (%)','Kandungan metana (%)','甲烷含量（%）')}</label><input id="q_ch4" type="number" value="60" step="0.5" min="40" max="99"><div class="hint">{L(lang,'Engine limit is 45% minimum.','Had enjin minimum 45%.','机组下限 45%。')}</div></div>
        <div class="field"><label for="q_load">{L(lang,'Average load factor (%)','Faktor beban purata (%)','平均负荷率（%）')}</label><input id="q_load" type="number" value="90" step="1" min="50" max="100"><div class="hint">{L(lang,'Long-term output on variable biogas is 90–100%.','Output jangka panjang pada biogas berubah ialah 90–100%.','沼气波动下长期出力 90–100%。')}</div></div>
      </div>
      <div class="calc-out">
        <div class="kv hl"><span>{L(lang,'Recommended model','Model disyorkan','推荐机型')}</span><b id="q_model">—</b></div>
        <div class="kv hl"><span>{L(lang,'Output at full load','Output beban penuh','满负荷出力')}</span><b id="q_out">—</b></div>
        <div class="kv"><span>{L(lang,'Pure methane required','Metana tulen diperlukan','需纯甲烷')}</span><b id="q_ch4">—</b></div>
        <div class="kv"><span>{L(lang,'Raw biogas required at your CH₄','Biogas mentah diperlukan','对应原气量')}</span><b id="q_need">—</b></div>
        <div class="kv"><span>{L(lang,'Share of measured gas used','Bahagian gas digunakan','气量利用率')}</span><b id="q_util">—</b></div>
        <div class="kv"><span>{L(lang,'Annual generation (8,000 h × load)','Penjanaan tahunan (8,000 j × beban)','年发电量（8,000 h × 负荷）')}</span><b id="q_ann">—</b></div>
        <div class="kv"><span>{L(lang,'Recoverable heat','Haba boleh pulih','可回收热量')}</span><b id="q_heat">—</b></div>
      </div>
    </div>
    <div class="warn" id="q_warn"></div>
    <div class="table-wrap" style="margin-top:26px">
      <table>
        <thead><tr><th>{L(lang,'Model','Model','机型')}</th><th>{L(lang,'CH₄ needed (Nm³/h)','CH₄ perlu (Nm³/j)','需纯甲烷（Nm³/h）')}</th><th>{L(lang,'Raw gas @45%','Gas mentah @45%','原气 @45%')}</th><th>{L(lang,'@55%','@55%','@55%')}</th><th>{L(lang,'@60%','@60%','@60%')}</th><th>{L(lang,'MWh/yr @90% load','MWh/tahun @90%','年发电 MWh @90%')}</th><th>{L(lang,'Heat (kW)','Haba (kW)','余热（kW）')}</th></tr></thead>
        <tbody>
          <tr><td class="num">500 kW</td><td class="num">142</td><td class="num">316</td><td class="num">258</td><td class="num">237</td><td class="num">3,600</td><td class="num">593</td></tr>
          <tr><td class="num">600 kW</td><td class="num">172</td><td class="num">382</td><td class="num">313</td><td class="num">287</td><td class="num">4,320</td><td class="num">718</td></tr>
          <tr><td class="num">700 kW</td><td class="num">200</td><td class="num">444</td><td class="num">364</td><td class="num">333</td><td class="num">5,040</td><td class="num">835</td></tr>
          <tr><td class="num">800 kW</td><td class="num">229</td><td class="num">508</td><td class="num">416</td><td class="num">381</td><td class="num">5,760</td><td class="num">954</td></tr>
          <tr><td class="num">1,000 kW</td><td class="num">286</td><td class="num">636</td><td class="num">520</td><td class="num">477</td><td class="num">7,200</td><td class="num">1,194</td></tr>
        </tbody>
      </table>
    </div>
    <p class="small" style="margin-top:14px">{L(lang,
      'Based on manufacturer gas consumption (≈3.50 kWh per Nm³ CH₄), 8,000 operating hours and 90% load. Size on the 45% methane column when gas quality is uncertain — running out of gas costs more than buying one size larger.',
      'Berdasarkan penggunaan gas pengeluar (≈3.50 kWh per Nm³ CH₄), 8,000 jam operasi dan beban 90%. Guna lajur metana 45% jika kualiti gas tidak pasti — kehabisan gas lebih mahal daripada beli satu saiz lebih besar.',
      '厂口气耗 ≈3.50 kWh/Nm³ 甲烷，按 8,000 运行小时、90% 负荷。气质不确定时按 45% 那一列选型——气不够的代价高于买大一档。')}</p>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="tabs" id="tabs">
      <button class="tab-btn active" data-tab="tool1">1 · {L(lang,'Gas to power &amp; heat','Gas ke kuasa &amp; haba','气量→电与热')}</button>
      <button class="tab-btn" data-tab="tool2">2 · {L(lang,'Capacity sizing','Saiz kapasiti','容量选型')}</button>
      <button class="tab-btn" data-tab="tool3">3 · {L(lang,'Mill to biogas','Kilang ke biogas','压榨量→沼气')}</button>
      <button class="tab-btn" data-tab="tool4">4 · {L(lang,'Upgrading yield','Hasil peningkatan','提纯收率')}</button>
      <button class="tab-btn" data-tab="tool5">5 · {L(lang,'Project economics','Ekonomi projek','项目经济性')}</button>
    </div>

    <div class="tab-panel active" id="tool1">
      <div class="tool-head">
        <div><p class="eyebrow">{L(lang,'Tool 01','Alat 01','工具 01')}</p><h2>{L(lang,'Biogas flow → electricity and heat','Aliran biogas → elektrik dan haba','沼气流量 → 电与热')}</h2></div>
        <div class="tool-actions"><button class="btn ghost sm" onclick="window.print()">{print_btn}</button><button class="btn sm" onclick="copySummary('tool1')">{copy_btn}</button></div>
      </div>
      <div class="calc">
        <div class="calc-form">
          <div class="field"><label for="t1_flow">{L(lang,'Biogas flow available (Nm³/h)','Aliran biogas tersedia (Nm³/j)','可用沼气量（Nm³/h）')}</label><input id="t1_flow" type="number" value="300" step="1" min="0"><div class="hint">{L(lang,'Normal cubic metres per hour at 0 °C, 101.3 kPa.','Meter padu normal sejam pada 0 °C, 101.3 kPa.','0°C、101.3 kPa 下的标方每小时。')}</div></div>
          <div class="field"><label for="t1_ch4">{L(lang,'Methane content (%)','Kandungan metana (%)','甲烷含量（%）')}</label><input id="t1_ch4" type="number" value="60" step="0.5" min="40" max="99"><div class="hint">{L(lang,'POME biogas is typically 55–65%.','Biogas POME biasanya 55–65%.','POME 沼气通常 55–65%。')}</div></div>
          <div class="field"><label for="t1_eff">{L(lang,'Electrical efficiency (%)','Kecekapan elektrik (%)','发电效率（%）')}</label><input id="t1_eff" type="number" value="35.2" step="0.1" min="20" max="45"><div class="hint">{L(lang,'Manufacturer gas data: ≈3.50 kWh per Nm³ CH₄ = 35.2%. Premium European 40–43%.','Data gas pengeluar: ≈3.50 kWh per Nm³ CH₄ = 35.2%. Eropah premium 40–43%.','厂家气耗口径：每方甲烷约 3.50 kWh 电 = 35.2%。（欧洲高端 40–43%）')}</div></div>
          <div class="field"><label for="t1_heat">{L(lang,'Recoverable heat (% of fuel)','Haba boleh pulih (% bahan api)','可回收热量（占燃料能量）')}</label><input id="t1_heat" type="number" value="43" step="1" min="0" max="60"><div class="hint">{L(lang,'Jacket + exhaust, typically 40–45%.','Jaket + ekzos, biasanya 40–45%.','缸套水＋烟气，通常 40–45%。')}</div></div>
          <div class="field"><label for="t1_hours">{L(lang,'Operating hours per year','Jam operasi setahun','年运行小时')}</label><input id="t1_hours" type="number" value="8000" step="100" min="0" max="8760"></div>
          <div class="field"><label for="t1_load">{L(lang,'Average load factor (%)','Faktor beban purata (%)','平均负荷率（%）')}</label><input id="t1_load" type="number" value="90" step="1" min="10" max="100"><div class="hint">{L(lang,'On variable biogas, long-term output is 90–100% of rating.','Pada biogas berubah, output jangka panjang ialah 90–100% daripada saiz.','沼气波动下长期出力为额定值的 90–100%。')}</div></div>
        </div>
        <div class="calc-out">
          <h3>{L(lang,'Results','Keputusan','测算结果')}</h3>
          <div class="out-grid">
            <div class="kv hl"><span>{L(lang,'Electrical output at full load','Output elektrik beban penuh','满负荷发电功率')}</span><b id="t1_kw">—</b></div>
            <div class="kv hl"><span>{L(lang,'Recoverable heat','Haba boleh pulih','可回收热量')}</span><b id="t1_heatkw">—</b></div>
            <div class="kv"><span>{L(lang,'Fuel energy input','Tenaga bahan api masuk','输入燃料能量')}</span><b id="t1_energy">—</b></div>
            <div class="kv"><span>{L(lang,'Total efficiency (power + heat)','Jumlah kecekapan (kuasa + haba)','综合效率（电＋热）')}</span><b id="t1_total">—</b></div>
            <div class="kv"><span>{L(lang,'Biogas per kWh generated','Biogas per kWh dijana','每度电耗气量')}</span><b id="t1_gas_kwh">—</b></div>
            <div class="kv"><span>{L(lang,'Annual generation','Penjanaan tahunan','年发电量')}</span><b id="t1_year_kwh">—</b></div>
            <div class="kv"><span>{L(lang,'Annual heat delivered','Haba tahunan','年供热量')}</span><b id="t1_year_heat">—</b></div>
            <div class="kv"><span>{L(lang,'Diesel avoided','Diesel dielak','替代柴油量')}</span><b id="t1_diesel">—</b></div>
          </div>
          <div class="warn" id="t1_warn"></div>
          <p class="note">{L(lang,'Methane LHV 9.94 kWh/Nm³ (35.8 MJ/Nm³). Diesel genset at 35% efficiency and 2.68 kg CO₂/litre for the avoided-fuel figure.','LHV metana 9.94 kWh/Nm³ (35.8 MJ/Nm³). Genset diesel pada kecekapan 35% dan 2.68 kg CO₂/liter untuk angka pengelakan.','甲烷低热值 9.94 kWh/Nm³（35.8 MJ/Nm³）。柴油机组按 35% 效率、2.68 kg CO₂/升计。')}</p>
        </div>
      </div>
    </div>

    <div class="tab-panel" id="tool2">
      <div class="tool-head">
        <div><p class="eyebrow">{L(lang,'Tool 02','Alat 02','工具 02')}</p><h2>{L(lang,'Target output → gas demand','Sasaran output → keperluan gas','目标功率 → 需气量')}</h2></div>
        <div class="tool-actions"><button class="btn ghost sm" onclick="window.print()">{print_btn}</button><button class="btn sm" onclick="copySummary('tool2')">{copy_btn}</button></div>
      </div>
      <div class="calc">
        <div class="calc-form">
          <div class="field"><label for="t2_kw">{L(lang,'Target electrical output (kW)','Sasaran output elektrik (kW)','目标发电功率（kW）')}</label><input id="t2_kw" type="number" value="600" step="10" min="0"></div>
          <div class="field"><label for="t2_ch4">{L(lang,'Methane content (%)','Kandungan metana (%)','甲烷含量（%）')}</label><input id="t2_ch4" type="number" value="60" step="0.5" min="40" max="99"></div>
          <div class="field"><label for="t2_eff">{L(lang,'Electrical efficiency (%)','Kecekapan elektrik (%)','发电效率（%）')}</label><input id="t2_eff" type="number" value="35.2" step="0.1" min="20" max="45"><div class="hint">{L(lang,'≈3.50 kWh per Nm³ CH₄ from manufacturer data.','≈3.50 kWh per Nm³ CH₄ daripada data pengeluar.','按厂家气耗，每方甲烷约 3.50 kWh 电。')}</div></div>
          <div class="field"><label for="t2_load">{L(lang,'Average load factor (%)','Faktor beban purata (%)','平均负荷率（%）')}</label><input id="t2_load" type="number" value="85" step="1" min="10" max="100"><div class="hint">{L(lang,'Demand is calculated at full load; average scales with load.','Keperluan dikira pada beban penuh; purata mengikut beban.','按满负荷计算；平均耗气随负荷折算。')}</div></div>
        </div>
        <div class="calc-out">
          <h3>{L(lang,'Gas demand','Keperluan gas','需气量')}</h3>
          <div class="out-grid">
            <div class="kv hl"><span>{L(lang,'Biogas at full load','Biogas beban penuh','满负荷沼气量')}</span><b id="t2_flow">—</b></div>
            <div class="kv hl"><span>{L(lang,'Biogas per day at full load','Biogas sehari beban penuh','满负荷日耗气')}</span><b id="t2_day">—</b></div>
            <div class="kv"><span>{L(lang,'Average at load factor','Purata pada faktor beban','按负荷率平均')}</span><b id="t2_avg">—</b></div>
            <div class="kv"><span>{L(lang,'Methane flow','Aliran metana','甲烷流量')}</span><b id="t2_ch4flow">—</b></div>
            <div class="kv"><span>{L(lang,'Fuel energy input','Tenaga bahan api','燃料输入能量')}</span><b id="t2_energy">—</b></div>
            <div class="kv"><span>{L(lang,'Annual biogas','Biogas tahunan','年耗气量')}</span><b id="t2_year">—</b></div>
          </div>
          <div class="warn" id="t2_warn"></div>
          <p class="note">{L(lang,'Use this to test whether an offered engine matches your measured gas flow.','Gunakan untuk menguji sama ada enjin yang ditawarkan sepadan dengan aliran gas anda.','用它检验供应商推荐的机组是否配得上你的实测气量。')}</p>
        </div>
      </div>
    </div>

    <div class="tab-panel" id="tool3">
      <div class="tool-head">
        <div><p class="eyebrow">{L(lang,'Tool 03','Alat 03','工具 03')}</p><h2>{L(lang,'Mill throughput → biogas potential','Kemampuan kilang → potensi biogas','压榨量 → 沼气潜力')}</h2></div>
        <div class="tool-actions"><button class="btn ghost sm" onclick="window.print()">{print_btn}</button><button class="btn sm" onclick="copySummary('tool3')">{copy_btn}</button></div>
      </div>
      <div class="calc">
        <div class="calc-form">
          <div class="field"><label for="t3_ffb">{L(lang,'FFB throughput (t/h)','Kemampuan FFB (t/j)','FFB 处理量（t/h）')}</label><input id="t3_ffb" type="number" value="60" step="1" min="0"></div>
          <div class="field"><label for="t3_pome">{L(lang,'POME generated (m³ per t FFB)','POME dijana (m³ per t FFB)','POME 产生量（m³/t FFB）')}</label><input id="t3_pome" type="number" value="0.65" step="0.05" min="0.2" max="1.2"></div>
          <div class="field"><label for="t3_yield">{L(lang,'Biogas yield (Nm³ per m³ POME)','Hasil biogas (Nm³ per m³ POME)','沼气产率（Nm³/m³ POME）')}</label><input id="t3_yield" type="number" value="24" step="1" min="5" max="40"><div class="hint">{L(lang,'Covered lagoon 20–28; well-mixed CSTR can reach 30+.','Kolam bertutup 20–28; CSTR bercampur baik boleh 30+.','覆盖塘 20–28；充分搅拌的 CSTR 可达 30 以上。')}</div></div>
          <div class="field"><label for="t3_ch4">{L(lang,'Methane content (%)','Kandungan metana (%)','甲烷含量（%）')}</label><input id="t3_ch4" type="number" value="60" step="0.5" min="40" max="99"></div>
          <div class="field"><label for="t3_capture">{L(lang,'Capture efficiency (%)','Kecekapan tangkapan (%)','收集效率（%）')}</label><input id="t3_capture" type="number" value="85" step="1" min="30" max="100"><div class="hint">{L(lang,'Share of generated gas actually delivered.','Bahagian gas dijana yang benar-benar dihantar.','实际送入机组的比例。')}</div></div>
          <div class="field"><label for="t3_eff">{L(lang,'Electrical efficiency (%)','Kecekapan elektrik (%)','发电效率（%）')}</label><input id="t3_eff" type="number" value="35.2" step="0.1" min="20" max="45"></div>
        </div>
        <div class="calc-out">
          <h3>{L(lang,'Biogas &amp; power potential','Potensi biogas &amp; kuasa','沼气与发电潜力')}</h3>
          <div class="out-grid">
            <div class="kv"><span>{L(lang,'POME produced','POME dijana','POME 产量')}</span><b id="t3_pome_day">—</b></div>
            <div class="kv hl"><span>{L(lang,'Biogas generated','Biogas dijana','沼气生成量')}</span><b id="t3_gas_day">—</b></div>
            <div class="kv hl"><span>{L(lang,'Biogas to engine','Biogas ke enjin','送入机组气量')}</span><b id="t3_gas_h">—</b></div>
            <div class="kv"><span>{L(lang,'Methane available','Metana tersedia','可用甲烷')}</span><b id="t3_ch4_h">—</b></div>
            <div class="kv"><span>{L(lang,'Electrical potential','Potensi elektrik','发电潜力')}</span><b id="t3_kw">—</b></div>
            <div class="kv"><span>{L(lang,'Annual generation (8,000 h)','Penjanaan tahunan (8,000 j)','年发电量（8000 小时）')}</span><b id="t3_mwh">—</b></div>
          </div>
          <div class="warn" id="t3_warn"></div>
          <p class="note">{L(lang,'Assumes continuous 24-hour POME production. Real mills have shifts and stoppages — use measured inflow where available. Screening only, not a design basis.','Menganggap pengeluaran POME 24 jam berterusan. Kilang sebenar ada syif dan henti — guna data masuk sebenar jika ada. Untuk saringan sahaja.','假设 24 小时连续产 POME。实际有班次与停机，有实测数据请用实测。仅作筛选，不作设计依据。')}</p>
        </div>
      </div>
    </div>

    <div class="tab-panel" id="tool4">
      <div class="tool-head">
        <div><p class="eyebrow">{L(lang,'Tool 04','Alat 04','工具 04')}</p><h2>{L(lang,'Raw biogas → biomethane yield','Biogas mentah → hasil biometana','原沼气 → 生物天然气收率')}</h2></div>
        <div class="tool-actions"><button class="btn ghost sm" onclick="window.print()">{print_btn}</button><button class="btn sm" onclick="copySummary('tool4')">{copy_btn}</button></div>
      </div>
      <div class="calc">
        <div class="calc-form">
          <div class="field"><label for="t4_flow">{L(lang,'Raw biogas flow (Nm³/h)','Aliran biogas mentah (Nm³/j)','原沼气流量（Nm³/h）')}</label><input id="t4_flow" type="number" value="500" step="10" min="0"></div>
          <div class="field"><label for="t4_ch4">{L(lang,'Methane content in (%)','Kandungan metana masuk (%)','进气甲烷含量（%）')}</label><input id="t4_ch4" type="number" value="60" step="0.5" min="40" max="80"></div>
          <div class="field"><label for="t4_rec">{L(lang,'Methane recovery (%)','Pemulihan metana (%)','甲烷回收率（%）')}</label><input id="t4_rec" type="number" value="97" step="0.5" min="80" max="100"><div class="hint">{L(lang,'PSA 95–98, membrane 96–99, water scrubber 98–99.','PSA 95–98, membran 96–99, scrubber air 98–99.','PSA 95–98，膜 96–99，水洗 98–99。')}</div></div>
          <div class="field"><label for="t4_purity">{L(lang,'Product purity (% CH₄)','Ketulenan produk (% CH₄)','产品纯度（% 甲烷）')}</label><input id="t4_purity" type="number" value="97" step="0.5" min="90" max="99.9"></div>
          <div class="field"><label for="t4_power">{L(lang,'Upgrading power (kWh/Nm³ raw)','Kuasa peningkatan (kWh/Nm³ mentah)','提纯电耗（kWh/Nm³ 原气）')}</label><input id="t4_power" type="number" value="0.27" step="0.01" min="0.05" max="0.6"></div>
        </div>
        <div class="calc-out">
          <h3>{L(lang,'Upgrading output','Output peningkatan','提纯产出')}</h3>
          <div class="out-grid">
            <div class="kv"><span>{L(lang,'Methane entering','Metana masuk','进气甲烷')}</span><b id="t4_ch4in">—</b></div>
            <div class="kv hl"><span>{L(lang,'Biomethane product','Produk biometana','生物天然气产量')}</span><b id="t4_product">—</b></div>
            <div class="kv"><span>{L(lang,'Methane in product','Metana dalam produk','产品中甲烷')}</span><b id="t4_ch4out">—</b></div>
            <div class="kv"><span>{L(lang,'Methane loss','Kehilangan metana','甲烷损失')}</span><b id="t4_loss">—</b></div>
            <div class="kv"><span>{L(lang,'CO₂ removed','CO₂ dibuang','脱除二氧化碳')}</span><b id="t4_co2">—</b></div>
            <div class="kv hl"><span>{L(lang,'Product energy (LHV)','Tenaga produk (LHV)','产品热值（低热值）')}</span><b id="t4_mw">—</b></div>
            <div class="kv"><span>{L(lang,'Upgrading power demand','Keperluan kuasa peningkatan','提纯耗电')}</span><b id="t4_kw">—</b></div>
            <div class="kv"><span>{L(lang,'Diesel equivalent','Setara diesel','折合柴油')}</span><b id="t4_diesel">—</b></div>
          </div>
          <p class="note">{L(lang,'Product = CH₄ in × recovery ÷ purity. Diesel equivalent at 35.8 MJ/L LHV.','Produk = CH₄ masuk × pemulihan ÷ ketulenan. Setara diesel pada 35.8 MJ/L LHV.','产量 = 进气甲烷 × 回收率 ÷ 纯度。柴油按 35.8 MJ/L 低热值折算。')}</p>
        </div>
      </div>
    </div>

    <div class="tab-panel" id="tool5">
      <div class="tool-head">
        <div><p class="eyebrow">{L(lang,'Tool 05','Alat 05','工具 05')}</p><h2>{L(lang,'Project economics','Ekonomi projek','项目经济性')}</h2></div>
        <div class="tool-actions"><button class="btn ghost sm" onclick="window.print()">{print_btn}</button><button class="btn sm" onclick="copySummary('tool5')">{copy_btn}</button></div>
      </div>
      <div class="calc">
        <div class="calc-form">
          <div class="field"><label for="t5_kw">{L(lang,'Plant capacity (kW)','Kapasiti loji (kW)','电站容量（kW）')}</label><input id="t5_kw" type="number" value="600" step="10" min="0"></div>
          <div class="field"><label for="t5_capex">{L(lang,'Turnkey capex (USD per kW)','Capex turnkey (USD per kW)','交钥匙投资（美元/kW）')}</label><input id="t5_capex" type="number" value="2200" step="50" min="0"><div class="hint">{L(lang,'Engine package FOB ≈ USD 580–630/kW (600–800 kW); complete plant typically USD 1,800–2,600/kW.','Pakej enjin FOB ≈ USD 580–630/kW (600–800 kW); loji lengkap biasanya USD 1,800–2,600/kW.','机组成套 FOB 约 580–630 美元/kW（600–800 kW）；完整电站通常 1,800–2,600 美元/kW。')}</div></div>
          <div class="field"><label for="t5_cur">{L(lang,'Currency','Mata wang','币种')}</label><select id="t5_cur"><option value="MYR">MYR (Malaysia)</option><option value="IDR">IDR (Indonesia)</option><option value="USD">USD</option></select></div>
          <div class="field"><label for="t5_tariff">{L(lang,'Value of electricity (local/kWh)','Nilai elektrik (tempatan/kWh)','电价价值（当地币/kWh）')}</label><input id="t5_tariff" type="number" value="0.65" step="0.01" min="0"><div class="hint">{L(lang,'Inland Sabah diesel: RM 0.55–0.75. Grid import RM 0.40–0.50. Indonesia USD 0.07–0.10.','Diesel pedalaman Sabah: RM 0.55–0.75. Import grid RM 0.40–0.50. Indonesia USD 0.07–0.10.','沙巴内陆柴油 RM 0.55–0.75；市电 RM 0.40–0.50；印尼 USD 0.07–0.10。')}</div></div>
          <div class="field"><label for="t5_use">{L(lang,'Share of output displacing bought power (%)','Bahagian output mengganti kuasa beli (%)','替代外购电的比例（%）')}</label><input id="t5_use" type="number" value="75" step="5" min="0" max="100"><div class="hint">{L(lang,'Only self-consumed kWh carry the full displaced-fuel value.','Hanya kWh digunakan sendiri membawa nilai penuh.','只有自用的电量才享受完整的替代价值。')}</div></div>
          <div class="field"><label for="t5_fx">{L(lang,'Exchange rate (local per USD)','Kadar tukaran (tempatan per USD)','汇率（当地币/美元）')}</label><input id="t5_fx" type="number" value="4.2" step="0.01" min="1"></div>
          <div class="field"><label for="t5_hours">{L(lang,'Operating hours per year','Jam operasi setahun','年运行小时')}</label><input id="t5_hours" type="number" value="8000" step="100" min="0" max="8760"></div>
          <div class="field"><label for="t5_om">{L(lang,'Variable O&amp;M (USD/kWh)','O&amp;M berubah (USD/kWh)','可变运维（美元/kWh）')}</label><input id="t5_om" type="number" value="0.0169" step="0.0001" min="0"><div class="hint">{L(lang,'Full-service O&amp;M incl. overhauls ≈ USD 0.017/kWh.','O&amp;M perkhidmatan penuh termasuk baik pulih ≈ USD 0.017/kWh.','全包运维（含大修）约 0.017 美元/kWh。')}</div></div>
          <div class="field"><label for="t5_omfix">{L(lang,'Fixed O&amp;M (USD/year)','O&amp;M tetap (USD/tahun)','固定运维（美元/年）')}</label><input id="t5_omfix" type="number" value="0" step="1000" min="0"></div>
          <div class="field"><label for="t5_disc">{L(lang,'Discount rate (%)','Kadar diskaun (%)','折现率（%）')}</label><input id="t5_disc" type="number" value="8" step="0.5" min="0" max="30"></div>
        </div>
        <div class="calc-out">
          <h3>{L(lang,'Financial summary','Ringkasan kewangan','财务摘要')}</h3>
          <div class="out-grid">
            <div class="kv"><span>{L(lang,'Total capex','Jumlah capex','总投资')}</span><b id="t5_total_capex">—</b></div>
            <div class="kv"><span>{L(lang,'Annual generation','Penjanaan tahunan','年发电量')}</span><b id="t5_gen">—</b></div>
            <div class="kv hl"><span>{L(lang,'Annual revenue','Hasil tahunan','年收入')}</span><b id="t5_rev">—</b></div>
            <div class="kv"><span>{L(lang,'Annual O&amp;M','O&amp;M tahunan','年运维成本')}</span><b id="t5_opex">—</b></div>
            <div class="kv hl"><span>{L(lang,'Net annual cash flow','Aliran tunai bersih tahunan','年净现金流')}</span><b id="t5_net">—</b></div>
            <div class="kv hl"><span>{L(lang,'Simple payback','Tempoh pulang mudah','静态回收期')}</span><b id="t5_payback">—</b></div>
            <div class="kv"><span>{L(lang,'10-year net (undiscounted)','Bersih 10 tahun (tanpa diskaun)','10 年净收益（未折现）')}</span><b id="t5_cum10">—</b></div>
            <div class="kv"><span>NPV</span><b id="t5_npv">—</b></div>
            <div class="kv"><span>IRR (10 {L(lang,'years','tahun','年')})</span><b id="t5_irr">—</b></div>
            <div class="kv"><span>LCOE</span><b id="t5_lcoe">—</b></div>
          </div>
          <div class="warn" id="t5_warn"></div>
          <p class="note">{L(lang,'Revenue assumes the stated value for each valued kWh. Excludes financing, land and utility grid upgrades. Screening model, not bankable.','Hasil menganggap nilai dinyatakan bagi setiap kWh dinilai. Tidak termasuk pembiayaan, tanah dan naik taraf grid. Model saringan, bukan bankable.','收入按可计价电量与给定电价计算。不含融资、土地与电网改造费用。仅作筛选，不可用于融资。')}</p>
        </div>
      </div>
    </div>

    <div class="assume" style="margin-top:28px">
      <b>{L(lang,'Method &amp; constants.','Kaedah &amp; pemalar.','方法与常数。')}</b> {L(lang,
        'Methane LHV 35.8 MJ/Nm³ = 9.94 kWh/Nm³. Biogas energy = flow × CH₄ fraction × 9.94. Electrical output = fuel energy × electrical efficiency. Recoverable heat = fuel energy × heat fraction. All results are indicative; guarantees are issued only against measured site data.',
        'LHV metana 35.8 MJ/Nm³ = 9.94 kWh/Nm³. Tenaga biogas = aliran × pecahan CH₄ × 9.94. Output elektrik = tenaga bahan api × kecekapan. Haba boleh pulih = tenaga bahan api × pecahan haba. Semua keputusan indikatif; jaminan hanya berdasarkan data tapak yang diukur.',
        '甲烷低热值 35.8 MJ/Nm³ = 9.94 kWh/Nm³。沼气能量 = 流量 × 甲烷比例 × 9.94；发电功率 = 燃料能量 × 发电效率；可回收热 = 燃料能量 × 热回收比例。所有结果为参考值，性能保证只对实测现场数据出具。')}
      <br><br>
      <b>{L(lang,'Why we publish the formulas.','Mengapa kami terbitkan formula.','为什么公开公式。')}</b> {L(lang,
        'Most supplier calculators hide their assumptions. A biogas project is decided on gas quality and operating hours, not on a polished number.',
        'Kebanyakan kalkulator pembekal menyembunyikan andaian. Projek biogas ditentukan oleh kualiti gas dan jam operasi, bukan angka yang digilap.',
        '多数供应商的计算器藏着假设。沼气项目的成败取决于气质与运行小时，而不是一个漂亮的数字。')}
    </div>
  </div>
</section>
<script src="{asset}assets/js/calc.js"></script>
"""


def about(lang):
    asset = "../" if lang != "en" else ""
    return f"""
<section class="page-head">
  <div class="wrap">
    <p class="eyebrow">{L(lang,'About KSTS','Tentang KSTS','关于 KSTS')}</p>
    <h1>{L(lang,'A Sabah contractor with the right registrations — and a factory behind it','Kontraktor Sabah dengan kelayakan betul — dan kilang di belakangnya','一家资质齐全的沙巴本地承包商，背后有工厂')}</h1>
    <p class="lead">{L(lang,
      'KSTS K. S. Technical Services is a CIDB-registered, Bumiputera-owned technical services company based in Telupid, Sabah. We deliver biogas and bioenergy projects for the palm oil and agro-industrial sector in Sabah and Sarawak.',
      'KSTS K. S. Technical Services ialah syarikat perkhidmatan teknikal milik Bumiputera berdaftar CIDB yang berpangkalan di Telupid, Sabah. Kami melaksanakan projek biogas dan bio tenaga untuk sektor kelapa sawit dan industri pertanian di Sabah dan Sarawak.',
      'KSTS K. S. Technical Services 是 CIDB 注册、沙巴土著持有的技术服务公司，总部位于 Telupid。我们为沙巴与砂拉越的棕榈油及农产加工业交付沼气与生物能源项目。')}</p>
  </div>
</section>

<section>
  <div class="wrap grid-2" style="gap:48px;align-items:start">
    <div>
      <p class="eyebrow">{L(lang,'The company','Syarikat','公司')}</p>
      <h2>{L(lang,'What KSTS does','Apa KSTS lakukan','KSTS 做什么')}</h2>
      <p>{L(lang,
        'Founded to serve the estates and mills of the Labuk–Sugut and Telupid belt, KSTS works across civil, mechanical and electrical scope, and holds the statutory registrations a biogas plant needs before it can legally run.',
        'Ditubuhkan untuk berkhidmat kepada estet dan kilang di jalur Labuk–Sugut dan Telupid, KSTS merangkumi skop awam, mekanikal dan elektrik, serta memegang pendaftaran berkanun yang diperlukan loji biogas sebelum boleh beroperasi secara sah.',
        'KSTS 起家于服务 Labuk–Sugut 与 Telupid 一带的庄园和油厂，业务覆盖土建、机装与电气，并持有沼气站合法运行所需的法定资质。')}</p>
      <ul class="checks">
        <li>{L(lang,'Agricultural, building, civil and mechanical works','Kerja pertanian, bangunan, awam dan mekanikal','农业、建筑、土建与机装工程')}</li>
        <li>{L(lang,'I.C.E. and steam engineering visitation under FMA 1967','Pemeriksaan kejuruteraan I.C.E. dan stim di bawah FMA 1967','FMA 1967 下的内燃机与蒸汽工程检验')}</li>
        <li>{L(lang,'Energy management, project management and technical solutions','Pengurusan tenaga, pengurusan projek dan penyelesaian teknikal','能源管理、项目管理与技术支持')}</li>
        <li>{L(lang,'Land transportation services','Perkhidmatan pengangkutan darat','陆路运输服务')}</li>
        <li>{L(lang,'Drone aerial surveying and agricultural spraying','Tinjauan udara dron dan penyemburan pertanian','无人机航测与农业植保')}</li>
      </ul>
      <div class="table-wrap" style="margin-top:22px"><table style="min-width:0"><tbody>
        <tr><td>{L(lang,'Registered name','Nama berdaftar','注册名称')}</td><td>KSTS K. S. TECHNICAL SERVICES</td></tr>
        <tr><td>{L(lang,'Registration','Pendaftaran','注册号')}</td><td>MPS: R14722/2009</td></tr>
        <tr><td>{L(lang,'Status','Status','资质状态')}</td><td>{L(lang,'Syarikat Status Bumiputera Sabah · CIDB Registered Contractor','Syarikat Status Bumiputera Sabah · Kontraktor Berdaftar CIDB','沙巴土著企业 · CIDB 注册承包商')}</td></tr>
        <tr><td>{L(lang,'Base','Pangkalan','所在地')}</td><td>Kg. Nangoh, Telupid, Sabah</td></tr>
        <tr><td>{L(lang,'Coverage','Liputan','服务范围')}</td><td>{L(lang,'Sabah and Sarawak','Sabah dan Sarawak','沙巴与砂拉越')}</td></tr>
      </tbody></table></div>
    </div>
    <div>
      <p class="eyebrow">{L(lang,'Managing Director','Pengarah Urusan','董事总经理')}</p>
      <h2>Sdr. Leong Kian Sheng</h2>
      <p class="small" style="margin-bottom:16px">{L(lang,'Known as Alvin · B.E.Tech (Mechanical, USQ) · Eng Tech (BEM) · MIEM · AMIMechE · MMOSTA','Dikenali sebagai Alvin · B.E.Tech (Kejuruteraan Mekanikal, USQ) · Eng Tech (BEM) · MIEM · AMIMechE · MMOSTA','通称 Alvin（梁健成）· B.E.Tech 机械工程（南昆士兰大学）· Eng Tech (BEM) · MIEM · AMIMechE · MMOSTA')}</p>
      <p>{L(lang,
        'Alvin Leong has spent 22 years in the Sabah palm oil milling and plantation industry. He built his career at a palm oil mill in Sandakan (Kilang Kelapa Sawit Fortuna Sdn Bhd), rising from Assistant Mill Manager &amp; Project Engineer to head of operations and development, and now serves as Managing Director of KSTS. His work covers palm-based biomass watertube steam boiler operations for CHP generation, green technology development projects including palm biomass composting for pelletised fertiliser, three field ESP installations for air pollution control, and feasibility studies for POME biogas power generation.',
        'Alvin Leong telah menempuh 22 tahun dalam industri pengilangan kelapa sawit dan ladang di Sabah. Beliau membina kerjayanya di sebuah kilang kelapa sawit di Sandakan (Kilang Kelapa Sawit Fortuna Sdn Bhd), dari Penolong Pengurus Kilang &amp; Jurutera Projek sehingga mengetuai operasi dan pembangunan, dan kini berkhidmat sebagai Pengarah Urusan KSTS. Kerjanya merangkumi operasi dandang stim tiub air biomas berasaskan sawit untuk penjanaan CHP, projek pembangunan teknologi hijau termasuk pengkomposan biomas sawit untuk baja berbutir, tiga pemasangan ESP lapangan untuk kawalan pencemaran udara, dan kajian kemungkinan penjanaan kuasa biogas POME.',
        'Alvin Leong 在沙巴棕榈油压榨与种植业深耕 22 年：职业生涯起步于山打根一油厂（Kilang Kelapa Sawit Fortuna Sdn Bhd），从副厂长兼项目工程师做到运营与发展负责人，现任 KSTS 董事总经理。其工作涵盖棕榈基生物质水管蒸汽锅炉的 CHP 运行、绿色技术开发（棕榈生物质堆肥制颗粒肥）、3 套现场 ESP 大气污染控制系统，以及 POME 沼气发电可行性研究。')}</p>
      <div class="card" style="margin-top:18px">
        <h3 style="font-size:17px">{L(lang,'Registrations','Pendaftaran','法定资质')}</h3>
        <ul class="checks" style="margin-bottom:0">
          <li>{L(lang,'ECOS Certified Energy Manager (CEM) &amp; Registered Electrical Energy Manager (REEM)','Pengurus Tenaga Bertauliah ECOS (CEM) &amp; Pengurus Tenaga Elektrik Berdaftar (REEM)','ECOS 认证能源管理师（CEM）与注册电能管理师（REEM）')} <span class="small">EREEM-00016-2025</span></li>
          <li>{L(lang,'DOSH Registered 2nd Grade Internal Combustion Engine Engineer','Jurutera Enjin Pembakaran Dalam Gred 2 Berdaftar DOSH','DOSH 注册二级内燃机工程师')} <span class="small">JKKP/2024/EPD02/1322</span></li>
          <li>{L(lang,'DOSH Registered 2nd Grade Steam Engineer','Jurutera Stim Gred 2 Berdaftar DOSH','DOSH 注册二级蒸汽工程师')} <span class="small">JKKP/2024/JS02/1113</span></li>
          <li>{L(lang,'DOSH Certified OSH Coordinator','Penyelaras OSH Bertauliah DOSH','DOSH 认证职业安全健康协调员')} <span class="small">SB/21/OSHC/02/00512</span></li>
          <li>{L(lang,'BEM Registered Engineering Technologist (Manufacturing)','Teknolog Kejuruteraan Berdaftar BEM (Pembuatan)','BEM 注册工程技术师（制造）')} <span class="small">T10283</span></li>
          <li>{L(lang,'AER Registered ASEAN Engineering Technologist','Teknolog Kejuruteraan ASEAN Berdaftar AER','AER 注册东盟工程技术师')} <span class="small">AET0192</span></li>
          <li>{L(lang,'CIDB Registered Green Card Holder · ADMS Management &amp; IRWS Professional Engineer','Pemegang Kad Hijau Berdaftar CIDB · ADMS Management &amp; IRWS Professional Engineer','CIDB 注册绿卡 · ADMS 管理与 IRWS 专业工程师')}</li>
        </ul>
        <p class="small" style="margin:14px 0 0">{L(lang,'Drone operations: CAAM Certified Remote Pilot (B) &amp; AGRI (2).','Operasi dron: Juruterbang Dron Bertauliah CAAM (B) &amp; AGRI (2).','无人机作业：CAAM 认证驾驶员（B 类）与农业植保（2 类）。')}</p>
      </div>
      <div class="card" style="margin-top:18px">
        <h3 style="font-size:17px">{L(lang,'Education','Pendidikan','教育背景')}</h3>
        <div class="table-wrap"><table style="min-width:0"><tbody>
          <tr><td>2004</td><td>{L(lang,'University of Southern Queensland (Australia) — B.E.Tech, Mechanical Engineering','Universiti Southern Queensland (Australia) — B.E.Tech, Kejuruteraan Mekanikal','南昆士兰大学（澳大利亚）— 机械工程 工程技术学士')}</td></tr>
          <tr><td>2006</td><td>{L(lang,'Malaysian Palm Oil Board (MPOB) — Diploma, Palm Oil Mill Process &amp; Management','Lembaga Minyak Sawit Malaysia (MPOB) — Diploma, Proses &amp; Pengurusan Kilang Kelapa Sawit','马来西亚棕榈油局（MPOB）— 棕榈油厂工艺与管理文凭')}</td></tr>
          <tr><td>&mdash;</td><td>{L(lang,'NIOSH Malaysia — Occupational Safety and Health training','NIOSH Malaysia — latihan Keselamatan dan Kesihatan Pekerjaan','NIOSH 马来西亚 — 职业安全与卫生培训')}</td></tr>
        </tbody></table></div>
        <h3 style="font-size:17px;margin-top:18px">{L(lang,'Memberships','Keahlian','学会会员')}</h3>
        <ul class="checks" style="margin-bottom:0">
          <li>{L(lang,'IEM — Corporate Member No. 35532 (Mechanical), Sabah Branch, since 2009','IEM — Ahli Korporat No. 35532 (Mekanikal), Cawangan Sabah, sejak 2009','IEM 马来西亚工程师学会 — 正式会员 35532（机械专业，沙巴分会，2009 年入会）')}</li>
          <li>{L(lang,'AMIMechE — Associate Member, Institution of Mechanical Engineers (UK)','AMIMechE — Ahli Bersekutu, Institution of Mechanical Engineers (UK)','AMIMechE — 英国机械工程师学会准会员')}</li>
          <li>{L(lang,'MMOSTA — Malaysian Oil Scientists and Technologists Association','MMOSTA — Persatuan Saintis dan Teknolog Minyak Malaysia','MMOSTA — 马来西亚油料科学家与技术专家协会')}</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section id="press">
  <div class="wrap grid-2" style="gap:44px;align-items:center">
    <figure style="margin:0">
      <img src="{asset}assets/img/press-iem-sabah-cpd-2026.jpg" alt="Report on the IEM Sabah Branch CPD talk on palm oil mill biomass presented by Alvin Leong" loading="lazy" style="border:1px solid var(--line);border-radius:12px;box-shadow:0 10px 30px rgba(12,26,38,.10)">
      <figcaption class="small" style="margin-top:12px">{L(lang,
        'Report on the IEM Sabah Branch CPD talk, Kota Kinabalu.',
        'Laporan ceramah CPD IEM Cawangan Sabah, Kota Kinabalu.',
        'IEM 沙巴分会 CPD 讲座报道，亚庇。')}</figcaption>
      <img src="{asset}assets/img/press-iem-sabah-cpd-2026-zh.jpg" alt="Chinese-language report on the IEM Sabah Branch CPD talk, Asia Times Sabah edition, 23 August 2026" loading="lazy" style="margin-top:22px;border:1px solid var(--line);border-radius:12px;box-shadow:0 10px 30px rgba(12,26,38,.10)">
      <figcaption class="small" style="margin-top:12px">{L(lang,
        'Chinese-language report, Asia Times (Sabah edition), 23 August 2026.',
        'Laporan bahasa Cina, Asia Times (edisi Sabah), 23 Ogos 2026.',
        '中文报道：《亚洲时报》沙巴新闻 A10 版，2026 年 8 月 23 日。')}</figcaption>
    </figure>
    <div>
      <p class="eyebrow">{L(lang,'In the news','Dalam berita','媒体报道')}</p>
      <h2>{L(lang,
        'Invited to speak at the Institution of Engineers Malaysia, Sabah Branch',
        'Dijemput berucap di Institution of Engineers Malaysia, Cawangan Sabah',
        '受邀在马来西亚工程师学会沙巴分会主讲')}</h2>
      <p>{L(lang,
        'Alvin Leong was the speaker at the IEM Sabah Branch Continuing Professional Development talk, “Transforming Palm Oil Mill Biomass Wastes”, in Kota Kinabalu. The session covered cogeneration and Bio-CNG from palm kernel shells, palm fibre and POME, and the three constraints that decide whether a project actually gets built: securing a reliable biomass supply, the capital cost, and a long-term commercial arrangement.',
        'Alvin Leong ialah penceramah dalam ceramah Pembangunan Profesional Berterusan IEM Cawangan Sabah, “Transforming Palm Oil Mill Biomass Wastes”, di Kota Kinabalu. Sesi itu merangkumi kogenerasi dan Bio-CNG daripada tempurung isirung sawit, gentian sawit dan POME, serta tiga kekangan yang menentukan sama ada projek benar-benar dibina: bekalan biomas yang boleh dipercayai, kos modal, dan pengaturan komersial jangka panjang.',
        'Alvin Leong 在亚庇举行的 IEM（马来西亚工程师学会）沙巴分会持续专业发展（CPD）讲座担任主讲，题目为《Transforming Palm Oil Mill Biomass Wastes》。内容涵盖棕仁壳、棕纤维与 POME 的热电联产与 Bio-CNG 路线，以及决定项目能否落地的三项硬约束：生物质稳定供应、初始投资与长期商业安排。')}</p>
      <p>{L(lang,
        'Sabah has 129 active palm oil mills producing an estimated 25.75 million tonnes of biomass a year — the resource base behind every capacity we size.',
        'Sabah mempunyai 129 kilang kelapa sawit aktif yang menghasilkan kira-kira 25.75 juta tan biomas setahun — asas sumber bagi setiap kapasiti yang kami kira.',
        '沙巴现有 129 家运营中的棕榈油厂，每年产生约 2,575 万吨生物质——这就是我们做容量测算的资源底盘。')}</p>
    </div>
  </div>
</section>

<section class="alt" id="partner">
  <div class="wrap">
    <div class="sec-head"><p class="eyebrow">{L(lang,'Technology partner','Rakan teknologi','技术伙伴')}</p>
      <h2>{L(lang,'SINOPEC Dalian Research Institute of Petroleum and Petrochemicals','Institut Penyelidikan Petroleum dan Petrokimia Dalian SINOPEC','中国石化大连研究院')}</h2>
      <p class="lead">{L(lang,
        'Engineering, gas engines and upgrading equipment come from a Chinese manufacturer with an export track record. KSTS is the in-country partner: site data, permitting, civil works, installation, statutory inspection and operations.',
        'Kejuruteraan, enjin gas dan peralatan peningkatan datang dari pengeluar China dengan rekod eksport. KSTS ialah rakan dalam negara: data tapak, kebenaran, kerja awam, pemasangan, pemeriksaan berkanun dan operasi.',
        '工程、燃气机组与提纯设备来自有出口业绩的中国制造商。KSTS 是本地伙伴：现场数据、审批、土建、安装、法定检验与运维。')}</p></div>
    <div class="table-wrap">
      <table>
        <thead><tr><th>{L(lang,'Function','Fungsi','职能')}</th><th>KSTS (Malaysia)</th><th>{L(lang,'Technology partner (China)','Rakan teknologi (China)','技术伙伴（中国）')}</th></tr></thead>
        <tbody>
          <tr><td>{L(lang,'Site survey &amp; gas measurement','Tinjauan tapak &amp; pengukuran gas','现场勘察与气量实测')}</td><td>{L(lang,'Yes','Ya','是')}</td><td>{L(lang,'Protocol and interpretation','Protokol dan tafsiran','测试方案与解读')}</td></tr>
          <tr><td>{L(lang,'Process design &amp; gas balance','Reka proses &amp; imbangan gas','工艺设计与气量平衡')}</td><td>{L(lang,'Review','Semakan','审核')}</td><td>{L(lang,'Yes','Ya','是')}</td></tr>
          <tr><td>{L(lang,'Equipment manufacture','Pembuatan peralatan','设备制造')}</td><td>—</td><td>{L(lang,'Yes','Ya','是')}</td></tr>
          <tr><td>{L(lang,'Civil / mechanical execution','Pelaksanaan awam / mekanikal','土建／机装施工')}</td><td>{L(lang,'Yes (CIDB)','Ya (CIDB)','是（CIDB）')}</td><td>{L(lang,'Supervision','Penyeliaan','监督')}</td></tr>
          <tr><td>{L(lang,'Commissioning &amp; DOSH witness','Pentauliahan &amp; saksi DOSH','调试与 DOSH 见证')}</td><td>{L(lang,'Yes','Ya','是')}</td><td>{L(lang,'Engineer on site','Jurutera di tapak','工程师到场')}</td></tr>
          <tr><td>O&amp;M</td><td>{L(lang,'Yes','Ya','是')}</td><td>{L(lang,'Remote diagnostics, spares','Diagnostik jauh, alat ganti','远程诊断与备件')}</td></tr>
        </tbody>
      </table>
    </div>
    <div class="grid-3" style="margin-top:30px">
      <div class="card"><p class="tag">{L(lang,'Why it matters','Mengapa penting','为什么重要')}</p><h3>{L(lang,'One accountable chain','Satu rantaian bertanggungjawab','一条责任链')}</h3><p>{L(lang,'Gas quality, engine warranty and civil works meet at one interface.','Kualiti gas, waranti enjin dan kerja awam bertemu di satu antara muka.','气质、机组质保与土建在一个界面上对接。')}</p></div>
      <div class="card"><p class="tag">{L(lang,'Why it matters','Mengapa penting','为什么重要')}</p><h3>{L(lang,'Local statutory knowledge','Pengetahuan berkanun tempatan','本地法规经验')}</h3><p>{L(lang,'FMA 1967 inspections, DOSH and ECOS reporting handled by the design team.','Pemeriksaan FMA 1967, pelaporan DOSH dan ECOS dikendalikan pasukan reka bentuk.','FMA 1967 检验、DOSH 与 ECOS 报告由设计团队自己处理。')}</p></div>
      <div class="card"><p class="tag">{L(lang,'Why it matters','Mengapa penting','为什么重要')}</p><h3>{L(lang,'Factory-backed pricing','Harga disokong kilang','工厂直供价格')}</h3><p>{L(lang,'Direct supply, typically 25–35% below European equipment pricing.','Bekalan terus, biasanya 25–35% lebih rendah daripada harga peralatan Eropah.','直供价格通常比欧洲设备低 25–35%。')}</p></div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-head"><p class="eyebrow">{L(lang,'How we work','Cara kami bekerja','我们怎么干')}</p><h2>{L(lang,'Four steps, no surprises','Empat langkah, tanpa kejutan','四步走，不埋雷')}</h2></div>
    <div class="grid-4">
      <div class="card"><p class="tag">{L(lang,'Step 1','Langkah 1','第 1 步')}</p><h3>{L(lang,'Data','Data','数据')}</h3><p>{L(lang,'Throughput, pond volume, one to two weeks of gas data, tariff and load profile.','Kemampuan, isipadu kolam, satu hingga dua minggu data gas, tarif dan profil beban.','处理量、池塘容积、1–2 周气量数据、电价与负荷曲线。')}</p></div>
      <div class="card"><p class="tag">{L(lang,'Step 2','Langkah 2','第 2 步')}</p><h3>{L(lang,'Pre-feasibility','Pra-kelayakan','预可研')}</h3><p>{L(lang,'Gas balance, recommended capacity, indicative capex and opex, payback range. Free of charge.','Imbangan gas, kapasiti disyorkan, capex dan opex indikatif, julat pulangan. Percuma.','气量平衡、推荐容量、投资与运维区间、回收期区间。免费。')}</p></div>
      <div class="card"><p class="tag">{L(lang,'Step 3','Langkah 3','第 3 步')}</p><h3>{L(lang,'Engineering','Kejuruteraan','工程设计')}</h3><p>{L(lang,'P&amp;ID, GA drawings, equipment selection, firm quotation and commercial model.','P&amp;ID, lukisan GA, pemilihan peralatan, sebut harga tetap dan model komersial.','P&amp;ID、总图、设备选型、正式报价与商务模式。')}</p></div>
      <div class="card"><p class="tag">{L(lang,'Step 4','Langkah 4','第 4 步')}</p><h3>{L(lang,'Delivery','Pelaksanaan','交付')}</h3><p>{L(lang,'Supply, install, commission, DOSH witness, training, then O&amp;M if required.','Bekal, pasang, tauliah, saksi DOSH, latihan, kemudian O&amp;M jika perlu.','供货、安装、调试、DOSH 见证、培训，需要时接管运维。')}</p></div>
    </div>
  </div>
</section>
"""


def contact(lang):
    return f"""
<section class="page-head">
  <div class="wrap">
    <p class="eyebrow">{L(lang,'Contact','Hubungi','联系我们')}</p>
    <h1>{L(lang,'Send mill data, get a capacity','Hantar data kilang, dapat kapasiti','发油厂数据，得到容量结论')}</h1>
    <p class="lead">{L(lang,
      'The fastest route to a useful answer is measured gas data. If you do not have it yet, send throughput and pond volume — we will tell you what to measure and for how long.',
      'Laluan terpantas kepada jawapan berguna ialah data gas yang diukur. Jika belum ada, hantar kemampuan dan isipadu kolam — kami akan beritahu apa perlu diukur dan berapa lama.',
      '最快得到有用答案的方式是实测气量数据。如果还没有，先发处理量与池塘容积，我们告诉你该测什么、测多久。')}</p>
  </div>
</section>

<section>
  <div class="wrap grid-2" style="gap:56px;align-items:start">
    <div>
      <form class="enquiry" action="https://formsubmit.co/k.s.t.s_sabah@hotmail.com" method="POST">
        <input type="hidden" name="_subject" value="Website enquiry — KSTS bioenergy">
        <input type="hidden" name="_captcha" value="false">
        <div><label class="small" for="name">{L(lang,'Name','Nama','姓名')}</label><input id="name" name="name" required></div>
        <div><label class="small" for="company">{L(lang,'Company / mill','Syarikat / kilang','公司／油厂')}</label><input id="company" name="company"></div>
        <div><label class="small" for="email">Email</label><input id="email" name="email" type="email" required></div>
        <div><label class="small" for="phone">{L(lang,'Phone / WhatsApp','Telefon / WhatsApp','电话／WhatsApp')}</label><input id="phone" name="phone"></div>
        <div class="full"><label class="small" for="site">{L(lang,'Site data','Data tapak','现场数据')}</label><textarea id="site" name="site" placeholder="{L(lang,'FFB t/h · operating days · POME pond stages and volume · measured biogas Nm³/h and CH₄ % · H₂S ppm · tariff or diesel price · grid status · boiler fuel and steam demand','FFB t/j · hari operasi · peringkat dan isipadu kolam POME · biogas Nm³/j dan CH₄ % · H₂S ppm · tarif atau harga diesel · status grid · bahan api dandang dan keperluan stim','FFB t/h · 运行天数 · POME 池塘级数与容积 · 实测沼气 Nm³/h 与甲烷% · 硫化氢 ppm · 电价或柴油价 · 并网条件 · 锅炉燃料与蒸汽量')}"></textarea></div>
        <div class="full"><label class="small" for="interest">{L(lang,'Interest','Minat','意向')}</label>
          <select id="interest" name="interest">
            <option>{L(lang,'Biogas to power (electricity and heat)','Biogas ke kuasa (elektrik dan haba)','沼气发电（电与热）')}</option>
            <option>{L(lang,'Biomethane for boiler fuel','Biometana untuk bahan api dandang','生物天然气供锅炉')}</option>
            <option>{L(lang,'Bio-CNG / virtual pipeline','Bio-CNG / saluran maya','Bio-CNG / 虚拟管网')}</option>
            <option>{L(lang,'Equipment supply only','Bekalan peralatan sahaja','仅设备供货')}</option>
            <option>{L(lang,'BOO / shared savings','BOO / perkongsian penjimatan','BOO / 合同能源管理')}</option>
          </select>
        </div>
        <div class="full"><button class="btn" type="submit">{L(lang,'Send enquiry','Hantar pertanyaan','提交询价')}</button></div>
      </form>
      <p class="small" style="margin-top:14px">{L(lang,'The form is delivered by email. Prefer to write directly?','Borang dihantar melalui e-mel. Lebih suka tulis terus?','表单通过邮件送达。也可直接写信：')} <a href="mailto:k.s.t.s_sabah@hotmail.com">k.s.t.s_sabah@hotmail.com</a></p>
    </div>
    <div>
      <div class="card">
        <h3>{L(lang,'Malaysia — KSTS','Malaysia — KSTS','马来西亚 — KSTS')}</h3>
        <div class="kv" style="color:var(--ink);border-color:var(--line)"><span class="muted">{L(lang,'Contact','Hubungi','联系人')}</span><b>Sdr. Leong Kian Sheng (Alvin)</b></div>
        <div class="kv" style="color:var(--ink);border-color:var(--line)"><span class="muted">Email</span><b><a href="mailto:k.s.t.s_sabah@hotmail.com">k.s.t.s_sabah@hotmail.com</a></b></div>
        <div class="kv" style="color:var(--ink);border-color:var(--line)"><span class="muted">{L(lang,'Phone','Telefon','电话')}</span><b><a href="tel:+60138833833">+60 13-883 3833</a></b></div>
        <div class="kv" style="color:var(--ink);border:0"><span class="muted">{L(lang,'Address','Alamat','地址')}</span><b style="font-weight:600;text-align:right">Kg. Nangoh, NT 083017181 (Lot 2),<br>34 km Off Jalan Simpang Sapi Nangoh,<br>Labuk–Sugut, Telupid, Sabah</b></div>
      </div>
      <div class="card" style="margin-top:20px">
        <h3>{L(lang,'What happens next','Apa berlaku seterusnya','接下来')}</h3>
        <ul class="checks">
          <li>{L(lang,'We review the data and reply within three working days','Kami semak data dan balas dalam tiga hari bekerja','三个工作日内审阅并回复')}</li>
          <li>{L(lang,'You get a gas balance, capacity and indicative budget','Anda dapat imbangan gas, kapasiti dan bajet indikatif','你会得到气量平衡、容量建议与预算区间')}</li>
          <li>{L(lang,'If a site visit is needed for gas measurement, we say so up front','Jika lawatan tapak diperlukan untuk ukuran gas, kami nyatakan di awal','如需现场实测，我们会提前说明')}</li>
        </ul>
      </div>
      <div class="card" style="margin-top:20px">
        <h3>{L(lang,'Trade terms','Terma dagang','商务条款')}</h3>
        <p class="small" style="margin:0">{L(lang,'Quotations in USD or MYR. English documentation, GA drawings, test reports and O&amp;M manuals with every plant. CIF Kota Kinabalu or Sandakan, or delivered to site.','Sebut harga dalam USD atau MYR. Dokumentasi Inggeris, lukisan GA, laporan ujian dan manual O&amp;M dengan setiap loji. CIF Kota Kinabalu atau Sandakan, atau dihantar ke tapak.','报价以美元或马币计。随每套设备提供英文文件、总图、测试报告与运维手册。CIF 亚庇或山打根，或送货到现场。')}</p>
      </div>
    </div>
  </div>
</section>
"""
