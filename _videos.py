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
Shorts (shorts=True) artik sayfalarda kullanilmiyor; yerlerini REELS aldi.
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

# Instagram reels — https://www.instagram.com/dr.oguzacarturk/
# Hoca talebi (Ekim 2026): sitede YouTube Shorts yerine yalnizca Instagram reels.
# Uzun (yatay) YouTube videolari kaliyor. Kapaklar assets/reels/<kod>.jpg (360px,
# hesabin kendi gorselleri). Tarih: kisa koddan (medya kimligi) hesaplandi.
# kod: (baslik, uploadDate, sure_sn, aciklama)
REELS = {
 "DeMtPTWtoQS": ("Mikrotia: ideal ameliyat yaşı", "2026-10-07", 60, "Mikrotia kulak onarımında ameliyat için uygun yaş ve zamanlama."),
 "DeKd2qvtVMn": ("Her lenfödemde LVA yapılabilir mi?", "2026-10-06", 74, "LVA'nın hangi hastalarda uygun olduğu; ileri evrede eksizyonel cerrahinin yeri."),
 "DeHLR8INVaV": ("Mikrotia: en erken ameliyat yaşı", "2026-10-05", 56, "Doğuştan kulak yokluğunda zamanlama ve hastanın kendi kıkırdağıyla onarım planı."),
 "DddmImHtoEN": ("Lenfödem yalnızca bacaklarda olmaz", "2026-09-19", 58, "Meme kanseri tedavisi sonrası kolda gelişen lenfödem."),
 "DdWr1z1N136": ("Lenfödemde hangi hastaya hangi ameliyat?", "2026-09-16", 55, "Lenfödem ameliyatının hastaya ve evreye göre seçilmesi."),
 "DdRDHIYtu54": ("Köpek memesi (hidradenit) cerrahi tedavisi", "2026-09-14", 77, "Hidradenitis suppurativanın cerrahi tedavisi."),
 "DdOcNWuNBkA": ("Lipödem mi, lenfödem mi? Doğru teşhis", "2026-09-13", 79, "Lipödem ile lenfödemin ayırt edilmesi ve doğru teşhisin önemi."),
 "DdLvpwmtQc3": ("Lenfödemde cerrahi ne zaman yapılmalı?", "2026-09-12", 54, "Lenfödemde cerrahi zamanlamanın önemi."),
 "DQHjByeiEbu": ("Dünya Lenfoloji Kongresi 2025", "2025-10-22", 434, "World Congress of Lymphology 2025 — lenfödem mikrocerrahisi."),
 "DNJTfnFIuW2": ("Lenfödem cerrahisi", "2025-08-09", 175, "Lenfödemin erken dönemden itibaren cerrahi tedavisi."),
 "DLrJ4WWoX9i": ("İzmir yangınları sonrası yanık onarımı", "2025-07-04", 16, "Yangınlarda yaralananlar için uzun dönem yanık onarımı duyurusu."),
 "CpehyZfpe7P": ("Mikrotia ameliyatları için Vietnam'da", "2023-03-07", 29, "Vietnam'da mikrotia kulak onarımı ameliyatları."),
 "CfeoBVfJEyq": ("10 yıl önce kopan eli diktiğim hastam", "2022-07-01", 88, "El replantasyonundan 10 yıl sonra hastayla karşılaşma."),
 "Cc-R7uCoVrr": ("Meme büyütmede implant seçimi", "2022-04-30", 53, "Meme büyütme ameliyatında implant boyutu ve profil seçimi."),
 "CNeppBoJK5G": ("Göz kapağı estetiğinde planlama", "2021-04-10", 47, "Blefaroplastide kişiye özel planlama."),
 "CNJ-6J0p_Uo": ("Kepçe kulak estetiği (otoplasti)", "2021-04-02", 45, "Kepçe kulak düzeltme ameliyatı."),
 "CMFzWugJjEt": ("Göz kapağı estetiği", "2021-03-06", 60, "Her göz kapağının ihtiyacına göre ameliyat tekniği."),
 "CLMyzeopT1e": ("Erkekte göz kapağı ameliyatı", "2021-02-12", 60, "Erkeklerde maskülen görünümü koruyan göz kapağı ameliyatı."),
 "CK8__TYpbFo": ("Burun estetiğinde doğal sonuç", "2021-02-06", 36, "Rinoplastide doğal görünüm hedefi."),
 "CKgv_lQJ_yd": ("Kombine ameliyat: meme küçültme ve liposuction", "2021-01-26", 44, "Meme küçültme ile karın ve uyluk liposuction'ın aynı seansta yapılması."),
 "CGkh4-WJtHH": ("Lenfödemde lenfovenöz anastomoz (LVA)", "2020-10-20", 45, "Lenfödem mikrocerrahisi ve liposuction sonrası bir yıllık sonuç."),
 "CFJ3kI0JjBm": ("Yüz ve boyun germe", "2020-09-15", 60, "Yüz ve boyun germe ameliyatı."),
 "CD_D9qQpouT": ("Meme küçültmede kesiler", "2020-08-17", 60, "Daha kısa kesilerle meme küçültme."),
 "CDQtU-lJjj8": ("Meme büyütmede doğru implant boyutu", "2020-07-30", 56, "Ameliyat öncesi planlama ile uygun implant seçimi."),
 "CCqYOc_JVTO": ("Yüz germe hakkında sık sorulanlar", "2020-07-15", 702, "Yüz germe ameliyatı ile ilgili sık sorulan sorular."),
 "CCmdF4kJLGt": ("Liposuction hakkında merak edilenler", "2020-07-13", 538, "Liposuction ile ilgili sık sorulan sorular."),
 "CCjTMNDJ-ZQ": ("Estetik ve işlevsel burun ameliyatı: sorular", "2020-07-12", 552, "Rinoplasti ve nefes alma sorunlarına yönelik burun ameliyatı hakkında sorular."),
 "CCQr6d6pKaj": ("Meme büyütme: sık sorulan sorular", "2020-07-05", 333, "Meme büyütme ameliyatı ile ilgili sık sorulan sorular."),
 "B44xCxFpvHr": ("Bacağı kurtarmak için serbest doku aktarımı", "2019-11-15", 58, "Mikrocerrahi ile serbest doku aktarımı."),
 "B4ia6drp1Ko": ("3 boyutlu planlama ile orta yüz onarımı", "2019-11-06", 60, "Bilgisayar ve model cerrahisi ile orta yüz rekonstrüksiyonu."),
 "B4SD_PxpXBa": ("Yüz onarımında 3 boyutlu planlama", "2019-10-31", 60, "Ateşli silah yaralanması sonrası orta yüz kaybında bilgisayar simülasyonu."),
 "B3Ow5kqnYFb": ("Mikrocerrahi ile topuk onarımı", "2019-10-05", 47, "Yıllardır basamayan hastada topuk rekonstrüksiyonu."),
 "B2yI5RyHHcl": ("Yanık sonrası kulak onarımı", "2019-09-24", 60, "Yanıkla kaybedilen kulağın onarımı."),
 "B21DtltnO1k": ("Mikrotia 1. aşama: kaburga kıkırdağından kulak çatısı", "2019-09-25", 30, "Kaburga kıkırdağından kulak iskeletinin hazırlanması."),
 "B1v2XDzH1Gk": ("Mikrocerrahi ile çene onarımı — 12 yıllık takip", "2019-08-29", 60, "Serbest doku aktarımı ile alt çene rekonstrüksiyonunun uzun dönem sonucu."),
 "BzjHLNOnoEC": ("Mikrotia düzeltme (revizyon) ameliyatı", "2019-07-05", 58, "Daha önce yapılmış mikrotia onarımının düzeltilmesi."),
 "BrievoEF7Ho": ("Parmak ucunda sinir onarımı", "2018-12-18", 60, "Mikrocerrahi ile parmak sinirinin onarımı."),
 "Bj2eJndjWu0": ("Kopan parmak ucunun mikroskopla onarımı", "2018-06-10", 56, "Parmak ucu amputasyonunda mikrocerrahi replantasyon."),
 "BXAnXvSlm7O": ("Kemik grefti ile alt çene onarımı", "2017-07-26", 53, "Alt çene kırığı ve kemik kaybında greftle rekonstrüksiyon."),
 "BWxVPo7FfYa": ("Serbest flep ile ayak onarımı", "2017-07-20", 50, "Anterolateral uyluk flebi ile ayak rekonstrüksiyonu."),
 "BVzOfLFlIbS": ("Kendi dokusuyla meme rekonstrüksiyonu (DIEP)", "2017-06-26", 43, "Mikrocerrahi ile karın dokusundan meme onarımı."),
 "BVoDdFYlN1Y": ("Serbest flep ile meme rekonstrüksiyonu", "2017-06-22", 51, "Mikrocerrahi ile meme onarımı."),
}

