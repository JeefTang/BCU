/* KSTS · on-site consultation widget (BCU site)
   Layer 1: offline knowledge base (built from the site's own published figures)
   Layer 2: optional LLM endpoint (assets/data/chat-config.json -> endpoint)
   Layer 3: escalate to the KSTS desk (stored in the relay DB, pushed to the owner) */
(function () {
  "use strict";
  var LANG = (document.documentElement.lang || "en").toLowerCase();
  var ZH = LANG.indexOf("zh") === 0;
  var MS = LANG.indexOf("ms") === 0;

  var T = ZH ? {
    btn: "在线咨询",
    title: "KSTS 技术咨询",
    sub: "工程师在线 · 三个工作日内回复",
    ph: "描述你的工况：压榨量、池塘容积、气量、甲烷含量…",
    note: "自动应答仅供参考，正式方案以现场数据与工程师确认为准",
    greet: "你好，我是 KSTS 的沼气技术咨询助手。\n可以帮你：估算发电规模、判断该走发电还是提纯、查设备范围与价格区间、说明气体净化要求。\n最快的方式是告诉我：油厂压榨量（t/h FFB）、池塘容积、实测沼气流量与甲烷含量。",
    chips: ["油厂能发多大电", "沼气发电 vs 提纯", "氢能热电联供价格", "联系工程师"],
    human: "转工程师",
    escTitle: "留下联系方式，KSTS 工程师三个工作日内回复",
    escName: "姓名（选填）",
    escMail: "邮箱或电话（必填）",
    escBtn: "发送并等待回复",
    escOk: "已收到，工程师会尽快联系你。",
    escFail: "发送失败，请直接发邮件到 ",
    escAlt: "或直接发邮件：",
    typing: "正在输入",
    errNet: "网络不可用，已切换为本地知识库回答。",
    waitHuman: "已转给 KSTS 工程师。你继续在这里留言即可，回复会直接显示在这个窗口。",
    handoff: "已通知工程师，请稍等。",
    humanTag: "工程师",
    aiPaused: "工程师已收到你的留言，稍后在这里回复。",
    humanBtn: "转人工"
  } : MS ? {
    btn: "Tanya jurutera",
    title: "KSTS · pertanyaan teknikal",
    sub: "Jurutera dalam talian · balasan dalam 3 hari bekerja",
    ph: "Terangkan keadaan: kadar kilang, isipadu kolam, aliran gas, kandungan CH₄…",
    note: "Jawapan automatik adalah indikatif — pemilihan muktamad disahkan oleh jurutera",
    greet: "Helo — saya pembantu teknikal KSTS untuk projek biogas.\nSaya boleh anggar saiz loji, bandingkan jana kuasa dengan peningkatan biometana, terangkan julat peralatan dan harga indikatif, serta syarat kualiti gas.\nCara terpantas: beri saya kadar kilang (t/j FFB), isipadu kolam, aliran biogas dan kandungan metana.",
    chips: ["Berapa kW untuk kilang saya", "Jana kuasa vs biometana", "Harga CHP hidrogen", "Hubungi jurutera"],
    human: "Hubungi jurutera",
    escTitle: "Tinggalkan kontak — jurutera KSTS membalas dalam 3 hari bekerja",
    escName: "Nama (pilihan)",
    escMail: "E-mel atau telefon (wajib)",
    escBtn: "Hantar dan tunggu balasan",
    escOk: "Diterima. Jurutera akan menghubungi anda tidak lama lagi.",
    escFail: "Penghantaran gagal — sila e-mel ",
    escAlt: "Atau e-mel terus: ",
    typing: "menaip",
    errNet: "Rangkaian tiada — dijawab daripada pangkalan pengetahuan tempatan.",
    waitHuman: "Telah dipindahkan kepada jurutera KSTS. Teruskan menulis di sini — balasan muncul dalam tetingkap ini.",
    handoff: "Jurutera dimaklumkan, sekejap.",
    humanTag: "Jurutera",
    aiPaused: "Jurutera kami telah menerima mesej anda dan akan membalas di sini.",
    humanBtn: "Hubungi manusia"
  } : {
    btn: "Ask an engineer",
    title: "KSTS technical chat",
    sub: "Engineers online · replies within three working days",
    ph: "Describe the site: mill throughput, pond volume, gas flow, methane…",
    note: "Automated answers are indicative — final scope is confirmed by an engineer",
    greet: "Hello — I answer technical questions for KSTS biogas projects.\nI can estimate plant size, tell you whether power generation or biomethane fits better, quote the equipment range and indicative prices, and explain gas-quality limits.\nFastest way: give me mill throughput (t/h FFB), pond volume, measured biogas flow and methane content.",
    chips: ["How much power for my mill", "Power vs biomethane", "Hydrogen CHP price", "Talk to an engineer"],
    human: "Talk to an engineer",
    escTitle: "Leave your contact — a KSTS engineer replies within three working days",
    escName: "Name (optional)",
    escMail: "Email or phone (required)",
    escBtn: "Send and wait for a reply",
    escOk: "Received. An engineer will contact you shortly.",
    escFail: "Send failed — please email ",
    escAlt: "Or email directly: ",
    typing: "typing",
    errNet: "Network unavailable — answered from the local knowledge base.",
    waitHuman: "Passed to our engineer. Keep writing here — the reply appears in this window.",
    handoff: "Engineer notified, one moment.",
    humanTag: "Engineer",
    aiPaused: "Our engineer has your message and will reply here shortly.",
    humanBtn: "Talk to a human"
  };

  var EMAIL = "k.s.t.s_sabah@hotmail.com";
  var PHONE = "+60 13-883 3833";

  /* ---------------------------------------------------------------- knowledge base
     Every figure below is taken from this website. Do not add unverified numbers. */
  var KB = [
    { id: "range", k: ["range", "capacity", "how much power", "max power", "size", "规格", "容量", "多大", "能发多少", "范围", "julat", "saiz"],
      en: "Gas engines: 300 kW to 2 MW electrical, 415 V / 50 Hz (11 kV option at 2 MW).\nHydrogen CHP (fuel cell): 7.5 to 100 kW.\nBiomethane upgrading: from a few hundred to 1,500 Nm³/h of raw biogas; the reference case is 500 Nm³/h at 60% CH₄.\nTell me your mill throughput or measured gas flow and I will point to the right size.",
      ms: "Enjin gas: 300 kW hingga 2 MW elektrik, 415 V / 50 Hz (pilihan 11 kV pada 2 MW).\nCHP hidrogen (sel bahan api): 7.5 hingga 100 kW.\nPeningkatan biometana: daripada beberapa ratus hingga 1,500 Nm³/j biogas mentah; kes rujukan 500 Nm³/j pada 60% CH₄.\nBeritahu kadar kilang atau aliran gas yang diukur, saya tunjukkan saiz yang sesuai.",
      zh: "燃气机组：300 kW – 2 MW 电功率，415 V / 50 Hz（2 MW 可选 11 kV）。\n氢能热电联供（燃料电池）：7.5 – 100 kW。\n生物天然气提纯：几百到 1,500 Nm³/h 原沼气；参考案例为 500 Nm³/h、60% 甲烷。\n告诉我压榨量或实测气量，我直接给对应规模。" },

    { id: "sizing", k: ["how much gas", "gas per kw", "nm3", "sizing", "how many kw", "气量", "每千瓦", "选型", "多少气", "berapa gas", "saiz"],
      en: "At 60% CH₄ and 38–40% electrical efficiency, one cubic metre of biogas carries about 2.2 kWh of electricity.\nTypical gas demand at 60% CH₄: 300 kW → 132–140 Nm³/h; 600 kW → 265–280; 1,000 kW → 441–466; 2,000 kW → 883–932 Nm³/h.\nThe engineering calculator on this site does the arithmetic — open Engineering Tools, or send me the numbers.",
      ms: "Pada 60% CH₄ dan kecekapan elektrik 38–40%, satu meter padu biogas membawa kira-kira 2.2 kWh elektrik.\nKeperluan gas biasa pada 60% CH₄: 300 kW → 132–140 Nm³/j; 600 kW → 265–280; 1,000 kW → 441–466; 2,000 kW → 883–932 Nm³/j.\nKalkulator kejuruteraan di laman ini boleh mengiranya — buka Alat Kejuruteraan, atau beri saya angkanya.",
      zh: "按 60% 甲烷、38–40% 发电效率，1 m³ 沼气约含 2.2 kWh 电。\n60% 甲烷下的典型气耗：300 kW → 132–140 Nm³/h；600 kW → 265–280；1,000 kW → 441–466；2,000 kW → 883–932 Nm³/h。\n站上工程计算器可以直接算——打开「工程测算工具」，或把数据发我。" },

    { id: "engine", k: ["engine", "genset", "efficiency", "机组", "效率", "发电效率", "enjin", "kecekapan"],
      en: "Gas engine electrical efficiency: 36–38% at 300 kW, about 35.2% at 500–1,000 kW, 39–42% at 1.5–2 MW.\nThese figures come from manufacturer gas consumption of roughly 3.50 kWh per Nm³ CH₄ — deliberately lower than the 38–40% sometimes quoted for Chinese units.\nHeat recovery adds about 330 kW at 300 kW, 560 kW at 500 kW, 680 kW at 600 kW, 1,700 kW at 1.5 MW.",
      ms: "Kecekapan elektrik enjin gas: 36–38% pada 300 kW, kira-kira 35.2% pada 500–1,000 kW, 39–42% pada 1.5–2 MW.\nAngka ini daripada penggunaan gas pengeluar kira-kira 3.50 kWh per Nm³ CH₄ — sengaja lebih rendah daripada 38–40% yang kadang-kadang disebut untuk unit China.\nPemulihan haba menambah kira-kira 330 kW pada 300 kW, 560 kW pada 500 kW, 680 kW pada 600 kW, 1,700 kW pada 1.5 MW.",
      zh: "燃气机发电效率：300 kW 为 36–38%，500–1,000 kW 约 35.2%，1.5–2 MW 为 39–42%。\n数据取自厂家气耗约 3.50 kWh/Nm³ 甲烷——刻意低于中国机组常被标称的 38–40%。\n余热回收：300 kW 约 330 kW 热，500 kW 约 560 kW，600 kW 约 680 kW，1.5 MW 约 1,700 kW。" },

    { id: "bdfg", k: ["bdfg", "doubly fed", "brushless", "variable speed", "双馈", "无刷", "变速", "两台两速", "dua suapan"],
      en: "Brushless doubly-fed generator (optional): no brushes, no slip rings — nothing to replace on a service interval and no carbon dust beside the gas train.\nSpeed can swing about ±30% while terminals stay at 415 V / 50 Hz, so the engine follows the gas instead of tripping when the pond is lean.\nOnly slip power passes through the converter (25–30% of rating) instead of the full 100%.\nThe same machine motors: it rolls the engine to ignition speed, gives soft synchronising, can act as a synchronous condenser and black-start.\nBoundary: motoring is starting, barring and light-drive duty — not continuous full-torque drive; a larger converter is priced per project.",
      ms: "Penjana dua-suapan tanpa berus (pilihan): tiada berus, tiada gelang slip — tiada apa untuk diganti pada selang servis dan tiada habuk karbon di sebelah train gas.\nKelajuan boleh berubah kira-kira ±30% sementara terminal kekal 415 V / 50 Hz, jadi enjin mengikut gas dan tidak trip apabila kolam lemah.\nHanya kuasa slip melalui penukar (25–30% daripada kadaran) bukan 100% penuh.\nMesin yang sama boleh bermotor: memutar enjin ke kelajuan penyalaan, penyegerakan lembut, bertindak sebagai kondenser segerak dan black start.\nHad: operasi motor hanya untuk permulaan, barring dan panduan ringan — bukan pemanduan tork penuh berterusan; penukar lebih besar dinilai per projek.",
      zh: "无刷双馈发电机（选配）：无电刷、无滑环——没有定期更换件，也没有碳粉落在气路上。\n转速可在约 ±30% 内变化而端电压/频率保持 415 V / 50 Hz，气量低时降速运行而不是跳机。\n变流器只走转差功率（额定的 25–30%），不是全功率 100%。\n同一台机还能电动：把燃气机拖到点火转速、软同期、停机当调相机、可黑启动。\n边界：电动只定位在启动、盘车与轻载拖动，不是满转矩长期驱动；大转差需加大变流器，按项目单独报价。" },

    { id: "gasquality", k: ["h2s", "sulphur", "sulfur", "dew point", "gas quality", "pressure", "脱硫", "硫化氢", "气quality", "气体质量", "kualiti gas", "tekanan"],
      en: "Engine inlet specification: methane ≥50% (design 55–65%); H₂S ≤200 ppm, target ≤100; water dew point ≤10 °C above ambient; gas temperature ≤40 °C; inlet pressure 5–15 kPa ±1; fluctuation ≤10% per minute.\nThe most common mistake is accepting raw POME gas at 2,000–4,000 ppm H₂S: it halves lube-oil life and doubles maintenance cost, invisibly, until the first overhaul.",
      ms: "Spesifikasi masuk enjin: metana ≥50% (reka bentuk 55–65%); H₂S ≤200 ppm, sasaran ≤100; titik embun air ≤10 °C di atas ambien; suhu gas ≤40 °C; tekanan masuk 5–15 kPa ±1; turun naik ≤10% seminit.\nKesilapan paling biasa ialah menerima gas POME mentah pada 2,000–4,000 ppm H₂S: ia mengurangkan hayat minyak pelincir separuh dan menggandakan kos penyelenggaraan, tanpa disedari, sehingga overhaul pertama.",
      zh: "机组进气规范：甲烷 ≥50%（设计 55–65%）；H₂S ≤200 ppm，目标 ≤100；水露点 ≤环境温度+10 °C；进气温度 ≤40 °C；进气压力 5–15 kPa ±1；压力波动 ≤10%/分钟。\n最常见的错误是接受 2,000–4,000 ppm H₂S 的原沼气：机油寿命减半、维护成本翻倍，而且直到第一次大修前都看不出来。" },

    { id: "chain", k: ["process", "treatment", "desulfurisation", "flare", "cover", "cstr", "工艺", "脱硫", "覆盖", "净化", "proses", "rawatan"],
      en: "Six stages, one gas specification: capture (covered lagoon or CSTR, condensate traps, headers) → buffer gas holder → desulfurisation (biological scrubber plus iron-oxide polishing) → conditioning (chilling, coalescing, blower to engine pressure) → generation (island or parallel) → heat recovery (jacket water ~90 °C and exhaust to hot water or steam).\nWe supply the chain as one scope with one party accountable for gas quality at the engine inlet.",
      ms: "Enam peringkat, satu spesifikasi gas: penangkapan (kolam bertutup atau CSTR, perangkap kondensat, header) → penampan gas holder → nyahsulfur (scrubber biologi plus penggilap oksida besi) → pengkondisian (penyejukan, coalescing, blower ke tekanan enjin) → penjanaan (pulau atau selari) → pemulihan haba (air jaket ~90 °C dan ekzos ke air panas atau stim).\nKami membekalkan rantaian ini sebagai satu skop dengan satu pihak bertanggungjawab atas kualiti gas di masuk enjin.",
      zh: "六个环节、一个气体规范：收集（覆盖塘或 CSTR、冷凝水捕集、集气总管）→ 缓冲气柜 → 脱硫（生物脱硫+氧化铁精脱）→ 净化（降温、除雾、增压至机组进气压力）→ 发电（孤网或并网）→ 余热回收（缸套水约 90 °C 与烟气制热水或蒸汽）。\n我们按一个供货范围交付整条链，并对机组进气质量负责。" },

    { id: "biomethane", k: ["biomethane", "upgrade", "upgrading", "bio-cng", "biocng", "cng", "提纯", "生物天然气", "biometana", "peningkatan"],
      en: "Upgrading takes 60% biogas to ≥97% CH₄: desulfurise → compress → dry → remove CO₂ (PSA, water scrubbing or membrane) → deliver to the burner or 250 bar for tube-trailer bio-CNG.\nGuaranteed gas: CH₄ ≥97% (96–99% adjustable), CO₂ ≤2–3%, H₂S ≤5 ppm, water dew point ≤−40 °C at pressure, O₂ ≤0.5%.\nIf the mill boiler runs on diesel, LPG or natural gas, replacing that fuel is often the fastest payback — not electricity.",
      ms: "Peningkatan membawa biogas 60% ke ≥97% CH₄: nyahsulfur → mampat → kering → buang CO₂ (PSA, scrubber air atau membran) → hantar ke pembakar atau 250 bar untuk bio-CNG treler tiub.\nGas dijamin: CH₄ ≥97% (boleh laras 96–99%), CO₂ ≤2–3%, H₂S ≤5 ppm, titik embun air ≤−40 °C pada tekanan, O₂ ≤0.5%.\nJika dandang kilang menggunakan diesel, LPG atau gas asli, menggantikan bahan api itu selalunya pulangan terpantas — bukan elektrik.",
      zh: "提纯把 60% 沼气做到 ≥97% 甲烷：脱硫 → 压缩 → 干燥 → 脱碳（PSA、水洗或膜分离）→ 送锅炉燃烧器，或 250 bar 装管束车做 Bio-CNG。\n保证气质：CH₄ ≥97%（可在 96–99% 调整）、CO₂ ≤2–3%、H₂S ≤5 ppm、带压水露点 ≤−40 °C、O₂ ≤0.5%。\n如果油厂锅炉烧柴油、LPG 或天然气，把那份燃料换掉，往往比发电回本更快。" },

    { id: "techsel", k: ["psa", "water scrubbing", "membrane", "which technology", "水洗", "膜", "选哪种", "teknologi"],
      en: "No universal best choice — it depends on gas volume, purity, power cost and space.\nPSA: 96–98% CH₄, recovery 95–98%, 0.25–0.30 kWh/Nm³, medium footprint, best at 200–1,500 Nm³/h.\nWater scrubbing: 97–99% CH₄, recovery 98–99%, 0.20–0.30 kWh/Nm³, large footprint, best for large plants.\nMembrane: 96–98% CH₄, recovery 96–99%, 0.20–0.28 kWh/Nm³, small skid footprint.",
      ms: "Tiada pilihan terbaik sejagat — bergantung pada isipadu gas, ketulenan, kos kuasa dan ruang.\nPSA: 96–98% CH₄, pemulihan 95–98%, 0.25–0.30 kWh/Nm³, ruang sederhana, terbaik pada 200–1,500 Nm³/j.\nScrubber air: 97–99% CH₄, pemulihan 98–99%, 0.20–0.30 kWh/Nm³, ruang besar, terbaik untuk loji besar.\nMembran: 96–98% CH₄, pemulihan 96–99%, 0.20–0.28 kWh/Nm³, skid kecil.",
      zh: "没有通用最优解，要看气量、纯度要求、电价和占地。\nPSA：96–98% 甲烷，回收率 95–98%，0.25–0.30 kWh/Nm³，占地中等，适合 200–1,500 Nm³/h。\n水洗：97–99% 甲烷，回收率 98–99%，0.20–0.30 kWh/Nm³，占地大，适合大型站。\n膜分离：96–98% 甲烷，回收率 96–99%，0.20–0.28 kWh/Nm³，撬装占地小。" },

    { id: "hchp", k: ["hydrogen", "fuel cell", "chp", "氢能", "燃料电池", "热电联供", "hidrogen", "sel bahan api"],
      en: "Hydrogen CHP, 7.5–100 kW: bottled 97% biomethane — or raw 60% biogas with an integrated purification front end — is reformed on site to hydrogen and converted by a fuel cell.\nOutput: 42% electricity (guaranteed, LHV), 43% recoverable heat at 60–70 °C, 0.24 Nm³ fuel per kWh sent out, total efficiency about 85%.\nNo flame at the point of use: about 55 dB(A), NOx = 0, SOx = 0, particulates = 0, water is the only by-product.\nIt competes with diesel at RM 0.90–1.30/kWh in off-grid Sabah, not with the subsidised grid tariff.",
      ms: "CHP hidrogen, 7.5–100 kW: biometana 97% dalam botol — atau biogas mentah 60% dengan penulenan bersepadu di hadapan — dibentuk semula di tapak menjadi hidrogen dan ditukar oleh sel bahan api.\nOutput: 42% elektrik (dijamin, LHV), 43% haba boleh pulih pada 60–70 °C, 0.24 Nm³ bahan api per kWh keluar, jumlah kecekapan kira-kira 85%.\nTiada nyalaan di tempat guna: kira-kira 55 dB(A), NOx = 0, SOx = 0, zarah = 0, air satu-satunya hasil sampingan.\nIa bersaing dengan diesel pada RM 0.90–1.30/kWh di Sabah luar grid, bukan tarif grid bersubsidi.",
      zh: "氢能热电联供 7.5–100 kW：瓶装 97% 生物天然气，或 60% 原沼气配一体化前端净化，现场重整制氢，由燃料电池转换。\n输出：42% 电（LHV 保证）、43% 可回收 60–70 °C 热水、每送出 1 kWh 耗 0.24 Nm³ 燃料，综合效率约 85%。\n使用点无明火：约 55 dB(A)，NOx = 0、SOx = 0、粉尘 = 0，唯一副产物是水。\n它对标的是沙巴离网柴油电价的 RM 0.90–1.30/kWh，不是补贴后的电网电价。" },

    { id: "hchp_price", k: ["price", "cost", "how much", "rm", "budget", "价格", "多少钱", "报价", "harga", "kos"],
      en: "Published FOB prices:\nHydrogen CHP — RM 10,000/kW for bottled 97% biomethane, RM 19,500/kW for raw 60% biogas with integrated purification (installation excluded). Examples: 10 kW → RM 100,000 / RM 195,000; 50 kW → RM 500,000 / RM 975,000; 100 kW → RM 1,000,000 / RM 1,950,000.\nGas engines, upgrading plants and bio-CNG are quoted per site from gas data — the site does not publish those prices. Send flow, methane content and H₂S and you get a budgetary number.",
      ms: "Harga FOB yang diterbitkan:\nCHP hidrogen — RM 10,000/kW untuk biometana 97% dalam botol, RM 19,500/kW untuk biogas mentah 60% dengan penulenan bersepadu (pemasangan tidak termasuk). Contoh: 10 kW → RM 100,000 / RM 195,000; 50 kW → RM 500,000 / RM 975,000; 100 kW → RM 1,000,000 / RM 1,950,000.\nEnjin gas, loji peningkatan dan bio-CNG dinilai per tapak daripada data gas — laman ini tidak menerbitkan harga tersebut. Hantar aliran, kandungan metana dan H₂S untuk angka anggaran.",
      zh: "站上公开的 FOB 价格：\n氢能热电联供——瓶装 97% 生物天然气 RM 10,000/kW；60% 原沼气含一体化净化 RM 19,500/kW（不含安装）。示例：10 kW → RM 10 万 / 19.5 万；50 kW → RM 50 万 / 97.5 万；100 kW → RM 100 万 / 195 万。\n燃气机组、提纯站、Bio-CNG 按现场气价单独报价，站上不公布——给气量、甲烷含量与 H₂S，我们回预算价。" },

    { id: "om", k: ["o&m", "maintenance", "operating cost", "overhaul", "运维", "维护", "运行成本", "大修", "penyelenggaraan"],
      en: "O&M for a 600 kW set at 8,000 h/year on 60% CH₄: oil/filters/plugs 0.014, service labour 0.012, overhaul reserve 0.016, desulfurisation media 0.005, spares/insurance 0.008 — total RM 0.048–0.058/kWh (≈USD 0.011–0.014/kWh).\nFull-service O&M including overhauls: RM 0.065–0.085/kWh. Pond O&M and upgrading are excluded.\nLong periods below 70% load cause carbon build-up and shorten the overhaul interval — size down or split into two units.",
      ms: "O&M untuk set 600 kW pada 8,000 j/tahun dengan 60% CH₄: minyak/penapis/plug 0.014, buruh servis 0.012, rizab overhaul 0.016, media nyahsulfur 0.005, alat ganti/insurans 0.008 — jumlah RM 0.048–0.058/kWh (≈USD 0.011–0.014/kWh).\nO&M perkhidmatan penuh termasuk overhaul: RM 0.065–0.085/kWh. O&M kolam dan peningkatan tidak termasuk.\nTempoh panjang di bawah 70% beban menyebabkan pembentukan karbon dan memendekkan selang overhaul — kecilkan saiz atau pecahkan kepada dua unit.",
      zh: "600 kW 机组、年运行 8,000 h、60% 甲烷的运维成本：机油/滤芯/火花塞 0.014，维修人工 0.012，大修预留 0.016，脱硫剂 0.005，备件保险杂项 0.008——合计 RM 0.048–0.058/kWh（约 USD 0.011–0.014/kWh）。\n含大修的全包运维：RM 0.065–0.085/kWh，不含池塘运维与提纯。\n长期低于 70% 负荷会积碳并缩短大修周期——宁可缩小单机或拆成两台。" },

    { id: "refs", k: ["reference", "installation", "project", "case", "业绩", "案例", "案例现场", "rujukan", "projek"],
      en: "Shengdong biogas gensets in Malaysia: 16.4 MW across 30 units, 14 mills — 20 units running since 2009–2013 on POME biogas.\nNamed references include BELL Eco Power (500 kW × 4, 2009), Prosper Group mills (Rompin, Kosfarm, Wujud, Prosper), Cahaya Muda, Apas Balung (Sawit), KLK Group (600 kW × 4, 2013), and units under installation for Wilmar (Sapi, Saremas 1), Carotino and Biolermech.",
      ms: "Genset biogas Shengdong di Malaysia: 16.4 MW merentas 30 unit, 14 kilang — 20 unit beroperasi sejak 2009–2013 dengan biogas POME.\nRujukan termasuk BELL Eco Power (500 kW × 4, 2009), kilang Prosper Group (Rompin, Kosfarm, Wujud, Prosper), Cahaya Muda, Apas Balung (Sawit), KLK Group (600 kW × 4, 2013), dan unit dalam pemasangan untuk Wilmar (Sapi, Saremas 1), Carotino dan Biolermech.",
      zh: "盛东沼气机组在马来西亚：30 台、14 家油厂、合计 16.4 MW，其中 20 台自 2009–2013 年运行至今。\n具名业绩包括 BELL Eco Power（500 kW × 4，2009）、Prosper 集团旗下 Rompin／Kosfarm／Wujud／Prosper、Cahaya Muda、Apas Balung（Sawit）、KLK 集团（600 kW × 4，2013），以及正在安装的 Wilmar（Sapi、Saremas 1）、Carotino、Biolermech。" },

    { id: "scope", k: ["scope", "supply", "what do you supply", "battery limit", "供货范围", "供什么", "skop"],
      en: "Standard battery limit covers: gas capture and treatment, buffer holder, desulfurisation, conditioning, genset or fuel-cell package, heat recovery, controls, flare, and commissioning.\nCivil works, pond construction and grid-connection charges are normally by the mill unless agreed otherwise — we state the boundary in the quotation rather than leaving it ambiguous.",
      ms: "Had bateri standard merangkumi: penangkapan dan rawatan gas, gas holder penampan, nyahsulfur, pengkondisian, pakej genset atau sel bahan api, pemulihan haba, kawalan, flare dan pentauliahan.\nKerja awam, pembinaan kolam dan caj sambungan grid biasanya oleh kilang melainkan dipersetujui — kami nyatakan sempadan dalam sebut harga.",
      zh: "标准供货边界包括：气体收集与净化、缓冲气柜、脱硫、调质、机组或燃料电池成套、余热回收、控制系统、火炬与调试。\n土建、池塘施工与并网费用原则上由油厂承担（另有约定除外）——我们在报价里把边界写清楚，不留模糊。" },

    { id: "calc", k: ["calculator", "calculate", "tool", "计算器", "测算", "算一下", "kalkulator"],
      en: "Five free calculators: biogas to electricity and heat, capacity sizing, mill throughput to biogas, upgrading yield, and project economics.\nOpen Engineering Tools in the top menu. If you would rather I run it, send mill throughput, pond volume, measured gas flow and methane content.",
      ms: "Lima kalkulator percuma: biogas ke elektrik dan haba, saiz kapasiti, kemampuan kilang ke biogas, hasil peningkatan, dan ekonomi projek.\nBuka Alat Kejuruteraan di menu atas. Jika mahu saya kira, hantar kadar kilang, isipadu kolam, aliran gas dan kandungan metana.",
      zh: "五个免费计算器：沼气发电与余热、容量选型、压榨量产气、提纯收率、项目经济性。\n顶部菜单「工程测算工具」。想让我算，给我压榨量、池塘容积、实测气量与甲烷含量。" },

    { id: "terms", k: ["fob", "cif", "trade", "delivery", "documentation", "贸易", "交货", "单证", "条款", "penghantaran", "dokumen"],
      en: "Quotations in USD or MYR. CIF Kota Kinabalu or Sandakan, or delivered to site.\nEnglish documentation with every plant: datasheets, GA drawings, performance curves, test reports and O&M manuals.\nLead time depends on the engine or fuel-cell model and the upgrading scope — it is stated in the quotation.",
      ms: "Sebut harga dalam USD atau MYR. CIF Kota Kinabalu atau Sandakan, atau dihantar ke tapak.\nDokumentasi bahasa Inggeris dengan setiap loji: lembaran data, lukisan GA, lengkung prestasi, laporan ujian dan manual O&M.\nMasa penghantaran bergantung pada model enjin atau sel bahan api dan skop peningkatan — dinyatakan dalam sebut harga.",
      zh: "报价用 USD 或 MYR，CIF 亚庇或山打根，或送到现场。\n每套装置随附英文资料：数据表、总图、性能曲线、试验报告与运维手册。\n交期取决于机组或燃料电池型号与提纯范围——在报价单里写明。" },

    { id: "contact", k: ["contact", "email", "phone", "whatsapp", "call", "联系", "电话", "邮箱", "怎么联系", "hubungi", "e-mel"],
      en: "KSTS K. S. Technical Services — Sdr. Leong Kian Sheng (Alvin).\nEmail: " + EMAIL + "\nPhone / WhatsApp: " + PHONE + "\nAddress: Kg. Nangoh, NT 083017181 (Lot 2), 34 km Off Jalan Simpang Sapi Nangoh, Labuk–Sugut, Telupid, Sabah.\nWe review data and reply within three working days.",
      ms: "KSTS K. S. Technical Services — Sdr. Leong Kian Sheng (Alvin).\nE-mel: " + EMAIL + "\nTelefon / WhatsApp: " + PHONE + "\nAlamat: Kg. Nangoh, NT 083017181 (Lot 2), 34 km Off Jalan Simpang Sapi Nangoh, Labuk–Sugut, Telupid, Sabah.\nKami menyemak data dan membalas dalam tiga hari bekerja.",
      zh: "KSTS K. S. Technical Services — 联系人：Leong Kian Sheng（Alvin）。\n邮箱：" + EMAIL + "\n电话／WhatsApp：" + PHONE + "\n地址：Kg. Nangoh, NT 083017181 (Lot 2), 34 km Off Jalan Simpang Sapi Nangoh, Labuk–Sugut, Telupid, Sabah。\n我们审阅数据后三个工作日内回复。" },

    { id: "who", k: ["who are you", "company", "about", "ksts", "contractor", "你们是谁", "公司", "介绍", "syarikat", "tentang"],
      en: "KSTS K. S. Technical Services — a CIDB-registered Bumiputera contractor in Telupid, Sabah, with DOSH and ECOS registrations (MPS R14722/2009).\nTechnology partner: SINOPEC Dalian Research Institute of Petroleum and Petrochemicals; engineering by a Tsinghua University PhD team.\nWe design, build and support biogas power plants, biomethane upgrading and bio-CNG for palm oil mills across Sabah and Sarawak.",
      ms: "KSTS K. S. Technical Services — kontraktor Bumiputera berdaftar CIDB di Telupid, Sabah, dengan pendaftaran DOSH dan ECOS (MPS R14722/2009).\nRakan teknologi: Institut Penyelidikan Petroleum dan Petrokimia Dalian SINOPEC; kejuruteraan oleh pasukan PhD Universiti Tsinghua.\nKami merekabentuk, membina dan menyokong loji kuasa biogas, peningkatan biometana dan bio-CNG untuk kilang kelapa sawit di Sabah dan Sarawak.",
      zh: "KSTS K. S. Technical Services——沙巴 Telupid 的 CIDB 注册土著承包商，持 DOSH 与 ECOS 资质（MPS R14722/2009）。\n技术伙伴：中国石化大连研究院；工程技术团队来自清华大学博士团队。\n我们为沙巴与砂拉越棕榈油厂设计、建设并运维沼气发电、生物天然气提纯与 Bio-CNG。" },

    { id: "feedstock", k: ["pome", "ffb", "throughput", "pond", "feedstock", "原料", "压榨量", "池塘", "废水", "bahan mentah", "kolam"],
      en: "The fuel is POME from the mill's own pond. What decides the plant size is steady gas, not peak gas: FFB throughput sets the COD load, pond volume and temperature set the retention and yield.\nSend throughput (t/h), pond volume and a measured flow — if you have no measurement yet, we say what to measure and for how long.",
      ms: "Bahan api ialah POME dari kolam kilang sendiri. Yang menentukan saiz loji ialah gas yang stabil, bukan gas puncak: kadar FFB menetapkan beban COD, isipadu dan suhu kolam menetapkan masa tahan dan hasil.\nHantar kadar (t/j), isipadu kolam dan aliran yang diukur — jika belum ada ukuran, kami beritahu apa dan berapa lama perlu diukur.",
      zh: "燃料是油厂自有池塘的 POME。决定规模的是稳定气量，不是峰值气量：压榨量决定 COD 负荷，池塘容积与温度决定停留时间与产气率。\n给我处理量（t/h）、池塘容积和实测流量；还没有实测的，我们告诉你要测什么、测多久。" },

    { id: "grid", k: ["grid", "grid connection", "net metering", "sell", "并网", "上网", "卖电", "grid", "sambungan"],
      en: "Sets run island or parallel; 415 V / 50 Hz standard, 11 kV option at 2 MW. Grid-connection charges and the interconnection application are normally the mill's scope — we supply the generator, protection settings and documentation the utility asks for.\nWhether export is allowed, and at what tariff, depends on the local utility and the scheme; we confirm it for the specific site rather than assume.",
      ms: "Set beroperasi pulau atau selari; 415 V / 50 Hz standard, pilihan 11 kV pada 2 MW. Caj sambungan grid dan permohonan interkoneksi biasanya skop kilang — kami membekalkan penjana, tetapan perlindungan dan dokumen yang diminta utiliti.\nSama ada eksport dibenarkan, dan pada tarif apa, bergantung pada utiliti tempatan dan skema; kami sahkan untuk tapak tertentu.",
      zh: "机组可孤网或并网运行；标准 415 V / 50 Hz，2 MW 可选 11 kV。并网费用与接入申请原则上属油厂范围——我们提供机组、保护定值和电网要求的文件。\n能否上网、按什么电价，取决于当地电力公司与政策；我们按具体项目确认，不预设。" }
  ];

  /* ---------------------------------------------------------------- helpers */
  function norm(s) {
    return (s || "").toLowerCase().replace(/[，。？、；：！（）]/g, " ").replace(/\s+/g, " ").trim();
  }
  function match(text) {
    var q = norm(text), best = null, bestScore = 0;
    for (var i = 0; i < KB.length; i++) {
      var s = 0, k = KB[i].k;
      for (var j = 0; j < k.length; j++) {
        var kw = k[j].toLowerCase();
        if (q.indexOf(kw) !== -1) s += kw.length > 4 ? 2 : 1;
      }
      if (s > bestScore) { bestScore = s; best = KB[i]; }
    }
    return bestScore >= 1 ? best : null;
  }
  var HUMAN_RE = /human|engineer|sales|person|call me|contact me|工程师|人工|销售|联系我|转人工|真人|jurutera|manusia|hubungi saya/i;
  function textOf(hit) { return ZH ? hit.zh : (MS ? hit.ms : hit.en); }

  /* ---------------------------------------------------------------- DOM */
  var root = document.createElement("div");
  root.id = "hs-chat-root";
  document.body.appendChild(root);

  var btn = document.createElement("button");
  btn.className = "hs-chat-btn";
  btn.type = "button";
  btn.setAttribute("aria-label", T.btn);
  btn.innerHTML = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 11.5a8.4 8.4 0 0 1-9 8.4 9.6 9.6 0 0 1-3.4-.6L3 21l1.7-4.6A8.4 8.4 0 0 1 12 3.1a8.4 8.4 0 0 1 9 8.4Z"/></svg><span class="hs-btn-label">' + T.btn + '</span>';

  var panel = document.createElement("section");
  panel.className = "hs-chat-panel";
  panel.setAttribute("role", "dialog");
  panel.setAttribute("aria-label", T.title);
  panel.innerHTML =
    '<div class="hs-chat-head"><div><div class="hs-title">' + T.title + '</div><div class="hs-sub">' + T.sub + '</div></div><button class="hs-close" type="button" aria-label="Close">&times;</button></div>' +
    '<div class="hs-chat-body" id="hs-body"></div>' +
    '<div class="hs-chat-foot"><div class="hs-inputrow"><textarea id="hs-ta" rows="1" placeholder="' + T.ph + '"></textarea>' +
    '<button class="hs-send" id="hs-send" type="button" aria-label="Send"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 2 11 13"/><path d="M22 2 15 22l-4-9-9-4Z"/></svg></button></div>' +
    '<div class="hs-note">' + T.note + '</div></div>';

  root.appendChild(btn);
  root.appendChild(panel);

  var body = panel.querySelector("#hs-body");
  var ta = panel.querySelector("#hs-ta");
  var send = panel.querySelector("#hs-send");
  var history = [];
  var opened = false;

  function scroll() { body.scrollTop = body.scrollHeight; }

  function plain(s) {
    return String(s).replace(/\*\*(.+?)\*\*/g, "$1").replace(/^#{1,6}\s*/gm, "").replace(/`/g, "");
  }
  function add(who, text) {
    var row = document.createElement("div");
    row.className = "hs-msg " + who;
    var b = document.createElement("div");
    b.className = "hs-bubble";
    b.textContent = who === "bot" ? plain(text) : text;
    row.appendChild(b);
    body.appendChild(row);
    if (who !== "sys") history.push({ role: who === "me" ? "user" : "assistant", content: text });
    scroll();
    return row;
  }

  function chips(list) {
    var wrap = document.createElement("div");
    wrap.className = "hs-chips";
    list.forEach(function (label) {
      var c = document.createElement("button");
      c.className = "hs-chip";
      c.type = "button";
      c.textContent = label;
      c.addEventListener("click", function () {
        wrap.remove();
        ask(label);
      });
      wrap.appendChild(c);
    });
    body.appendChild(wrap);
    scroll();
  }

  function typing(on) {
    var el = document.getElementById("hs-typing");
    if (on) {
      if (el) return;
      var row = document.createElement("div");
      row.className = "hs-msg bot";
      row.id = "hs-typing";
      row.innerHTML = '<div class="hs-bubble"><span class="hs-typing"><i></i><i></i><i></i></span></div>';
      body.appendChild(row);
      scroll();
    } else if (el) { el.remove(); }
  }

  function convIdGet() {
    var id = null;
    try { id = localStorage.getItem("ksts_conv"); } catch (e) {}
    if (!id) {
      id = "k" + Date.now().toString(36) + Math.random().toString(36).slice(2, 8);
      try { localStorage.setItem("ksts_conv", id); } catch (e) {}
    }
    return id;
  }
  var convId = convIdGet();

  function api(path, body) {
    if (!endpoint) return Promise.reject(new Error("no endpoint"));
    return fetch(endpoint.replace(/\/$/, "") + path, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(body || {})
    });
  }

  function escalate(prefix) {
    var box = document.createElement("div");
    box.className = "hs-escalate";
    box.innerHTML = '<p>' + T.escTitle + '</p>' +
      '<input id="hs-name" placeholder="' + T.escName + '" autocomplete="name">' +
      '<input id="hs-mail" placeholder="' + T.escMail + '" autocomplete="email">' +
      '<button type="button">' + T.escBtn + '</button>' +
      '<div class="hs-alt">' + T.escAlt + '<a href="mailto:' + EMAIL + '">' + EMAIL + '</a></div>';
    body.appendChild(box);
    scroll();
    var nameEl = box.querySelector("#hs-name");
    var mailEl = box.querySelector("#hs-mail");
    box.querySelector("button").addEventListener("click", function () {
      var mail = (mailEl.value || "").trim();
      if (mail.length < 4) { mailEl.focus(); return; }
      var msg = (ZH ? "【留资】" : MS ? "[Kontak] " : "[Lead] ") +
        (nameEl.value || "-") + " / " + mail + (prefix ? " / " + prefix : "");
      var self = this;
      self.disabled = true;
      api("/handoff", { conv: convId, message: msg, lang: ZH ? "zh" : (MS ? "ms" : "en") })
        .then(function () { box.remove(); add("bot", T.escOk); startPoll(); })
        .catch(function () {
          self.disabled = false;
          add("bot", T.escFail + EMAIL);
          add("bot", T.escAlt + EMAIL + " · " + PHONE);
        });
    });
  }

  function answerFor(text) {
    var hit = match(text);
    if (hit) {
      var a = textOf(hit);
      add("bot", a);
      api("/log", { conv: convId, message: text, answer: a, lang: ZH ? "zh" : (MS ? "ms" : "en") }).catch(function () {});
      return true;
    }
    return false;
  }

  var endpoint = null;
  /* Site config lives at <site-root>/assets/data/chat-config.json. Resolve it by
     trying candidates (script URL, script URL minus a trailing language dir,
     site-root guess) because pages live at "/", "/ms/" and "/zh/". */
  var CFG_CANDIDATES = (function () {
    var out = [], seen = {};
    function add(u) { if (u && !seen[u]) { seen[u] = 1; out.push(u); } }
    try {
      var s = document.currentScript;
      if (!s) {
        var list = document.getElementsByTagName("script");
        for (var i = list.length - 1; i >= 0; i--) {
          if (/chat\.js(\?|$)/.test(list[i].src || "")) { s = list[i]; break; }
        }
      }
      if (s && s.src) {
        var p = new URL(s.src, location.href).pathname;
        var m = p.match(/^(.*?)assets\/js\/chat\.js$/);
        if (m) {
          add(m[1] + "assets/data/chat-config.json");
          add(m[1].replace(/(zh|ms)\/$/, "") + "assets/data/chat-config.json");
        }
      }
    } catch (e) {}
    var seg = location.pathname.split("/")[1];
    if (seg) add("/" + seg + "/assets/data/chat-config.json");
    add("/assets/data/chat-config.json");
    return out;
  })();
  function loadConfig() {
    var i = 0;
    (function next() {
      if (i >= CFG_CANDIDATES.length) return;
      fetch(CFG_CANDIDATES[i++], { cache: "no-store" })
        .then(function (r) { return r.ok ? r.json() : null; })
        .then(function (c) {
          if (c && c.endpoint) { endpoint = c.endpoint; startPoll(); } else { next(); }
        })
        .catch(next);
    })();
  }

  var lastId = 0, mode = "ai", polling = false;

  /* ---- human replies come back through long polling ---- */
  function startPoll() {
    if (polling || !endpoint) return;
    polling = true;
    function loop() {
      if (!panel.classList.contains("open")) { polling = false; return; }
      fetch(endpoint.replace(/\/$/, "") + "/poll?conv=" + encodeURIComponent(convId) + "&after=" + lastId + "&wait=20", { cache: "no-store" })
        .then(function (r) { return r.ok ? r.json() : null; })
        .then(function (j) {
          if (j) {
            if (j.mode) mode = j.mode;
            (j.messages || []).forEach(function (m) {
              if (m.id > lastId) lastId = m.id;
              if (m.role === "human") add("human", m.text);
              else add("bot", m.text);
            });
          }
          setTimeout(loop, 700);
        })
        .catch(function () { setTimeout(loop, 5000); });
    }
    loop();
  }

  function handoff(text) {
    api("/handoff", { conv: convId, message: text, lang: ZH ? "zh" : (MS ? "ms" : "en") })
      .then(function () { mode = "human"; add("bot", T.waitHuman); startPoll(); })
      .catch(function () { add("bot", T.waitHuman); add("bot", T.escAlt + EMAIL + " · " + PHONE); });
  }

  function ask(text) {
    text = (text || "").trim();
    if (!text) return;
    add("me", text);
    var lang = ZH ? "zh" : (MS ? "ms" : "en");
    if (HUMAN_RE.test(text) && endpoint) { handoff(text); return; }
    if (mode === "human" && endpoint) { api("/chat", { conv: convId, message: text, lang: lang }).catch(function () {}); startPoll(); return; }
    if (answerFor(text)) return;
    if (endpoint) {
      typing(true);
      api("/chat", { conv: convId, message: text, lang: lang })
        .then(function (r) { return r.ok ? r.json() : Promise.reject(); })
        .then(function (j) {
          typing(false);
          if (j.mode) mode = j.mode;
          if (j.id && j.id > lastId) lastId = j.id;
          if (j.reply) {
            add("bot", j.reply);
            if (j.escalate) escalate(text);
          } else if (j.mode === "human") {
            add("bot", T.aiPaused);
          } else { throw new Error("empty"); }
          if (mode === "human") startPoll();
        })
        .catch(function () {
          typing(false);
          add("bot", T.errNet);
          escalate(text);
        });
      return;
    }
    add("bot", ZH
      ? "这个问题我这边拿不准，转给工程师更靠谱。留个联系方式，三个工作日内回复；急的话直接发邮件。"
      : MS
      ? "Soalan ini di luar apa yang saya boleh jawab dengan yakin — lebih baik terus kepada jurutera. Tinggalkan kontak dan anda akan dibalas dalam tiga hari bekerja."
      : "That one is outside what I can answer reliably — better to pass it to an engineer. Leave a contact and you will get a reply within three working days.");
    escalate(text);
  }

  function openPanel() {
    panel.classList.add("open");
    btn.style.display = "none";
    if (!opened) {
      opened = true;
      add("bot", T.greet);
      chips(T.chips);
      loadConfig();
    }
    startPoll();
    ta.focus();
  }
  function closePanel() {
    panel.classList.remove("open");
    btn.style.display = "";
  }

  btn.addEventListener("click", openPanel);
  panel.querySelector(".hs-close").addEventListener("click", closePanel);

  send.addEventListener("click", function () {
    var v = ta.value;
    ta.value = "";
    ta.style.height = "";
    ask(v);
  });
  ta.addEventListener("keydown", function (e) {
    if (e.key === "Enter" && !e.shiftKey) { e.preventDefault(); send.click(); }
  });
  ta.addEventListener("input", function () {
    ta.style.height = "auto";
    ta.style.height = Math.min(ta.scrollHeight, 96) + "px";
  });

  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape" && panel.classList.contains("open")) closePanel();
  });
})();
