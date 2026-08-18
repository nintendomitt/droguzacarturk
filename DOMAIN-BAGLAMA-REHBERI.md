# Domain Bağlama Rehberi — droguzacarturk.com

**Hazırlık tarihi:** 18 Ağustos 2026
**Durum:** Site hazır, CNAME ve yönlendirmeler repoda. Sıra DNS'te.

---

## ÖNEMLİ: Önce bunu okuyun

Bu geçişte kritik bir teknik gerçek var ve planı buna göre kurmak zorundayız:

> **DNS'i GitHub'a çevirdiğiniz anda Wix sitesi tamamen erişilemez olur.**

Yani "Wix'te 301 yönlendirmesi kuralım" seçeneği masada değil. Wix artık hiçbir şey servis etmiyor olacak. Bu yüzden eski URL'lerin yönlendirmesini **yeni sitenin içinde** çözdüm — repoda 11 adet yönlendirme sayfası hazır durumda.

Bunun anlamı: geçiş tek seferde ve geri dönüşsüz. Aşağıdaki sırayı takip etmek bu yüzden önemli.

---

## 1. Geçiş öncesi kontrol listesi

Bunlar DNS'e dokunmadan **önce** tamamlanmalı:

- [ ] **Wix sitesinin tam yedeği** — ekran görüntüleri, metinler, fotoğraflar. Geri dönüş ihtimali için değil, arşiv için.
- [ ] **Domain nerede kayıtlı?** Wix üzerinden mi alındı, yoksa başka bir kayıt firmasında mı? Bu, DNS'i nereden değiştireceğinizi belirler.
- [ ] **E-posta kontrolü.** `info@droguzacarturk.com` adresi çalışıyor. Eğer bu e-posta Wix üzerinden veriliyorsa, DNS değişince **e-posta da kesilir**. MX kayıtlarını mutlaka not alın ve yeni DNS'e aynen taşıyın. Bu, geçişlerde en sık yapılan ve en pahalıya mal olan hatadır.
- [ ] **Google Search Console erişimi** — eski site için doğrulanmış bir hesap var mı? (Wix sayfalarında `google-site-verification` etiketi görünüyor, yani birileri doğrulamış.) Bu hesaba erişim şart.
- [ ] **Google Analytics** varsa erişim bilgileri.

---

## 2. DNS kayıtları

Kanonik adresimiz **www.droguzacarturk.com**. Yani www ana adres, çıplak domain ona yönlenecek.

### Çıplak domain (droguzacarturk.com) — 4 adet A kaydı

| Tip | Ad | Değer |
|---|---|---|
| A | @ | 185.199.108.153 |
| A | @ | 185.199.109.153 |
| A | @ | 185.199.110.153 |
| A | @ | 185.199.111.153 |

İsteğe bağlı olarak IPv6 (AAAA) kayıtları da eklenebilir:
`2606:50c0:8000::153`, `2606:50c0:8001::153`, `2606:50c0:8002::153`, `2606:50c0:8003::153`

### www alt alan adı — 1 adet CNAME kaydı

| Tip | Ad | Değer |
|---|---|---|
| CNAME | www | nintendomitt.github.io |

> Dikkat: CNAME değerinin sonunda repo adı **yok**. Sadece `nintendomitt.github.io`.

### Korunacak kayıtlar

- **MX kayıtları** — e-posta için. Aynen taşıyın.
- **TXT kayıtları** — Google doğrulaması, SPF/DKIM varsa. Aynen taşıyın.

---

## 3. GitHub tarafı

> **Önemli — CNAME dosyası geçiş gününe kadar bekliyor.**
> Dosyayı önce ekledim, sonra geri aldım. Sebebi: repoda `CNAME` dosyası bulunduğu anda GitHub Pages, `nintendomitt.github.io/droguzacarturk` adresini `www.droguzacarturk.com`'a **301 ile yönlendirmeye başlıyor.** DNS henüz taşınmadığı için bu adres Wix'e düşüyor ve test/önizleme adresi kırılıyor.
> Dosya şu an repoda `CNAME.gecis-gunu-ekle` adıyla duruyor. **Geçiş günü** adını `CNAME` yapıp push etmeniz yeterli.

Geçiş günü sırası:

1. `CNAME.gecis-gunu-ekle` → `CNAME` olarak yeniden adlandırın ve push edin
2. DNS yayıldıktan sonra:

- [ ] GitHub → repo → **Settings → Pages**
- [ ] Custom domain alanında `www.droguzacarturk.com` görünmeli
- [ ] Yeşil onay işareti bekleyin (DNS kontrolü)
- [ ] **Enforce HTTPS** kutusunu işaretleyin

> HTTPS sertifikası DNS doğrulandıktan sonra otomatik üretilir. Bu birkaç dakika ile birkaç saat arası sürebilir. O süre boyunca sertifika hatası görmek normaldir — panik yapmayın, sadece bekleyin.

---

## 4. Eski URL yönlendirmeleri (hazır)

Wix sitemap'inden 12 URL çıkardım ve her birinin gerçek içeriğini kontrol ettim. Wix slug'ları yanıltıcıydı — örneğin `/meme` aslında **İletişim** sayfası, `/copy-of-lenfödem` ise **Mikrotia** sayfası.

