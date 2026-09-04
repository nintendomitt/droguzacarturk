# -*- coding: utf-8 -*-
"""
GSC firsat raporu — birinci sayfaya yakin ama tiklama alamayan sayfalari bulur.

NEDEN BU ARAC:
  Sitenin darbogazi icerik sayisi degil, sira. 9-15. sirada olup tiklama
  alamayan sayfalari yukari tasimak, yeni yazi yazmaktan daha cok tiklama
  getiriyor. Bu arac o sayfalari onceliklendirir.

NEDEN CSV:
  GSC API'si OAuth kimlik bilgisi ister. Kimlik bilgisi tutmamak icin
  Search Console'un kendi disa aktarimini okuyoruz. Kimse token saklamiyor.

KULLANIM:
  1. Search Console > Performans > sag ustte EXPORT > "Virgulle ayrilmis deger"
     (ya da Excel/Google E-Tablolar > CSV indir)
  2. Cikan zip'i acin; icinde "Sorgular.csv" ve "Sayfalar.csv" olur
  3. Bu klasordeki _gsc/ dizinine koyun
  4. python3 _gsc_firsat.py

Dosya adlari TR/EN farkedmez; icerik basliklarindan anlar.
"""
import csv, os, glob, io, re, sys

DIZIN = "_gsc"

# --- esikler ---
YAKIN_ALT, YAKIN_UST = 5.0, 20.0   # "birinci sayfaya yakin" bandi
MIN_GOSTERIM        = 20           # bu altindaki gurultu
DUSUK_TO            = 2.0          # % — bu altindakiler baslik/snippet sorunu


def _sayi(s):
    if s is None:
        return 0.0
    s = str(s).strip().replace("%", "").replace("\xa0", "")
    if not s:
        return 0.0
    # GSC TR ciktisi "1.234,5" / EN ciktisi "1,234.5" verebilir
    if "," in s and "." in s:
        s = s.replace(".", "").replace(",", ".") if s.rfind(",") > s.rfind(".") else s.replace(",", "")
    elif "," in s:
        s = s.replace(",", ".") if len(s.split(",")[-1]) <= 2 else s.replace(",", "")
    try:
        return float(s)
    except ValueError:
        return 0.0


def _oku(yol):
    """CSV'yi basliklarindan taniyarak okur (TR ve EN GSC ciktisi)."""
    ham = open(yol, "rb").read()
    for enc in ("utf-8-sig", "utf-16", "cp1254", "latin-1"):
        try:
            metin = ham.decode(enc)
            break
        except UnicodeDecodeError:
            continue
    else:
        return []
    ayirici = ";" if metin.count(";") > metin.count(",") else ","
    satirlar = list(csv.DictReader(io.StringIO(metin), delimiter=ayirici))
    if not satirlar:
        return []

    def alan(*adaylar):
        for a in satirlar[0]:
            if a and a.strip().lower() in adaylar:
                return a
        return None

    k_ad  = alan("en popüler sorgular", "top queries", "sorgu", "query",
                 "en popüler sayfalar", "top pages", "sayfa", "page")
    k_tik = alan("tıklamalar", "clicks")
    k_gos = alan("gösterimler", "impressions")
    k_pos = alan("konum", "position", "ortalama konum", "average position")
    if not (k_ad and k_gos and k_pos):
        return []

    out = []
    for r in satirlar:
        out.append({
            "ad":  (r.get(k_ad) or "").strip(),
            "tik": _sayi(r.get(k_tik)),
            "gos": _sayi(r.get(k_gos)),
            "pos": _sayi(r.get(k_pos)),
        })
    return [x for x in out if x["ad"]]


def _to(x):
    return (x["tik"] / x["gos"] * 100) if x["gos"] else 0.0


def _puan(x):
    """Oncelik puani: cok gosterim + birinci sayfaya yakinlik = buyuk firsat."""
    yakinlik = max(0.0, (YAKIN_UST - x["pos"])) / (YAKIN_UST - YAKIN_ALT)
    return x["gos"] * max(0.05, yakinlik)


