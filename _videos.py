# -*- coding: utf-8 -*-
"""
YouTube videolari — https://www.youtube.com/@dr.tahsinoguzacarturk
Kanal: UCXiQzMdqnc0frjPFdcA39NA

Tek kaynak: hizmet sayfalari (_build.py) ve anasayfa (index.html elle) buradan
beslenir. Yeni video eklemek icin:
  1) VIDEOS'a satir ekle (id, baslik, yukleme tarihi, sure-sn, shorts mu, kisa aciklama)
  2) PAGE_VIDEOS'ta ilgili sayfa anahtarina id'yi ekle
  3) python3 _build.py  (anasayfa seridi icin: python3 _videos.py --home)

Basliklar kanaldakinin birebir kopyasi degil; sayfada okunur, hasta diliyle
yazildi. Tarih/sure YouTube izleme sayfasindan alindi (VideoObject icin gerekli).
Oynatma: kapaga tiklaninca youtube-nocookie iframe'i ayni yerde acilir
(assets/yt.js). Tiklamadan once YouTube'a hic istek gitmez (kapak i.ytimg.com).
"""

# id: (baslik, uploadDate, sure_sn, shorts, aciklama)
VIDEOS = {
 "FqiyGWjJ6pQ": ("Lenfödem nedir? Genel bilgiler", "2025-08-05", 441, False,
                 "Lenfödemin nedenleri, belirtileri ve neden erken dönemde ele alınması gerektiği."),
 "vRznz6VO0hw": ("Lenfödemde tedavi seçenekleri", "2025-08-09", 627, False,
                 "Konservatif tedaviden LVA ve lenf nodu naklina kadar lenfödem tedavi seçenekleri."),
 "7kAkq6cXGeU": ("Lenf damarını toplardamara bağlama (LVA) ameliyatı", "2025-08-19", 208, False,
                 "Lenfovenöz anastomoz: tıkalı lenf damarının mikroskop altında toplardamara bağlanması."),
 "frMamTWmPMQ": ("Dünya Lenfoloji Kongresi 2025 — lenfödem mikrocerrahisi", "2025-10-22", 434, False,
                 "World Congress of Lymphology 2025'ten lenfödem mikrocerrahisi sunumu."),
 "CVWyERjh7-A": ("Deneysel lenfödem modelinde LVA — RMES, İspanya", "2025-09-19", 64, False,
                 "Lenfovenöz anastomoz tekniğinin deneysel modelde gösterimi (RMES, İspanya)."),
 "b9zZBTMD2eM": ("Doğumsal lenfödemin cerrahi tedavisi", "2016-10-24", 283, False,
                 "Doğuştan gelen (primer) lenfödemde cerrahi tedavi ve sonuçları."),
 "awjG1ww4CZ8": ("Doğumsal lenfödem — cerrahi tedavi sonucu", "2017-12-09", 49, False,
                 "Doğumsal lenfödemde cerrahi tedavi sonrası görünüm."),
 "PaXDdLXzDoI": ("Hidradenit (köpek memesi) hastalığı", "2026-08-24", 55, True,
                 "Hidradenitis suppurativa nedir, neden geçmez ve nasıl tedavi edilir."),
 "25Ur5fsyPZg": ("Yanık sonrası kulak onarımı — kaburga kıkırdağı ile", "2017-04-23", 195, False,
                 "Yanıkla kaybedilen kulağın kaburga kıkırdağından şekillendirilen iskeletle onarımı (Nagata tekniği)."),
 "6HqWBc4906Y": ("El sırtında ganglion kisti ameliyatı", "2022-11-17", 51, False,
                 "Dorsal el bileği ganglion kistinin cerrahi olarak çıkarılması."),
 "rhQm0QfI4x4": ("Meme dikleştirme ve büyütme", "2020-03-11", 43, False,
                 "Meme dikleştirme ve protezle büyütmenin birlikte uygulanması."),
 # --- Shorts (dikey) ---
 "pLrQktZnH7c": ("Kollarda lenfödem", "2026-09-20", 58, True,
                 "Meme kanseri tedavisi sonrası kolda gelişen lenfödem."),
 "C3tF2SlLhG4": ("Hangi lenfödem ameliyatı size uygun?", "2026-09-16", 55, True,
                 "Lenfödem ameliyatının hastaya ve evreye göre seçilmesi."),
 "5YwRObRGB9w": ("Lenfödemde cerrahi ne zaman: erken mi, geç mi?", "2026-09-12", 61, True,
                 "Lenfödemde cerrahi zamanlamanın önemi."),
 "u9ZPUljsmj4": ("Lipödem mi, lenfödem mi? Doğru teşhis", "2026-09-13", 79, True,
                 "Lipödem ile lenfödemin ayırt edilmesi ve doğru teşhisin önemi."),
 "5IFq9hwDI4k": ("Köpek memesi (hidradenit) cerrahi tedavisi", "2026-09-14", 77, True,
                 "Hidradenitis suppurativanın cerrahi tedavisi."),
 "cmbbMc_3Oyw": ("Açık bacak kırığı sonrası damar onarımı", "2019-07-21", 33, True,
                 "Açık tibia kırığı sonrası ön tibial arter yaralanmasının mikrocerrahi ile onarımı."),
 "yiZbM8f0frE": ("Profiloplasti: burun ve çene ucu estetiği", "2020-01-12", 55, True,
                 "Rinoplasti ile çene ucu estetiğinin birlikte uygulanması."),
 "kNccCNH5nXY": ("Yüz ve boyun germe", "2020-03-11", 36, True,
                 "Yüz germe ve boyun germe (facelift, necklift) sonuçları."),
 "zrKEQG3HO_0": ("Meme büyütme", "2020-03-11", 35, True,
                 "Protezle meme büyütme sonucu."),
 "yOkSwqD5kRM": ("Meme dikleştirme ve büyütme — sonuç", "2020-03-11", 59, True,
                 "Meme dikleştirme ve büyütme sonrası görünüm."),
 "NYE7FiFbfE4": ("Labioplasti ve meme estetiği aynı seansta", "2021-06-17", 31, True,
                 "Labioplasti ve meme estetiğinin aynı ameliyatta yapılması."),
 "RYKO0u11jho": ("Meme ve karın estetiği aynı seansta", "2020-08-03", 36, True,
                 "Meme ve karın estetiğinin aynı ameliyatta yapılması."),
 "4oR39pRJsoY": ("Liposuction ile karın germe (lipoabdominoplasti)", "2019-12-19", 37, True,
                 "Karın germe ile birlikte liposuction uygulaması."),
 "3xLQoR0Te9Y": ("Dudak yarığı onarımı", "2020-01-12", 51, True,
                 "Doğumsal dudak yarığının cerrahi onarımı."),
}