Yönlendirme haritası:

| Eski adres | Gerçek içeriği | Yeni hedef |
|---|---|---|
| `/` | Anasayfa | `/` |
| `/lenfodem` | Lenfödem | `/lenfodem-lipodem-cerrahisi.html` |
| `/copy-of-lenfödem` | **Mikrotia** | `/mikrotia-kulak-onarimi.html` |
| `/cerrahiniz-dr-oguz` | Cerrahınız | `/#hakkinda` |
| `/meme` | **İletişim** | `/#iletisim` |
| `/meme-buyutme` | Meme büyütme | `/meme-estetigi.html` |
| `/goez-kapagi` | Göz kapağı | `/goz-kapagi-estetigi.html` |
| `/burun` | Burun | `/burun-estetigi-rinoplasti.html` |
| `/yuz` | Yüz germe | `/yuz-germe.html` |
| `/vucut` | Vücut | `/liposuction-vucut-sekillendirme.html` |
| `/karin-germe-abdominoplasti` | Karın germe | `/karin-germe.html` |
| `/onarim-cerrahisi` | Onarım cerrahisi | `/#onarim` |

Bu sayfaların her biri `noindex` etiketli, canonical'ı hedefe bakıyor ve hem meta-refresh hem JavaScript ile anında yönlendiriyor. GitHub Pages sunucu tarafı 301 veremediği için standart çözüm budur; Google bu yapıyı yönlendirme olarak değerlendirir.

**Yönlendirmeler en az 12 ay kalmalı.** Silmek için acele etmeyin.

### `/meme-buyutme` hakkında bir düzeltme

Daha önce bu sayfayı anasayfaya yönlendirmenizi önermiştim, çünkü pornografik bir aramada 4. sırada çıkıyor. Yeniden düşününce görüşümü değiştiriyorum: aynı sayfa "meme büyümesi" (aylık 590) gibi meşru aramalarda da sıralanıyor. Tek kötü sorgu için meşru değeri çöpe atmak fazla sert bir tepki.

Yönlendirmeyi `/meme-estetigi.html`'e kurdum. Yeni sayfa açıkça tıbbi içerikte ve Google birkaç tarama içinde eşleşmeyi yeniden değerlendirecek. Yine de GSC'de "Performans → Sorgular" bölümünden bu sorguyu birkaç ay takip edelim; devam ederse o zaman sayfayı ayrıştırırız.

---

## 5. Geçiş günü sırası

1. **DNS kayıtlarını girin** (A + CNAME + MX/TXT koruma)
2. **Bekleyin.** Yayılma genelde 1–4 saat, bazen 24 saati bulur.
3. `www.droguzacarturk.com` açılınca GitHub Pages ayarlarından **Enforce HTTPS**'i işaretleyin
4. **Test edin:**
   - `droguzacarturk.com` → www'ye yönleniyor mu?
   - `https://www.droguzacarturk.com/lenfodem` → yeni lenfödem sayfasına gidiyor mu?
   - `https://www.droguzacarturk.com/lipodem-nedir.html` → açılıyor mu?
   - E-posta çalışıyor mu? **Kendinize test maili atın.**
5. **Google Search Console:**
   - `www.droguzacarturk.com` için yeni mülk oluşturun (Domain mülkü tercih edilir)
   - `sitemap.xml` gönderin
   - "URL Denetimi" ile anasayfa ve lenfödem sayfası için **indeksleme isteyin**
6. **Bing Webmaster Tools**'a da ekleyin — Türkiye'de payı küçük ama ChatGPT aramaları Bing indeksini kullanıyor

---

## 6. Geçiş sonrası ilk hafta — neyi izlemeli

| Ne | Nerede | Beklenen |
|---|---|---|
| İndeksleme | GSC → Sayfalar | Sayfa sayısı günden güne artmalı |
| Tarama hataları | GSC → Sayfalar → Neden dizine eklenmedi | 404 birikmesi olmamalı |
| Marka aramaları | GSC → Performans | "tahsin oğuz acartürk" sıralaması korunmalı |
| HTTPS | Tarayıcı | Kilit simgesi, uyarı yok |
| E-posta | Test maili | Gidip geliyor |

> Geçişten sonraki ilk 2–4 haftada sıralamalarda dalgalanma normaldir. Google yeni yapıyı yeniden değerlendiriyor. Panik yapıp değişiklik yapmayın — bu dönemde sabit durmak en doğrusu.

---

## 7. Bilmeniz gereken riskler

**E-posta kesintisi.** En yüksek risk bu. MX kayıtları taşınmazsa `info@droguzacarturk.com` çalışmaz ve hasta iletileri kaybolur. DNS'e dokunmadan önce mevcut MX kayıtlarının ekran görüntüsünü alın.

**Geri dönüş yok.** Wix DNS'ten çıktığı anda eski site erişilemez. Bu yüzden yedek şart.

**İlk dönem dalgalanma.** Marka aramalarında geçici düşüş görebilirsiniz. Yönlendirmeler doğru kurulduğu için bu telafi edilir, ama 2–4 hafta sabır gerekiyor.

**Sertifika gecikmesi.** HTTPS birkaç saat gecikebilir. Bu sürede site "güvenli değil" uyarısı verebilir — geçicidir.
