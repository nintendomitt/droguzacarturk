# SEO Büyüme Planı — droguzacarturk.com

**Hedef:** "lenfödem tedavisi" aramasında birinci sıra
**Hazırlık tarihi:** 17 Ağustos 2026
**Veri kaynağı:** Semrush TR veritabanı + canlı SERP analizi

---

## 1. Önce iyi haber: hedef sandığınızdan kolay

"lenfödem tedavisi" için zorluk skoru **13/100**. Bu çok düşük. Karşılaştırma için: "lipödem tedavisi" 21, "burun estetiği" gibi terimler 60+.

Daha önemlisi — SERP'te şu an **bireysel doktor siteleri hastanelerin arasında ilk sayfada duruyor**:

| Sıra | Site | Tip |
|---|---|---|
| 1 | lenfodemdernegi.org.tr | Dernek |
| 2 | baskenthastaneleri.com | Hastane |
| 3 | acibadem.com.tr | Hastane |
| 5 | **youtube.com** | Video |
| 8 | **youtube.com** | Video |
| 9 | **drsalihaerogludemir.com** | Bireysel doktor |
| 13 | **drgultentanaksoy.com** | Bireysel doktor |
| 14 | **sibelkibar.com** | Bireysel doktor |

Bu tablo iki şey söylüyor:

1. **Hastaneleri geçmek mümkün.** Üç bireysel doktor sitesi zaten orada. Onlar fizik tedavi hekimi; Oğuz Hoca ise cerrahi tarafında ve akademik kimliği çok daha güçlü.
2. **İki YouTube videosu ilk sayfada.** Google bu sorgu için video istiyor. Bu, elimizde olan ama kullanmadığımız bir kanal.

---

## 2. Kötü haber: mevcut site hiçbir tıbbi terimde yok

Eski Wix sitesinin tüm organik görünürlüğü **doktorun kendi adından** geliyor:

| Anahtar kelime | Sıra | Aylık arama |
|---|---|---|
| tahsin oğuz acartürk | 1 | 590 |
| estetik cerrah tahsin oğuz acartürk | 1 | 320 |
| oğuz acartürk | 1 | 260 |

"lenfödem", "lipödem", "meme rekonstrüksiyonu" — hiçbirinde sıralama yok. Site marka sorgularının dışına çıkamamış.

**Bunun iki sonucu var:**
- Taşınmada kaybedecek sıralama neredeyse yok → **migration riski çok düşük**
- Marka aramalarını korumak için 301'ler yine de şart (ayda ~1.200 aramalık trafik)

> **Acil uyarı:** Eski sitedeki `/meme-buyutme` sayfası pornografik bir arama teriminde 4. sırada çıkıyor. Bu sayfaya gelen trafik hasta trafiği değil ve sayfa kalite sinyalleri açısından risk taşıyor. Taşımada bu URL'yi yeni meme estetiği sayfasına 301'lemek yerine **doğrudan anasayfaya yönlendirmenizi** öneriyorum.

---

## 3. En kritik bulgu: yanlış hedefe nişan alıyoruz

Lenfödem odağı doğru ama **lipödem 5 kat büyük bir pazar** — ve Oğuz Hoca zaten ikisini de yapıyor.

| Küme | Toplam aylık arama |
|---|---|
| Lenfödem (tüm varyantlar) | ~25.000 |
| **Lipödem (tüm varyantlar)** | **~120.000** |

Tek tek en değerli fırsatlar:

| Anahtar kelime | Aylık | Zorluk | Durum |
|---|---|---|---|
| lipödem nedir | 33.100 | 20 | Sayfa yok |
| lipödem diyeti | 9.900 | 21 | Sayfa yok |
| lipödem tedavisi | 9.900 | 21 | Kısmen |
| lipödem belirtileri | 4.400 | 15 | Sayfa yok |
| **lipödem hangi doktor bakar** | **2.400** | **8** | Sayfa yok |
| **ameliyatsız lipödem tedavisi** | **2.400** | **9** | Sayfa yok |
| **bacakta lenfödem belirtileri** | **2.400** | **17** | Sayfa yok |
| lenfödem tedavisi | 2.900 | 13 | Var |
| bacaklarda lenfödem tedavisi | 1.300 | 17 | Sayfa yok |
| lenfödem neden olur | 1.000 | 21 | Kısmen |
| lenfödem belirtileri | 1.600 | 18 | Kısmen |
| kolda lenfödem belirtileri | 720 | 11 | Sayfa yok |
| **lenfödeme hangi bölüm bakar** | **390** | **6** | Sayfa yok |
| lenfödem evreleri | 320 | 6 | Var |
| lipödem lenfödem farkı | 210 | 10 | Var |

