# Doç. Dr. Tahsin Oğuz Acartürk — Yeni Website

Kurulum, mevzuat ve SEO yol haritası. Ağustos 2026.

---

## 1. Dosyalar

| Dosya | Ne işe yarar |
|---|---|
| `index.html` | Ana sayfa. TR / EN / DE / RU dil değiştirici, tam JSON-LD, WhatsApp + telefon dönüşüm akışı. Kendi kendine yeten — harici dosya bağımlılığı yok (yalnızca Google Fonts). |
| `lenfodem-lipodem-cerrahisi.html` | Derin SEO açılış sayfası. Evreleme, tanı, LVA / VLNT / azaltıcı cerrahi, lipödem, iyileşme süreci, 8 soruluk SSS. |
| `sitemap.xml` | Arama motorları için site haritası + hreflang eşlemesi. Sonraki sayfalar yorum satırı olarak hazır. |
| `robots.txt` | Tarama kuralları. UTM/fbclid parametreli URL'leri engeller, AI arama botlarına açık erişim verir. |

### Görseller — hazır olanlar

`assets/` klasöründe şunlar hazır ve siteye bağlı:

| Dosya | Kullanım |
|---|---|
| `dr-acarturk.jpg` (1200×1500) | Anasayfa portresi |
| `dr-acarturk@2x.jpg` (1800×2250) | Retina ekranlar için |
| `dr-acarturk.webp` | Modern tarayıcılar için, %60 daha küçük |
| `og-image.jpg` · `og-lenfodem.jpg` (1200×630) | WhatsApp / Instagram / Facebook paylaşım görseli |
| `logos/abps-logo.png` + `.webp` | American Board of Plastic Surgery resmî logosu |

Portre 4:5 oranına kırpıldı, üç boyutta üretildi ve `<picture>` etiketiyle bağlandı — tarayıcı hangisini indireceğine kendisi karar veriyor.

**Hâlâ eklemeniz gereken:** `favicon.ico` ve `apple-touch-icon.png`.

### American Board logosu

Gönderdiğiniz resmî ABPS logosu işlendi ve siteye yerleştirildi: beyaz arka plan şeffaflaştırıldı, kenar boşlukları kırpıldı, PNG ve WebP olmak üzere iki formatta kaydedildi. Anasayfada sertifika bölümünün solunda büyük boyutta duruyor.

Tasarım aşamasında yaptığım geçici mühür (`abps-seal.svg`) klasörde duruyor ama artık kullanılmıyor; silebilirsiniz.

> **Not:** ABPS logosu tescilli markadır ve kullanımı ABPS'nin marka kurallarına tabidir. Sertifikalı hekimler logoyu kullanabilir, ancak ABPS logonun etrafında belirli bir boşluk bırakılmasını, renginin değiştirilmemesini ve oranının bozulmamasını şart koşar. Siteye bu kurallara uygun şekilde yerleştirildi — orijinal renkler ve oran korundu, çevresinde yeterli boşluk var. Kaynak dosya elinizde daha yüksek çözünürlükte varsa (270×224'ten büyük), `assets/logos/abps-logo.png` üzerine yazmanız yeterli.

### Üniversite logoları

`assets/logos/` klasörüne şu dosyaları ekleyin (SVG tercih edilir, şeffaf PNG de olur):

`hacettepe.svg` · `pittsburgh.svg` · `carnegie-mellon.svg` · `helsinki.svg` · `cukurova.svg` · `gata.svg` · `mersin.svg`

Logo dosyası **yokken** kutular kurum adını serif tipografiyle, altın çizgili tasarımlı bir kart olarak gösteriyor — yani site şu an da eksik görünmüyor, bilinçli bir "akademik künye" şeridi gibi duruyor. Dosyayı ekler eklemez logo otomatik devreye girer, metin gizlenir. Kodda hiçbir değişiklik gerekmez.

Logoları resmî basın/kurumsal kimlik sayfalarından indirin (çoğu üniversitenin "Brand" veya "Kurumsal Kimlik" sayfası vardır).

> **Telif notu:** Üniversite logoları tescilli markadır. Çoğu üniversite "mezunumuz / öğretim üyemiz" bağlamında kullanıma izin verir, ancak bazılarının yazılı izin şartı vardır. Logoyu koymadan önce ilgili kurumun marka kullanım koşullarını kontrol edin. İzin alınamayan kurumlar için mevcut tipografik kart zaten yeterli ve tamamen güvenlidir.

