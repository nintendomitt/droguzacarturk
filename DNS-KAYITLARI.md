# DNS Kayıtları — droguzacarturk.com

**Sorgulama tarihi:** 18 Ağustos 2026
**Mevcut DNS yöneticisi:** Wix (`ns14.wixdns.net`, `ns15.wixdns.net`)
**E-posta sağlayıcısı:** Google Workspace

---

## Önce durum tespiti

Domainin DNS'i şu an Wix'te yönetiliyor. Bu iyi haber: **nameserver'ları değiştirmenize gerek yok.** Sadece Wix'in DNS kayıtları ekranından A ve www kayıtlarını değiştireceksiniz. E-posta kayıtlarına hiç dokunmayacağız — bu, riski büyük ölçüde azaltıyor.

> Wix'te DNS kayıtlarını düzenleyebilmek için önce domaini Wix sitesinden **bağlantısını kesmeniz** gerekebilir. Wix, siteye bağlı domainlerde A kayıtlarını kilitler. Panelde "Alan adını siteden kaldır" veya benzeri bir seçenek arayın; domain hesabınızda kalır, sadece Wix sitesiyle bağı kopar.

---

## 1. SİLİNECEK kayıtlar

Bunlar Wix sunucularını gösteriyor, artık gerekmiyor:

| Tip | Ad | Mevcut değer |
|---|---|---|
| A | @ | `185.230.63.186` |
| A | @ | `185.230.63.107` |
| A | @ | `185.230.63.171` |
| A veya CNAME | www | `34.149.87.45` (Wix) |

---

## 2. EKLENECEK kayıtlar

### Çıplak domain — 4 adet A kaydı

| Tip | Ad | Değer | TTL |
|---|---|---|---|
| A | @ | `185.199.108.153` | 3600 |
| A | @ | `185.199.109.153` | 3600 |
| A | @ | `185.199.110.153` | 3600 |
| A | @ | `185.199.111.153` | 3600 |

### www — 1 adet CNAME kaydı

| Tip | Ad | Değer | TTL |
|---|---|---|---|
| CNAME | www | `nintendomitt.github.io` | 3600 |

> **Dikkat:** CNAME değerinin sonunda repo adı **yok**. Sadece `nintendomitt.github.io`.
> Bazı paneller sonuna nokta ister: `nintendomitt.github.io.` — panel nasıl istiyorsa öyle girin.

### İsteğe bağlı — IPv6 (AAAA)

Zorunlu değil, ama eklemek isterseniz:

```
AAAA  @  2606:50c0:8000::153
AAAA  @  2606:50c0:8001::153
AAAA  @  2606:50c0:8002::153
AAAA  @  2606:50c0:8003::153
```

---

## 3. DOKUNULMAYACAK kayıtlar

Bunlara **kesinlikle dokunmayın.** Silinirse e-posta çalışmaz.

### MX — Google Workspace e-postası

| Tip | Ad | Öncelik | Değer |
|---|---|---|---|
| MX | @ | 10 | `aspmx.l.google.com` |
| MX | @ | 20 | `alt1.aspmx.l.google.com` |
| MX | @ | 30 | `alt2.aspmx.l.google.com` |
| MX | @ | 40 | `alt3.aspmx.l.google.com` |
| MX | @ | 50 | `alt4.aspmx.l.google.com` |

### TXT — SPF ve Google doğrulaması

| Tip | Ad | Değer |
|---|---|---|
| TXT | @ | `v=spf1 include:_spf.google.com ~all` |
| TXT | @ | `google-site-verification=PtfnwOP1VtB9Gws1t7FEHon5NyChyv8imyofuJciluU` |

> SPF kaydı silinirse gönderdiğiniz e-postalar spam'e düşmeye başlar.
> Google doğrulama kaydı silinirse Search Console ve Workspace doğrulaması bozulabilir.

---

## 4. Özet: değişiklik tablosu

| Kayıt | İşlem |
|---|---|
| A @ (3 adet Wix IP) | **SİL** |
| www (Wix) | **SİL** |
| A @ (4 adet GitHub IP) | **EKLE** |
| CNAME www → nintendomitt.github.io | **EKLE** |
| MX (5 adet Google) | **DOKUNMA** |
| TXT SPF | **DOKUNMA** |
| TXT google-site-verification | **DOKUNMA** |

---

## 5. Geçiş sırası

