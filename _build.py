#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Cok dilli hizmet sayfasi ureticisi.

  Turkce icerik : _pages_micro.py / _pages_estetik.py
  Ceviriler     : _trans/<dil>.py  ->  T = {"<key>": {...cevrilmis alanlar...}}
  Arayuz metni  : _ui.py

Kullanim:  python3 _build.py

Turkce sayfalar kok dizine, cevirilenler /en/, /de/, /ru/, /ar/ altina yazilir.
Cevirisi olmayan sayfa o dilde uretilmez ve hreflang'e eklenmez.
Elle HTML duzenlemeyin; bu betigi calistirin.
"""
import json, os, html, importlib.util
from _pages import PAGES, SITE, EXTRA_REFS
from _ui import UI, LANGS, LANGNAME, RTL, LOCALE, DATE_TR

WA = "https://wa.me/905449714801"
BASE = SITE["base"]
FIELDS = ("title", "ogtitle", "desc", "crumb", "h1", "lead", "eyebrow", "watopic",
          "about", "card", "cardsub", "authority", "creds", "keyfacts", "sections",
          "faqs", "ctah", "ctap", "procedure")
_AVAIL = {}


def load_trans():
    out = {}
    for lg in LANGS:
        if lg == "tr":
            continue
        merged_t = {}
        import glob
        for path in sorted(glob.glob(os.path.join("_trans", lg + "*.py"))):
            name = os.path.basename(path)[:-3]
            spec = importlib.util.spec_from_file_location("t_" + name, path)
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
            merged_t.update(getattr(mod, "T", {}))
        out[lg] = merged_t
    return out


def merged(p, trans, lg):
    if lg == "tr":
        return p
    t = trans.get(lg, {}).get(p["key"])
    if not t:
        return None
    m = dict(p)
    for f in FIELDS:
        if f in t:
            m[f] = t[f]
    return m


def url_for(p, lg):
    return f"{BASE}/{p['slug']}" if lg == "tr" else f"{BASE}/{lg}/{p['slug']}"


def wa_link(topic, lg):
    from urllib.parse import quote
    return f"{WA}?text={quote(UI[lg]['wamsg'].format(t=topic))}"


def jsonld(p, lg, url):
    u = UI[lg]
    graph = [{
        "@type": "MedicalWebPage", "@id": url + "#page", "url": url, "name": p["h1"],
        "inLanguage": lg, "datePublished": SITE["published"], "dateModified": SITE["modified"],
        "lastReviewed": SITE["modified"],
        "reviewedBy": {"@id": BASE + "/#physician"}, "author": {"@id": BASE + "/#physician"},
        "publisher": {"@id": BASE + "/#physician"}, "specialty": "PlasticSurgery",
        "about": {"@type": p.get("aboutType", "MedicalCondition"), "name": p["about"]},
        "isPartOf": {"@type": "WebSite", "@id": BASE + "/#website"},
    }, {
        "@type": "Physician", "@id": BASE + "/#physician",
        "name": "Doç. Dr. Tahsin Oğuz Acartürk", "url": BASE + "/",
        "medicalSpecialty": "PlasticSurgery",
        "address": {"@type": "PostalAddress",
                    "streetAddress": "Bayraklı Tower, Mansuroğlu Mah. Ankara Cad. No:81 İç Kapı No:23",
                    "addressLocality": "Bayraklı", "addressRegion": "İzmir",
                    "postalCode": "35030", "addressCountry": "TR"},
    }]
    if p.get("procedure"):
        pr = p["procedure"]
        graph.append({"@type": "MedicalProcedure", "name": pr["name"],
                      "procedureType": "https://schema.org/SurgicalProcedure",
                      "howPerformed": pr["how"], "preparation": pr.get("prep", ""),
                      "followup": pr.get("follow", ""), "bodyLocation": pr.get("body", "")})
    if p.get("faqs"):
        graph.append({"@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in p["faqs"]]})
    graph.append({"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": u["home"], "item": BASE + "/"},
        {"@type": "ListItem", "position": 2, "name": p["crumb"], "item": url}]})
    return json.dumps({"@context": "https://schema.org", "@graph": graph},
                      ensure_ascii=False, separators=(",", ":"))


def body_html(p):
    out = []
    for i, sec in enumerate(p["sections"]):
        alt = ' class="alt"' if i % 2 == 0 else ""
        sid = sec.get("id", f"b{i+1}")
        out.append(f'<section id="{sid}"{alt}><div class="wrap"><div class="narrow prose">')
        out.append(f'<span class="tag">{sec["tag"]}</span><h2>{sec["h2"]}</h2>')
        for blk in sec["body"]:
            if isinstance(blk, str):
                out.append(f"<p>{blk}</p>")
            elif blk[0] == "ul":
                out.append("<ul>" + "".join(f"<li>{x}</li>" for x in blk[1]) + "</ul>")
            elif blk[0] == "h3":
                out.append(f"<h3>{blk[1]}</h3>")
            elif blk[0] == "note":
                out.append(f'<div class="note"><p>{blk[1]}</p></div>')
            elif blk[0] == "table":
                t = ["<table><thead><tr>" + "".join(f"<th>{c}</th>" for c in blk[1]) + "</tr></thead><tbody>"]
                for r in blk[2]:
                    t.append("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>")
                out.append('<div class="tw">' + "".join(t) + "</tbody></table></div>")
            elif blk[0] == "steps":
                out.append('<ul class="tlmap">' + "".join(
                    f"<li><b>{a}</b><span>{b}</span></li>" for a, b in blk[1]) + "</ul>")
        out.append("</div></div></section>")
    return "\n".join(out)


def render(p, lg, index, avail):
    u, url = UI[lg], url_for(p, lg)
    A = "" if lg == "tr" else "../"
    home = A + "index.html"
    rtl = ' dir="rtl"' if lg in RTL else ""
    arfont = ("&family=Noto+Kufi+Arabic:wght@400;500;600;700"
              "&family=Noto+Sans+Arabic:wght@300;400;500;600") if lg in RTL else ""

    alts = "".join(f'<link rel="alternate" hreflang="{l}" href="{url_for(p, l)}">' for l in avail)
    alts += f'<link rel="alternate" hreflang="x-default" href="{url_for(p, "tr")}">'
    langbtns = "".join(
        '<button data-lang="%s"%s%s>%s</button>' % (
            l, " aria-current='true'" if l == lg else "",
            "" if l in avail else ' data-nopage="1"', LANGNAME[l]) for l in LANGS)
    def _links(keys):
        return "".join(
            f'<a href="{A}{index[k]["slug"]}">{index[k]["card"]}</a>'
            for k in keys if k in index)
    drop1 = _links(("lenfodem", "lipodem"))
    drop2 = _links(("mikrotia", "yanik", "bas-boyun", "yuz-felci", "meme-rek", "el-cerrahisi"))
    drop3 = _links(("rinoplasti", "meme-estetigi", "yuz-germe", "goz-kapagi", "karin-germe",
                    "liposuction", "yag-enjeksiyonu", "kol-uyluk-germe", "jinekomasti", "lip-lift"))

    kf = ""
    if p.get("keyfacts"):
        kf = '<div class="keyfacts">' + "".join(
            f'<div class="kf"><b>{a}</b><span>{b}</span></div>' for a, b in p["keyfacts"]) + "</div>"
    toc = "".join(f'<li><a href="#{s.get("id", f"b{i+1}")}">{s["h2"]}</a></li>'
                  for i, s in enumerate(p["sections"]))
    faq = ""
    if p.get("faqs"):
        items = "".join(f'<details{" open" if i == 0 else ""}><summary>{q}</summary><p>{a}</p></details>'
                        for i, (q, a) in enumerate(p["faqs"]))
        faq = (f'<section id="sss"><div class="wrap"><div class="narrow"><span class="tag">{u["faqtag"]}</span>'
               f'<h2 style="margin:0 0 26px">{u["faqh"]}</h2>{items}</div></div></section>')
    rel = ""
    if p.get("related"):
        cards = ""
        for k in p["related"]:
            if k not in index:
                continue
            rp = index[k]
            href = rp["slug"] if k in _AVAIL.get(lg, set()) else A + rp["slug"]
            cards += f'<a href="{href}"><b>{rp["card"]}</b><span>{rp["cardsub"]}</span></a>'
        rel = (f'<section class="alt"><div class="wrap"><div class="narrow prose">'
               f'<span class="tag">{u["reltag"]}</span><h2>{u["relh"]}</h2>'
               f'<div class="rel">{cards}</div></div></div></section>')

    creds = "".join(f"<li>{c}</li>" for c in p.get("creds", []))
    surgeon = f'''<section id="cerrah"><div class="wrap"><div class="narrow">
<span class="tag">{u["surgtag"]}</span>
<h2 style="margin:0 0 8px">Doç. Dr. Tahsin Oğuz Acartürk</h2>
<p style="font-size:.86rem;color:var(--muted);margin-bottom:22px">{u["surgsub"]}</p>
<div class="surg">
<div class="surg-img"><img src="{A}assets/dr-acarturk.webp" width="900" height="1125" loading="lazy" decoding="async" alt="Doç. Dr. Tahsin Oğuz Acartürk"></div>
<div class="surg-txt">
<p><strong>{u["surgexp"]}</strong> {p.get("authority","")}</p>
<ul class="surg-cred">{creds}</ul>
<a class="btn btn-o" href="{home}#hakkinda">{u["surgcv"]}</a>
</div></div></div></div></section>'''

    return f"""<!DOCTYPE html>