---

## 2. Yayına alma

### Seçenek A — Netlify (önerilen, ücretsiz katman yeterli)

1. netlify.com → **Add new site → Deploy manually** → klasörü sürükleyip bırakın.
2. **Domain settings** → `droguzacarturk.com` ekleyin, DNS kayıtlarını Netlify'ın verdiği değerlerle güncelleyin.
3. HTTPS otomatik gelir. İletişim formu `data-netlify="true"` ile hazır — form gönderileri **Forms** sekmesinde birikir, e-posta bildirimi açabilirsiniz.

### Seçenek B — Mevcut hosting / cPanel

Dosyaları `public_html` içine yükleyin. Bu durumda form için ayrı bir servis gerekir (Formspree, Web3Forms) — `<form>` etiketindeki `action` alanını o servisin URL'i ile değiştirin.

### Wix'ten geçiş — kritik adım

Eski site Wix üzerinde. Eski URL'lerin arama motorlarındaki değeri kaybolmasın diye **301 yönlendirme** kurun. Netlify'da klasöre bir `_redirects` dosyası ekleyin:

```
/cerrahiniz-dr-oguz    /            301
/lenfodem              /lenfodem-lipodem-cerrahisi   301
/yuz                   /            301
/goez-kapagi           /            301
/meme-buyutme          /            301
/meme                  /#iletisim   301
```

> İleride ayrı hizmet sayfaları açtıkça bu yönlendirmeleri o sayfalara güncelleyin.

---

## 3. Mevzuat uyarısı — önemli

Türkiye'de sağlık hizmetlerinde tanıtım, T.C. Sağlık Bakanlığı'nın *Sağlık Hizmetlerinde Tanıtım ve Bilgilendirme Faaliyetleri Hakkında Yönetmelik* hükümlerine tabidir. Site buna göre kurgulandı:

**Bilerek yapılmadı:**

- Öncesi/sonrası hasta fotoğrafı yok
- Hasta yorumu / referans / puanlama yok
- Fiyat, kampanya, indirim, taksit ifadesi yok
- "En iyi", "Türkiye'nin bir numarası", "garantili sonuç" gibi üstünlük ve garanti iddiaları yok
- Karşılaştırmalı ("X hekiminden daha iyi") ifade yok

**Yapıldı:**

- Her sayfanın altında bilgilendirme + sorumluluk reddi metni
- "Sonuçlar kişiden kişiye değişir" ve "muayene yerine geçmez" vurgusu
- Doğrulanabilir akademik kimlik bilgileri (üniversite, board sertifikası, yayın sayısı)

> Reklam ajansı veya sosyal medya yöneticisi bu siteye yeni içerik eklerken bu çerçeveyi bozmamalı. Öncesi/sonrası görsel eklemek istiyorsanız, mevzuat gereği şifreli/kapalı hasta alanına taşınması gerekir.

### Hasta deneyimleri bölümü — dikkat

Talebiniz üzerine iki katman birden kuruldu:

**1. "Doğrulanabilir Kimlik" bölümü (mevzuata uygun, şu an aktif)**
Hasta beyanı içermez. Yayın sayısı, sunum sayısı, Pittsburgh direktörlük görevi ve meslektaş yönlendirmesi üzerinden güven kurar. Yanına Pittsburgh Üniversitesi profili, LinkedIn ve PubMed'e doğrulama linkleri eklendi — ziyaretçi iddiaları kendisi teyit edebiliyor. Sağlık aramalarında en çok işe yarayan güven sinyali budur; Google'ın E-E-A-T değerlendirmesi de tam olarak buna bakar.

**2. "Hasta Deneyimleri" bölümü (yapı hazır, kartlar boş)**
Kartlar şu an yer tutucu metinle duruyor; tasarımı görebilesiniz diye. **Metinleri doldurmadan yayına almayın.**

Yönetmelik, sağlık hizmeti tanıtımında hasta beyanlarına ve tedavi deneyimi aktarımlarına yer verilmesini sınırlandırıyor ve ihlalde idari para cezası uygulanabiliyor. Bu bölümü doldurmadan önce bir sağlık hukuku danışmanına teyit ettirin.

