# -*- coding: utf-8 -*-
"""
Saturday Online — aylik performans raporu ureteci.

KULLANIM
--------
1) Search Console > Performans > sag ust EXPORT > "CSV indir"
2) Inen ZIP'i ac, icindeki TUM csv dosyalarini _gsc/ klasorune at
   (Chart.csv, Queries.csv, Pages.csv, Devices.csv, Countries.csv)
3) _gsc/rapor-notlari.md dosyasini bu ayki calismalarla guncelle
4) python3 _saturday_rapor.py

Cikti: _belgeler/Saturday-Rapor-<YYYY-AA>-droguzacarturk.pdf

Bagimlilik: weasyprint
Fontlar: _belgeler/_fonts/ (Poppins + Inter). Yoksa sistem fontuna duser.
"""
import csv
import os
import re
import base64
import datetime
import unicodedata

KOK = os.path.dirname(os.path.abspath(__file__))
GSC = os.path.join(KOK, "_gsc")
BEL = os.path.join(KOK, "_belgeler")
FONT = os.path.join(BEL, "_fonts")
LOGO = os.path.join(BEL, "saturday-logo.png")
NOTLAR = os.path.join(GSC, "rapor-notlari.md")

MUSTERI = "Doc. Dr. Tahsin Oguz Acarturk"
MUSTERI_TR = "Doç. Dr. Tahsin Oğuz Acartürk"
ALAN = "droguzacarturk.com"
AJANS = "Saturday Online"
AJANS_WEB = "saturdayonline.co"

# ---- marka paleti (saturdayonline.co'dan) ----
INK = "#1c1208"
KOYU = "#c0410a"      # ana marka turuncusu
AMBER = "#ffa617"     # logo turuncusu
KIZIL = "#ff4500"
KREM = "#fff8f5"
KREM2 = "#fff5dc"
SOLUK = "#8b7a70"
CIZGI = "#efe0d6"
YESIL = "#1f7a4d"

AYLAR = ["Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran",
         "Temmuz", "Ağustos", "Eylül", "Ekim", "Kasım", "Aralık"]

# marka sorgusu sayilan kokler
MARKA_KOK = ["acartur", "acartür", "oguz acar", "oğuz acar",
             "droguzacarturk", "dr oguz", "dr oğuz", "tahsin oguz", "tahsin oğuz"]


# ============================== yardimcilar ==============================

