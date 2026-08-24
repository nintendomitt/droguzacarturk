# -*- coding: utf-8 -*-
"""
Blog uretici. _build.py'den SONRA calisir; sitemap'e blog URL'lerini ekler.

Tasarim kararlari:
  - Blog ANASAYFADA gorunmez. Kesif: /blog/ hub + sitemap + footer'da tek baglanti.
  - Her yazinin altinda WhatsApp donusum blogu var (GA4 olayi: method='cta').
  - Gelecek tarihli yazilar uretilmez — zamanlanmis gorev tarih geldikce yayinlar.
  - Yazilar hizmet sayfalarina link verir (otorite akisi para sayfalarina dogru).
"""
import os, re, json, html, datetime
from urllib.parse import quote
from _pages import PAGES, SITE
from _build import body_html, wa_link
from _ui import UI

BASE = SITE["base"]
WA = "905449714801"
GA = "G-DNFV21E4BS"
TODAY = datetime.date.today().isoformat()

AY = {1:"Ocak",2:"Şubat",3:"Mart",4:"Nisan",5:"Mayıs",6:"Haziran",
      7:"Temmuz",8:"Ağustos",9:"Eylül",10:"Ekim",11:"Kasım",12:"Aralık"}

def tr_date(d):
    y, m, g = d.split("-")
    return f"{int(g)} {AY[int(m)]} {y}"

def head(title, desc, url, ogtitle, extra=""):
    return f"""<!DOCTYPE html>
<html lang="tr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{html.escape(desc, quote=True)}">
<link rel="canonical" href="{url}">
<meta name="robots" content="index,follow,max-image-preview:large">
<meta property="og:type" content="article">
<meta property="og:locale" content="tr_TR">
<meta property="og:title" content="{html.escape(ogtitle, quote=True)}">
<meta property="og:description" content="{html.escape(desc, quote=True)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{BASE}/assets/og-image.jpg">
<meta name="theme-color" content="#0B1A38">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,500;9..144,600&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../assets/page.css">
{extra}
{ga_snippet()}
</head>
<body>"""

def ga_snippet():
    return (
'<style>#ckb{position:fixed;left:0;right:0;bottom:0;z-index:9999;background:#0B1A38;color:#E6ECF6;'
'padding:14px 18px;display:none;gap:14px;align-items:center;justify-content:center;flex-wrap:wrap;'
'font-size:.86rem;line-height:1.5;box-shadow:0 -2px 18px rgba(0,0,0,.22)}'
'#ckb p{margin:0;max-width:62ch}#ckb .ckbtns{display:flex;gap:9px;flex:none}'
'#ckb button{font:inherit;font-weight:600;border-radius:999px;padding:8px 18px;cursor:pointer;border:1px solid transparent}'
'#ckOk{background:#B8934A;color:#0B1A38}#ckNo{background:transparent;color:#E6ECF6;border-color:rgba(230,236,246,.4)}'
'@media(max-width:640px){#ckb{flex-direction:column;align-items:stretch;text-align:center;padding:15px}'
'#ckb .ckbtns{justify-content:center}}</style>\n'
'<div id="ckb" role="region" aria-label="cookie"><p id="ckt"></p>'
'<div class="ckbtns"><button id="ckOk"></button><button id="ckNo"></button></div></div>\n'
'<script>\n(function(){\n'
'var t=["Bu sitede ziyaret istatistiklerini ölçmek için çerez kullanılıyor. Analitik çerezler yalnızca onayınızla çalışır.","Kabul et","Reddet"],K="ck-consent";\n'
'function loadGA(){if(window.__ga)return;window.__ga=1;'
'var s=document.createElement("script");s.async=1;s.src="https://www.googletagmanager.com/gtag/js?id=' + GA + '";document.head.appendChild(s);'
'window.dataLayer=window.dataLayer||[];window.gtag=function(){dataLayer.push(arguments)};'
'gtag("js",new Date());gtag("config","' + GA + '");}\n'
'function ev(m){if(window.gtag)gtag("event","whatsapp_click",{method:m,page_location:location.pathname,language:"tr"})}\n'
'document.addEventListener("click",function(e){var a=e.target&&e.target.closest?e.target.closest(\'a[href*="wa.me"]\'):null;if(!a)return;'
'ev(a.classList.contains("tb-wa")?"topbar":a.classList.contains("wa-float")?"float":"cta");});\n'
'var c=null;try{c=localStorage.getItem(K)}catch(_){}\n'
'if(c==="1"){loadGA()}else if(c!=="0"){document.addEventListener("DOMContentLoaded",function(){'
'var b=document.getElementById("ckb");if(!b)return;'
'document.getElementById("ckt").textContent=t[0];document.getElementById("ckOk").textContent=t[1];'
'document.getElementById("ckNo").textContent=t[2];b.style.display="flex";'
'document.getElementById("ckOk").onclick=function(){try{localStorage.setItem(K,"1")}catch(_){}b.style.display="none";loadGA()};'
'document.getElementById("ckNo").onclick=function(){try{localStorage.setItem(K,"0")}catch(_){}b.style.display="none"};});}\n'
'})();\n</script>')

