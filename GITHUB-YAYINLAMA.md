# Yayınlama — son adım

Repo açıldı ve GitHub Pages ayarlandı. Geriye yalnızca dosyaları göndermek kaldı.

| | |
|---|---|
| **Repo** | https://github.com/nintendomitt/droguzacarturk |
| **Yayın adresi** | https://nintendomitt.github.io/droguzacarturk/ |
| **Pages kaynağı** | `main` dalı, kök dizin — ayarlandı |
| **HTTPS** | Zorunlu, açık |

Şu an repoda yalnızca `.nojekyll`, `.gitignore`, `robots.txt` ve `sitemap.xml` var. Sayfalar ve görseller gidince site canlanacak.

---

## Yöntem 1 — Sürükle bırak (terminal yok, ~30 saniye)

1. Şu adresi açın: **https://github.com/nintendomitt/droguzacarturk/upload/main**
2. Bu klasördeki şu dosyaları tarayıcı penceresine sürükleyin:
   - `index.html`
   - `lenfodem-lipodem-cerrahisi.html`
   - `404.html`
   - `README.md`
   - `KURULUM-VE-SEO-YOL-HARITASI.md`
   - `assets` klasörünün tamamı
3. Altta **Commit changes** düğmesine basın.

> `assets` klasörünü olduğu gibi sürükleyin — GitHub klasör yapısını korur. Nokta ile başlayan gizli dosyaları sürüklemeyin, onlar zaten yüklendi.

## Yöntem 2 — Terminal

Bu klasörde:

```bash
git init -b main
git remote add origin https://github.com/nintendomitt/droguzacarturk.git
git fetch origin
git reset --soft origin/main
git add .
git commit -m "Website: sayfalar ve gorseller"
git push -u origin main
```

Şifre sorarsa GitHub şifreniz değil, bir *personal access token* girin: GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic) → Generate new token → `repo` yetkisi.

## Yöntem 3 — GitHub Desktop

File → Clone repository → `nintendomitt/droguzacarturk` → dosyaları klasöre kopyalayın → Commit → Push.

---

## Sonrasında

Yükleme bittikten 1–2 dakika sonra site şu adreste açılır:

**https://nintendomitt.github.io/droguzacarturk/**

İlk açılışta kontrol edin:

- [ ] Fotoğraf ve American Board logosu görünüyor mu
- [ ] Dil değiştirici çalışıyor mu (TR / EN / DE / RU)
- [ ] Formu doldurup gönderin — WhatsApp hazır mesajla açılmalı
- [ ] Telefonda sayfayı açıp alt bardaki butonları deneyin

---

## Sonraki güncellemeler

Dosyalarda değişiklik yapınca:

```bash
git add .
git commit -m "Ne değiştiğini yazın"
git push
```

Push'tan ~1 dakika sonra site otomatik güncellenir. Sürükle bırak yöntemini kullanıyorsanız aynı upload sayfasından yeni sürümü yükleyip commit etmeniz yeterli.

---

## Özel domain (droguzacarturk.com) bağlamaya hazır olduğunuzda

Şu an test adresinde yayında; eski Wix siteniz çalışmaya devam ediyor. Geçişe karar verdiğinizde:

**1.** Repoya `CNAME` adında, içinde tek satır olan bir dosya ekleyin:

```
www.droguzacarturk.com
```

**2.** Domain sağlayıcınızın DNS panelinde:

| Tip | Ad | Değer |
|---|---|---|
| CNAME | `www` | `nintendomitt.github.io` |
| A | `@` | `185.199.108.153` |
| A | `@` | `185.199.109.153` |
| A | `@` | `185.199.110.153` |
| A | `@` | `185.199.111.153` |

**3.** Settings → Pages → Custom domain alanına `www.droguzacarturk.com` yazın.

**4.** Eski Wix URL'lerinin arama motorlarındaki değerini korumak için Wix panelinden 301 yönlendirme kurun:

| Eski | Yeni |
|---|---|
| `/cerrahiniz-dr-oguz` | `/` |
| `/lenfodem` | `/lenfodem-lipodem-cerrahisi.html` |
| `/yuz` · `/goez-kapagi` · `/meme-buyutme` | `/` |
| `/meme` | `/#iletisim` |

> GitHub Pages sunucu tarafında yönlendirme yapamaz — bu yönlendirmeler Wix tarafında kurulmalı ve en az birkaç ay çalışmalı. Wix aboneliğini hemen iptal etmeyin, yoksa mevcut arama sıralamanız sıfırlanır.