1. **Bir gün önce:** Mümkünse A kayıtlarının TTL'ini 300 saniyeye düşürün. Bu, geçiş anında yayılmayı hızlandırır. (Wix panelinde TTL düzenlenemiyorsa bu adımı atlayın.)
2. **Geçiş anı:**
   - GitHub reposunda `CNAME.gecis-gunu-ekle` dosyasının adını `CNAME` yapın ve push edin
   - Wix'te eski A ve www kayıtlarını silin
   - Yeni A ve CNAME kayıtlarını girin
   - MX ve TXT'ye dokunmayın
3. **Bekleyin.** Genelde 1–4 saat, en fazla 24 saat.
4. **Doğrulayın** (aşağıdaki komutlarla)
5. GitHub → Settings → Pages → **Enforce HTTPS**'i işaretleyin

---

## 6. Doğrulama komutları

Terminalde çalıştırıp sonucu kontrol edebilirsiniz:

```bash
# A kayitlari GitHub IP'lerini gostermeli
dig +short A droguzacarturk.com

# www GitHub'a isaret etmeli
dig +short CNAME www.droguzacarturk.com

# MX hala Google olmali — EN ONEMLI KONTROL
dig +short MX droguzacarturk.com

# SPF yerinde mi
dig +short TXT droguzacarturk.com
```

Beklenen sonuçlar:

| Komut | Beklenen |
|---|---|
| `A droguzacarturk.com` | 185.199.108–111.153 |
| `CNAME www` | nintendomitt.github.io |
| `MX` | aspmx.l.google.com ve alt1–4 |
| `TXT` | v=spf1 ... ve google-site-verification=... |

**En kritik test:** DNS yayıldıktan sonra `info@droguzacarturk.com` adresine dışarıdan bir test e-postası gönderin ve ulaştığını doğrulayın.

---

## 7. Wix'e özel notlar (resmî dokümandan doğrulandı)

Domain Wix'ten alınmış. Yaptığımız işin Wix'teki adı **"pointing"** — yani domaini Wix'te bırakıp dışarıdaki bir siteye yönlendirmek. Wix bunu resmen destekliyor ve adım adım anlatıyor.

### Desteklenen ✓

- A kayıtlarını silip yenilerini ekleyebilirsiniz
- www için CNAME ekleyebilirsiniz — Wix dokümanı bunu açıkça yazıyor: *"For your main www address, enter www as the host name if instructed by your host."*
- MX ve TXT kayıtları etkilenmez

### Desteklenmeyen ✗

- **Nameserver değiştirilemez.** Wix domainlerinde NS kaydı düzenlenemiyor. Bizim planımız NS değişikliği gerektirmediği için sorun değil — ama ileride Cloudflare gibi bir DNS sağlayıcısına geçmek isterseniz, domaini Wix'ten **taşımanız** gerekir.

### Sıra önemli: önce siteden ayırın

Wix'te `www` host adı, siteye bağlı domainlerde **rezerve**. Domain hâlâ Wix sitesine bağlıyken www CNAME eklemeye çalışırsanız *"Hostname already in use"* hatası alırsınız.

Bu yüzden sıra şu olmalı:

1. Domaini Wix **sitesinden ayırın** (domain hesabınızda kalır, sadece siteyle bağı kopar)
2. Sonra DNS kayıtlarını düzenleyin

### Abonelikler: ikisi ayrı

Wix'te iki ayrı abonelik var ve karıştırılmamalı:

| Abonelik | Ne işe yarar | Ne yapmalı |
|---|---|---|
| **Domain kaydı** (yıllık) | Domainin sahipliği + DNS yönetimi | **Devam etmeli.** Yenilemezseniz domaini kaybedersiniz. |
| **Premium site planı** | Wix sitesinin yayınlanması | İptal edilebilir — site artık GitHub'dan yayınlanacak |

Site planını iptal etseniz bile, domain aboneliği aktif olduğu sürece DNS kayıtlarını yönetmeye devam edebilirsiniz.

> **Tavsiyem:** Site planını geçişle aynı gün iptal etmeyin. Önce yeni site oturusun, e-posta ve tüm sayfalar doğrulansın; birkaç hafta sonra iptali ayrı bir iş olarak yapın. İki riskli işi aynı anda yapmayalım.

### Yayılma süresi

Wix, DNS değişikliklerinin **48 saate kadar** sürebileceğini belirtiyor. Genelde çok daha hızlı olur (1–4 saat), ama bu süre boyunca bazı ziyaretçiler eski siteyi görmeye devam edebilir. Bu normaldir; panik yapıp kayıtları geri almayın.