def topbar_nav():
    """Hizmet sayfalariyla birebir ayni baslik — yollar ../ ile."""
    return """<div class="topbar"><div class="wrap">
<div class="tb-left"><span>İzmir · Bayraklı</span>
<a class="tb-wa" href="https://wa.me/%s" target="_blank" rel="noopener">WhatsApp ile yazın</a></div>
<div class="langs" role="group" aria-label="Language"><button data-lang="tr" aria-current='true'>TR</button><button data-lang="en">EN</button><button data-lang="de">DE</button><button data-lang="ru">RU</button><button data-lang="ar">AR</button></div>
</div></div>
<header><div class="wrap">
<a class="brand" href="../index.html"><b>Doç. Dr. Tahsin Oğuz Acartürk</b><small>Plastik, Rekonstrüktif ve Estetik Cerrahi</small></a>
<nav class="main" id="nav">
<div class="navdrop"><a href="../lenfodem-lipodem-cerrahisi.html">Lenfödem &amp; Lipödem</a>
<div class="dropm"><a href="../lenfodem-lipodem-cerrahisi.html">Lenfödem cerrahisi</a><a href="../lipodem-cerrahisi.html">Lipödem cerrahisi</a></div></div>
<div class="navdrop"><a href="../index.html#onarim">Onarım</a>
<div class="dropm"><a href="../mikrotia-kulak-onarimi.html">Mikrotia onarımı</a><a href="../yanik-travma-onarimi.html">Yanık ve travma onarımı</a><a href="../bas-boyun-cene-rekonstruksiyonu.html">Baş–boyun onarımı</a><a href="../yuz-felci-tedavisi.html">Yüz felci cerrahisi</a><a href="../meme-rekonstruksiyonu.html">Meme rekonstrüksiyonu</a><a href="../el-cerrahisi-replantasyon.html">El cerrahisi</a></div></div>
<div class="navdrop"><a href="../index.html#estetik">Estetik</a>
<div class="dropm"><a href="../burun-estetigi-rinoplasti.html">Rinoplasti</a><a href="../meme-estetigi.html">Meme estetiği</a><a href="../yuz-germe.html">Yüz germe</a><a href="../goz-kapagi-estetigi.html">Göz kapağı estetiği</a><a href="../karin-germe.html">Karın germe</a><a href="../liposuction-vucut-sekillendirme.html">Liposuction</a><a href="../yag-enjeksiyonu.html">Yağ enjeksiyonu</a><a href="../kol-uyluk-germe.html">Kol ve uyluk germe</a><a href="../jinekomasti.html">Jinekomasti</a><a href="../lip-lift-bisektomi-kulak-estetigi.html">Lip lift · Bişektomi · Otoplasti</a></div></div>
<a href="../index.html#hakkinda">Cerrahınız</a>
<a href="./">Yazılar</a>
<a class="btn btn-p" href="#iletisim">Randevu Al</a>
</nav>
<button class="menu-tgl" id="tgl" aria-label="Menu" aria-expanded="false"><span></span></button>
</div></header>""" % WA

