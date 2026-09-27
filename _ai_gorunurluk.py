# -*- coding: utf-8 -*-
"""
AI gorunurluk takibi — ChatGPT / Perplexity / Google AI Overview / Claude
gibi yapay zeka arama motorlarinda site ve rakiplerin ne siklikla
gosterildigini elle kaydedip 4 KPI'a donusturur:

  1) AI Gorunurluk Skoru   — sorgu-platform kombinasyonlarinin yuzde kaci
                              bizi hic gosterdi (atif ya da marka adi gecti)
  2) AI Share of Voice     — gosterildigimiz yerlerde, rakiplere kiyasla
                              ne kadar yer kapladik
  3) AI Oneri Orani        — sadece "gecti" degil, acikca "gidin" denen oran
  4) AI Trafik & Donusum   — bu platformlardan gelen ziyaret/randevu (GA4'ten
                              elle CSV dusurulerek okunur; API/OAuth yok)

NEDEN ELLE KAYIT (otomatik degil):
  ChatGPT / Perplexity / Google AI Overview / Claude'un resmi bir "kim atif
  aldi" API'si yok. Peec AI, Otterly, ZipTie gibi ucretli araclar bunu
  otomatiklestirir ama bu asamada gerek yok: ayda 15-20 dakika ayirip asagidaki
  ONCELIKLI_SORGULAR listesini (ve eklemek istediklerinizi) dort platformda
  tek tek sorup _gsc/ai-gorunurluk-log.csv dosyasina birer satir eklemek
  yeterli bir baslangic.

KULLANIM:
  1) ONCELIKLI_SORGULAR listesindeki (ya da kendi ekledigimiz) sorgulari
     ChatGPT, Perplexity, Google (AI Overview varsa) ve Claude'da sorun.
  2) Her sorgu-platform kombinasyonu icin _gsc/ai-gorunurluk-log.csv'ye
     bir satir ekleyin — sutunlar asagida.
  3) (Istege bagli) GA4 > Trafik edinme > Kullanici edinme raporunu
     "Oturum kaynagi" ile chatgpt.com / perplexity.ai / gemini.google.com /
     claude.ai icin filtreleyip _gsc/ai-trafik.csv olarak disa aktarin.
  4) python3 _ai_gorunurluk.py

CIKTI: terminale 4 KPI + rakip haritasi (PDF degil, ic kullanim — GSC firsat
raporuyla ayni mantik).

LOG SUTUNLARI (_gsc/ai-gorunurluk-log.csv):
  tarih                 YYYY-AA-GG
  platform              chatgpt / perplexity / google-ai-overview / claude
  sorgu                 test edilen soru, oldugu gibi
  atif_var_mi           0/1 — droguzacarturk.com kaynak/link olarak gectiyse 1
  marka_bahsedildi_mi   0/1 — link olmasa da "Dr. Acarturk" adi gectiyse 1
  oneri_seviyesi        yok / bahsedildi / onerildi
  rakip_sayisi          cevapta isim isim gecen baska hekim/kurum sayisi
  rakip_adlari          ; ile ayrik isim listesi (bos olabilir)
  kaynak_sayfa          atif aldiysa hangi sayfamiz (bos olabilir)
  not                   serbest metin, kisa

TRAFIK SUTUNLARI (_gsc/ai-trafik.csv, opsiyonel):
  tarih_araligi, kaynak, oturum, donusum
"""
import csv
import os
import sys
from collections import defaultdict, Counter

KOK = os.path.dirname(os.path.abspath(__file__))
GSC = os.path.join(KOK, "_gsc")
LOG = os.path.join(GSC, "ai-gorunurluk-log.csv")
TRAFIK = os.path.join(GSC, "ai-trafik.csv")

ALANLAR = ["tarih", "platform", "sorgu", "atif_var_mi", "marka_bahsedildi_mi",
           "oneri_seviyesi", "rakip_sayisi", "rakip_adlari", "kaynak_sayfa", "not"]

# Cowork'te belirlenen oncelikli sorgular — istediginiz kadar ekleyin/cikarin.
ONCELIKLI_SORGULAR = [
    "izmir lenfödem cerrahı kime gidilir",
    "izmir yanık ameliyatı hangi doktor",
    "lipödem belirtileri nelerdir",
    "izmir lenfödem özel muayene nerede yaptırabilirim",
    "izmir mikrotia ameliyatı uzmanı",
    "izmir mikrocerrahi onarım uzmanı",
]