# Hizmet sayfasi anahtari -> videolar (sirasiyla gosterilir; YouTube id ya da reels kodu)
PAGE_VIDEOS = {
 "lenfodem": ["FqiyGWjJ6pQ", "DdWr1z1N136", "vRznz6VO0hw", "DeKd2qvtVMn", "7kAkq6cXGeU",
              "DdLvpwmtQc3", "b9zZBTMD2eM", "DNJTfnFIuW2", "frMamTWmPMQ", "CGkh4-WJtHH",
              "DQHjByeiEbu", "CVWyERjh7-A"],
 "kolda-lenfodem": ["DddmImHtoEN", "7kAkq6cXGeU", "DeKd2qvtVMn"],
 "bacakta-lenfodem": ["b9zZBTMD2eM", "awjG1ww4CZ8", "vRznz6VO0hw", "DdWr1z1N136"],
 "lenfodem-belirtileri": ["FqiyGWjJ6pQ", "DddmImHtoEN"],
 "lenfodem-evreleri": ["DdLvpwmtQc3", "vRznz6VO0hw", "DeKd2qvtVMn"],
 "lenfodem-hangi-doktor": ["DdWr1z1N136", "DdLvpwmtQc3"],
 "lenfodem-neden-olur": ["FqiyGWjJ6pQ", "b9zZBTMD2eM", "DddmImHtoEN"],
 "lipodem": ["DdOcNWuNBkA"],
 "lipodem-nedir": ["DdOcNWuNBkA"],
 "lipodem-belirtileri": ["DdOcNWuNBkA"],
 "lipodem-hangi-doktor": ["DdOcNWuNBkA"],
 "hidradenit": ["DdRDHIYtu54"],
 "mikrotia": ["DeMtPTWtoQS", "DeHLR8INVaV", "B21DtltnO1k", "25Ur5fsyPZg", "BzjHLNOnoEC", "CpehyZfpe7P"],
 "yanik": ["25Ur5fsyPZg", "B2yI5RyHHcl", "DLrJ4WWoX9i"],
 "el-cerrahisi": ["CfeoBVfJEyq", "Bj2eJndjWu0", "BrievoEF7Ho", "6HqWBc4906Y"],
 "alt-ekstremite": ["B3Ow5kqnYFb", "B44xCxFpvHr", "BWxVPo7FfYa"],
 "bas-boyun": ["B4ia6drp1Ko", "B4SD_PxpXBa", "B1v2XDzH1Gk"],
 "yuz-kiriklari": ["B1v2XDzH1Gk", "BXAnXvSlm7O"],
 "meme-rek": ["BVzOfLFlIbS", "BVoDdFYlN1Y"],
 "rinoplasti": ["CK8__TYpbFo", "CCjTMNDJ-ZQ"],
 "yuz-germe": ["CFJ3kI0JjBm", "CCqYOc_JVTO"],
 "goz-kapagi": ["CMFzWugJjEt", "CNeppBoJK5G", "CLMyzeopT1e"],
 "lip-lift": ["CNJ-6J0p_Uo"],
 "meme-estetigi": ["Cc-R7uCoVrr", "CDQtU-lJjj8", "CCQr6d6pKaj", "CD_D9qQpouT", "rhQm0QfI4x4"],
 "karin-germe": ["CKgv_lQJ_yd"],
 "liposuction": ["CKgv_lQJ_yd", "CCmdF4kJLGt"],
}