def footer():
    return """<footer><div class="wrap">
<div class="f-row">
<div><strong style="color:#fff">Doç. Dr. Tahsin Oğuz Acartürk</strong><p class="f-id"><span>Plastik, Rekonstrüktif ve Estetik Cerrahi</span><span>Ağız, Yüz ve Çene Cerrahisi</span><span class="f-loc">İzmir · Pittsburgh · Hanoi</span></p></div>
<div><a href="mailto:info@droguzacarturk.com">info@droguzacarturk.com</a><br><a href="../index.html">Anasayfa</a><br><a href="../lenfodem-lipodem-cerrahisi.html">Lenfödem cerrahisi</a><br><a href="./">Yazılar</a></div>
</div>
<p class="disclaimer">Bu sayfadaki içerikler yalnızca genel bilgilendirme amaçlıdır; tıbbi tanı,
tedavi veya reklam niteliği taşımaz ve hekim muayenesinin yerine geçmez. Her hastanın anatomisi,
sağlık geçmişi ve iyileşme süreci farklıdır; sonuçlar kişiden kişiye değişir ve hiçbir sonuç
garanti edilemez. Cerrahi kararlar yalnızca yüz yüze muayene ve gerekli tetkiklerin ardından verilebilir.</p>
<p style="margin-top:16px;font-size:.76rem;color:#7A88A6">© <span id="yr">2026</span> Doç. Dr. Tahsin Oğuz Acartürk</p>
</div></footer>
<a class="wa-float" href="https://wa.me/%s" target="_blank" rel="noopener" aria-label="WhatsApp">
<svg viewBox="0 0 24 24" width="27" height="27" fill="currentColor" aria-hidden="true"><path d="M17.5 14.4c-.3-.2-1.7-.9-2-1-.3-.1-.5-.2-.7.1-.2.3-.7 1-.9 1.2-.2.2-.3.2-.6.1-.3-.2-1.2-.5-2.3-1.4-.9-.8-1.4-1.7-1.6-2-.2-.3 0-.5.1-.6l.5-.5c.1-.2.2-.3.3-.5 0-.2 0-.4 0-.5-.1-.2-.7-1.6-.9-2.2-.2-.6-.5-.5-.7-.5h-.6c-.2 0-.5.1-.8.4-.3.3-1 1-1 2.5s1.1 2.9 1.2 3.1c.2.2 2.1 3.2 5.1 4.4.7.3 1.3.5 1.7.6.7.2 1.4.2 1.9.1.6-.1 1.7-.7 2-1.4.2-.7.2-1.2.2-1.4-.1-.1-.3-.2-.6-.3z"/><path d="M12 2C6.5 2 2 6.5 2 12c0 1.8.5 3.5 1.3 4.9L2 22l5.2-1.3c1.4.8 3 1.2 4.8 1.2 5.5 0 10-4.5 10-10S17.5 2 12 2zm0 18.2c-1.6 0-3.1-.4-4.4-1.2l-.3-.2-3.1.8.8-3-.2-.3c-.9-1.4-1.3-2.9-1.3-4.5 0-4.6 3.8-8.4 8.4-8.4s8.4 3.8 8.4 8.4-3.7 8.4-8.3 8.4z"/></svg></a>
<script>
var y=document.getElementById('yr'); if(y){y.textContent=new Date().getFullYear()}
var t=document.getElementById('tgl'),n=document.getElementById('nav');
if(t&&n){
t.addEventListener('click',function(){var o=n.classList.toggle('open');t.setAttribute('aria-expanded',o)});
n.addEventListener('click',function(e){if(e.target.tagName==='A'){n.classList.remove('open');t.setAttribute('aria-expanded','false')}});
}
/* Blog yazilari yalnizca Turkce. Dil secimi cevirisi olmayan sayfaya degil,
   o dilin anasayfasina goturur — aksi halde 404 olurdu. */
document.querySelectorAll('.langs button').forEach(function(b){
b.addEventListener('click',function(){
var l=b.dataset.lang;
try{localStorage.setItem('lang',l)}catch(e){}
location.href='../'+(l==='tr'?'':l+'/')+'index.html';
});
});
</script>
</body></html>""" % WA

