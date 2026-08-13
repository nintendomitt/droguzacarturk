#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hizmet sayfasi ureticisi.

Sayfa iceriklerini _pages.py icinde tanimlar, buradaki sablonla HTML uretir.
Kullanim:  python3 _build.py
Yeni sayfa eklemek icin _pages.py icindeki PAGES listesine bir kayit ekleyin
ve bu betigi tekrar calistirin. Elle HTML duzenlemeyin.
"""
import json, os, html, re
from _pages import PAGES, SITE, EXTRA_REFS

WA = "https://wa.me/905449714801"
BASE = SITE["base"]


def wa_link(topic):
    from urllib.parse import quote
    msg = f"Merhaba, {topic} hakkında bilgi almak istiyorum."
    return f"{WA}?text={quote(msg)}"


def jsonld(p):
    url = f"{BASE}/{p['slug']}"
    graph = [{
        "@type": "MedicalWebPage",
        "@id": url + "#page",
        "url": url,
        "name": p["h1"],
        "inLanguage": "tr-TR",
        "datePublished": SITE["published"],
        "dateModified": SITE["modified"],
        "lastReviewed": SITE["modified"],
        "reviewedBy": {"@id": BASE + "/#physician"},
        "author": {"@id": BASE + "/#physician"},
        "publisher": {"@id": BASE + "/#physician"},
        "specialty": "PlasticSurgery",
        "about": {"@type": p.get("aboutType", "MedicalCondition"), "name": p["about"]},
        "isPartOf": {"@type": "WebSite", "@id": BASE + "/#website"},
    }, {
        "@type": "Physician",
        "@id": BASE + "/#physician",
        "name": "Doç. Dr. Tahsin Oğuz Acartürk",
        "url": BASE + "/",
        "medicalSpecialty": "PlasticSurgery",
        "address": {
            "@type": "PostalAddress",
            "streetAddress": "Bayraklı Tower, Mansuroğlu Mah. Ankara Cad. No:81 İç Kapı No:23",
            "addressLocality": "Bayraklı", "addressRegion": "İzmir",
            "postalCode": "35030", "addressCountry": "TR"},
    }]
    if p.get("procedure"):
        graph.append({
            "@type": "MedicalProcedure",
            "name": p["procedure"]["name"],
            "procedureType": "https://schema.org/SurgicalProcedure",
            "howPerformed": p["procedure"]["how"],
            "preparation": p["procedure"].get("prep", ""),
            "followup": p["procedure"].get("follow", ""),
            "bodyLocation": p["procedure"].get("body", ""),
        })
    if p.get("faqs"):
        graph.append({"@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in p["faqs"]]})
    graph.append({"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Anasayfa", "item": BASE + "/"},
        {"@type": "ListItem", "position": 2, "name": p["crumb"], "item": url}]})
    return json.dumps({"@context": "https://schema.org", "@graph": graph},
                      ensure_ascii=False, separators=(",", ":"))


def body_html(p):
    out = []
    for i, sec in enumerate(p["sections"]):
        alt = ' class="alt"' if i % 2 == 0 else ""
        sid = sec.get("id", f"b{i+1}")
        out.append(f'<section id="{sid}"{alt}><div class="wrap"><div class="narrow prose">')
        out.append(f'<span class="tag">{sec["tag"]}</span>')
        out.append(f'<h2>{sec["h2"]}</h2>')
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
                head, rows = blk[1], blk[2]
                t = ["<table><thead><tr>" + "".join(f"<th>{c}</th>" for c in head) + "</tr></thead><tbody>"]
                for r in rows:
                    t.append("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>")
                t.append("</tbody></table>")
                out.append("".join(t))
            elif blk[0] == "steps":
                out.append('<ul class="tlmap">' + "".join(
                    f"<li><b>{a}</b><span>{b}</span></li>" for a, b in blk[1]) + "</ul>")
        out.append("</div></div></section>")
    return "\n".join(out)


def render(p, index):
    url = f"{BASE}/{p['slug']}"
    kf = ""
    if p.get("keyfacts"):
        kf = '<div class="keyfacts">' + "".join(
            f'<div class="kf"><b>{a}</b><span>{b}</span></div>' for a, b in p["keyfacts"]) + "</div>"
    toc = "".join(f'<li><a href="#{s.get("id", f"b{i+1}")}">{s["h2"]}</a></li>'
                  for i, s in enumerate(p["sections"]))
    faq = ""
    if p.get("faqs"):
        items = "".join(
            f'<details{" open" if i == 0 else ""}><summary>{q}</summary><p>{a}</p></details>'
            for i, (q, a) in enumerate(p["faqs"]))
        faq = ('<section id="sss"><div class="wrap"><div class="narrow">'
               '<span class="tag">S.S.S.</span><h2 style="margin:0 0 26px">Sık sorulan sorular</h2>'
               f"{items}</div></div></section>")
    rel = ""
    if p.get("related"):
        cards = "".join(
            f'<a href="{index[s]["slug"]}"><b>{index[s]["card"]}</b>'
            f'<span>{index[s]["cardsub"]}</span></a>' for s in p["related"] if s in index)
        rel = ('<section class="alt"><div class="wrap"><div class="narrow prose">'
               '<span class="tag">İlgili</span><h2>İlgili uzmanlık alanları</h2>'
               f'<div class="rel">{cards}</div></div></div></section>')
    return f"""<!DOCTYPE html>
