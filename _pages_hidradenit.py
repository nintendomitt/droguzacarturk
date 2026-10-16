# -*- coding: utf-8 -*-
"""
Hidradenitis suppurativa (HS) onarim sayfasi.

KAPSAM NOTU — bu sayfa neden yazilabilir:
  HS'nin ILERI EVRESI (Hurley 3) cerrahi bir hastaliktir; genis eksizyon ve
  ardindan flep/greft ile rekonstruksiyon plastik cerrahinin alanidir. Yani
  lenfoma orneginin aksine burada uzmanlik-icerik uyumu var.

  Hoca talebi (Ekim 2026): sayfada dermatoloji vurgusu ve halk agzi ifadeler
  ("durust cevap" vb.) olmayacak; dil kurumsal ve olcülü kalacak.

Semrush TR: hidradenitis supurativa 6.600/ay (KD 19) · hidradenit 1.000 (16)
            hidradenit nedir 720 (15) · ter bezi iltihabi 590 (25)
            koltuk alti ciban 390 (23) · akne inversa 110 (21)
"""

HIDRADENIT = [{
 "key": "hidradenit",
 "modified": {"tr": "2026-10-16", "en": "2026-10-16", "de": "2026-10-16", "ru": "2026-10-16", "ar": "2026-10-16"},
 # Öncesi-sonrası (Sağlık Hizmetlerinde Tanıtım ve Bilgilendirme Faaliyetleri Hk. Yönetmelik,
 # RG 12.11.2025/33075, m.7). Yayın şartları: hastadan Ek-1 Onam Formu alınmış olmalı (m.7/1-b),
 # işlem tarihi + her iki çekim tarihi yazılmalı (m.7/1-f), rötuş/filtre yok (m.7/1-e),
 # zorunlu uyarı metni (m.7/1-k) şablonda sabit. "yayinda": True yapılana kadar sayfada görünmez.
 "sonuc": {"yayinda": True,
           "baslik": "Koltuk altı hidradenitinde geniş eksizyon ve onarım",
           "aciklama": "İleri evre koltuk altı hidradenitinde hastalıklı bölgenin bütünüyle çıkarılıp onarıldığı bir hastamızın tedavi öncesi ve sonrası görünümü.",
           "islem_tarihi": "Ekim 2015",
           "konu": "Hidradenitis suppurativa (koltuk altı hidradeniti)",
           "oncesi": {"src": "assets/sonuc/koltuk-alti-hidradenit-tedavi-oncesi", "w": 600, "h": 800, "tarih": "15 Ekim 2015", "iso": "2015-10-15", "etiket": "Tedavi öncesi",
                      "alt": "Koltuk altında ileri evre hidradenit (koltuk altı çıbanı): şişlik, apse ve akıntılı kanallar — tedavi öncesi görünüm"},
           "sonrasi": {"src": "assets/sonuc/koltuk-alti-hidradenit-tedavi-sonrasi", "w": 600, "h": 800, "tarih": "29 Ekim 2016", "iso": "2016-10-29", "etiket": "Tedavi sonrası",
                       "alt": "Koltuk altı hidradenit tedavisi sonrası: hastalıklı bölgenin çıkarılıp onarıldığı, iyileşmiş koltuk altı"}},
 "authority": "Hidradenitis süpürativanın ileri evresinde tek kalıcı çözüm geniş eksizyon ve ardından yapılan rekonstrüksiyondur. Bu, tekrarlayan apse drenajından tamamen farklı bir cerrahidir: hastalıklı ter bezi alanının bütünüyle çıkarılması ve oluşan geniş defektin flep ya da greftle kapatılması gerekir. Doç. Dr. Acartürk'ün serbest doku aktarımı ve flep cerrahisindeki pratiği, koltuk altı ve kasık gibi hareketli bölgelerde kontraktür bırakmayan kapama planlaması için belirleyicidir.",
 "creds": ["University of Pittsburgh'da 600+ mikrocerrahi ve flep vakası",
           "Yanık ve travma sonrası skar-kontraktür rekonstrüksiyonu deneyimi",
           "Ağız, Yüz ve Çene Cerrahisi üst uzmanlığı"],
 "slug": "hidradenit-onarimi.html", "prio": "0.75",
 "crumb": "Hidradenitis Süpürativa Onarımı",
 "title": "Hidradenitis Süpürativa Cerrahisi ve Onarımı | Doç. Dr. T. Oğuz Acartürk",
 "ogtitle": "Hidradenitis Süpürativa Cerrahisi ve Onarımı",
 "desc": "İleri evre hidradenitis süpürativada geniş eksizyon ve flep ile onarım. Hangi evrede cerrahi gerekir, ameliyat nasıl yapılır, nüks riski ve iyileşme süreci.",
 "eyebrow": "Rekonstrüktif Cerrahi",
 "h1": "Hidradenitis süpürativa cerrahisi ve onarımı",
 "lead": "Hidradenitis süpürativa, koltuk altı, kasık ve meme altı gibi bölgelerde tekrarlayan ağrılı şişlikler, apseler ve akıntılı tüneller yapan kronik bir deri hastalığıdır. Erken evrede ilaçla kontrol edilebilir. Ancak dokuda kalıcı tünelleşme ve nedbeleşme başladıysa, tek kalıcı çözüm hastalıklı alanın bütünüyle çıkarılıp onarılmasıdır.",
 "watopic": "hidradenitis süpürativa cerrahisi",
 "about": "Hidradenitis suppurativa", "aboutType": "MedicalCondition",
 "card": "Hidradenit onarımı",
 "cardsub": "İleri evre HS'de geniş eksizyon ve flep ile rekonstrüksiyon",
 "procedure": {"name": "Hidradenitis Süpürativa Geniş Eksizyonu ve Rekonstrüksiyon",
   "how": "Hastalıklı ter bezi alanı sağlam dokuya kadar bütünüyle çıkarılır; oluşan defekt bölgeye göre lokal flep, perforatör flebi veya deri grefti ile kapatılır.",
   "prep": "Hurley evrelemesi, tutulan bölgelerin haritalanması, aktif enfeksiyonun kontrol altına alınması ve sigara bırakma.",
   "follow": "Bölgeye göre 2–6 hafta hareket kısıtlaması, yara bakımı, kontraktür önleyici egzersiz ve düzenli kontrol.",
   "body": "Koltuk altı, kasık, meme altı, kalça"},
 "keyfacts": [("Evreleme", "Hurley 1–2–3"),
              ("Cerrahi kararı", "Genellikle Hurley 2–3"),
              ("Yöntem", "Geniş eksizyon + flep/greft"),
              ("İyileşme", "Bölgeye göre 2–6 hafta")],
 "sections": [
  {"id": "nedir", "tag": "Tanım", "h2": "Hidradenitis süpürativa nedir?", "body": [
   "Hidradenitis süpürativa (HS), tıp literatüründe <strong>akne inversa</strong> olarak da geçen kronik ve tekrarlayıcı bir deri hastalığıdır. Halk arasında \"ter bezi iltihabı\" ya da \"koltuk altı çıbanı\" denilen tablonun tekrarlayan ve tünelleşen biçimi çoğunlukla budur.",
   "Hastalık kıl folikülünün tıkanmasıyla başlar. Tıkanan folikül şişer, iltihaplanır ve patlar; iyileşirken deri altında <strong>sinüs traktı</strong> denilen tüneller bırakır. Bu tüneller birbirine bağlanır, akıntı yapar ve her atakta nedbe dokusu artar.",
   ("note", "<strong>Tekrarlayan drenajın sınırı:</strong> Apsenin boşaltılması o anki ağrıyı giderir; ancak tünelleri ve hastalıklı ter bezi alanını yerinde bırakır. Bu nedenle şikâyet çoğu zaman birkaç ay içinde aynı bölgede yeniden ortaya çıkar. Tekrarlayan drenaj, hastalığın kalıcı tedavisi değildir."),
   ("h3", "En sık tutulan bölgeler"),
   ("ul", ["Koltuk altı",
           "Kasık ve genital bölge",
           "Meme altı ve memeler arası",
           "Kalça ve makat çevresi",
           "Ense ve bel"])]},

  {"id": "evre", "tag": "Evreleme", "h2": "Hurley evrelemesi: cerrahi hangi evrede gerekir?", "body": [
   "Tedavi kararı, hastalığın evresine göre verilir. Kullanılan sınıflama <strong>Hurley evrelemesi</strong>dir ve üç basamaklıdır.",
   ("table", ["Evre", "Tablo", "Öncelikli tedavi"],
    [["Hurley 1", "Tek tek apseler, tünel ve nedbe yok", "Medikal tedavi"],
     ["Hurley 2", "Tekrarlayan apseler, ayrı ayrı tüneller ve nedbeler", "Medikal tedavi + sınırlı cerrahi"],
     ["Hurley 3", "Bölgenin tamamına yayılmış birleşik tüneller", "Geniş eksizyon ve rekonstrüksiyon"]]),
   ("note", "Erken evrede hastalık çoğu zaman ilaç tedavisiyle kontrol altına alınabilir ve ameliyat gerekmeyebilir. Bu sayfa, medikal tedaviye rağmen ilerlemiş ya da başlangıçta ileri evrede olan tabloları anlatır.")]},

  {"id": "ameliyat", "tag": "Cerrahi", "h2": "Ameliyat nasıl yapılır?", "body": [
   "İleri evre HS cerrahisinin temel ilkesi, <strong>hastalıklı ter bezi alanının tümüyle çıkarılmasıdır.</strong> Sınırlı çıkarma, geride kalan dokuda nüks riskini artırır.",
   ("steps", [
    ("Haritalama", "Tutulan alanın sınırları belirlenir. Görünen ağızlardan daha geniş bir tünel ağı olması olağandır."),
    ("Geniş eksizyon", "Hastalıklı alan sağlam dokuya kadar bütünüyle çıkarılır. Amaç iz küçültmek değil, hastalıklı dokuyu geride bırakmamaktır."),
    ("Kapama planı", "Oluşan defekt bölgeye ve boyuta göre kapatılır — küçükse doğrudan, geniş ve hareketli bölgedeyse flep ile."),
    ("İyileşme", "Bölgeye göre 2–6 hafta hareket kısıtlaması, ardından kontraktürü önleyecek egzersiz programı.")]),
   ("h3", "Kapama yöntemleri"),
   ("ul", ["<strong>Lokal flep:</strong> Komşu sağlam dokunun kaydırılması. Koltuk altı gibi hareketli bölgelerde tercih edilir; deri kalitesi ve hareket korunur.",
           "<strong>Perforatör flebi:</strong> Geniş defektlerde, kendi damarıyla birlikte taşınan doku bloğu. Kontraktür riskini belirgin azaltır.",
           "<strong>Deri grefti:</strong> Çok geniş alanlarda seçenektir. Ancak eklem üzerinde tek başına kullanıldığında kontraktür riski taşır.",
           "<strong>Sekonder iyileşme:</strong> Yaranın kendi kendine kapanmasının beklenmesi. Uzun sürer ve nedbe kalitesi düşüktür; hareketli bölgelerde tercih edilmez."]),
   ("note", "Koltuk altı ve kasık, kolun ve bacağın hareket ettiği bölgelerdir. Buradaki kapamanın yalnızca yarayı kapatması yetmez; <strong>hareketi kısıtlamaması</strong> gerekir. Flep seçiminin asıl konusu budur.")]},

  {"id": "nuks", "tag": "Beklenti", "h2": "Nüks olur mu, ne kadar sürer?", "body": [
   "Geniş eksizyon sonrasında da <strong>nüks mümkündür.</strong> Cerrahi, çıkarılan alandaki hastalığı ortadan kaldırır; ancak HS'de sistemik bir yatkınlık bulunduğundan hastalık başka bir bölgede yeniden başlayabilir.",
   "Literatürde geniş eksizyonun, sınırlı cerrahi ve tekrarlayan drenaja kıyasla aynı bölgede belirgin biçimde daha düşük nüks oranı sağladığı gösterilmiştir. Kesin sonuç vaadi verilemez; ancak doğru planlanan cerrahiyle tekrarlayan apse drenajı döngüsü sonlandırılabilir.",
   ("ul", ["<strong>Sigara</strong> hem hastalığın seyrini hem yara iyileşmesini kötüleştirir; bırakmak tedavinin parçasıdır.",
           "<strong>Kilo kontrolü</strong> özellikle kasık ve meme altı tutulumunda atak sıklığını azaltır.",
           "<strong>Düzenli kontrol</strong> ameliyattan sonra da sürer; gerekirse medikal tedavi cerrahiyle birlikte planlanır."]),
   ("note", "Hiçbir cerrahi teknik HS'de %100 kalıcı sonuç garanti etmez; tedavi planı her hastada evreye ve tutulan bölgelere göre belirlenir.")]}],

 "faqs": [
  ("Hidradenitis süpürativa hangi doktora gidilir?",
   "Erken evrede (Hurley 1 ve bazı Hurley 2 olgularında) ilaç tedavisi yeterli olabilir. Deri altında tünelleşme, kalıcı nedbe ve tekrarlayan akıntı varsa, hastalıklı alanın çıkarılması ve onarımı için plastik ve rekonstrüktif cerrahi değerlendirmesi gerekir."),
  ("Apsemi boşalttırıyorum ama sürekli tekrarlıyor, neden?",
   "Drenaj yalnızca içerideki iltihabı boşaltır; hastalığı oluşturan tünelleri ve hastalıklı ter bezi alanını yerinde bırakır. Bu yüzden şikâyet birkaç ay içinde aynı yerde geri döner. Kalıcı sonuç için hastalıklı alanın bütünüyle çıkarılması gerekir."),
  ("Ameliyat izi büyük olur mu?",
   "Çıkarılan alan geniş olduğu için iz de belirgindir; izi küçültmek amacıyla daha dar çıkarım yapılması nüks riskini artırır. Buradaki öncelik, hastalığın durdurulması ve bölgenin hareketinin korunmasıdır. Flep ile kapama, izin hareket kısıtlamayacak şekilde yerleşmesini sağlar."),
  ("Hidradenitis süpürativa bulaşıcı mı?",
   "Hayır. Akıntı ve iltihap görüntüsü bulaşıcı bir enfeksiyon izlenimi verse de HS bulaşmaz. Kıl folikülünün tıkanmasıyla başlayan, bağışıklık sisteminin de rol oynadığı kronik bir deri hastalığıdır."),
  ("İyileşme ne kadar sürer?",
   "Bölgeye ve kapama yöntemine göre değişir. Koltuk altı flep onarımında hareket kısıtlaması genellikle 2–4 hafta, tam iyileşme 6–8 haftadır. Greftle kapatılan geniş alanlarda süre uzar ve fizyoterapi gerekebilir."),
  ("Ameliyat sonrası ilaç tedavisi devam eder mi?",
   "Hastaya göre değişir. Cerrahi, çıkarılan bölgedeki hastalığı ortadan kaldırır ancak sistemik yatkınlığı gidermez. Gerekli görülürse medikal tedavi ameliyattan sonra da sürdürülür.")],

 "related": ["yanik", "meme-rek", "el-cerrahisi"],
 "ctah": "Hidradenitis süpürativa için değerlendirme",
 "ctap": "Hangi bölgelerin tutulduğunu, kaç yıldır şikâyetinizin olduğunu ve daha önce uygulanan tedavileri yazın. Varsa fotoğraf ekleyin — evre değerlendirmesi ve cerrahi gerekip gerekmediği için bunlar yeterli olur.",
 "sources": [("Hidradenitis Suppurativa — StatPearls, NCBI Bookshelf",
              "https://www.ncbi.nlm.nih.gov/books/NBK534867/")],
}]
