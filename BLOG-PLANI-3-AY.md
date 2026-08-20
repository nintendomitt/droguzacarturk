# 3 Aylık Blog İçerik Planı

**Hedef:** Lenfödem, fil hastalığı ve ilgili aramalarda ilk sıralar
**Hazırlık:** 20 Ağustos 2026
**Veri:** Semrush TR

---

## Önce iki tespit

### 1. "Fil hastalığı" beklediğimizden çok daha büyük

Bunu ayrı bir başlık olarak düşünmemiştik ama veriler net:

| Anahtar kelime | Aylık | Zorluk |
|---|---|---|
| fil hastalığı | **14.800** | 25 |
| fil hastalığı nedir | **5.400** | 26 |
| fil hastalığı neden olur | 1.900 | 21 |
| fil ayağı hastalığı | 1.300 | 20 |
| fil hastalığı belirtileri | 1.300 | 20 |
| fil hastalığı görüntüleri | 1.000 | 25 |
| fil hastalığı tedavisi | 1.000 | 24 |
| fil hastalığı nasıl geçer | 480 | 21 |
| fil hastalığı hangi bölüm bakar | 320 | **12** |
| fil hastalığı bulaşıcı mıdır | 260 | 21 |
| fil hastalığı nasıl bulaşır | 110 | 18 |
| fil hastalığına iyi gelen bitkiler | 110 | **12** |
| fil hastalığı genetik mi | 90 | **11** |

**Küme toplamı: ~30.000 arama/ay.** Lenfödem kümesinin (~25.000) üzerinde.

Ve bu tamamen hocanın alanı: fil hastalığı = elefantiyazis = **ileri evre lenfödem**. Yani zaten yaptığı işin halk arasındaki adı.

**Kritik fırsat:** Bu aramaları yapanların önemli bir kısmı hastalığın bulaşıcı olduğunu sanıyor ("bulaşıcı mıdır", "nasıl bulaşır", "sivrisinek"). Bu, tropik bölgelerdeki parazit hastalığı filariazis ile karışmasından geliyor — **Türkiye'de görülmez.** Türkiye'de "fil hastalığı" denen tablo neredeyse her zaman ileri evre lenfödemdir.

Bu yanlış bilgiyi düzelten bir hekim içeriği hem ciddi trafik alır hem de korkmuş bir hastaya gerçekten yardım eder.

### 2. "Lenfoma" konusunda açık konuşmam gerekiyor

Rakamlar cazip:

| Anahtar kelime | Aylık | Zorluk |
|---|---|---|
| lenfoma nedir | 27.100 | 21 |
| lenfoma belirtileri | 12.100 | 22 |
| lenfoma | 8.100 | 25 |
| lenfoma tedavisi | 1.000 | 21 |

Toplam ~48.000/ay. Ama **lenfoma, lenfatik sistemin kanseridir** ve tedavisi hematoloji-onkolojinin işidir. Oğuz Hoca lenfoma tedavi etmiyor.

"Lenfoma tedavisi" aramasında çıkan bir plastik cerrahi sitesi üç sorun yaratır:

- **Hasta zararı riski.** Lenfoma erken tanı ve kemoterapi gerektiren bir kanser. Yanlış branşa yönlenen bir hastanın kaybettiği hafta gerçek bir kayıp.
- **Regülasyon riski.** Sağlık Bakanlığı tanıtım yönetmeliği, hekimin uzmanlık alanı dışında hizmet sunuyor izlenimi vermesini yasaklıyor.
- **Google güven kaybı.** YMYL kategorisinde uzmanlık-içerik uyumsuzluğu doğrudan sıralama kaybı getiriyor. Bu, sitenin tamamını riske atar.

**Ama bu trafiği dürüstçe alabileceğimiz iki yol var:**

**a) Ayrım içeriği.** "Lenfödem mi lenfoma mı?" — iki kelimeyi karıştıran çok sayıda insan var. Farkı net anlatan, lenfoma şüphesi olanı doğru branşa yönlendiren bir yazı hem meşru hem değerli. Bu sayfa lenfoma hastasını tutmaya değil, doğru yere göndermeye çalışır — ve tam da bu yüzden Google'ın ödüllendirdiği içerik tipidir.

**b) Lenfoma sonrası lenfödem.** Bu gerçek ve doğrudan hocanın alanı. Lenfoma tedavisinde uygulanan lenf nodu diseksiyonu ve radyoterapi, sekonder lenfödemin bilinen nedenlerinden. Bu hastalar onkolojik tedavileri bittikten sonra gerçekten Oğuz Hoca'ya ihtiyaç duyuyor.

Planda lenfoma bu iki başlıkla yer alıyor. "Lenfoma tedavisi" iddiası içeren içerik yazmıyorum.

### 3. Küçük ama değerli bir bulgu