<html lang="tr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{p['title']}</title>
<meta name="description" content="{html.escape(p['desc'], quote=True)}">
<link rel="canonical" href="{url}">
<meta name="robots" content="index,follow,max-image-preview:large">
<link rel="alternate" hreflang="tr" href="{url}">
<link rel="alternate" hreflang="x-default" href="{url}">
<meta property="og:type" content="article">
<meta property="og:locale" content="tr_TR">
<meta property="og:title" content="{html.escape(p['ogtitle'], quote=True)}">
<meta property="og:description" content="{html.escape(p['desc'], quote=True)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{BASE}/assets/og-image.jpg">
<meta name="theme-color" content="#0B1A38">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,500;9..144,600&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/page.css">
<script type="application/ld+json">{jsonld(p)}</script>
</head>
<body>
<div class="topbar"><div class="wrap">
<span>İzmir · Bayraklı Tower</span>
<a href="{WA}" target="_blank" rel="noopener">WhatsApp ile yazın</a>
</div></div>
<header><div class="wrap">
<a class="brand" href="index.html"><b>Doç. Dr. Tahsin Oğuz Acartürk</b><small>Plastik, Rekonstrüktif ve Estetik Cerrahi</small></a>
<a class="btn btn-p" href="#randevu">Randevu Al</a>
</div></header>
<div class="wrap"><nav class="crumb" aria-label="breadcrumb"><a href="index.html">Anasayfa</a> &rsaquo; <span>{p['crumb']}</span></nav></div>
<main>
<div class="hero2"><div class="wrap">
<p class="eyebrow">{p['eyebrow']}</p>
<h1>{p['h1']}</h1>
<p class="lead">{p['lead']}</p>
<div class="hcta">
<a class="btn btn-w btn-lg" href="{wa_link(p['watopic'])}" target="_blank" rel="noopener">WhatsApp'tan bilgi alın</a>
<a class="btn btn-o btn-lg" href="index.html#iletisim">Ön değerlendirme formu</a>
</div>
<p style="font-size:.83rem;color:var(--muted);margin-top:22px;padding-top:16px;border-top:1px solid var(--line)">Yazan ve tıbbi olarak inceleyen: <strong style="color:var(--ink)">Doç. Dr. Tahsin Oğuz Acartürk</strong> — Plastik, Rekonstrüktif ve Estetik Cerrahi; Pittsburgh Üniversitesi. <span style="white-space:nowrap">Son güncelleme: <time datetime="{SITE['modified']}">{SITE['modifiedtr']}</time></span></p>
{kf}
<div class="toc"><b>Bu sayfada</b><ol>{toc}</ol></div>
</div></div>
{body_html(p)}
{faq}
{rel}
<section class="cta" id="randevu"><div class="wrap">
<h2>{p['ctah']}</h2>
<p>{p['ctap']}</p>
<div class="hcta">
<a class="btn btn-w btn-lg" href="{wa_link(p['watopic'])}" target="_blank" rel="noopener">WhatsApp'tan yazın</a>
<a class="btn btn-o btn-lg" href="index.html#iletisim">Randevu formu</a>
</div>
</div></section>
</main>
<footer><div class="wrap">
<div class="f-row">
<div><strong style="color:#fff">Doç. Dr. Tahsin Oğuz Acartürk</strong><br>Bayraklı Tower, Mansuroğlu Mah. Ankara Cad. No:81 İç Kapı No:23 · Bayraklı / İzmir</div>
<div><a href="mailto:info@droguzacarturk.com">info@droguzacarturk.com</a><br><a href="index.html">Anasayfa</a><br><a href="index.html#uzmanlik">Uzmanlık alanları</a></div>
</div>
<p class="disclaimer">Bu sayfadaki içerikler yalnızca genel bilgilendirme amaçlıdır; tıbbi tanı, tedavi veya reklam niteliği taşımaz ve hekim muayenesinin yerine geçmez. Her hastanın anatomisi, sağlık geçmişi ve iyileşme süreci farklıdır; sonuçlar kişiden kişiye değişir ve hiçbir sonuç garanti edilemez. Cerrahi kararlar yalnızca yüz yüze muayene ve gerekli tetkiklerin ardından verilebilir. Son gözden geçirme: {SITE['modifiedtr']}.</p>
<p style="margin-top:16px;font-size:.76rem;color:#7A88A6">© <span id="yr">2026</span> Doç. Dr. Tahsin Oğuz Acartürk</p>
</div></footer>
<div class="sticky">
<a class="btn btn-w" href="{wa_link(p['watopic'])}" target="_blank" rel="noopener">WhatsApp</a>
<a class="btn btn-p" href="index.html#iletisim">Randevu Formu</a>
</div>
<script>document.getElementById('yr').textContent=new Date().getFullYear();</script>
</body>
</html>
"""


def main():
    index = {p["key"]: p for p in PAGES}
    for r in EXTRA_REFS:
        index.setdefault(r["key"], r)
    for p in PAGES:
        out = render(p, index)
        with open(p["slug"], "w", encoding="utf-8") as f:
            f.write(out)
        words = len(re.sub(r"<[^>]+>", " ", out).split())
        print(f"  {p['slug']:44} {len(out)//1024:3d} KB  ~{words} kelime")

    # sitemap
    urls = [("", "1.0", "monthly"), ("lenfodem-lipodem-cerrahisi", "0.9", "monthly")]
    urls += [(p["slug"].replace(".html", ""), p.get("prio", "0.8"), "monthly") for p in PAGES]
    x = ['<?xml version="1.0" encoding="UTF-8"?>',
         '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">']
    for loc, prio, freq in urls:
        u = BASE + "/" + loc
        x.append("  <url>")
        x.append(f"    <loc>{u}</loc>")
        x.append(f"    <lastmod>{SITE['modified']}</lastmod>")
        x.append(f"    <changefreq>{freq}</changefreq>")
        x.append(f"    <priority>{prio}</priority>")
        if loc == "":
            for lg in ("tr", "en", "de", "ru", "ar"):
                href = BASE + "/" if lg == "tr" else f"{BASE}/{lg}/"
                x.append(f'    <xhtml:link rel="alternate" hreflang="{lg}" href="{href}"/>')
            x.append(f'    <xhtml:link rel="alternate" hreflang="x-default" href="{BASE}/"/>')
        x.append("  </url>")
    x.append("</urlset>")
    open("sitemap.xml", "w", encoding="utf-8").write("\n".join(x) + "\n")
    print(f"\n  sitemap.xml: {len(urls)} URL")


if __name__ == "__main__":
    main()
