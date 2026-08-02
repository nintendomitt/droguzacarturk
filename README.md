# droguzacarturk.com

Doç. Dr. Tahsin Oğuz Acartürk — Plastik, Rekonstrüktif ve Estetik Cerrahi.

Statik website. Derleme adımı yok, bağımlılık yok. Dosyalar olduğu gibi sunulur.

## Yapı

```
index.html                        Anasayfa (TR / EN / DE / RU)
lenfodem-lipodem-cerrahisi.html   Lenfödem & lipödem açılış sayfası
404.html                          Hata sayfası
assets/                           Görseller ve logolar
sitemap.xml  robots.txt           Teknik SEO
.nojekyll                         GitHub Pages'in Jekyll işlemesini kapatır
```

## Yerelde çalıştırma

`index.html` dosyasını tarayıcıda açmanız yeterli. Tam doğruluk için basit bir sunucu:

```bash
python3 -m http.server 8000
# http://localhost:8000
```

## Yayınlama

`main` dalına push edildiğinde GitHub Pages otomatik yayınlar. Ayarlar:
**Settings → Pages → Source: Deploy from a branch → main / (root)**

## Notlar

- İletişim formu sunucu kullanmaz; girilen bilgileri hazır bir WhatsApp mesajına dönüştürür.
- `canonical` etiketleri `droguzacarturk.com` adresini gösterir. Bu kasıtlıdır: test yayını arama motorlarında asıl domainin kopyası olarak indekslenmez.
- Ayrıntılı kurulum, mevzuat notları ve SEO yol haritası için `KURULUM-VE-SEO-YOL-HARITASI.md` dosyasına bakın.