**"lenf ödemi"** ayrı yazımı ayda **8.100** arama alıyor (zorluk 21). Bizim sayfalarımız "lenfödem" bitişik yazımını hedefliyor. Bu ayrı bir sorgu ve şu an kaçırıyoruz — blog yazılarında her iki yazımı da doğal biçimde kullanacağız.

---

## Blog altyapısı

Sitede henüz blog bölümü yok. Kurulması gerekenler:

- `/blog/` dizini ve liste sayfası
- Yazı şablonu: `Article` + `MedicalWebPage` yapısal verisi
- Yazar kutusu: Doç. Dr. Tahsin Oğuz Acartürk, unvan, kurum, yayın bağlantısı
- "Tıbbi inceleme tarihi" ve "son güncelleme" satırı
- Kategori etiketleri: Lenfödem · Lipödem · Mikrocerrahi · Hasta Rehberi
- İlgili hizmet sayfasına iç link (her yazıdan en az bir tane)
- Blog yazıları sitemap'e otomatik girecek

Bu altyapıyı mevcut üretici sisteme ekleyeceğim; yazılar da `_pages` mantığıyla tek yerden yönetilecek.

---

## AY 1 — Fil hastalığı kümesini ele geçir

En büyük hacim, en net uzmanlık eşleşmesi. Buradan başlıyoruz.

| # | Başlık | Hedef sorgu | Aylık | Zorluk |
|---|---|---|---|---|
| 1 | Fil hastalığı nedir? Türkiye'de görülen tablo hangisi? | fil hastalığı nedir | 5.400 | 26 |
| 2 | Fil hastalığı bulaşıcı mı? Sivrisinek efsanesi ve gerçek | fil hastalığı bulaşıcı mıdır / nasıl bulaşır | 370 | 18–21 |
| 3 | Fil hastalığı neden olur? Nedenler ve risk faktörleri | fil hastalığı neden olur | 1.900 | 21 |
| 4 | Fil hastalığı belirtileri: hangi aşamada hekime gitmeli? | fil hastalığı belirtileri | 1.300 | 20 |
| 5 | Fil hastalığı tedavi edilebilir mi? Cerrahi seçenekler | fil hastalığı tedavisi / nasıl geçer | 1.480 | 21–24 |
| 6 | Fil hastalığına hangi bölüm bakar? | fil hastalığı hangi bölüm bakar | 320 | **12** |
| 7 | Fil ayağı: bacakta ileri evre lenfödem | fil ayağı hastalığı / fil bacak hastalığı | 1.820 | 13–20 |
| 8 | Fil hastalığı genetik mi? Kalıtım ve aile öyküsü | fil hastalığı genetik mi | 90 | **11** |

**Ay 1 hedef hacmi: ~12.700/ay**

> **6 ve 8 numaralı yazılar öncelikli.** Zorlukları 11-12 — birkaç hafta içinde ilk sayfaya girebilirler ve erken sinyal verirler.

---

## AY 2 — Lenfoma ayrımı, karışan tablolar ve alternatif tedavi

Bu ay iki iş yapıyoruz: kafa karışıklığını gideren içerikler ve kanıtsız yöntem arayanları doğru bilgiye yönlendiren içerikler.

| # | Başlık | Hedef sorgu | Aylık | Zorluk |
|---|---|---|---|---|
| 9 | Lenfödem mi lenfoma mı? İki kelimenin karıştırdığı iki farklı hastalık | lenfoma / lenfödem ayrımı | — | — |
| 10 | Lenfoma tedavisi sonrası lenfödem: neden olur, ne yapılır? | lenfoma sonrası lenfödem | — | — |
| 11 | Lenf bezi şişliği ile lenfödem aynı şey mi? | lenf bezi şişliği | 880 | **13** |
| 12 | Ayak ve bacak şişmesi: hangi durumda ciddi? | ayak şişmesi / bacak şişmesi nedenleri | 2.070 | 20–21 |
| 13 | Zerdeçal lenfödeme iyi gelir mi? Literatür ne diyor? | zerdeçal lenfödem | 1.600 | **8** |
| 14 | Hacamat lenfödem tedavisinde işe yarar mı? | hacamat ile lenfödem tedavisi | 720 | **6** |
| 15 | Lenfödeme iyi gelen bitkiler: kanıt ne düzeyde? | lenfödeme iyi gelen bitkiler / bitkisel tedavi | 430 | 5 |
| 16 | Lenf drenajı nedir, kimlere fayda sağlar? | lenf drenajı / lenfödem masajı | — | — |

**Ay 2 hedef hacmi: ~5.700/ay**