# Anasayfa kayan seridi (en altta): uzun YouTube videolari + reels karisik.
HOME_VIDEOS = ["FqiyGWjJ6pQ", "DddmImHtoEN", "7kAkq6cXGeU", "DdOcNWuNBkA", "vRznz6VO0hw",
               "DdRDHIYtu54", "DeMtPTWtoQS", "25Ur5fsyPZg", "DdWr1z1N136", "6HqWBc4906Y",
               "DeKd2qvtVMn", "CfeoBVfJEyq", "b9zZBTMD2eM", "DdLvpwmtQc3", "B3Ow5kqnYFb",
               "frMamTWmPMQ", "DeHLR8INVaV", "B4ia6drp1Ko", "rhQm0QfI4x4", "CMFzWugJjEt",
               "Cc-R7uCoVrr", "CFJ3kI0JjBm"]

INSTAGRAM = "https://www.instagram.com/dr.oguzacarturk/"
CHANNEL = "https://www.youtube.com/@dr.tahsinoguzacarturk"


def _esc(s):
    return (s.replace("&", "&amp;").replace('"', "&quot;")
             .replace("<", "&lt;").replace(">", "&gt;"))


def card(vid, extra_cls=""):
    """Tek video karti. Tiklaninca assets/yt.js oynaticiyi acar
    (YouTube: kartin icinde; Instagram reels: sayfa ustunde pencere)."""
    if vid in REELS:
        t = REELS[vid][0]
        cls = "vd-card short ig" + (" " + extra_cls if extra_cls else "")
        tt = _esc(t)
        return (f'<div class="{cls}" data-ig="{vid}" role="button" tabindex="0" aria-label="{tt} — oynat">'
                f'<img src="/assets/reels/{vid}.jpg" alt="{tt}" loading="lazy" width="360" height="640">'
                f'<span class="vd-play" aria-hidden="true"></span><span class="vd-ig" aria-hidden="true"></span>'
                f'<span class="vd-t">{tt}</span></div>')
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
    if vid in REELS:
        t, up, sec, d = REELS[vid]
        return {"@type": "VideoObject", "name": t, "description": d,
                "thumbnailUrl": [f"https://www.droguzacarturk.com/assets/reels/{vid}.jpg"],
                "uploadDate": up, "duration": iso_duration(sec),
                "embedUrl": f"https://www.instagram.com/reel/{vid}/embed/",
                "contentUrl": f"https://www.instagram.com/reel/{vid}/",
                "author": {"@id": "https://www.droguzacarturk.com/#physician"}}
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
    ALL = set(VIDEOS) | set(REELS)
    missing = [v for vs in PAGE_VIDEOS.values() for v in vs if v not in ALL]
    missing += [v for v in HOME_VIDEOS if v not in ALL]
    import os
    missing += [f"kapak:{v}" for v in REELS if not os.path.exists(f"assets/reels/{v}.jpg")]
    shorts = [v for vs in list(PAGE_VIDEOS.values()) + [HOME_VIDEOS] for v in vs if v in VIDEOS and VIDEOS[v][3]]
    print("sitede kalan YouTube Shorts:", shorts or "yok")
    print("eksik id:", missing or "yok")