Kalın yazılanlar **zorluğu 10'un altında** — yani doğru sayfayla birkaç ay içinde ilk sıraya oturabilecek sorgular.

`lenfödeme hangi bölüm bakar` ve `lipödem hangi doktor bakar` özellikle değerli: bunlar **doktor arayan** insanlar. Zorluk 6 ve 8. Bu iki sorgunun cevabı bir doçent doktorun kendi sitesinden gelmeli.

---

## 4. Öneriler — öncelik sırasıyla

### ÖNCELİK 1 — Alan adı taşıma (her şeyin önkoşulu)

Yapılmadan aşağıdakilerin hiçbiri işe yaramaz. Site canonical olarak droguzacarturk.com'u gösteriyor ama orada değil; Google hiçbir sayfayı indekslemiyor.

- [ ] DNS: A kayıtları + CNAME → GitHub Pages
- [ ] CNAME dosyası ve HTTPS zorlaması
- [ ] Wix'te sayfa bazlı 301 haritası (en az 12 ay açık kalmalı)
- [ ] Google Search Console: adres değişikliği bildirimi + sitemap gönderimi
- [ ] `/meme-buyutme` → anasayfa (yukarıdaki uyarı)

### ÖNCELİK 2 — Lenfödem kümesini parçalara ayır

Şu an lenfödem tek sayfada. Google, her ayrı niyet için ayrı sayfa görmek istiyor. Mevcut sayfayı **hub** yapıp altına uydu sayfalar açalım:

```
lenfodem-lipodem-cerrahisi.html   (hub — mevcut)
├── bacakta-lenfodem.html          → 3.700/ay
├── kolda-lenfodem.html            → 720+/ay (meme kanseri sonrası)
├── lenfodem-belirtileri.html      → 1.600/ay
├── lenfodem-neden-olur.html       → 1.000/ay
├── lenfodem-hangi-doktor.html     → 390/ay, zorluk 6
└── lenfodem-evreleri.html         → 320/ay
```

Her sayfa hub'a, hub her sayfaya link verecek. Bu yapı Google'a konu otoritesi sinyali gönderiyor.

### ÖNCELİK 3 — Lipödem kümesini kur (en büyük getiri)

```
lipodem-cerrahisi.html            (hub — mevcut)
├── lipodem-nedir.html             → 33.100/ay
├── lipodem-belirtileri.html       → 4.400/ay
├── lipodem-hangi-doktor.html      → 2.400/ay, zorluk 8
├── ameliyatsiz-lipodem-tedavisi.html → 2.400/ay, zorluk 9
├── lipodem-diyeti.html            → 9.900/ay
└── lipodem-evreleri.html          → 590/ay
```

**Not:** "ameliyatsız lipödem tedavisi" sayfası dürüst yazılmalı — konservatif yöntemlerin ne yapıp ne yapamadığını anlatıp, cerrahinin ne zaman gerektiğini söyleyen bir sayfa. Bu hem etik hem de dönüşüm açısından satış dilinden daha etkili.

### ÖNCELİK 4 — Alternatif tedavi sorgularını dürüstçe karşıla

Ayda ~2.800 arama, kanıtı olmayan yöntemlere gidiyor:

| Sorgu | Aylık | Zorluk |
|---|---|---|
| zerdeçal lenfödem | 1.600 | 8 |
| hacamat ile lenfödem tedavisi | 720 | 6 |
| lenfödeme iyi gelen bitkiler | 260 | 5 |
| lenfödem bitkisel tedavisi | 170 | 5 |