> **13, 14, 15 numaralı yazıların tonu kritik.** "Bunlar işe yaramaz" demeyeceğiz. Yöntemin ne olduğunu, literatürün ne söylediğini ve gerçekten neyin işe yaradığını anlatacağız. Bu insanlar şu an yanlış bilgi buluyor; bir doçentin dürüst cevabı hem trafik hem güven getirir.
>
> Zorlukları 5–8. Bu, neredeyse rakipsiz bir alan.

---

## AY 3 — Hasta yolculuğu ve derinlik

İlk iki ay geniş kitleyi çekti. Bu ay dönüşüme yakın ve otorite kuran içerikler.

| # | Başlık | Hedef | Not |
|---|---|---|---|
| 17 | Lenfödem ameliyatı öncesi: hangi tetkikler, nasıl hazırlanılır? | Hasta yolculuğu | Dönüşüme yakın |
| 18 | LVA ameliyatı nasıl yapılır? Adım adım süreç | lva ameliyatı | Uzmanlık kanıtı |
| 19 | Lenfödem ameliyatı sonrası iyileşme: ilk 6 ay | Hasta yolculuğu | Beklenti yönetimi |
| 20 | Bası çorabı nasıl seçilir, nasıl kullanılır? | lenfödem çorabı (390) | Pratik değer |
| 21 | Selülit (erizipel) atağı: nasıl tanınır, ne zaman acil? | Hasta güvenliği | Yüksek değer |
| 22 | Meme kanseri sonrası kol lenfödemi: önleme mümkün mü? | LYMPHA / önleme | Onkoloji kesişimi |
| 23 | Lenfödem ve seyahat: uçuş, sıcak iklim, uzun yolculuk | Uzun kuyruk | Mevsimsel |
| 24 | Lenfödem ile yaşamak: günlük hayat rehberi | Marka değeri | Paylaşılabilir |

**Ay 3 hedef hacmi: ~1.500/ay + otorite**

---

## Yayın temposu

**Haftada 2 yazı, 12 hafta = 24 yazı.**

Bu tempo neden: Google yeni sitelerde düzenli yayını tazelik sinyali olarak okuyor. Haftada 2, sürdürülebilir ve fark edilir bir ritim. Ayda 8 yazı biriktirip tek seferde yayınlamak aynı etkiyi vermiyor.

| Hafta | Yazılar |
|---|---|
| 1–4 | Ay 1 yazıları (1–8) |
| 5–8 | Ay 2 yazıları (9–16) |
| 9–12 | Ay 3 yazıları (17–24) |

---

## Her yazının uyacağı standart

**Uzunluk:** 1.200–2.000 kelime. Kısa yazı bu rekabette işe yaramıyor; şişirilmiş yazı da okunmuyor.

**Yapı:**
- Sorunun cevabı ilk paragrafta (Google öne çıkan snippet için buraya bakıyor)
- H2/H3 hiyerarşisi, sorgu diliyle
- En az bir tablo veya adım listesi
- 4–6 soruluk SSS bölümü + `FAQPage` yapısal verisi
- İlgili hizmet sayfasına iç link
- Yazar kutusu ve tıbbi inceleme tarihi

**Ton:** Site genelinde kurduğumuz dilin aynısı — dürüst, abartısız, hastayı suçlamayan. Tam şifa vaadi yok. Belirsizlik varsa belirsizlik olarak yazılıyor.

**Uyulacak sınırlar:**
- Öncesi-sonrası fotoğraf yok
- Hasta yorumu yok
- Fiyat bilgisi yok
- Üstünlük ve garanti ifadesi yok
- Uzmanlık alanı dışında tedavi iması yok

---

## Ölçüm

Her ayın raporunda blog için ayrı bölüm:

| Gösterge | Takip |
|---|---|
| Yayınlanan yazı | Hedef 8/ay |
| İndekslenen yazı | GSC |
| Blog organik gösterim | GSC |
| Blog organik tıklama | GSC |
| En çok tıklanan 5 yazı | GSC |
| Blogdan hizmet sayfasına geçiş | GA4 |
| Blogdan WhatsApp tıklaması | GA4 |

---

## Toplam beklenti

| | Hedef hacim |
|---|---|
| Ay 1 (fil hastalığı) | ~12.700/ay |
| Ay 2 (ayrım + alternatif) | ~5.700/ay |
| Ay 3 (hasta yolculuğu) | ~1.500/ay |
| **Toplam** | **~19.900/ay** |

Bu, mevcut 12 uydu sayfanın hedeflediği ~61.000'in üzerine ekleniyor. Üç ay sonunda site, lenfödem–lipödem–fil hastalığı üçgeninde ayda 80.000 aramalık bir alanı hedefliyor olacak.

Gerçekçi olalım: bu hacmin tamamı gelmez. Ama zorluk skorları 5–26 aralığında ve rakipler bu içeriği yazmıyor. Bu üç ayın sonunda "fil hastalığı" aramasında ilk sayfada olmamak için teknik bir sebep göremiyorum.