def _yaz(baslik, satirlar, aciklama):
    print("\n" + "=" * 78)
    print(baslik)
    print("-" * 78)
    print(aciklama)
    if not satirlar:
        print("  (bu kategoride kayit yok)")
        return
    print(f"\n  {'':2} {'GÖSTERİM':>9} {'TIK':>5} {'TO':>6} {'SIRA':>6}  KAYIT")
    for i, x in enumerate(satirlar, 1):
        ad = x["ad"]
        if len(ad) > 52:
            ad = ad[:49] + "..."
        print(f"  {i:>2} {int(x['gos']):>9} {int(x['tik']):>5} {_to(x):>5.1f}% {x['pos']:>6.1f}  {ad}")


def main():
    if not os.path.isdir(DIZIN):
        os.makedirs(DIZIN, exist_ok=True)
        print(f"'{DIZIN}/' klasörü oluşturuldu. GSC dışa aktarımını buraya koyup tekrar çalıştırın.")
        print(__doc__)
        return 1

    dosyalar = sorted(glob.glob(os.path.join(DIZIN, "*.csv")))
    if not dosyalar:
        print(f"'{DIZIN}/' içinde CSV yok.")
        print(__doc__)
        return 1

    sorgular, sayfalar = [], []
    for d in dosyalar:
        kayit = _oku(d)
        if not kayit:
            print(f"  (okunamadı, atlandı: {os.path.basename(d)})")
            continue
        ad = os.path.basename(d).lower()
        hedef = sayfalar if ("sayfa" in ad or "page" in ad) else sorgular
        hedef.extend(kayit)
        print(f"  okundu: {os.path.basename(d)} — {len(kayit)} satır")

    if not sorgular and not sayfalar:
        print("Tanınabilir veri bulunamadı.")
        return 1

    # --- 1. Birinci sayfaya yakin sorgular ---
    yakin = [x for x in sorgular
             if YAKIN_ALT <= x["pos"] <= YAKIN_UST and x["gos"] >= MIN_GOSTERIM]
    yakin.sort(key=_puan, reverse=True)
    _yaz("1) BİRİNCİ SAYFAYA YAKIN SORGULAR  —  en yüksek getirili iş",
         yakin[:15],
         "  Bu sorgularda zaten görünüyoruz ama tıklama alamıyoruz. Sırayı 3-5 basamak\n"
         "  yukarı taşımak, yeni yazı yazmaktan çok daha fazla tıklama getirir.\n"
         "  Yapılacak: ilgili sayfayı derinleştir, iç link ver, kaynak ekle.")

    # --- 2. Iyi sirada ama tiklanmiyor: baslik/snippet sorunu ---
    to_dusuk = [x for x in sorgular
                if x["pos"] <= 10.0 and x["gos"] >= MIN_GOSTERIM and _to(x) < DUSUK_TO]
    to_dusuk.sort(key=lambda x: x["gos"], reverse=True)
    _yaz("2) SIRASI İYİ AMA TIKLANMIYOR  —  başlık/açıklama sorunu",
         to_dusuk[:10],
         "  İlk 10'dayız ama TO çok düşük. Sıra sorunu değil, snippet sorunu.\n"
         "  Yapılacak: title ve meta description'ı sorgunun diline yaklaştır.")

    # --- 3. Sayfa bazli ayni analiz ---
    sy = [x for x in sayfalar
          if YAKIN_ALT <= x["pos"] <= YAKIN_UST and x["gos"] >= MIN_GOSTERIM]
    sy.sort(key=_puan, reverse=True)
    _yaz("3) YUKARI TAŞINACAK SAYFALAR",
         sy[:12],
         "  Sayfa bazında aynı fırsat. Bu URL'lere iç link vermek en hızlı kaldıraç.")

    # --- 4. Ozet ---
    print("\n" + "=" * 78)
    print("ÖZET")
    print("-" * 78)
    kayip = sum(x["gos"] for x in yakin)
    print(f"  İncelenen sorgu           : {len(sorgular)}")
    print(f"  İncelenen sayfa           : {len(sayfalar)}")
    print(f"  Birinci sayfaya yakın     : {len(yakin)} sorgu, ~{int(kayip)} gösterim")
    print(f"  Snippet sorunu olan       : {len(to_dusuk)} sorgu")
    if yakin:
        # 11. siradan 6. siraya cikis kabaca %2 -> %6 TO demek
        print(f"\n  Kaba tahmin: bu {len(yakin)} sorgu ilk 5'e taşınsa,")
        print(f"  aynı gösterimden ~{int(kayip * 0.06)} tıklama çıkar")
        print(f"  (şu an ~{int(sum(x['tik'] for x in yakin))} alıyor).")
    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