<html lang="{lg}"{rtl}>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{p['title']}</title>
<meta name="description" content="{html.escape(p['desc'], quote=True)}">
<link rel="canonical" href="{url}">
<meta name="robots" content="index,follow,max-image-preview:large">
{alts}
<meta property="og:type" content="article">
<meta property="og:locale" content="{LOCALE[lg]}">
<meta property="og:title" content="{html.escape(p['ogtitle'], quote=True)}">
<meta property="og:description" content="{html.escape(p['desc'], quote=True)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{BASE}/assets/og-image.jpg">
<meta name="theme-color" content="#0B1A38">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,500;9..144,600&family=Inter:wght@300;400;500;600{arfont}&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{A}assets/page.css">
<script type="application/ld+json">{jsonld(p, lg, url)}</script>
<script async src="https://www.googletagmanager.com/gtag/js?id=G-DNFV21E4BS"></script>
<script>
window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments)}}
gtag('js',new Date());gtag('config','G-DNFV21E4BS');
document.addEventListener('click',function(e){{
var a=e.target&&e.target.closest?e.target.closest('a[href*="wa.me"]'):null;if(!a)return;
var m=a.classList.contains('tb-wa')?'topbar':a.classList.contains('wa-float')?'float':'cta';
gtag('event','whatsapp_click',{{method:m,page_location:location.pathname,language:document.documentElement.lang}});
}});
</script>
</head>
<body>
<div class="topbar"><div class="wrap">
<div class="tb-left"><span>{u['loc']}</span>
<a class="tb-wa" href="{WA}" target="_blank" rel="noopener">{u['wa']}</a></div>
<div class="langs" role="group" aria-label="Language">{langbtns}</div>
</div></div>
<header><div class="wrap">
<a class="brand" href="{home}"><b>Doç. Dr. Tahsin Oğuz Acartürk</b><small>{u['sub']}</small></a>
<nav class="main" id="nav">
<div class="navdrop"><a href="{A}lenfodem-lipodem-cerrahisi.html">{u['g1']}</a>
<div class="dropm">{drop1}</div></div>
<div class="navdrop"><a href="{home}#onarim">{u['g2']}</a>
<div class="dropm">{drop2}</div></div>
<div class="navdrop"><a href="{home}#estetik">{u['g3']}</a>
<div class="dropm">{drop3}</div></div>
<a href="{home}#hakkinda">{u['nav2']}</a>
<a href="#sss">{u['nav3']}</a>
<a class="btn btn-p" href="#randevu">{u['cta']}</a>
</nav>
<button class="menu-tgl" id="tgl" aria-label="Menu" aria-expanded="false"><span></span></button>
</div></header>
<div class="wrap"><nav class="crumb" aria-label="breadcrumb"><a href="{home}">{u['home']}</a> &rsaquo; <span>{p['crumb']}</span></nav></div>
<main>
<div class="hero2"><div class="wrap">
<p class="eyebrow">{p['eyebrow']}</p>
<h1>{p['h1']}</h1>
<p class="lead">{p['lead']}</p>
<div class="hcta">
<a class="btn btn-w btn-lg" href="{wa_link(p['watopic'], lg)}" target="_blank" rel="noopener">{u['wabtn']}</a>
<a class="btn btn-o btn-lg" href="{home}#iletisim">{u['formbtn']}</a>
</div>
<p style="font-size:.83rem;color:var(--muted);margin-top:22px;padding-top:16px;border-top:1px solid var(--line)">{u['byline']} <strong style="color:var(--ink)">Doç. Dr. Tahsin Oğuz Acartürk</strong> — {u['bylinesub']} <span style="white-space:nowrap">{u['updated']} <time datetime="{SITE['modified']}">{DATE_TR[lg]}</time></span></p>
{kf}
<div class="toc"><b>{u['toc']}</b><ol>{toc}</ol></div>
</div></div>
{body_html(p)}
{faq}
{surgeon}
{rel}
<section class="cta" id="randevu"><div class="wrap">
<h2>{p['ctah']}</h2>
<p>{p['ctap']}</p>
<div class="hcta">
<a class="btn btn-w btn-lg" href="{wa_link(p['watopic'], lg)}" target="_blank" rel="noopener">{u['wabtn2']}</a>
<a class="btn btn-o btn-lg" href="{home}#iletisim">{u['formbtn2']}</a>
</div>
</div></section>
</main>
<footer><div class="wrap">
<div class="f-row">
<div><strong style="color:#fff">Doç. Dr. Tahsin Oğuz Acartürk</strong><p class="f-id"><span>{u['sub']}</span><span>{u['spec2']}</span><span class="f-loc">{u['loc3']}</span></p></div>
<div><a href="mailto:info@droguzacarturk.com">info@droguzacarturk.com</a><br><a href="{home}">{u['home']}</a><br><a href="{home}#uzmanlik">{u['expertise']}</a></div>
</div>
<p class="disclaimer">{u['disc']} {u['review']} {DATE_TR[lg]}.</p>
<p style="margin-top:16px;font-size:.76rem;color:#7A88A6">© <span id="yr">2026</span> Doç. Dr. Tahsin Oğuz Acartürk</p>
</div></footer>
<div class="sticky">
<a class="btn btn-w" href="{wa_link(p['watopic'], lg)}" target="_blank" rel="noopener">WhatsApp</a>
<a class="btn btn-p" href="{home}#iletisim">{u['formbtn2']}</a>
</div>
<script>
document.getElementById('yr').textContent=new Date().getFullYear();
var t=document.getElementById('tgl'),n=document.getElementById('nav');
if(t&&n){{
t.addEventListener('click',function(){{var o=n.classList.toggle('open');t.setAttribute('aria-expanded',o)}});
n.addEventListener('click',function(e){{if(e.target.tagName==='A'){{n.classList.remove('open');t.setAttribute('aria-expanded','false')}}}});
}}
document.querySelectorAll('.langs button').forEach(function(b){{
b.addEventListener('click',function(){{
var l=b.dataset.lang,f=location.pathname.split('/').pop()||'index.html';
try{{localStorage.setItem('lang',l)}}catch(e){{}}
var base='{A}';
if(b.dataset.nopage){{location.href=(l==='tr'?base:base+l+'/')+'index.html';return}}
location.href=(l==='tr'?base:base+l+'/')+f;
}});
}});
</script>
</body>
</html>
"""


def main():
    trans = load_trans()
    index = {p["key"]: p for p in PAGES}
    for r in EXTRA_REFS:
        index.setdefault(r["key"], r)

    for lg in LANGS:
        _AVAIL[lg] = {p["key"] for p in PAGES if merged(p, trans, lg)}

    total = 0
    for p in PAGES:
        avail = [l for l in LANGS if p["key"] in _AVAIL[l]]
        for lg in avail:
            m = merged(p, trans, lg)
            d = "" if lg == "tr" else lg
            if d:
                os.makedirs(d, exist_ok=True)
            path = os.path.join(d, p["slug"]) if d else p["slug"]
            open(path, "w", encoding="utf-8").write(render(m, lg, index, avail))
            total += 1
        if len(avail) > 1:
            print(f"  {p['slug']:42} {' '.join(avail)}")

    x = ['<?xml version="1.0" encoding="UTF-8"?>',
         '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">',
         "  <url>", f"    <loc>{BASE}/</loc>", f"    <lastmod>{SITE['modified']}</lastmod>",
         "    <changefreq>monthly</changefreq>", "    <priority>1.0</priority>"]
    for lg in LANGS:
        href = BASE + "/" if lg == "tr" else f"{BASE}/{lg}/"
        x.append(f'    <xhtml:link rel="alternate" hreflang="{lg}" href="{href}"/>')
    x += [f'    <xhtml:link rel="alternate" hreflang="x-default" href="{BASE}/"/>', "  </url>",
          "  <url>", f"    <loc>{BASE}/lenfodem-lipodem-cerrahisi.html</loc>",
          f"    <lastmod>{SITE['modified']}</lastmod>", "    <changefreq>monthly</changefreq>",
          "    <priority>0.9</priority>", "  </url>"]
    n = 2
    for p in PAGES:
        avail = [l for l in LANGS if p["key"] in _AVAIL[l]]
        for lg in avail:
            x.append("  <url>")
            x.append(f"    <loc>{url_for(p, lg)}</loc>")
            x.append(f"    <lastmod>{SITE['modified']}</lastmod>")
            x.append("    <changefreq>monthly</changefreq>")
            x.append(f"    <priority>{p.get('prio','0.8')}</priority>")
            for l2 in avail:
                x.append(f'    <xhtml:link rel="alternate" hreflang="{l2}" href="{url_for(p, l2)}"/>')
            x.append("  </url>")
            n += 1
    x.append("</urlset>")
    open("sitemap.xml", "w", encoding="utf-8").write("\n".join(x) + "\n")
    print(f"\n  toplam {total} sayfa · sitemap {n} URL")

    # Dil klasorlerine index.html — /en, /de, /ru, /ar bos kalmasin.
    # Eski Wix sitesinde Ingilizce icerik /en yolundaydi; o adres canli kalmali.
    LANGNAMES = {"en": "English", "de": "Deutsch", "ru": "Русский", "ar": "العربية"}
    for lg in [l for l in LANGS if l != "tr"]:
        os.makedirs(lg, exist_ok=True)
        rtl = ' dir="rtl"' if lg in RTL else ""
        html_doc = (
            '<!doctype html>\n<html lang="%s"%s>\n<head>\n<meta charset="utf-8">\n'
            '<title>%s — Assoc. Prof. Dr. T. Oguz Acarturk</title>\n'
            '<link rel="canonical" href="%s/">\n'
            '<meta name="robots" content="noindex, follow">\n'
            '<meta http-equiv="refresh" content="0; url=/">\n'
            '<style>body{font-family:system-ui,-apple-system,\'Segoe UI\',Roboto,sans-serif;'
            'background:#0B1A38;color:#fff;display:flex;align-items:center;justify-content:center;'
            'min-height:100vh;margin:0;text-align:center;padding:24px}a{color:#B8934A}</style>\n'
            '</head>\n<body>\n'
            '<p>Redirecting… <a href="/">Continue</a></p>\n'
            '<script>try{localStorage.setItem("lang","%s")}catch(e){}location.replace("/");</script>\n'
            '</body>\n</html>\n'
        ) % (lg, rtl, LANGNAMES.get(lg, lg), SITE["base"], lg)
        open(os.path.join(lg, "index.html"), "w", encoding="utf-8").write(html_doc)
    print(f"  dil klasoru index.html: {len(LANGS)-1} adet")


if __name__ == "__main__":
    main()