def cta_block(post):
    """Her yazinin altinda: WhatsApp donusum blogu."""
    link = "https://wa.me/%s?text=%s" % (WA, quote(
        "Merhaba, %s için bilgi almak istiyorum." % post["watopic"]))
    return f"""<section class="spot" id="iletisim"><div class="wrap"><div class="narrow">
<span class="tag">Değerlendirme</span>
<h2>Durumunuzu birlikte değerlendirelim</h2>
<p>Şikâyetinizin ne kadar süredir devam ettiğini, geçirdiğiniz tedavileri ve varsa
görüntüleme sonuçlarınızı yazın. Fotoğraf da ekleyebilirsiniz — ön değerlendirme için
bunlar yeterli olur.</p>
<div class="hero-cta">
<a class="btn btn-w btn-lg" href="{link}" target="_blank" rel="noopener">WhatsApp'tan bilgi alın</a>
<a class="btn btn-o btn-lg" href="../#iletisim">Ön değerlendirme formu</a>
</div>
<p class="disc" style="margin-top:18px">Yanıtlar genel bilgilendirme niteliğindedir;
tanı ve tedavi planı ancak muayene sonrası oluşturulur.</p>
</div></div></section>"""

def author_box(post):
    return f"""<section class="alt"><div class="wrap"><div class="narrow prose">
<div class="note"><p><b>Yazan ve tıbbi olarak inceleyen:</b> Doç. Dr. Tahsin Oğuz Acartürk —
Plastik, Rekonstrüktif ve Estetik Cerrahi · Ağız, Yüz ve Çene Cerrahisi üst uzmanlığı ·
Pittsburgh Üniversitesi Baş–Boyun Onarımları eski Direktörü · 300+ mikrocerrahi vaka.
<br><span style="color:var(--muted);font-size:.9rem">Yayın: {tr_date(post['date'])} ·
Son tıbbi inceleme: {tr_date(post['date'])}</span></p></div>
</div></div></section>"""

def related_block(post, index):
    cards = ""
    for k in post.get("related", []):
        if k not in index: continue
        rp = index[k]
        cards += f'<a href="../{rp["slug"]}"><b>{rp["card"]}</b><span>{rp["cardsub"]}</span></a>'
    if not cards: return ""
    return (f'<section><div class="wrap"><div class="narrow prose">'
            f'<span class="tag">İlgili sayfalar</span><h2>Daha ayrıntılı bilgi</h2>'
            f'<div class="rel">{cards}</div></div></div></section>')

def faq_block(post):
    if not post.get("faqs"): return ""
    items = "".join(f'<details{" open" if i==0 else ""}><summary>{q}</summary><p>{a}</p></details>'
                    for i,(q,a) in enumerate(post["faqs"]))
    return (f'<section id="sss" class="alt"><div class="wrap"><div class="narrow">'
            f'<span class="tag">Sık sorulanlar</span>'
            f'<h2 style="margin:0 0 26px">Sık sorulan sorular</h2>{items}</div></div></section>')

def jsonld_post(post, url):
    g = [{"@context":"https://schema.org","@type":"MedicalWebPage",
          "@id":url+"#page","url":url,"name":post["ogtitle"],
          "description":post["desc"],"inLanguage":"tr-TR",
          "datePublished":post["date"],"dateModified":post["date"],
          "author":{"@type":"Physician","name":"Doç. Dr. Tahsin Oğuz Acartürk",
                    "url":BASE+"/","medicalSpecialty":"PlasticSurgery"},
          "reviewedBy":{"@type":"Physician","name":"Doç. Dr. Tahsin Oğuz Acartürk"},
          "publisher":{"@type":"Organization","name":"Doç. Dr. Tahsin Oğuz Acartürk",
                       "url":BASE+"/"},
          "breadcrumb":{"@type":"BreadcrumbList","itemListElement":[
              {"@type":"ListItem","position":1,"name":"Anasayfa","item":BASE+"/"},
              {"@type":"ListItem","position":2,"name":"Yazılar","item":BASE+"/blog/"},
              {"@type":"ListItem","position":3,"name":post["ogtitle"]}]}}]
    if post.get("faqs"):
        g.append({"@context":"https://schema.org","@type":"FAQPage",
                  "@id":url+"#faq","mainEntity":[
                    {"@type":"Question","name":q,
                     "acceptedAnswer":{"@type":"Answer","text":re.sub(r"<[^>]+>","",a)}}
                    for q,a in post["faqs"]]})
    return "\n".join(f'<script type="application/ld+json">{json.dumps(x,ensure_ascii=False)}</script>' for x in g)

