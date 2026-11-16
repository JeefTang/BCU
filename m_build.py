#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the mobile edition of the BCU / KSTS bioenergy site.

Reads the already-generated desktop pages (EN at root, MS under ms/, ZH under zh/),
linearises each page into a single-column, large-touch-target layout and writes
them to /m/, /ms/m/ and /zh/m/.

Run after build_all.py:
    python3 build_all.py && python3 m_build.py
"""
import os
import posixpath
import re
import sys

try:
    from lxml import html as LH
except ImportError:  # pragma: no cover
    sys.exit("lxml is required: pip3 install lxml --break-system-packages")

ROOT = os.path.dirname(os.path.abspath(__file__))
DOMAIN = "https://jeeftang.github.io/BCU"

# (code, desktop dir, mobile out dir)
LANGS = [("en", "", "m"), ("ms", "ms", "ms/m"), ("zh", "zh", "zh/m")]

SKIP = {"404.html"}
SKIP_TAGS = {"script", "style", "noscript", "header", "footer", "nav", "iframe"}
SKIP_CLASS_HINTS = ("chat", "hs-")

CUR_LANG = "en"

LOGO = (
    '<svg viewBox="0 0 34 34" fill="none" aria-hidden="true">'
    '<rect width="34" height="34" rx="9" fill="#0f7a52"/>'
    '<path d="M17 6.5c3.6 2.4 6 6.2 6 10.2 0 3.3-2.7 6-6 6s-6-2.7-6-6c0-4 2.4-7.8 6-10.2Z" fill="#fff"/>'
    '<path d="M17 22.7v4.8M11 14.5h12" stroke="#0c1a26" stroke-width="1.6" stroke-linecap="round" opacity=".85"/>'
    "</svg>"
)

# page, label EN, label MS, label ZH, tag EN, tag MS, tag ZH
NAV_PAGES = [
    ("biomethane.html", "Biomethane &amp; bio-CNG", "Biometana &amp; bio-CNG", "生物天然气 / Bio-CNG",
     "Upgrading to 97% CH₄", "Peningkatan ke 97% CH₄", "提纯至 97% 甲烷"),
    ("hydrogen-chp.html", "Hydrogen CHP", "CHP hidrogen", "氢能热电联供",
     "7.5 – 100 kW · fuel cell", "7.5 – 100 kW · sel bahan api", "7.5 – 100 kW · 燃料电池"),
    ("bhp.html", "BHP air-conditioning", "Penghawa dingin BHP", "沼气热泵空调 BHP",
     "30 – 480 kW · gas-engine driven", "30 – 480 kW · enjin gas", "30 – 480 kW · 燃气机驱动"),
    ("biogas-to-power.html", "Biogas power plant", "Loji kuasa biogas", "沼气发电站",
     "300 kW – 2 MW · POME biogas", "300 kW – 2 MW · biogas POME", "300 kW – 2 MW · POME 沼气"),
    ("equipment.html", "Equipment &amp; scope", "Peralatan &amp; skop", "设备与供货范围",
     "Battery limits · who does what", "Had skop · siapa buat apa", "供货界限 · 谁做什么"),
    ("calculator.html", "Engineering tools", "Alat kejuruteraan", "工程测算工具",
     "Gas, power and load sizing", "Saiz gas, kuasa dan beban", "气量、功率与负荷测算"),
    ("about.html", "About KSTS", "Tentang KSTS", "关于 KSTS",
     "Sabah · since 2009", "Sabah · sejak 2009", "沙巴 · 2009 年起"),
    ("contact.html", "Contact", "Hubungi", "联系我们",
     "Pre-feasibility in 3 days", "Pra-kelayakan dalam 3 hari", "三个工作日内回复"),
]

UI = {
    "en": {
        "html": "en", "brand_sub": "Biogas &amp; Bioenergy",
        "home": "Home", "solutions": "Solutions", "quote": "Get a study",
        "desktop": "Desktop", "sheet_title": "Solutions", "close": "Close",
        "foot": "Mobile edition", "langs": [("ms", "BM"), ("zh", "中文")],
    },
    "ms": {
        "html": "ms", "brand_sub": "Biogas &amp; Biotenaga",
        "home": "Utama", "solutions": "Penyelesaian", "quote": "Minta kajian",
        "desktop": "Komputer", "sheet_title": "Penyelesaian", "close": "Tutup",
        "foot": "Edisi mudah alih", "langs": [("en", "EN"), ("zh", "中文")],
    },
    "zh": {
        "html": "zh", "brand_sub": "沼气与生物质能源",
        "home": "首页", "solutions": "解决方案", "quote": "申请评估",
        "desktop": "电脑版", "sheet_title": "解决方案", "close": "关闭",
        "foot": "手机版", "langs": [("en", "EN"), ("ms", "BM")],
    },
}
LANG_LABEL = {"en": "EN", "ms": "BM", "zh": "中文"}


# ---------------------------------------------------------------- helpers
def classes(el):
    return (el.get("class") or "").split()


def txt(el):
    return re.sub(r"\s+", " ", (el.text_content() or "")).strip()


def is_dropped(el):
    if el.tag in SKIP_TAGS:
        return True
    cls = " ".join(classes(el))
    return any(h in cls for h in SKIP_CLASS_HINTS)


def esc(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def render_table(el):
    el = LH.fromstring(LH.tostring(el))
    el.set("class", "")
    inner = re.sub(r'\s(class|style|width|height|align)="[^"]*"', "", LH.tostring(el, encoding="unicode"))
    inner = inner.replace("<tbody>", "").replace("</tbody>", "")
    return (
        '<div class="m-table-hint">← 左右滑动查看完整表格 / swipe to see all columns</div>'
        f'<div class="m-table">{inner}</div>'
    )


def render_figure(el):
    out = []
    for img in el.iter("img"):
        src = img.get("src") or ""
        alt = img.get("alt") or ""
        if src:
            out.append(f'<img src="{src}" alt="{esc(alt)}" loading="lazy">')
    cap = el.find("figcaption")
    caption = txt(cap) if cap is not None else ""
    body = "".join(out)
    if not body:
        return ""
    return f'<figure class="m-fig">{body}{f"<figcaption>{esc(caption)}</figcaption>" if caption else ""}</figure>'


def render_card(el, heading_tag="h3"):
    parts = []
    for child in el:
        cls_c = classes(child)
        if child.tag == "p":
            t = txt(child)
            if not t:
                continue
            if "tag" in cls_c:
                parts.append(f'<p class="tag">{esc(t)}</p>')
            else:
                parts.append(f"<p>{esc(t)}</p>")
        elif child.tag in ("h3", "h4"):
            t = txt(child)
            if t:
                parts.append(f"<{heading_tag}>{esc(t)}</{heading_tag}>")
        elif child.tag in ("ul", "ol"):
            items = "".join(f"<li>{esc(txt(li))}</li>" for li in child.findall("li") if txt(li))
            if items:
                parts.append(f"<ul>{items}</ul>")
        elif child.tag == "a":
            href = child.get("href") or ""
            if href:
                parts.append(f'<a class="m-btn ghost" href="{href}">{esc(txt(child))}</a>')
        elif child.tag == "img":
            parts.append(f'<img src="{child.get("src")}" alt="{esc(child.get("alt") or "")}" loading="lazy">')
        elif child.tag == "div":
            parts.append(render_block(child))
    cls = "m-card checks" if el.find(".//ul") is not None and (el.find(".//ul").get("class") or "") == "checks" else "m-card"
    return f'<div class="{cls}">{"".join(parts)}</div>'


def render_stats(el):
    """div.stats → stacked number cards (mobile can't fit four columns)."""
    out = []
    for st in el.findall('.//div[@class="stat"]'):
        b = st.find("b")
        span = st.find("span")
        num = txt(b) if b is not None else ""
        lab = txt(span) if span is not None else ""
        if not (num or lab):
            continue
        out.append(f'<div class="m-stat"><b>{esc(num)}</b><span>{esc(lab)}</span></div>')
    if not out:
        return ""
    return f'<div class="m-stats">{"".join(out)}</div>'


def raw_form(el):
    """Keep interactive widgets verbatim — the calculator JS depends on classes and ids."""
    inner = LH.tostring(el, encoding="unicode")
    inner = re.sub(r'\sstyle="[^"]*"', "", inner)
    return f'<div class="m-form">{inner}</div>'


def render_block(el, seen=None):
    if seen is None:
        seen = set()
    if is_dropped(el):
        return ""
    cls = classes(el)
    tag = el.tag

    if tag in ("h1", "h2", "h3", "h4", "h5"):
        t = txt(el)
        if not t:
            return ""
        level = {"h1": "h1", "h2": "h2", "h3": "h3", "h4": "h3", "h5": "h3"}[tag]
        return f"<{level}>{esc(t)}</{level}>"

    if tag == "p":
        t = txt(el)
        if not t or t in seen:
            return ""
        seen.add(t)
        if "eyebrow" in cls:
            return f'<p class="eyebrow">{esc(t)}</p>'
        if "tag" in cls:
            return f'<p class="tag">{esc(t)}</p>'
        if "lead" in cls:
            return f'<p class="lead">{esc(t)}</p>'
        return f"<p>{esc(t)}</p>"

    if tag in ("ul", "ol"):
        items = []
        for li in el.findall("li"):
            t = txt(li)
            if t and t not in seen:
                seen.add(t)
                items.append(f"<li>{esc(t)}</li>")
        return f"<ul>{''.join(items)}</ul>" if items else ""

    if tag == "figure":
        return render_figure(el)

    if tag == "img":
        src = el.get("src") or ""
        return f'<img src="{src}" alt="{esc(el.get("alt") or "")}" loading="lazy">' if src else ""

    if tag == "table":
        return render_table(el)

    if tag == "article":
        if "card" in cls:
            return render_card(el)
        return "".join(render_block(c, seen) for c in el)

    if tag == "blockquote":
        t = txt(el)
        return f'<div class="callout"><p>{esc(t)}</p></div>' if t else ""

    if tag == "a":
        href = el.get("href") or ""
        t = txt(el)
        if not href or not t:
            return ""
        if "btn" in cls or "cta" in cls:
            return f'<a class="m-btn" href="{href}">{esc(t)}</a>'
        return f'<p><a href="{href}">{esc(t)}</a></p>'

    if tag in ("form", "input", "select", "textarea", "button", "label"):
        return raw_form(el)

    if tag == "div":
        if "stats" in cls and el.find('.//div[@class="stat"]') is not None:
            return render_stats(el)
        if (
            el.find(".//input") is not None
            or el.find(".//select") is not None
            or el.find(".//textarea") is not None
            or el.find(".//button") is not None
        ):
            return raw_form(el)
        if "card" in cls:
            return render_card(el)
        if "callout" in cls:
            out = "".join(render_block(c, seen) for c in el)
            return f'<div class="callout">{out}</div>'
        if any(c.startswith("grid") for c in cls) or "prose" in cls or "sec-head" in cls or "wrap" in cls:
            return "".join(render_block(c, seen) for c in el)
        if any(c.tag in ("p", "div", "ul", "ol", "h2", "h3", "figure", "table", "img", "a") for c in el):
            return "".join(render_block(c, seen) for c in el)
        t = txt(el)
        return f"<p>{esc(t)}</p>" if t and t not in seen else ""

    return ""


def section_heading(sec):
    for h in sec.iter("h2", "h1"):
        t = txt(h)
        if t:
            return t
    return ""


def build_page(path, lang):
    global CUR_LANG
    CUR_LANG = lang
    doc = LH.parse(path).getroot()
    body = doc.find("body")
    title_el = doc.find(".//title")
    title = txt(title_el) if title_el is not None else "KSTS"
    desc_el = doc.find('.//meta[@name="description"]')
    desc = desc_el.get("content", "") if desc_el is not None else ""

    sections = body.findall(".//section")
    chunks = []
    fold_after = 4
    for i, sec in enumerate(sections):
        sec_cls = classes(sec)
        wrap = sec.find('.//div[@class="wrap"]')
        holder = wrap if wrap is not None else sec
        inner = "".join(render_block(child, set()) for child in holder)
        if not inner.strip():
            continue

        if "page-head" in sec_cls or "hero" in sec_cls:
            chunks.append(f'<div class="mhero">{inner}</div>')
            continue

        tint = " tint" if "alt" in sec_cls else ""
        head = section_heading(sec)
        if i >= fold_after and head:
            inner_folded = re.sub(r"<h2>" + re.escape(esc(head)) + r"</h2>", "", inner, count=1)
            chunks.append(
                f'<section class="m-sec{tint}"><details class="m-fold"><summary>{esc(head)}</summary>'
                f'<div class="fold-body">{inner_folded}</div></details></section>'
            )
        else:
            chunks.append(f'<section class="m-sec{tint}">{inner}</section>')

    return title, desc, "".join(chunks)


def rewrite_paths(html_s, src_dir, out_dir):
    def sub(m):
        attr, val = m.group(1), m.group(2)
        if not val:
            return m.group(0)
        low = val.lower()
        if low.startswith(("http://", "https://", "//", "mailto:", "tel:", "data:", "javascript:", "#", "/")):
            return m.group(0)
        path, sep, frag = val.partition("#")
        if not path:
            return m.group(0)
        target = posixpath.normpath(posixpath.join(src_dir, path))
        new = posixpath.relpath(target, out_dir)
        return f'{attr}="{new}{"#" + frag if sep else ""}"'

    return re.sub(r'(href|src)="([^"]*)"', sub, html_s)


def page_shell(lang, slug, title, desc, content, src_dir, out_dir, canonical):
    ui = UI[lang]
    # language links: same page in another language's mobile edition
    lang_links = ""
    for code in [c for c, _, _ in LANGS if c != lang]:
        out = dict((c, o) for c, _, o in LANGS)[code]
        href = posixpath.relpath(posixpath.join(out, slug), out_dir)
        lang_links += f'<a class="link" href="{href}" hreflang="{code}">{LANG_LABEL[code]}</a>'
    home = posixpath.relpath(posixpath.join(out_dir, "index.html"), out_dir)
    contact = posixpath.relpath(posixpath.join(out_dir, "contact.html"), out_dir)
    desktop_href = posixpath.relpath(posixpath.join(src_dir, slug), out_dir) + "?view=desktop"
    css = posixpath.relpath("assets/css/m.css", out_dir)
    ccss = posixpath.relpath("assets/css/chat.css", out_dir)
    sjs = posixpath.relpath("assets/js/site.js", out_dir)
    cjs = posixpath.relpath("assets/js/chat.js", out_dir)
    calcjs = (
        f'\n<script src="{posixpath.relpath("assets/js/calc.js", out_dir)}"></script>'
        if slug == "calculator.html" else ""
    )

    sheet_items = ""
    for href, *labels in NAV_PAGES:
        label = labels[0] if lang == "en" else (labels[1] if lang == "ms" else labels[2])
        tag = labels[3] if lang == "en" else (labels[4] if lang == "ms" else labels[5])
        cur = " is-cur" if href == slug else ""
        sheet_items += (
            f'<a class="m-sheet-item{cur}" href="{href}">'
            f'<span class="t"><strong>{label}</strong><small>{tag}</small></span>'
            '<span class="chev">›</span></a>'
        )
    foot_links = "".join(
        f'<a class="fnavlink" href="{href}">{labels[0] if lang == "en" else (labels[1] if lang == "ms" else labels[2])}</a>'
        for href, *labels in NAV_PAGES[:5]
    )

    return f"""<!doctype html>
<html lang="{ui['html']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{canonical}">
<link rel="alternate" media="only screen and (max-width: 640px)" href="{canonical}">
<meta name="theme-color" content="#0c1a26">
<meta name="format-detection" content="telephone=no">
<link rel="stylesheet" href="{ccss}">
<link rel="stylesheet" href="{css}">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 34 34'><rect width='34' height='34' rx='9' fill='%230c1a26'/><path d='M17 6.5c3.6 2.4 6 6.2 6 10.2 0 3.3-2.7 6-6 6s-6-2.7-6-6c0-4 2.4-7.8 6-10.2Z' fill='%230f7a52'/></svg>">
</head>
<body>
<div class="mhead">
  <a class="brand" href="{home}">{LOGO}<span>KSTS<small>{ui['brand_sub']}</small></span></a>
  <span class="sp"></span>
  {lang_links}
  <a class="link" href="{desktop_href}">{ui['desktop']}</a>
</div>
{content}
<div class="mfoot">
  <div class="fnav">{foot_links}</div>
  <p style="margin:0 0 8px">KSTS K. S. Technical Services · Sabah, Malaysia</p>
  <p style="margin:0"><a href="mailto:k.s.t.s_sabah@hotmail.com">k.s.t.s_sabah@hotmail.com</a> · <a href="tel:+60138833833">+60 13-883 3833</a></p>
  <p style="margin:8px 0 0;color:#6f8794">© 2026 · {ui['foot']}</p>
</div>
<div class="m-sheet" id="mSheet" hidden>
  <button type="button" class="m-sheet-bd" data-close aria-label="{ui['close']}"></button>
  <div class="m-sheet-panel" role="dialog" aria-modal="true" aria-label="{ui['sheet_title']}">
    <div class="m-sheet-hd"><strong>{ui['sheet_title']}</strong>
      <button type="button" class="m-sheet-x" data-close aria-label="{ui['close']}">✕</button>
    </div>
    <div class="m-sheet-list">
{sheet_items}
    </div>
  </div>
</div>
<div class="mbar">
  <a href="{home}"><span class="ic">⌂</span>{ui['home']}</a>
  <button type="button" class="mbar-prod" id="mProdBtn" aria-expanded="false" aria-controls="mSheet"><span class="ic">▤</span>{ui['solutions']}</button>
  <a class="cta" href="{contact}"><span class="ic">✉</span>{ui['quote']}</a>
</div>
<script src="{sjs}" defer></script>
<script src="{cjs}" defer></script>{calcjs}
<script>
(function(){{
  var b=document.getElementById('mProdBtn'),s=document.getElementById('mSheet');
  if(!b||!s)return;
  function open(){{s.hidden=false;document.body.classList.add('m-lock');b.setAttribute('aria-expanded','true');}}
  function close(){{s.hidden=true;document.body.classList.remove('m-lock');b.setAttribute('aria-expanded','false');}}
  b.addEventListener('click',function(){{s.hidden?open():close();}});
  s.addEventListener('click',function(e){{if(e.target.closest('[data-close]'))close();}});
  s.addEventListener('click',function(e){{var a=e.target.closest('a');if(a)close();}});
  document.addEventListener('keydown',function(e){{if(e.key==='Escape')close();}});
}}());
</script>
</body>
</html>"""


def build_dir(src_dir, out_dir, lang):
    out_abs = os.path.join(ROOT, out_dir)
    os.makedirs(out_abs, exist_ok=True)
    src_abs = os.path.join(ROOT, src_dir) if src_dir else ROOT
    count = 0
    for name in sorted(os.listdir(src_abs)):
        if not name.endswith(".html") or name in SKIP:
            continue
        path = os.path.join(src_abs, name)
        try:
            title, desc, content = build_page(path, lang)
        except Exception as exc:  # noqa: BLE001
            print(f"  ! {name}: {exc}")
            continue
        if not content.strip():
            print(f"  ! {name}: empty content, skipped")
            continue
        canonical = f"{DOMAIN}/{out_dir}/{name}"
        content = rewrite_paths(content, src_dir, out_dir)
        html_out = page_shell(lang, name, title, desc, content, src_dir, out_dir, canonical)
        with open(os.path.join(out_abs, name), "w", encoding="utf-8") as f:
            f.write(html_out)
        count += 1
        print(f"  wrote {out_dir}/{name}  {len(html_out)//1024} KB")
    return count


def main():
    print("building mobile edition →")
    total = 0
    for code, src, out in LANGS:
        total += build_dir(src, out, code)
    print(f"done: {total} mobile pages")


if __name__ == "__main__":
    main()