**Daha düşük riskli yol:** Yorumları sitede barındırmak yerine Google İşletme Profili'ne yönlendirin. Bölümün altındaki buton bunun için hazır — kartları silip yalnızca butonu bırakmanız yeterli. Yorumlar üçüncü taraf platformda kalır, sorumluluk sizde olmaz, üstelik Google İşletme puanı yerel SEO'yu da doğrudan besler.

Bölümü tamamen kaldırmak isterseniz `index.html` içinde `<section class="revs-sec" id="deneyimler">` ile kapanış `</section>` arasını silin. Kodun hemen üstünde bu talimat yorum olarak da duruyor.

---

## 4. Hemen yapılacaklar (yayın günü)

- [ ] Google Search Console'a her iki sayfayı ekleyin, `sitemap.xml` gönderin
- [ ] **Google Business Profile** kaydını açın/güncelleyin — İzmir Bayraklı adresi, kategori: *Plastik cerrah*. Yerel aramada en yüksek getirili tek adım budur.
- [ ] Facebook sayfası bağlantısını düzeltin — eski sitede `facebook.com/wix` adresine gidiyor (bozuk bağlantı, güven kaybı)
- [ ] GA4 + Google Tag Manager kurun; **dönüşüm olayları:** `whatsapp_click`, `phone_click`, `form_submit`
- [ ] Instagram bio'daki linki yeni siteye çevirin
- [ ] KVKK Aydınlatma Metni ve Gizlilik Politikası sayfalarını yazdırıp footer'daki `href="#"` bağlantılarına bağlayın

---

## 5. SEO anahtar kelime haritası

Odak: **dengeli** — hem rekonstrüktif/mikrocerrahi hem estetik.

### Katman 1 — Rekabeti düşük, niyeti yüksek (öncelik)

Burada ciddi bir boşluk var: bu kelimelerde ulusal ölçekte güçlü içerik az, doktorun otoritesi ise çok yüksek.

| Anahtar kelime | Hedef sayfa |
|---|---|
| lenfödem ameliyatı | `lenfodem-lipodem-cerrahisi` ✅ |
| lenfödem tedavisi | `lenfodem-lipodem-cerrahisi` ✅ |
| lipödem ameliyatı / lipödem cerrahisi | `lenfodem-lipodem-cerrahisi` ✅ |
| LVA ameliyatı / lenfatikovenöz anastomoz | `lenfodem-lipodem-cerrahisi` ✅ |
| lenf nodu transferi | `lenfodem-lipodem-cerrahisi` ✅ |
| meme kanseri sonrası kol şişmesi | yeni sayfa önerisi |
| lipödem mi lenfödem mi | `lenfodem-lipodem-cerrahisi` ✅ (tablo bölümü) |
| mikrotia ameliyatı / doğuştan kulak yokluğu | yeni sayfa önerisi |
| yüz felci ameliyatı | yeni sayfa önerisi |

### Katman 2 — Yerel + estetik (orta rekabet)

`izmir plastik cerrah`, `izmir estetik cerrah`, `bayraklı estetik cerrahi`, `izmir burun estetiği`, `izmir meme büyütme`, `marmaris plastik cerrah`, `muğla estetik cerrahi`

### Katman 3 — Ulusal estetik (yüksek rekabet, uzun vade)

`burun estetiği`, `meme büyütme`, `yüz germe`, `göz kapağı estetiği`, `karın germe`, `liposuction`

### Katman 4 — Uluslararası / sağlık turizmi

`lymphedema surgery Turkey`, `LVA surgery Turkey`, `lipedema surgery Turkey`, `american board certified plastic surgeon Turkey`, `Lipödem OP Türkei`, `Lymphödem Operation Türkei`, `липедема операция Турция`

---

## 6. Sonraki 6 sayfa (yazım sırası)

Her biri `lenfodem-lipodem-cerrahisi.html` şablonunu kopyalayarak üretilebilir — yapı, schema ve stiller hazır.