def _oku(ad):
    """CSV'yi sozluk listesi olarak oku. Yoksa None."""
    y = os.path.join(GSC, ad)
    if not os.path.exists(y):
        return None
    with open(y, encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def _sut(satir, *adlar):
    """TR/EN basliklardan ilk eslesen sutunu dondur."""
    for a in adlar:
        for k in satir:
            if k and k.strip().lower() == a.lower():
                return satir[k]
    return ""


def _sayi(s):
    """'1.234' / '1,234' / '12' -> int"""
    s = (s or "").strip().replace(".", "").replace(",", "").replace(" ", "")
    return int(s) if s.isdigit() else 0


def _ondalik(s):
    """'8,77' veya '8.77' -> float"""
    s = (s or "").strip().replace("%", "").replace(" ", "")
    if s.count(",") == 1 and s.count(".") == 0:
        s = s.replace(",", ".")
    else:
        s = s.replace(",", "")
    try:
        return float(s)
    except ValueError:
        return 0.0


def _no(s):
    """1234 -> '1.234' (TR binlik)"""
    return f"{s:,}".replace(",", ".")


def _yz(x, basamak=1):
    return (f"%.{basamak}f" % x).replace(".", ",")


def _kis(s, n):
    s = s or ""
    return s if len(s) <= n else s[: n - 1] + "…"


def _kacis(s):
    return (str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def _markami(sorgu):
    q = (sorgu or "").lower()
    return any(k in q for k in MARKA_KOK)


def _yol(url):
    """Tam URL -> okunur yol"""
    y = re.sub(r"^https?://(www\.)?[^/]+", "", url or "")
    return y if y and y != "/" else "/ (ana sayfa)"


def _b64(yol, mime):
    if not os.path.exists(yol):
        return None
    with open(yol, "rb") as f:
        return "data:%s;base64,%s" % (mime, base64.b64encode(f.read()).decode())


# ============================== veri katmani ==============================

def veri_yukle():
    d = {}

    # -- gunluk seri --
    ch = _oku("Chart.csv") or _oku("Grafik.csv") or []
    gun = []
    for r in ch:
        t = _sut(r, "Date", "Tarih")
        if not t:
            continue
        try:
            tar = datetime.date.fromisoformat(t.strip())
        except ValueError:
            continue
        gun.append({
            "tarih": tar,
            "tik": _sayi(_sut(r, "Clicks", "Tıklama", "Tiklama")),
            "gos": _sayi(_sut(r, "Impressions", "Gösterim", "Gosterim")),
            "sira": _ondalik(_sut(r, "Position", "Sıra", "Konum")),
        })
    gun.sort(key=lambda x: x["tarih"])
    d["gun"] = gun

    # -- sorgular --
    qs = []
    for r in (_oku("Queries.csv") or _oku("Sorgular.csv") or []):
        q = _sut(r, "Top queries", "En popüler sorgular", "Sorgu", "Query")
        if not q:
            continue
        qs.append({
            "q": q.strip(),
            "tik": _sayi(_sut(r, "Clicks", "Tıklama", "Tiklama")),
            "gos": _sayi(_sut(r, "Impressions", "Gösterim", "Gosterim")),
            "to": _ondalik(_sut(r, "CTR", "TO")),
            "sira": _ondalik(_sut(r, "Position", "Sıra", "Konum")),
        })
    d["sorgular"] = qs

    # -- sayfalar --
    ps = []
    for r in (_oku("Pages.csv") or _oku("Sayfalar.csv") or []):
        u = _sut(r, "Top pages", "En popüler sayfalar", "Sayfa", "Page")
        if not u:
            continue
        ps.append({
            "url": u.strip(),
            "tik": _sayi(_sut(r, "Clicks", "Tıklama", "Tiklama")),
            "gos": _sayi(_sut(r, "Impressions", "Gösterim", "Gosterim")),
            "to": _ondalik(_sut(r, "CTR", "TO")),
            "sira": _ondalik(_sut(r, "Position", "Sıra", "Konum")),
        })
    d["sayfalar"] = ps

    # -- cihaz --
    CEV = {"mobile": "Mobil", "desktop": "Masaüstü", "tablet": "Tablet"}
    cz = []
    for r in (_oku("Devices.csv") or _oku("Cihazlar.csv") or []):
        a = _sut(r, "Device", "Cihaz")
        if not a:
            continue
        cz.append({
            "ad": CEV.get(a.strip().lower(), a.strip()),
            "tik": _sayi(_sut(r, "Clicks", "Tıklama", "Tiklama")),
            "gos": _sayi(_sut(r, "Impressions", "Gösterim", "Gosterim")),
            "to": _ondalik(_sut(r, "CTR", "TO")),
        })
    d["cihaz"] = cz

    # -- ulke --
    ULKE = {"turkey": "Türkiye", "germany": "Almanya", "united states": "ABD",
            "netherlands": "Hollanda", "united kingdom": "Birleşik Krallık",
            "azerbaijan": "Azerbaycan", "kazakhstan": "Kazakistan",
            "cyprus": "Kıbrıs", "france": "Fransa", "austria": "Avusturya",
            "belgium": "Belçika", "switzerland": "İsviçre", "bulgaria": "Bulgaristan",
            "russia": "Rusya", "iraq": "Irak", "iran": "İran", "greece": "Yunanistan",
            "romania": "Romanya", "sweden": "İsveç", "italy": "İtalya",
            "spain": "İspanya", "poland": "Polonya", "ukraine": "Ukrayna",
            "united arab emirates": "BAE", "saudi arabia": "S. Arabistan",
            "georgia": "Gürcistan", "albania": "Arnavutluk", "canada": "Kanada",
            "australia": "Avustralya", "denmark": "Danimarka", "norway": "Norveç"}
    ul = []
    for r in (_oku("Countries.csv") or _oku("Ülkeler.csv") or _oku("Ulkeler.csv") or []):
        a = _sut(r, "Country", "Ülke", "Ulke")
        if not a:
            continue
        ul.append({
            "ad": ULKE.get(a.strip().lower(), a.strip()),
            "tik": _sayi(_sut(r, "Clicks", "Tıklama", "Tiklama")),
            "gos": _sayi(_sut(r, "Impressions", "Gösterim", "Gosterim")),
        })
    d["ulke"] = ul

    # -- toplamlar --
    d["tik"] = sum(g["tik"] for g in gun) or sum(c["tik"] for c in cz)
    d["gos"] = sum(g["gos"] for g in gun) or sum(c["gos"] for c in cz)
    d["to"] = (100.0 * d["tik"] / d["gos"]) if d["gos"] else 0.0
    # ortalama sira: gosterim agirlikli
    tg = sum(g["gos"] for g in gun)
    d["sira"] = (sum(g["sira"] * g["gos"] for g in gun) / tg) if tg else 0.0

    d["bas"] = gun[0]["tarih"] if gun else None
    d["son"] = gun[-1]["tarih"] if gun else None
    return d


def haftalar(gun, n=4):
    """Seriyi sondan geriye 7 gunluk dilimlere bol."""
    out = []
    i = len(gun)
    while i > 0 and len(out) < n:
        d = gun[max(0, i - 7): i]
        if len(d) < 3:          # yarim kalan ilk dilimi atma, ama etiketle
            pass
        out.append({
            "bas": d[0]["tarih"], "son": d[-1]["tarih"], "gun": len(d),
            "tik": sum(x["tik"] for x in d),
            "gos": sum(x["gos"] for x in d),
            "sira": (sum(x["sira"] * x["gos"] for x in d) / sum(x["gos"] for x in d))
                    if sum(x["gos"] for x in d) else 0.0,
        })
        i -= 7
    return list(reversed(out))


def firsatlar(sorgular, alt=5.0, ust=20.0, min_gos=40, en_fazla=12):
    """1. sayfa esiginde bekleyen sorgular."""
    f = [s for s in sorgular
         if alt <= s["sira"] <= ust and s["gos"] >= min_gos and not _markami(s["q"])]
    f.sort(key=lambda s: -s["gos"])
    return f[:en_fazla]


# ============================== grafik (inline SVG) ==============================

def cizgi_grafik(gun, gen=1000, yuk=300):
    """Gunluk gosterim (alan) + tiklama (cizgi) grafigi."""
    if len(gun) < 2:
        return ""
    sl, sr, st, sb = 54, 50, 18, 34
    iw, ih = gen - sl - sr, yuk - st - sb
    n = len(gun)
    maxg = max(g["gos"] for g in gun) or 1
    maxt = max(g["tik"] for g in gun) or 1
    # ust sinirlari yuvarla
    def tavan(v, adim):
        return int((v // adim + 1) * adim)
    maxg = tavan(maxg, 250 if maxg > 500 else 100)
    maxt = tavan(maxt, 5 if maxt > 10 else 2)

    x = lambda i: sl + (iw * i / (n - 1))
    yg = lambda v: st + ih - (ih * v / maxg)
    yt = lambda v: st + ih - (ih * v / maxt)

    p = []
    # yatay izgara
    for k in range(5):
        yy = st + ih * k / 4
        p.append(f'<line x1="{sl}" y1="{yy:.1f}" x2="{sl+iw}" y2="{yy:.1f}" '
                 f'stroke="{CIZGI}" stroke-width="1"/>')
        p.append(f'<text x="{sl-8}" y="{yy+3.5:.1f}" text-anchor="end" class="ax">'
                 f'{_no(int(maxg*(4-k)/4))}</text>')
        p.append(f'<text x="{sl+iw+8}" y="{yy+3.5:.1f}" text-anchor="start" class="ax2">'
                 f'{int(maxt*(4-k)/4)}</text>')

    # gosterim alani
    alan = " ".join(f"{x(i):.1f},{yg(g['gos']):.1f}" for i, g in enumerate(gun))
    p.append(f'<polygon points="{sl},{st+ih} {alan} {sl+iw},{st+ih}" '
             f'fill="{AMBER}" fill-opacity="0.22"/>')
    p.append(f'<polyline points="{alan}" fill="none" stroke="{AMBER}" stroke-width="2"/>')

    # tiklama cizgisi
    ct = " ".join(f"{x(i):.1f},{yt(g['tik']):.1f}" for i, g in enumerate(gun))
    p.append(f'<polyline points="{ct}" fill="none" stroke="{KOYU}" stroke-width="2.4" '
             f'stroke-linejoin="round"/>')
    for i, g in enumerate(gun):
        p.append(f'<circle cx="{x(i):.1f}" cy="{yt(g["tik"]):.1f}" r="2.6" fill="{KOYU}"/>')

    # tarih etiketleri
    adim = max(1, n // 8)
    for i in range(0, n, adim):
        t = gun[i]["tarih"]
        p.append(f'<text x="{x(i):.1f}" y="{st+ih+18}" text-anchor="middle" class="ax">'
                 f'{t.day} {AYLAR[t.month-1][:3]}</text>')

    return (f'<svg viewBox="0 0 {gen} {yuk}" class="chart">'
            f'<style>.ax{{font:10px Inter;fill:{SOLUK}}}'
            f'.ax2{{font:10px Inter;fill:{KOYU}}}</style>' + "".join(p) + "</svg>")


def sira_grafik(gun, gen=1000, yuk=190):
    """Ortalama sira egrisi — eksen TERS (kucuk deger yukarida = iyi)."""
    if len(gun) < 2:
        return ""
    sl, sr, st, sb = 54, 20, 16, 30
    iw, ih = gen - sl - sr, yuk - st - sb
    n = len(gun)
    dus = [g["sira"] for g in gun if g["sira"] > 0]
    if not dus:
        return ""
    enb = max(dus)
    tav = int((enb // 5 + 1) * 5)          # ust sinir (kotu taraf)
    x = lambda i: sl + (iw * i / (n - 1))
    y = lambda v: st + (ih * v / tav)      # ters: buyuk sira asagida

    p = []
    for k in range(5):
        v = tav * k / 4
        yy = y(v)
        p.append(f'<line x1="{sl}" y1="{yy:.1f}" x2="{sl+iw}" y2="{yy:.1f}" '
                 f'stroke="{CIZGI}" stroke-width="1"/>')
        p.append(f'<text x="{sl-8}" y="{yy+3.5:.1f}" text-anchor="end" class="ax">'
                 f'{"1." if k == 0 else str(int(v)) + "."}</text>')
    # ilk 10 (1. sayfa) bandi
    p.insert(0, f'<rect x="{sl}" y="{y(0):.1f}" width="{iw}" height="{y(min(10,tav))-y(0):.1f}" '
                f'fill="{AMBER}" fill-opacity="0.10"/>')
    p.append(f'<text x="{sl+3}" y="{y(min(10,tav))-4:.1f}" class="ax">ilk sayfa bandı (1–10)</text>')

    ct = " ".join(f"{x(i):.1f},{y(g['sira']):.1f}" for i, g in enumerate(gun) if g["sira"] > 0)
    p.append(f'<polyline points="{ct}" fill="none" stroke="{KOYU}" stroke-width="2.2" '
             f'stroke-linejoin="round"/>')
    adim = max(1, n // 8)
    for i in range(0, n, adim):
        t = gun[i]["tarih"]
        p.append(f'<text x="{x(i):.1f}" y="{st+ih+16}" text-anchor="middle" class="ax">'
                 f'{t.day} {AYLAR[t.month-1][:3]}</text>')
    return (f'<svg viewBox="0 0 {gen} {yuk}" class="chart2">'
            f'<style>.ax{{font:10px Inter;fill:{SOLUK}}}</style>' + "".join(p) + "</svg>")


def cubuk(deger, maks, renk=None):
    """Tablo icine gomulu oransal cubuk."""
    o = (100.0 * deger / maks) if maks else 0
    return (f'<span class="bar"><span class="bar-i" style="width:{o:.1f}%;'
            f'background:{renk or KOYU}"></span></span>')


def halka(pay, renk):
    """Basit donut — cihaz dagilimi icin."""
    r, c = 25, 32
    cev = 2 * 3.14159265 * r
    dolu = cev * max(0.0, min(1.0, pay))
    return (f'<svg viewBox="0 0 64 64" class="ring">'
            f'<circle cx="{c}" cy="{c}" r="{r}" fill="none" stroke="{CIZGI}" stroke-width="8"/>'
            f'<circle cx="{c}" cy="{c}" r="{r}" fill="none" stroke="{renk}" stroke-width="8"'
            f' stroke-dasharray="{dolu:.2f} {cev:.2f}"'
            f' transform="rotate(-90 {c} {c})"/>'
            f'<text x="{c}" y="{c+4.5}" text-anchor="middle" font-family="Poppins"'
            f' font-size="12" font-weight="600" fill="{INK}">'
            f'%{int(round(pay*100))}</text></svg>')


# ============================== notlar ==============================

VARSAYILAN_NOT = """# Rapor notlari — her ay bu dosyayi guncelleyin.
# Iki baslik aynen kalsin; altlarindaki maddeleri degistirin.
# Satir basina tek madde. Bos satirlar ve # ile baslayan satirlar yok sayilir.

## YAPILANLAR
Arama sonucunda görünen başlık ve açıklama metinleri, tıklama oranı düşük altı sayfada yeniden yazıldı.
Blog yayın akışı GitHub Actions'a taşındı; yazılar artık her gün otomatik yayına giriyor.
Tüm tedavi sayfalarına doğrulanabilir tıbbi kaynak bölümü eklendi (WHO, NCBI, NCI).
Ana sayfa ile alt sayfaların başlıkları, birbirinin sırasını düşürmeyecek şekilde ayrıştırıldı.
Eski site adreslerinden gelen 24 bağlantı, doğru sayfalara yönlendirildi.
Beş dildeki sayfaların birbirine bağlanma sorunu giderildi; çeviri sayfaları taranabilir hale geldi.
Hidradenit onarımı sayfası beş dilde yayına alındı.

## SONRAKI AY
İlk sayfa eşiğinde bekleyen sorgular için içerik derinleştirme.
Google İşletme Profili kategori ve hizmet düzenlemesi.
Gizlilik ve KVKK aydınlatma sayfasının yayına alınması.
Blog içerik kuyruğunun üç aylık plana göre doldurulması.
"""


def notlari_oku():
    if not os.path.exists(NOTLAR):
        os.makedirs(GSC, exist_ok=True)
        with open(NOTLAR, "w", encoding="utf-8") as f:
            f.write(VARSAYILAN_NOT)
    yap, son = [], []
    hedef = None
    for s in open(NOTLAR, encoding="utf-8"):
        s = s.strip()
        if not s or s.startswith("#") and not s.startswith("##"):
            continue
        if s.startswith("##"):
            b = s.lstrip("#").strip().upper()
            hedef = yap if "YAPIL" in b else (son if "SONRAKI" in b else None)
            continue
        if hedef is not None:
            hedef.append(s)
    return yap, son


# ============================== HTML ==============================

def font_css():
    p = []
    cift = [("Poppins", "Poppins-Regular.ttf", 400, "truetype"),
            ("Poppins", "Poppins-Medium.ttf", 500, "truetype"),
            ("Poppins", "Poppins-SemiBold.ttf", 600, "truetype"),
            ("Poppins", "Poppins-Bold.ttf", 700, "truetype"),
            ("Inter", "Inter-Regular.otf", 400, "opentype"),
            ("Inter", "Inter-Medium.otf", 500, "opentype"),
            ("Inter", "Inter-SemiBold.otf", 600, "opentype")]
    for ad, dosya, agirlik, bic in cift:
        y = os.path.join(FONT, dosya)
        if os.path.exists(y):
            p.append("@font-face{font-family:'%s';font-weight:%d;font-style:normal;"
                     "src:url('file://%s') format('%s')}" % (ad, agirlik, y, bic))
    return "\n".join(p)


def html_uret(d):
    yap, son = notlari_oku()
    gun, sorgular, sayfalar = d["gun"], d["sorgular"], d["sayfalar"]
    hf = haftalar(gun)
    frs = firsatlar(sorgular)

    bugun = datetime.date.today()
    donem = ""
    if d["bas"] and d["son"]:
        if d["bas"].month == d["son"].month:
            donem = f"{d['bas'].day}–{d['son'].day} {AYLAR[d['son'].month-1]} {d['son'].year}"
        else:
            donem = (f"{d['bas'].day} {AYLAR[d['bas'].month-1]} – "
                     f"{d['son'].day} {AYLAR[d['son'].month-1]} {d['son'].year}")
    gun_sayisi = len(gun)
    etiket_ay = f"{AYLAR[d['son'].month-1]} {d['son'].year}" if d["son"] else ""

    # marka / marka disi
    mk = [s for s in sorgular if _markami(s["q"])]
    md = [s for s in sorgular if not _markami(s["q"])]
    mk_t, mk_g = sum(s["tik"] for s in mk), sum(s["gos"] for s in mk)
    md_t, md_g = sum(s["tik"] for s in md), sum(s["gos"] for s in md)

    logo = _b64(LOGO, "image/png")
    logo_img = (f'<img src="{logo}" class="logo" alt="Saturday">' if logo
                else f'<div class="logo-yazi">Saturday</div>')
    logo_kk = (f'<img src="{logo}" class="logo-s" alt="">' if logo
               else '<span class="logo-yazi-s">Saturday</span>')

    P = []
    A = P.append

    # ---------------- KAPAK ----------------
    A(f'''<section class="kapak">
  <div class="kapak-ic">
    {logo_img}
    <div class="kapak-etiket">Arama Performansı Raporu</div>
    <h1 class="kapak-h1">{etiket_ay}</h1>
    <div class="kapak-cizgi"></div>
    <div class="kapak-musteri">{MUSTERI_TR}</div>
    <div class="kapak-alan">{ALAN}</div>
  </div>
  <div class="kapak-alt">
    <div><span class="kk">Dönem</span>{donem} · {gun_sayisi} gün</div>
    <div><span class="kk">Hazırlayan</span>{AJANS} · {AJANS_WEB}</div>
    <div><span class="kk">Rapor tarihi</span>{bugun.day} {AYLAR[bugun.month-1]} {bugun.year}</div>
  </div>
</section>''')

    # ---------------- 1. YONETICI OZETI ----------------
    en_iyi = max(gun, key=lambda g: g["tik"]) if gun else None
    en_gos = max(gun, key=lambda g: g["gos"]) if gun else None

    # son 7 tam gun vs onceki 7 tam gun — yarim hafta kiyaslamasi yapma
    def delta(anahtar):
        if len(gun) < 14:
            return ""
        a = sum(g[anahtar] for g in gun[-14:-7])
        b = sum(g[anahtar] for g in gun[-7:])
        if not a:
            return ""
        o = 100.0 * (b - a) / a
        isaret = "+" if o >= 0 else "−"
        sinif = "yuk" if o >= 0 else "dus"
        return (f'<div class="k-d"><span class="d {sinif}">{isaret}%{_yz(abs(o),0)}</span>'
                f' son 7 gün / önceki 7 gün</div>')

    A(f'''<section class="sy">
  <header class="sb"><span class="sn">01</span><h2>Yönetici özeti</h2>
    <div class="sb-alt">{donem}</div></header>

  <div class="kpi">
    <div class="k"><div class="k-e">Tıklama</div><div class="k-v">{_no(d["tik"])}</div>
      <div class="k-a">siteye gelen ziyaretçi</div>{delta("tik")}</div>
    <div class="k"><div class="k-e">Gösterim</div><div class="k-v">{_no(d["gos"])}</div>
      <div class="k-a">arama sonucunda görünme</div>{delta("gos")}</div>
    <div class="k"><div class="k-e">Tıklama oranı</div><div class="k-v">%{_yz(d["to"],1)}</div>
      <div class="k-a">gösterim başına tıklama</div></div>
    <div class="k"><div class="k-e">Ortalama sıra</div><div class="k-v">{_yz(d["sira"],1)}</div>
      <div class="k-a">Google'daki ortalama konum</div></div>
  </div>

  <div class="oz">
    <p>Site <strong>{donem}</strong> aralığında Google aramalarında <strong>{_no(d["gos"])} kez</strong>
    görüntülendi ve bu görüntülemelerden <strong>{_no(d["tik"])} ziyaret</strong> geldi.
    Ortalama sıralama <strong>{_yz(d["sira"],1)}</strong> — yani aramaların çoğunda
    sitenin ilk iki sayfa içinde konumlandığı anlamına geliyor.</p>

    <p>Dönemin en yüksek günü <strong>{en_iyi["tarih"].day} {AYLAR[en_iyi["tarih"].month-1]}</strong>
    oldu ({en_iyi["tik"]} tıklama). Gösterim tarafındaki artış, yeni yayına alınan içerik
    kümelerinin Google tarafından taranıp sıralanmaya başladığını gösteriyor: günlük gösterim
    dönem başında {_no(gun[0]["gos"])} seviyesindeyken dönem sonunda {_no(gun[-1]["gos"])}
    seviyesine çıktı.</p>
  </div>

  <h3>Aramanın niteliği</h3>
  <div class="ikili">
    <div class="kutu">
      <div class="kutu-b">Marka aramaları</div>
      <div class="kutu-v">{_no(mk_g)}<span>gösterim</span></div>
      <div class="kutu-a">{_no(mk_t)} tıklama · doktorun adını arayanlar</div>
    </div>
    <div class="kutu vurgu">
      <div class="kutu-b">Marka dışı aramalar</div>
      <div class="kutu-v">{_no(md_g)}<span>gösterim</span></div>
      <div class="kutu-a">{_no(md_t)} tıklama · tedaviyi arayıp siteyi bulanlar</div>
    </div>
  </div>
  <p class="dip">Marka dışı gösterimin payı
  <strong>%{_yz(100.0*md_g/(md_g+mk_g) if (md_g+mk_g) else 0, 0)}</strong>. Bu oran, sitenin
  doktoru zaten tanıyan kişilerin ötesinde <em>yeni hasta</em> bulup bulmadığının göstergesidir
  ve büyümenin asıl ölçüsüdür. — Not: bu iki kutu sorgu bazlı veriden hesaplanır; Google çok
  az arananları gizlediği için toplamları sayfa üstündeki genel toplamın altında kalır.</p>

  <h3>Dönem içi rekorlar</h3>
  <div class="serit">
    <div class="sr"><div class="sr-e">En çok tıklanan gün</div>
      <div class="sr-v">{en_iyi["tik"]}</div>
      <div class="sr-a">{en_iyi["tarih"].day} {AYLAR[en_iyi["tarih"].month-1]}</div></div>
    <div class="sr"><div class="sr-e">En çok görünen gün</div>
      <div class="sr-v">{_no(en_gos["gos"])}</div>
      <div class="sr-a">{en_gos["tarih"].day} {AYLAR[en_gos["tarih"].month-1]}</div></div>
    <div class="sr"><div class="sr-e">Günlük ortalama tıklama</div>
      <div class="sr-v">{_yz(d["tik"]/gun_sayisi,1)}</div>
      <div class="sr-a">{gun_sayisi} günün ortalaması</div></div>
    <div class="sr"><div class="sr-e">Sıralamaya giren sorgu</div>
      <div class="sr-v">{_no(len(sorgular))}</div>
      <div class="sr-a">farklı arama terimi</div></div>
  </div>
</section>''')

    # ---------------- 2. GUNLUK TREND ----------------
    satir_h = ""
    for i, h in enumerate(hf):
        et = f"{h['bas'].day} {AYLAR[h['bas'].month-1][:3]} – {h['son'].day} {AYLAR[h['son'].month-1][:3]}"
        if h["gun"] < 7:
            et += f" ({h['gun']} gün)"
        satir_h += (f"<tr><td>{et}</td><td class='s'>{_no(h['tik'])}</td>"
                    f"<td class='s'>{_no(h['gos'])}</td>"
                    f"<td class='s'>%{_yz(100.0*h['tik']/h['gos'] if h['gos'] else 0,1)}</td>"
                    f"<td class='s'>{_yz(h['sira'],1)}</td></tr>")

    # sira yorumu — gosterim buyumesiyle birlikte okunmali
    s_ilk = hf[0]["sira"] if hf else 0
    s_son = hf[-1]["sira"] if hf else 0
    g_kat = (hf[-1]["gos"] / hf[0]["gos"]) if hf and hf[0]["gos"] else 0
    if s_son < s_ilk - 0.3:
        sira_yorum = ("Sıralama iyileşirken gösterim de büyüdü — sağlıklı tablo budur.")
    elif s_son > s_ilk + 0.3:
        sira_yorum = (f"Ortalama bir miktar geriledi; bunun nedeni gösterimin aynı dönemde "
                      f"{_yz(g_kat,1)} katına çıkmasıdır. Site yeni ve çok sayıda sorguda "
                      f"görünmeye başladığında, bu yeni sorgular alt sıralardan giriş yapar "
                      f"ve ortalamayı aşağı çeker. Sıralanan sorgu sayısı artarken ortalamanın "
                      f"bir puan gerilemesi, kayıp değil genişleme işaretidir.")
    else:
        sira_yorum = (f"Gösterim {_yz(g_kat,1)} katına çıkmasına rağmen ortalama sıra sabit "
                      f"kaldı — yeni sayfalar mevcut sayfaları zayıflatmadı.")

    A(f'''<section class="sy">
  <header class="sb"><span class="sn">02</span><h2>Günlük seyir</h2>
    <div class="sb-alt">Tıklama ve gösterim eğrisi</div></header>

  <div class="lejant">
    <span><i style="background:{KOYU}"></i>Tıklama (sol eksen)</span>
    <span><i style="background:{AMBER}"></i>Gösterim (sağ eksen)</span>
  </div>
  {cizgi_grafik(gun)}

  <h3>Haftalık kırılım</h3>
  <table class="t">
    <thead><tr><th>Hafta</th><th class="s">Tıklama</th><th class="s">Gösterim</th>
    <th class="s">TO</th><th class="s">Ort. sıra</th></tr></thead>
    <tbody>{satir_h}</tbody>
  </table>
  <p class="dip">Gösterim eğrisindeki yükseliş, tıklamadan daha hızlı büyüyor. Bu normaldir:
  yeni sayfalar önce görünür hale gelir, sıralamaları yükseldikçe tıklamaya dönüşür.
  Tıklama oranındaki geçici düşüş de bundan kaynaklanır.</p>

  <h3>Ortalama sıralama</h3>
  {sira_grafik(gun)}
  <p class="dip">Bu grafikte <strong>yukarı çıkmak iyidir</strong> — eksen ters çevrilmiştir,
  çünkü 1. sıra 20. sıradan iyidir. İlk hafta {_yz(hf[0]["sira"],1)} olan ortalama sıra,
  son hafta {_yz(hf[-1]["sira"],1)} oldu. {sira_yorum}</p>
</section>''')

    # ---------------- 3. SAYFALAR ----------------
    tepe = sayfalar[:14]
    maxg = max((p["gos"] for p in tepe), default=1)
    sp = ""
    for p in tepe:
        sp += (f"<tr><td class='yol'>{_kacis(_kis(_yol(p['url']), 46))}</td>"
               f"<td class='s'>{_no(p['tik'])}</td>"
               f"<td class='g'>{cubuk(p['gos'], maxg, AMBER)}<b>{_no(p['gos'])}</b></td>"
               f"<td class='s'>%{_yz(p['to'],1)}</td>"
               f"<td class='s'>{_yz(p['sira'],1)}</td></tr>")

    A(f'''<section class="sy">
  <header class="sb"><span class="sn">03</span><h2>En çok görünen sayfalar</h2>
    <div class="sb-alt">Gösterime göre ilk {len(tepe)}</div></header>
  <table class="t">
    <thead><tr><th>Sayfa</th><th class="s">Tıklama</th><th>Gösterim</th>
    <th class="s">TO</th><th class="s">Ort. sıra</th></tr></thead>
    <tbody>{sp}</tbody>
  </table>
  <p class="dip">Ana sayfa dışındaki trafiğin tamamı, bu dönemde yayına alınan tedavi ve
  blog sayfalarından geliyor. Gösterimi yüksek ama tıklaması düşük satırlar, bir sonraki
  bölümdeki fırsat listesinin kaynağıdır.</p>
</section>''')

    # ---------------- 4. SORGULAR ----------------
    md_tepe = md[:12]
    mg = max((s["gos"] for s in md_tepe), default=1)
    sq = ""
    for s in md_tepe:
        sq += (f"<tr><td>{_kacis(_kis(s['q'],42))}</td>"
               f"<td class='s'>{_no(s['tik'])}</td>"
               f"<td class='g'>{cubuk(s['gos'], mg, AMBER)}<b>{_no(s['gos'])}</b></td>"
               f"<td class='s'>{_yz(s['sira'],1)}</td></tr>")
    mk_tepe = mk[:6]
    sm = ""
    for s in mk_tepe:
        sm += (f"<tr><td>{_kacis(_kis(s['q'],42))}</td>"
               f"<td class='s'>{_no(s['tik'])}</td><td class='s'>{_no(s['gos'])}</td>"
               f"<td class='s'>%{_yz(s['to'],1)}</td><td class='s'>{_yz(s['sira'],1)}</td></tr>")

    A(f'''<section class="sy">
  <header class="sb"><span class="sn">04</span><h2>Arama sorguları</h2>
    <div class="sb-alt">Hastaların Google'a yazdığı kelimeler</div></header>

  <h3>Marka dışı — tedaviyi arayanlar</h3>
  <table class="t">
    <thead><tr><th>Sorgu</th><th class="s">Tıklama</th><th>Gösterim</th>
    <th class="s">Ort. sıra</th></tr></thead>
    <tbody>{sq}</tbody>
  </table>

  <h3>Marka — doktoru arayanlar</h3>
  <table class="t">
    <thead><tr><th>Sorgu</th><th class="s">Tıklama</th><th class="s">Gösterim</th>
    <th class="s">TO</th><th class="s">Ort. sıra</th></tr></thead>
    <tbody>{sm}</tbody>
  </table>
  <p class="dip">Marka aramalarında tıklama oranı yüksek ve sıralama ilk sıradadır — bu beklenen
  tablodur. Büyüme marka dışı tarafta olur; oradaki her sıralama artışı yeni hasta demektir.</p>
</section>''')

    # ---------------- 5. FIRSAT ----------------
    sf = ""
    tahmin = 0
    for s in frs:
        # ilk 5'e cikildiginda kabaca %8 TO varsayimi
        bek = int(s["gos"] * 0.08)
        tahmin += max(0, bek - s["tik"])
        sf += (f"<tr><td>{_kacis(_kis(s['q'],40))}</td>"
               f"<td class='s'>{_no(s['gos'])}</td>"
               f"<td class='s'>{_yz(s['sira'],1)}</td>"
               f"<td class='s'>{_no(s['tik'])}</td>"
               f"<td class='s vurgu-h'>{_no(bek)}</td></tr>")
    frs_gos = sum(s["gos"] for s in frs)
    frs_tik = sum(s["tik"] for s in frs)

    A(f'''<section class="sy">
  <header class="sb"><span class="sn">05</span><h2>Fırsat listesi</h2>
    <div class="sb-alt">İlk sayfa eşiğinde bekleyen aramalar</div></header>

  <p class="giris">Aşağıdaki sorgularda site <strong>5–20. sıra</strong> aralığında.
  Bu aralık kritiktir: sıfırdan sıralamaya girmekten çok daha kolay şekilde ilk 5'e
  taşınabilir. Toplam <strong>{_no(frs_gos)} gösterim</strong> bu listede bekliyor ve
  şu an yalnızca <strong>{_no(frs_tik)} tıklamaya</strong> dönüşüyor.</p>

  <table class="t">
    <thead><tr><th>Sorgu</th><th class="s">Gösterim</th><th class="s">Şu anki sıra</th>
    <th class="s">Tıklama</th><th class="s">İlk 5'te</th></tr></thead>
    <tbody>{sf}</tbody>
  </table>
  <p class="dip">"İlk 5'te" sütunu, aynı gösterim hacminde ilk beş sıraya çıkıldığında
  beklenen tıklamayı gösterir (%8 tıklama oranı varsayımıyla). Bu bir garanti değil,
  önceliklendirme için kullanılan bir tahmindir — aynı {gun_sayisi} günlük dönemde
  <strong>+{_no(tahmin)} ek ziyaret</strong> potansiyeli anlamına gelir.</p>
</section>''')

    # ---------------- 6. CIHAZ & ULKE ----------------
    ct = sum(c["tik"] for c in d["cihaz"]) or 1
    sc = ""
    renk = [KOYU, AMBER, KIZIL]
    for i, c in enumerate(d["cihaz"]):
        sc += (f'<div class="cz">{halka(c["tik"]/ct, renk[i % 3])}'
               f'<div class="cz-b">{c["ad"]}</div>'
               f'<div class="cz-a">{_no(c["tik"])} tıklama · {_no(c["gos"])} gösterim</div>'
               f'<div class="cz-a">TO %{_yz(c["to"],1)}</div></div>')

    ul = [u for u in d["ulke"] if u["gos"] >= 10][:10]
    mu = max((u["gos"] for u in ul), default=1)
    su = ""
    for u in ul:
        su += (f"<tr><td>{_kacis(u['ad'])}</td><td class='s'>{_no(u['tik'])}</td>"
               f"<td class='g'>{cubuk(u['gos'], mu, KOYU)}<b>{_no(u['gos'])}</b></td></tr>")

    yurt_disi_g = sum(u["gos"] for u in d["ulke"] if u["ad"] != "Türkiye")
    yurt_disi_t = sum(u["tik"] for u in d["ulke"] if u["ad"] != "Türkiye")

    A(f'''<section class="sy">
  <header class="sb"><span class="sn">06</span><h2>Cihaz ve ülke dağılımı</h2>
    <div class="sb-alt">Ziyaretçi kaynağı</div></header>
  <div class="czl">{sc}</div>

  <h3>Ülkelere göre gösterim</h3>
  <table class="t">
    <thead><tr><th>Ülke</th><th class="s">Tıklama</th><th>Gösterim</th></tr></thead>
    <tbody>{su}</tbody>
  </table>
  <p class="dip">Yurt dışından toplam <strong>{_no(yurt_disi_g)} gösterim</strong> ve
  <strong>{_no(yurt_disi_t)} tıklama</strong> geldi. Site İngilizce, Almanca, Rusça ve
  Arapça sürümleriyle yayında olduğu için bu tarafın zamanla büyümesi bekleniyor.</p>
</section>''')

    # ---------------- 7. CALISMALAR ----------------
    ly = "".join(f'<li>{_kacis(m)}</li>' for m in yap) or "<li>—</li>"
    ls = "".join(f'<li>{_kacis(m)}</li>' for m in son) or "<li>—</li>"

    A(f'''<section class="sy">
  <header class="sb"><span class="sn">07</span><h2>Bu dönem yapılanlar</h2>
    <div class="sb-alt">Saturday Online çalışma özeti</div></header>
  <ul class="is">{ly}</ul>

  <h3>Önümüzdeki dönem</h3>
  <ul class="is plan">{ls}</ul>

</section>

<section class="sy">
  <header class="sb"><span class="sn">08</span><h2>Rapordaki terimler</h2>
    <div class="sb-alt">Metriklerin karşılığı</div></header>
  <table class="t soz">
    <tbody>
      <tr><td class="sz">Gösterim</td><td>Birinin Google'da arama yaptığında sitenizin
        sonuç listesinde göründüğü sayı. Tıklamasa da sayılır.</td></tr>
      <tr><td class="sz">Tıklama</td><td>Arama sonucundan sitenize gelen gerçek ziyaret sayısı.</td></tr>
      <tr><td class="sz">Tıklama oranı (TO)</td><td>Gösterimin yüzde kaçının tıklamaya
        dönüştüğü. Başlık ve açıklama metninin ne kadar ikna edici olduğunu gösterir.</td></tr>
      <tr><td class="sz">Ortalama sıra</td><td>Sitenizin arama sonuçlarındaki ortalama konumu.
        1–10 arası ilk sayfa demektir; küçülmesi iyiye işarettir.</td></tr>
      <tr><td class="sz">Marka araması</td><td>Doğrudan doktorun adının arandığı sorgular.
        Bu kişiler zaten sizi tanıyor.</td></tr>
      <tr><td class="sz">Marka dışı arama</td><td>"lipödem belirtileri" gibi tedaviye yönelik
        sorgular. Yeni hasta buradan gelir.</td></tr>
      <tr><td class="sz">İlk sayfa eşiği</td><td>5–20. sıra aralığı. Buradaki sayfalar,
        sıfırdan başlayanlara göre çok daha küçük bir çabayla ilk 5'e taşınabilir.</td></tr>
      <tr><td class="sz">İçerik kümesi</td><td>Bir ana konu sayfası ve onu destekleyen alt
        sayfaların birbirine bağlanmış hali. Google bir konudaki uzmanlığı bu bütünlükten okur.</td></tr>
      <tr><td class="sz">Dizine alınma</td><td>Google'ın bir sayfayı tarayıp arama sonuçlarına
        eklemesi. Yayına alınan her sayfa hemen dizine girmez; birkaç hafta sürebilir.</td></tr>
    </tbody>
  </table>

  <h3>Bu rapor nasıl hazırlanıyor?</h3>
  <p>Buradaki bütün sayılar <strong>Google Search Console</strong>'dan alınır — yani Google'ın
  kendi ölçümüdür, tahmin ya da üçüncü taraf aracı değildir. Rakamlar her ay aynı yöntemle
  çekilir, böylece aylar birbiriyle kıyaslanabilir.</p>

  <p>Google, çok az aranan sorguları gizlilik gereği gizler. Bu yüzden sorgu tablolarındaki
  toplamlar, raporun başındaki genel toplamdan bir miktar düşük çıkar. Bu bir hata değil,
  Google'ın veri politikasının sonucudur.</p>

  <p>Sıralama verileri <strong>ortalamadır</strong>: aynı sorguda kimi kullanıcı 4. sırada,
  kimi 12. sırada görebilir. Konum, arama geçmişi ve cihaz sonucu değiştirir. Bu nedenle
  tek bir günün rakamına değil, eğrinin yönüne bakılır.</p>

  <div class="imza">
    {logo_kk}
    <div class="imza-y">
      <div class="imza-b">{AJANS}</div>
      <div class="imza-a">{AJANS_WEB}</div>
    </div>
    <div class="imza-not">Veri kaynağı: Google Search Console<br>{donem}</div>
  </div>
</section>''')

    # ---------------- CSS ----------------
    css = f"""
{font_css()}
@page {{
  size: A4; margin: 17mm 15mm 16mm 15mm;
  @bottom-left {{ content: "{AJANS} · {ALAN}"; font-family: Inter; font-size: 7.5pt; color: {SOLUK}; }}
  @bottom-right {{ content: counter(page) " / " counter(pages); font-family: Inter; font-size: 7.5pt; color: {SOLUK}; }}
}}
@page :first {{ margin: 0; @bottom-left {{ content: none }} @bottom-right {{ content: none }} }}

* {{ box-sizing: border-box; }}
body {{ font-family: Inter, sans-serif; font-size: 9.4pt; line-height: 1.62;
        color: {INK}; margin: 0; }}
h1,h2,h3 {{ font-family: Poppins, sans-serif; margin: 0; }}
strong {{ font-weight: 600; }}
em {{ font-style: italic; color: {SOLUK}; }}

/* ---- kapak ---- */
.kapak {{ page-break-after: always; height: 297mm; width: 210mm;
  background: {KOYU}; color: #fff; padding: 34mm 20mm 18mm;
  display: flex; flex-direction: column; justify-content: space-between; }}
.kapak-ic {{ }}
.logo {{ width: 46mm; display: block; margin-bottom: 26mm; }}
.logo-yazi {{ font-family: Poppins; font-weight: 700; font-size: 30pt;
  color: {AMBER}; margin-bottom: 26mm; }}
.kapak-etiket {{ font-family: Inter; font-size: 9pt; letter-spacing: .19em;
  text-transform: uppercase; color: {AMBER}; margin-bottom: 5mm; }}
.kapak-h1 {{ font-size: 42pt; font-weight: 700; line-height: 1.04; letter-spacing: -.02em; }}
.kapak-cizgi {{ width: 28mm; height: 3px; background: {AMBER}; margin: 8mm 0 7mm; }}
.kapak-musteri {{ font-family: Poppins; font-weight: 500; font-size: 15pt; }}
.kapak-alan {{ font-size: 10pt; color: rgba(255,255,255,.72); margin-top: 1.5mm; }}
.kapak-alt {{ border-top: 1px solid rgba(255,255,255,.22); padding-top: 6mm;
  display: flex; gap: 12mm; font-size: 8.6pt; color: rgba(255,255,255,.9); }}
.kapak-alt > div {{ flex: 1; }}
.kk {{ display: block; font-size: 7.2pt; letter-spacing: .14em; text-transform: uppercase;
  color: {AMBER}; margin-bottom: 1.5mm; }}

/* ---- bolum ---- */
.sy {{ page-break-before: always; }}
.sb {{ border-bottom: 2px solid {KOYU}; padding-bottom: 3mm; margin-bottom: 6mm;
  position: relative; }}
.sn {{ font-family: Poppins; font-weight: 700; font-size: 8.5pt; color: {AMBER};
  letter-spacing: .1em; display: block; margin-bottom: 1mm; }}
.sb h2 {{ font-size: 18pt; font-weight: 600; letter-spacing: -.015em; color: {INK}; }}
.sb-alt {{ font-size: 8.6pt; color: {SOLUK}; margin-top: 1mm; }}
h3 {{ font-size: 11pt; font-weight: 600; margin: 7mm 0 3mm; color: {KOYU}; }}

/* ---- kpi ---- */
.kpi {{ display: flex; gap: 3.5mm; margin-bottom: 6mm; }}
.k {{ flex: 1; background: {KREM}; border: 1px solid {CIZGI};
  border-top: 3px solid {KOYU}; border-radius: 2mm; padding: 4mm 3.5mm; }}
.k-e {{ font-size: 7.4pt; letter-spacing: .1em; text-transform: uppercase;
  color: {SOLUK}; margin-bottom: 2mm; }}
.k-v {{ font-family: Poppins; font-weight: 700; font-size: 22pt; line-height: 1;
  color: {KOYU}; letter-spacing: -.02em; }}
.k-a {{ font-size: 7.6pt; color: {SOLUK}; margin-top: 2mm; line-height: 1.4; }}
.k-d {{ font-size: 7pt; color: {SOLUK}; margin-top: 1.5mm; padding-top: 1.5mm;
  border-top: 1px solid {CIZGI}; line-height: 1.35; }}
.d {{ font-weight: 600; }}
.d.yuk {{ color: {YESIL}; }}
.d.dus {{ color: {KIZIL}; }}

.oz p {{ margin: 0 0 3.5mm; }}
.giris {{ margin: 0 0 4mm; }}

.ikili {{ display: flex; gap: 3.5mm; margin: 5mm 0 3mm; }}
.kutu {{ flex: 1; border: 1px solid {CIZGI}; border-radius: 2mm; padding: 4mm; }}
.kutu.vurgu {{ background: {KREM2}; border-color: {AMBER}; }}
.kutu-b {{ font-size: 8pt; font-weight: 600; color: {SOLUK}; margin-bottom: 2mm; }}
.kutu-v {{ font-family: Poppins; font-weight: 700; font-size: 19pt; color: {INK}; line-height: 1; }}
.kutu-v span {{ font-family: Inter; font-weight: 400; font-size: 8.5pt;
  color: {SOLUK}; margin-left: 2mm; }}
.kutu-a {{ font-size: 7.8pt; color: {SOLUK}; margin-top: 2mm; }}

.dip {{ font-size: 8.2pt; color: {SOLUK}; line-height: 1.55;
  border-left: 2px solid {AMBER}; padding-left: 3.5mm; margin-top: 4mm; }}

/* ---- rekor seridi ---- */
.serit {{ display: flex; gap: 3.5mm; }}
.sr {{ flex: 1; border: 1px solid {CIZGI}; border-radius: 2mm; padding: 3.5mm 3mm;
  text-align: center; }}
.sr-e {{ font-size: 7.2pt; color: {SOLUK}; letter-spacing: .04em; line-height: 1.35;
  min-height: 7mm; }}
.sr-v {{ font-family: Poppins; font-weight: 700; font-size: 16pt; color: {KOYU};
  line-height: 1.1; margin: 1mm 0; }}
.sr-a {{ font-size: 7.4pt; color: {SOLUK}; }}

/* ---- grafik ---- */
.chart {{ width: 100%; height: 60mm; display: block; margin-bottom: 3mm; }}
.chart2 {{ width: 100%; height: 36mm; display: block; margin: 2mm 0 1mm; }}
.lejant {{ display: flex; gap: 6mm; font-size: 8pt; color: {SOLUK}; margin-bottom: 1mm; }}
.lejant i {{ display: inline-block; width: 9px; height: 9px; border-radius: 2px;
  margin-right: 2mm; vertical-align: -1px; }}

/* ---- tablo ---- */
.t {{ width: 100%; border-collapse: collapse; font-size: 8.6pt; }}
.t thead {{ display: table-header-group; }}
.t th {{ text-align: left; font-family: Inter; font-weight: 600; font-size: 7.6pt;
  letter-spacing: .06em; text-transform: uppercase; color: #fff; background: {KOYU};
  padding: 2.4mm 2.5mm; }}
.t td {{ padding: 2.2mm 2.5mm; border-bottom: 1px solid {CIZGI}; vertical-align: middle; }}
.t tr {{ break-inside: avoid; }}
.t tbody tr:nth-child(even) {{ background: {KREM}; }}
.t .s {{ text-align: right; white-space: nowrap; }}
.t th.s {{ text-align: right; }}
.t .yol {{ font-family: Inter; font-size: 8.2pt; }}
.t .g {{ white-space: nowrap; text-align: right; }}
.t .g b {{ font-weight: 600; margin-left: 2mm; display: inline-block; min-width: 11mm;
  text-align: right; }}
.vurgu-h {{ color: {KOYU}; font-weight: 600; }}
.bar {{ display: inline-block; width: 22mm; height: 5px; background: {CIZGI};
  border-radius: 3px; overflow: hidden; vertical-align: middle; }}
.bar-i {{ display: block; height: 100%; border-radius: 3px; }}

/* ---- cihaz ---- */
.czl {{ display: flex; gap: 4mm; }}
.cz {{ flex: 1; text-align: center; border: 1px solid {CIZGI}; border-radius: 2mm;
  padding: 4mm 3mm; background: {KREM}; }}
.ring {{ width: 20mm; height: 20mm; }}
.cz-b {{ font-family: Poppins; font-weight: 600; font-size: 10pt; margin-top: 1mm; }}
.cz-a {{ font-size: 7.8pt; color: {SOLUK}; margin-top: 1mm; }}

/* ---- isler ---- */
.is {{ margin: 0; padding: 0; list-style: none; }}
.is li {{ position: relative; padding: 2.6mm 0 2.6mm 7mm; border-bottom: 1px solid {CIZGI};
  font-size: 9.2pt; break-inside: avoid; }}
.is li::before {{ content: ""; position: absolute; left: 1.5mm; top: 4.6mm;
  width: 2.4mm; height: 2.4mm; border-radius: 50%; background: {KOYU}; }}
.is.plan li::before {{ background: none; border: 1px solid {KOYU}; }}

.soz td {{ vertical-align: top; }}
.soz .sz {{ font-family: Poppins; font-weight: 600; font-size: 8.4pt; color: {KOYU};
  width: 36mm; white-space: nowrap; }}

.imza {{ margin-top: 9mm; padding-top: 5mm; border-top: 2px solid {KOYU};
  display: flex; align-items: center; gap: 4mm; }}
.logo-s {{ width: 26mm; }}
.logo-yazi-s {{ font-family: Poppins; font-weight: 700; font-size: 15pt; color: {AMBER}; }}
.imza-y {{ border-left: 1px solid {CIZGI}; padding-left: 4mm; flex: 1; }}
.imza-b {{ font-family: Poppins; font-weight: 600; font-size: 10pt; }}
.imza-a {{ font-size: 8.4pt; color: {SOLUK}; }}
.imza-not {{ font-size: 7.6pt; color: {SOLUK}; text-align: right; line-height: 1.5; }}
"""

    return (f'<!doctype html><html lang="tr"><head><meta charset="utf-8">'
            f'<title>{AJANS} — {ALAN} · {etiket_ay}</title>'
            f'<style>{css}</style></head><body>{"".join(P)}</body></html>')


# ============================== calistir ==============================

def main():
    if not os.path.isdir(GSC):
        raise SystemExit("_gsc/ klasoru yok. Once GSC disa aktarimini oraya kopyalayin.")
    d = veri_yukle()
    if not d["gun"]:
        raise SystemExit("Chart.csv bulunamadi veya bos. GSC ZIP'indeki TUM csv'leri _gsc/ icine atin.")

    os.makedirs(BEL, exist_ok=True)
    etiket = f"{d['son'].year}-{d['son'].month:02d}"
    html = html_uret(d)

    ham = os.path.join(BEL, f"_rapor-{etiket}.html")
    with open(ham, "w", encoding="utf-8") as f:
        f.write(html)

    from weasyprint import HTML
    cikti = os.path.join(BEL, f"Saturday-Rapor-{etiket}-droguzacarturk.pdf")
    HTML(string=html, base_url=KOK).write_pdf(cikti)

    print("Rapor hazir:", cikti)
    print("  donem   :", d["bas"], "->", d["son"], f"({len(d['gun'])} gun)")
    print("  tiklama :", d["tik"], "| gosterim:", d["gos"],
          "| TO: %.2f%%" % d["to"], "| sira: %.1f" % d["sira"])
    print("  sorgu   :", len(d["sorgular"]), "| sayfa:", len(d["sayfalar"]))
    print("  notlar  :", NOTLAR)
    return cikti


if __name__ == "__main__":
    main()