# Hizmet sayfasi anahtari -> videolar (sirasiyla gosterilir)
PAGE_VIDEOS = {
 "lenfodem": ["FqiyGWjJ6pQ", "vRznz6VO0hw", "7kAkq6cXGeU", "C3tF2SlLhG4", "5YwRObRGB9w",
              "b9zZBTMD2eM", "frMamTWmPMQ", "CVWyERjh7-A"],
 "kolda-lenfodem": ["pLrQktZnH7c", "7kAkq6cXGeU"],
 "bacakta-lenfodem": ["b9zZBTMD2eM", "awjG1ww4CZ8", "vRznz6VO0hw"],
 "lenfodem-belirtileri": ["FqiyGWjJ6pQ", "pLrQktZnH7c"],
 "lenfodem-evreleri": ["5YwRObRGB9w", "vRznz6VO0hw"],
 "lenfodem-hangi-doktor": ["C3tF2SlLhG4", "5YwRObRGB9w"],
 "lenfodem-neden-olur": ["FqiyGWjJ6pQ", "b9zZBTMD2eM"],
 "lipodem": ["u9ZPUljsmj4"],
 "lipodem-nedir": ["u9ZPUljsmj4"],
 "lipodem-belirtileri": ["u9ZPUljsmj4"],
 "lipodem-hangi-doktor": ["u9ZPUljsmj4"],
 "hidradenit": ["PaXDdLXzDoI", "5IFq9hwDI4k"],
 "mikrotia": ["25Ur5fsyPZg"],
 "yanik": ["25Ur5fsyPZg"],
 "el-cerrahisi": ["6HqWBc4906Y"],
 "alt-ekstremite": ["cmbbMc_3Oyw"],
 "rinoplasti": ["yiZbM8f0frE"],
 "yuz-germe": ["kNccCNH5nXY"],
 "meme-estetigi": ["zrKEQG3HO_0", "yOkSwqD5kRM", "NYE7FiFbfE4", "RYKO0u11jho"],
 "karin-germe": ["4oR39pRJsoY", "RYKO0u11jho"],
 "liposuction": ["4oR39pRJsoY"],
}