1. **`/meme-kanseri-sonrasi-kol-lenfodemi`** — çok net hasta niyeti, düşük rekabet, doktorun tam uzmanlık alanı
2. **`/mikrotia-kulak-onarimi`** — Türkiye'de bu konuda yazılmış nitelikli içerik neredeyse yok; Vietnam misyonları güçlü hikâye
3. **`/burun-estetigi-rinoplasti`** — hacimli; "Pittsburgh'da meslektaşlarım rinoplasti hastalarını bana yönlendirdi" anlatısı güçlü farklılaştırıcı
4. **`/meme-estetigi`** — büyütme/küçültme/dikleştirme tek sayfada, "daha az iz bırakan teknik" vurgusuyla
5. **`/cerrahiniz-dr-oguz-acarturk`** — tam özgeçmiş, yayın listesi, ödüller. **E-E-A-T için kritik**; Google'ın sağlık içeriğinde en çok baktığı sinyal.
6. **`/en/`** — İngilizce tam sürüm (sağlık turizmi). Ardından `/de/` ve `/ru/`.

> Şu an dil değiştirici tek sayfa içinde JS ile çalışıyor — hızlı ve kullanıcı için iyi. Ancak arama motorları için **her dilin ayrı URL'e** taşınması gerekir (`/en/index.html` vb.). Trafik gelmeye başlayınca bu ayrıştırmayı yapın; `hreflang` etiketleri buna hazır durumda.

---

## 7. Dönüşüm — neyi neden yaptık

| Karar | Gerekçe |
|---|---|
| WhatsApp birincil CTA | Türkiye'de sağlık aramalarında form doldurmaya kıyasla belirgin şekilde düşük sürtünme. Sticky mobil bar + yüzen buton + her bölümde tekrar. |
| Ön yazılı WhatsApp mesajı | Lenfödem CTA'sı hazır metinle açılıyor — hasta ne yazacağını düşünmüyor, tereddüt aşaması ortadan kalkıyor. |
| Kimlik bilgileri hero'nun hemen altında | Sağlık kararlarında ilk engel güven. Board sertifikası, Pittsburgh, yayın sayısı ekranın üst yarısında. |
| Sayısal kanıt bandı | "300+ vaka", "%3 doku kaybı", "60+ yayın" — soyut övgü yerine doğrulanabilir veri. |
| Lenfödem/lipödem ayrım tablosu | Hasta zaten bu soruyu Google'a soruyor. Cevabı sayfada vermek hem SEO hem güven kazandırıyor. |
| Tek dokunuşta telefon | `tel:` bağlantısı her bölümde; mobilde sticky bar. |
| Süreç bölümü | Belirsizlik, ameliyat kararında en büyük frendir. 4 adımı önceden göstermek bu freni gevşetir. |

---

## 8. Ölçüm — 90 gün

**Birincil metrikler**

- WhatsApp tıklama oranı (hedef: ziyaretçilerin %4–7'si)
- Telefon tıklama oranı (mobilde hedef: %3–5)
- Form gönderimi (hedef: %1–2)

**İkincil**

- Lenfödem sayfası ortalama okuma süresi (hedef: 3 dakika üzeri)
- Organik giriş sayısı — kelime bazında Search Console
- Google Business Profile'da "yol tarifi" ve "arama" aksiyonları

**Erken A/B testi fikri:** Hero başlığında iki yaklaşımı karşılaştırın — mevcut otorite odaklı ("Zor vakaların cerrahı") ile sonuç odaklı bir alternatif ("Lenfödemde erken cerrahi fark yaratır"). Trafik yeterli hacme ulaştığında anlamlı olur.

---

## 9. Sitede bilerek yapılan teknik tercihler

- **Sıfır JS çerçevesi, sıfır harici kütüphane.** Sayfalar tek dosya; ilk boyama çok hızlı. Core Web Vitals için en güvenli zemin.
- **CSS satır içi.** Ek istek yok, render engelleyici dosya yok.
- **Google Fonts `preconnect` ile.** Tek harici bağımlılık; hızı önemsiyorsanız fontları yerelleştirebilirsiniz.
- **`prefers-reduced-motion` uyumlu** — animasyon minimumda tutuldu.
- **Erişilebilirlik:** `skip link`, `aria-expanded` mobil menüde, semantik başlık hiyerarşisi, form etiketleri, odak stilleri korunmuş.
- **`localStorage` ile dil hafızası** ve tarayıcı diline göre otomatik seçim.
