/* KSTS hydrogen CHP calculators — methane reforming + fuel cell, 7.5–100 kW */
(function () {
  "use strict";

  var CH4_KWH = 9.94;          // kWh per Nm³ CH4, LHV
  var MODELS = [7.5, 10, 15, 20, 30, 50, 75, 100];
  var PRICE_PER_KW = 10000;    // RM/kW FOB to Malaysia
  var GRID_EF = 0.60;          // t CO2 / MWh avoided, indicative Malaysia

  function $(id) { return document.getElementById(id); }
  function val(id, d) {
    var el = $(id);
    var v = el ? parseFloat(el.value) : NaN;
    return isFinite(v) ? v : (d || 0);
  }
  function nf(x, d) {
    if (!isFinite(x)) return "—";
    d = d === undefined ? 0 : d;
    return x.toLocaleString("en-US", { minimumFractionDigits: d, maximumFractionDigits: d });
  }
  function rm(x, d) { return "RM " + nf(x, d === undefined ? 0 : d); }
  function set(id, t) { var el = $(id); if (el) el.textContent = t; }
  function warn(id, t) {
    var el = $(id);
    if (!el) return;
    if (t) { el.textContent = t; el.classList.add("show"); }
    else { el.textContent = ""; el.classList.remove("show"); }
  }

  /* ---------------------------------------------------------- A · size & fuel */
  function toolA() {
    var kw = val("h1_kw"), eff = val("h1_eff", 42), heat = val("h1_heat", 43),
        load = val("h1_load", 85), hours = val("h1_hours", 8000);

    var fuel = eff > 0 ? kw / (eff / 100) : 0;          // kW fuel input
    var ch4 = fuel / CH4_KWH;                            // Nm³/h at full load
    var ch4day = ch4 * 24;
    var ch4yr = ch4 * hours * load / 100;
    var heatKW = fuel * heat / 100;
    var hot = heatKW * 3600 / (4.18 * 50);               // L/h at ΔT 50 K
    var gen = kw * hours * load / 100;                    // kWh/yr
    var heatYr = heatKW * hours * load / 100;             // kWh_th/yr

    set("h1_fuel", nf(fuel, 1) + " kW");
    set("h1_ch4", nf(ch4, 2) + " Nm³/h");
    set("h1_day", nf(ch4day, 1) + " Nm³/day");
    set("h1_year", nf(ch4yr, 0) + " Nm³/yr");
    set("h1_cyl", nf(ch4day / 10, 1) + " × 50 L @ 200 bar");
    set("h1_heatkw", nf(heatKW, 1) + " kW");
    set("h1_hot", nf(hot, 0) + " L/h");
    set("h1_gen", nf(gen / 1000, 0) + " MWh/yr");
    set("h1_heatyr", nf(heatYr / 1000, 0) + " MWh/yr");
    set("h1_total", nf(eff + heat, 0) + "%");

    var msgs = [];
    if (eff + heat > 90) msgs.push("Combined efficiency above 90% is not achievable for reformer + fuel cell: check both assumptions.");
    if (eff > 48) msgs.push("Electrical efficiency above 48% at this scale assumes a large SOFC; a reformer + PEM/PAFC unit is 40–45%.");
    if (load < 50) msgs.push("Average load below 50% wastes capex. Two smaller units cycling is usually better than one large unit idling.");
    warn("h1_warn", msgs.join(" "));
  }

  /* ---------------------------------------------------------- B · model match */
  function toolB() {
    var need = val("h2_need"), avail = val("h2_ch4"), load = val("h2_load", 85);
    var eff = 0.42, heatFrac = 0.43;

    var pick = MODELS[MODELS.length - 1];
    for (var i = 0; i < MODELS.length; i++) {
      if (MODELS[i] >= need) { pick = MODELS[i]; break; }
    }
    var size = Math.max(pick, 7.5);
    var ch4need = (size / eff) / CH4_KWH;
    var heatKW = (size / eff) * heatFrac;
    var cover = ch4need > 0 ? (avail / ch4need) * 100 : 0;

    set("h2_model", size.toLocaleString("en-US") + " kW");
    set("h2_price", rm(size * PRICE_PER_KW));
    set("h2_kw", nf(size, 1) + " kW");
    set("h2_needgas", nf(ch4need, 2) + " Nm³/h");
    set("h2_cover", avail > 0 ? nf(cover, 0) + "%" : "—");
    set("h2_heat", nf(heatKW, 1) + " kW");
    set("h2_gen", nf(size * 8000 * load / 100 / 1000, 0) + " MWh/yr");

    var msgs = [];
    if (avail > 0 && cover < 100) {
      msgs.push("Available gas covers only " + nf(cover, 0) + "% of full load. Either accept a lower load, size down, or add cylinders.");
    }
    if (avail > 0 && cover > 180) {
      msgs.push("More than 1.8× the gas needed: check whether a larger model uses the fuel better.");
    }
    if (need > 100) {
      msgs.push("Above 100 kW this range stops. Use 2–3 units in parallel, or look at a gas-engine CHP.");
    }
    if (need > 0 && need < 7.5) {
      msgs.push("Below 7.5 kW the fixed balance-of-plant dominates the price — consider one shared unit for several houses.");
    }
    warn("h2_warn", msgs.join(" "));
  }

  /* ---------------------------------------------------------- C · economics */
  function irr(capex, annual, years) {
    function npv(r) {
      var s = -capex;
      for (var t = 1; t <= years; t++) s += annual / Math.pow(1 + r, t);
      return s;
    }
    var lo = -0.95, hi = 5;
    if (npv(lo) * npv(hi) > 0) return NaN;
    for (var i = 0; i < 200; i++) {
      var mid = (lo + hi) / 2;
      if (npv(lo) * npv(mid) <= 0) hi = mid; else lo = mid;
    }
    return (lo + hi) / 2;
  }

  function toolC() {
    var kw = val("h3_kw"), capexKW = val("h3_capex", PRICE_PER_KW), omPct = val("h3_om", 3);
    var gasP = val("h3_gas"), tariff = val("h3_tariff"), heatP = val("h3_heat");
    var load = val("h3_load", 85), hours = val("h3_hours", 8000);
    var life = val("h3_life", 10), disc = val("h3_disc", 8) / 100;

    var capex = kw * capexKW;
    var gen = kw * hours * load / 100;                    // kWh/yr
    var fuelKW = kw / 0.42;
    var ch4yr = fuelKW * hours * load / 100 / CH4_KWH;    // Nm³/yr
    var heatKWh = fuelKW * 0.43 * hours * load / 100;

    var revE = gen * tariff;
    var revH = heatKWh * heatP;
    var costG = ch4yr * gasP;
    var costOM = capex * omPct / 100;
    var net = revE + revH - costG - costOM;
    var payback = net > 0 ? capex / net : Infinity;

    var npv = -capex;
    for (var t = 1; t <= life; t++) npv += net / Math.pow(1 + disc, t);
    var r = net > 0 ? irr(capex, net, life) : NaN;
    var crf = disc > 0 ? (disc * Math.pow(1 + disc, life)) / (Math.pow(1 + disc, life) - 1) : 1 / life;
    var lcoe = gen > 0 ? (capex * crf + costOM + costG) / gen : 0;
    var co2 = gen / 1000 * GRID_EF;

    set("h3_inv", rm(capex));
    set("h3_net", rm(net));
    set("h3_pb", isFinite(payback) ? nf(payback, 1) + " years" : "never");
    set("h3_rev_e", rm(revE));
    set("h3_rev_h", rm(revH));
    set("h3_cost_g", rm(costG));
    set("h3_cost_om", rm(costOM));
    set("h3_npv", rm(npv));
    set("h3_irr", isFinite(r) ? nf(r * 100, 1) + "%" : "n/a");
    set("h3_lcoe", "RM " + nf(lcoe, 3) + "/kWh");
    set("h3_co2", nf(co2, 0) + " t/yr");

    var msgs = [];
    if (net <= 0) {
      msgs.push("Negative annual benefit: fuel plus O&M costs more than the electricity and heat it replaces. Nothing else in the model can fix that — change the fuel cost or the avoided cost.");
    } else if (isFinite(payback) && life > 0 && payback > life) {
      msgs.push("Payback exceeds the evaluation period. At this price the unit needs a grant, a higher avoided cost, or free/cheap fuel.");
    }
    if (heatP === 0 && heatKWh > 0) {
      msgs.push("Heat is valued at zero: the 43% heat output is being thrown away, which is half the reason to buy a CHP.");
    }
    if (tariff < 0.6 && gasP >= 1.0) {
      msgs.push("Grid-connected at a subsidised tariff with bought gas: the economics rarely close. This product is for off-grid or high-cost power.");
    }
    if (kw > 100) msgs.push("Above 100 kW the model leaves this product range — use multiple units.");
    warn("h3_warn", msgs.join(" "));
  }

  var CALCS = { a: toolA, b: toolB, c: toolC };
  function runAll() { Object.keys(CALCS).forEach(function (k) { CALCS[k](); }); }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", function () {
      runAll();
      document.addEventListener("input", function (e) {
        if (e.target && e.target.id && /^h[123]_/.test(e.target.id)) runAll();
      });
      document.addEventListener("change", function (e) {
        if (e.target && e.target.id && /^h[123]_/.test(e.target.id)) runAll();
      });
    });
  } else {
    runAll();
    document.addEventListener("input", function (e) {
      if (e.target && e.target.id && /^h[123]_/.test(e.target.id)) runAll();
    });
  }
})();