# Anasayfa kayan seridi (en altta). Tekrar eden/akademik olanlar cikarildi.
HOME_VIDEOS = ["FqiyGWjJ6pQ", "pLrQktZnH7c", "7kAkq6cXGeU", "u9ZPUljsmj4", "vRznz6VO0hw",
               "5IFq9hwDI4k", "PaXDdLXzDoI", "25Ur5fsyPZg", "C3tF2SlLhG4", "6HqWBc4906Y",
               "kNccCNH5nXY", "b9zZBTMD2eM", "yiZbM8f0frE", "5YwRObRGB9w", "cmbbMc_3Oyw",
               "yOkSwqD5kRM", "frMamTWmPMQ", "NYE7FiFbfE4", "4oR39pRJsoY", "zrKEQG3HO_0",
               "3xLQoR0Te9Y", "RYKO0u11jho"]

CHANNEL = "https://www.youtube.com/@dr.tahsinoguzacarturk"


def _esc(s):
    return (s.replace("&", "&amp;").replace('"', "&quot;")
             .replace("<", "&lt;").replace(">", "&gt;"))


def card(vid, extra_cls=""):
    """Tek video karti. Tiklaninca assets/yt.js iframe'e cevirir."""
    t, _up, _sec, short, _d = VIDEOS[vid]
    cls = "vd-card" + (" short" if short else "") + (" " + extra_cls if extra_cls else "")
    tt = _esc(t)
    return (f'<div class="{cls}" data-yt="{vid}" role="button" tabindex="0" aria-label="{tt} — oynat">'
            f'<img src="https://i.ytimg.com/vi/{vid}/hqdefault.jpg" alt="{tt}" loading="lazy" '
            f'width="480" height="360"><span class="vd-play" aria-hidden="true"></span>'
            f'<span class="vd-t">{tt}</span></div>')


def iso_duration(sec):
    m, s = divmod(int(sec), 60)
    return f"PT{m}M{s}S" if m else f"PT{s}S"


def video_ld(vid):
    t, up, sec, _short, d = VIDEOS[vid]
    return {"@type": "VideoObject", "name": t, "description": d,
            "thumbnailUrl": [f"https://i.ytimg.com/vi/{vid}/hqdefault.jpg"],
            "uploadDate": up, "duration": iso_duration(sec),
            "embedUrl": f"https://www.youtube-nocookie.com/embed/{vid}",
            "contentUrl": f"https://www.youtube.com/watch?v={vid}",
            "author": {"@id": "https://www.droguzacarturk.com/#physician"}}


def home_strip():
    return "\n".join(card(v) for v in HOME_VIDEOS)


if __name__ == "__main__":
    import sys, re
    if "--home" in sys.argv:
        # index.html'deki <!--VIDEOS--> ... <!--/VIDEOS--> blogunu yeniden uretir
        p = "index.html"
        s = open(p, encoding="utf-8").read()
        new = "<!--VIDEOS-->\n" + home_strip() + "\n<!--/VIDEOS-->"
        s2, n = re.subn(r"<!--VIDEOS-->.*?<!--/VIDEOS-->", lambda m: new, s, flags=re.S)
        if not n:
            sys.exit("index.html icinde <!--VIDEOS--> isaretcisi yok")
        open(p, "w", encoding="utf-8").write(s2)
        print(f"anasayfa seridi: {len(HOME_VIDEOS)} video")
    missing = [v for vs in PAGE_VIDEOS.values() for v in vs if v not in VIDEOS]
    missing += [v for v in HOME_VIDEOS if v not in VIDEOS]
    print("eksik id:", missing or "yok")