Bu insanlar şu an yanlış bilgi bulan hastalar. **Bir doçent doktorun bu sorulara kanıta dayalı cevap vermesi** hem ciddi trafik getirir hem de sitenin güvenilirliğini yükseltir. Sayfa "bunlar işe yaramaz" demek yerine, bu yöntemlerin ne olduğunu, literatürün ne söylediğini ve neyin gerçekten işe yaradığını anlatmalı.

Zorluklar 5–8 — yani hemen hemen boş bir alan.

### ÖNCELİK 5 — Video (Google bu sorguda video istiyor)

"lenfödem tedavisi" ilk sayfasında iki YouTube videosu var. Oğuz Hoca'nın kanalı zaten mevcut.

- [ ] Her hub sayfasına ilgili videoyu göm
- [ ] `VideoObject` yapısal verisi ekle (Google video zengin sonucu verebiliyor)
- [ ] Video başlıklarını sorgu diliyle eşleştir: "Lenfödem Tedavisi Nasıl Yapılır?"
- [ ] Video açıklamasından ilgili sayfaya link

Bu, rekabetin en zayıf olduğu alan — hastaneler bunu iyi yapmıyor.

### ÖNCELİK 6 — E-E-A-T sinyallerini güçlendir

Sağlık içeriği Google'ın YMYL kategorisinde; yazar otoritesi doğrudan sıralama faktörü.

- [ ] Her sayfaya görünür yazar kutusu: unvan, kurum, deneyim (kısmen var)
- [ ] "Tıbbi inceleme tarihi" + "son güncelleme" satırı
- [ ] Her tıbbi iddiaya kaynak: PubMed, ISL kılavuzu, uluslararası dernek
- [ ] Oğuz Hoca'nın kendi yayınlarının listelendiği bir akademik sayfa — bu, konu otoritesinin en güçlü kanıtı
- [ ] `sameAs` ile PubMed, ORCID, LinkedIn, üniversite profili bağlantıları

### ÖNCELİK 7 — Yerel SEO

"lenfödem izmir" hacmi düşük (30/ay) ama niyeti çok yüksek. Asıl kazanç Google haritalarda.

- [ ] Google Business Profile aç/doğrula — hizmet listesine lenfödem ve lipödem cerrahisi
- [ ] `MedicalClinic` + `geo` koordinat yapısal verisi
- [ ] NAP tutarlılığı (isim-adres-telefon her yerde aynı)

### ÖNCELİK 8 — Bağlantı kazanımı

- [ ] **lenfodemdernegi.org.tr** "tedavi yapan merkezler" listesine başvuru — bu, konusuyla birebir alakalı ve o site "lenfödem tedavisi"nde 1. sırada
- [ ] Türk Plastik Rekonstrüktif ve Estetik Cerrahi Derneği üye profili
- [ ] Üniversite ve hastane profillerinden site linki
- [ ] Sağlık haber siteleriyle uzman görüşü içerikleri

---

## 5. Beklenen tablo

| Dönem | Beklenti |
|---|---|
| 0–1 ay | Taşıma, indeksleme başlar. Marka sorguları geri gelir. |
| 1–3 ay | Düşük zorluklu sorgular (zorluk <10) ilk sayfaya girer |
| 3–6 ay | "lenfödem tedavisi" ilk sayfa; uzun kuyruk trafiği birikir |
| 6–12 ay | Konu otoritesi oturur; ana sorgularda ilk 3 hedefi gerçekçi |

Sağlık alanında Google yeni siteye güvenmek için zaman istiyor. Zorluk skorları düşük olduğu için bu takvim iyimser değil — ama taşıma gecikirse her şey geriye kayar.

---

## 6. Ölçüm

- Google Search Console: indeksleme durumu, sorgu bazlı sıralama
- Google Analytics 4: WhatsApp tıklamaları hedef olarak işaretlenmeli
- Aylık sıralama takibi: lenfödem ve lipödem kümesi anahtar kelimeleri
- Core Web Vitals: mobil hız (siteyi hafif tuttuk, avantajımız)