PLATFORMLAR = ["chatgpt", "perplexity", "google-ai-overview", "claude"]


# ============================== yardimcilar ==============================

def _b(s):
    """'1' / 'evet' / 'true' -> True"""
    return str(s or "").strip().lower() in ("1", "evet", "true", "yes", "x")


def _int(s):
    s = str(s or "").strip()
    return int(s) if s.isdigit() else 0


def _oku_log():
    if not os.path.exists(LOG):
        return []
    with open(LOG, encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def _olustur_bos_log():
    os.makedirs(GSC, exist_ok=True)
    with open(LOG, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=ALANLAR)
        w.writeheader()


def _basli(baslik):
    print("\n" + "=" * 78)
    print(baslik)
    print("-" * 78)


# ============================== KPI hesaplari ==============================

def kpi_gorunurluk(satirlar):
    """Sorgu-platform kombinasyonlarinin yuzde kaci bizi hic gosterdi."""
    if not satirlar:
        return 0.0
    goruldu = sum(1 for r in satirlar
                  if _b(r.get("atif_var_mi")) or _b(r.get("marka_bahsedildi_mi")))
    return goruldu / len(satirlar) * 100


def kpi_sov(satirlar):
    """Gosterildigimiz yerlerde rakiplere kiyasla kapladigimiz pay (ortalama)."""
    if not satirlar:
        return 0.0
    toplam = 0.0
    for r in satirlar:
        biz = 1 if (_b(r.get("atif_var_mi")) or _b(r.get("marka_bahsedildi_mi"))) else 0
        rakip = _int(r.get("rakip_sayisi"))
        payda = biz + rakip
        toplam += (biz / payda) if payda else 0.0
    return toplam / len(satirlar) * 100


def kpi_oneri(satirlar):
    """Sadece 'gecti' degil, acikca 'gidin' denen oran."""
    if not satirlar:
        return 0.0
    onerildi = sum(1 for r in satirlar if (r.get("oneri_seviyesi") or "").strip().lower() == "onerildi")
    return onerildi / len(satirlar) * 100


def rakip_haritasi(satirlar):
    sayac = Counter()
    for r in satirlar:
        adlar = (r.get("rakip_adlari") or "").split(";")
        for ad in adlar:
            ad = ad.strip()
            if ad:
                sayac[ad] += 1
    return sayac.most_common(15)


def platform_kirilimi(satirlar):
    by_p = defaultdict(list)
    for r in satirlar:
        by_p[(r.get("platform") or "?").strip().lower()].append(r)
    out = {}
    for p, rows in by_p.items():
        out[p] = {
            "n": len(rows),
            "gorunurluk": kpi_gorunurluk(rows),
            "sov": kpi_sov(rows),
            "oneri": kpi_oneri(rows),
        }
    return out


def sorgu_kirilimi(satirlar):
    by_q = defaultdict(list)
    for r in satirlar:
        by_q[(r.get("sorgu") or "?").strip()].append(r)
    out = []
    for q, rows in by_q.items():
        out.append((q, kpi_gorunurluk(rows), kpi_sov(rows), len(rows)))
    out.sort(key=lambda x: x[1])  # en dusuk gorunurluk once (oncelik listesi)
    return out


def trafik_ozet():
    if not os.path.exists(TRAFIK):
        return None
    with open(TRAFIK, encoding="utf-8-sig", newline="") as f:
        satirlar = list(csv.DictReader(f))
    if not satirlar:
        return None
    by_kaynak = defaultdict(lambda: {"oturum": 0, "donusum": 0})
    for r in satirlar:
        k = (r.get("kaynak") or "?").strip()
        by_kaynak[k]["oturum"] += _int(r.get("oturum"))
        by_kaynak[k]["donusum"] += _int(r.get("donusum"))
    return by_kaynak


# ================================== rapor ==================================

def main():
    if not os.path.isdir(GSC):
        os.makedirs(GSC, exist_ok=True)

    if not os.path.exists(LOG):
        _olustur_bos_log()
        print(f"'{os.path.relpath(LOG, KOK)}' olusturuldu (bos).")
        print("Once oncelikli sorgulari AI platformlarinda sorup satir ekleyin:\n")
        for s in ONCELIKLI_SORGULAR:
            print(f"  - {s}")
        print(f"\nSutunlar: {', '.join(ALANLAR)}")
        return 1

    satirlar = _oku_log()
    if not satirlar:
        print(f"'{os.path.relpath(LOG, KOK)}' bos. Satir ekleyip tekrar calistirin.")
        return 1

    tarihler = sorted({(r.get("tarih") or "").strip() for r in satirlar if r.get("tarih")})
    donem = f"{tarihler[0]} — {tarihler[-1]}" if tarihler else "tarih belirtilmemis"

    _basli("AI GÖRÜNÜRLÜK — 4 KPI")
    print(f"  Dönem                 : {donem}")
    print(f"  Kayıtlı ölçüm         : {len(satirlar)} sorgu × platform")
    print(f"\n  1) AI Görünürlük Skoru : %{kpi_gorunurluk(satirlar):.1f}"
          "   (bizi hiç gösteren ölçüm oranı)")
    print(f"  2) AI Share of Voice   : %{kpi_sov(satirlar):.1f}"
          "   (göründüğümüz yerlerde rakiplere kıyasla payımız)")
    print(f"  3) AI Öneri Oranı      : %{kpi_oneri(satirlar):.1f}"
          "   (sadece geçmedik, açıkça önerildik)")

    trafik = trafik_ozet()
    _basli("4) AI TRAFİK & DÖNÜŞÜM")
    if trafik is None:
        print("  Veri yok — _gsc/ai-trafik.csv eklenmedi.")
        print("  GA4 > Trafik edinme > Kullanıcı edinme raporunu 'Oturum kaynağı'")
        print("  ile chatgpt.com / perplexity.ai / gemini.google.com / claude.ai için")
        print("  filtreleyip şu sütunlarla dışa aktarın: tarih_araligi,kaynak,oturum,donusum")
    else:
        print(f"  {'KAYNAK':<24} {'OTURUM':>8} {'DÖNÜŞÜM':>9} {'ORAN':>7}")
        for k, v in sorted(trafik.items(), key=lambda x: -x[1]["oturum"]):
            oran = (v["donusum"] / v["oturum"] * 100) if v["oturum"] else 0.0
            print(f"  {k:<24} {v['oturum']:>8} {v['donusum']:>9} {oran:>6.1f}%")

    _basli("PLATFORM KIRILIMI")
    pk = platform_kirilimi(satirlar)
    print(f"  {'PLATFORM':<20} {'ÖLÇÜM':>6} {'GÖRÜNÜRLÜK':>11} {'SOV':>7} {'ÖNERİ':>7}")
    for p in PLATFORMLAR + [x for x in pk if x not in PLATFORMLAR]:
        if p not in pk:
            print(f"  {p:<20} {'—':>6} {'—':>11} {'—':>7} {'—':>7}  (henüz kayıt yok)")
            continue
        v = pk[p]
        print(f"  {p:<20} {v['n']:>6} {v['gorunurluk']:>10.1f}% {v['sov']:>6.1f}% {v['oneri']:>6.1f}%")

    _basli("SORGU BAZINDA ÖNCELİK  —  en düşük görünürlükten yükseğe")
    print("  Bu sırayla ele alın: en altta kalanlar en büyük fırsat/risk.\n")
    for q, gor, sov, n in sorgu_kirilimi(satirlar):
        q_kisa = q if len(q) <= 46 else q[:43] + "..."
        print(f"  görünürlük %{gor:>5.1f}  ·  sov %{sov:>5.1f}  ·  n={n:<2}  {q_kisa}")

    _basli("RAKİP HARİTASI  —  AI cevaplarında en çok isim geçenler")
    rh = rakip_haritasi(satirlar)
    if not rh:
        print("  (kayıtlı rakip adı yok)")
    else:
        for ad, adet in rh:
            print(f"  {adet:>2}×  {ad}")

    eksik = [s for s in ONCELIKLI_SORGULAR
             if s not in {r.get("sorgu", "").strip() for r in satirlar}]
    if eksik:
        _basli("HENÜZ TEST EDİLMEMİŞ ÖNCELİKLİ SORGULAR")
        for s in eksik:
            print(f"  - {s}")

    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