def render_post(post, index):
    url = f"{BASE}/blog/{post['slug']}.html"
    parts = [head(post["title"], post["desc"], url, post["ogtitle"], jsonld_post(post, url)),
             topbar_nav(),
             '<main id="main">',
             f'''<section class="hero"><div class="wrap"><div class="narrow">
<nav class="crumbs"><a href="../">Anasayfa</a> › <a href="./">Yazılar</a> › {post["cat"]}</nav>
<span class="tag">{post["cat"]}</span>
<h1>{post["h1"]}</h1>
<p class="lead">{post["lead"]}</p>
</div></div></section>''',
             body_html(post),
             faq_block(post),
             author_box(post),
             related_block(post, index),
             cta_block(post),
             '</main>', footer()]
    return "\n".join(parts)

def render_hub(posts):
    url = f"{BASE}/blog/"
    cards = ""
    for p in posts:
        cards += (f'<a href="{p["slug"]}.html"><b>{p["h1"]}</b>'
                  f'<span>{p["cat"]} · {tr_date(p["date"])}</span></a>')
    ld = {"@context":"https://schema.org","@type":"CollectionPage","url":url,
          "name":"Yazılar — Doç. Dr. Tahsin Oğuz Acartürk","inLanguage":"tr-TR",
          "description":"Lenfödem, lipödem ve mikrocerrahi üzerine hekim tarafından yazılmış bilgilendirme yazıları."}
    return "\n".join([
      head("Yazılar | Doç. Dr. Tahsin Oğuz Acartürk",
           "Lenfödem, lipödem, fil hastalığı ve mikrocerrahi üzerine hekim tarafından yazılmış bilgilendirme yazıları.",
           url, "Yazılar",
           f'<script type="application/ld+json">{json.dumps(ld,ensure_ascii=False)}</script>'),
      topbar_nav(), '<main id="main">',
      f'''<section class="hero"><div class="wrap"><div class="narrow">
<nav class="crumbs"><a href="../">Anasayfa</a> › Yazılar</nav>
<span class="tag">Bilgilendirme</span>
<h1>Yazılar</h1>
<p class="lead">Lenfödem, lipödem ve mikrocerrahi üzerine, hasta sorularından yola çıkarak
yazılmış bilgilendirme metinleri. Her yazı Doç. Dr. Tahsin Oğuz Acartürk tarafından
kaleme alınmış ve tıbbi olarak incelenmiştir.</p>
</div></div></section>''',
      f'<section class="alt"><div class="wrap"><div class="narrow prose"><div class="rel">{cards}</div></div></div></section>',
      '</main>', footer()])

def main():
    from _blog import BLOG
    os.makedirs("blog", exist_ok=True)
    index = {p["key"]: p for p in PAGES}

    live = [p for p in BLOG if p["date"] <= TODAY]
    future = [p for p in BLOG if p["date"] > TODAY]
    live.sort(key=lambda p: p["date"], reverse=True)

    for p in live:
        open(f"blog/{p['slug']}.html","w",encoding="utf-8").write(render_post(p, index))
    open("blog/index.html","w",encoding="utf-8").write(render_hub(live))

    # sitemap'e ekle
    # Hub'in lastmod'u BUGUN degil, en yeni yazinin tarihi olmali. Bugunu yazarsak
    # icerik degismese de sitemap her gun degisir; zamanlanmis yayin is akisi da
    # her calistiginda bos commit atar.
    hub_mod = max((p["date"] for p in live), default=TODAY)
    sm = open("sitemap.xml",encoding="utf-8").read()
    add = [f'  <url>\n    <loc>{BASE}/blog/</loc>\n    <lastmod>{hub_mod}</lastmod>\n'
           f'    <changefreq>weekly</changefreq>\n    <priority>0.6</priority>\n  </url>']
    for p in live:
        add.append(f'  <url>\n    <loc>{BASE}/blog/{p["slug"]}.html</loc>\n'
                   f'    <lastmod>{p["date"]}</lastmod>\n'
                   f'    <changefreq>monthly</changefreq>\n    <priority>0.7</priority>\n  </url>')
    sm = sm.replace("</urlset>", "\n".join(add) + "\n</urlset>")
    open("sitemap.xml","w",encoding="utf-8").write(sm)

    print(f"  blog: {len(live)} yazi yayinda, {len(future)} yazi beklemede")
    if future:
        print("    beklemede:", ", ".join(f"{p['slug']} ({p['date']})" for p in future[:5]))

if __name__ == "__main__":
    main()
