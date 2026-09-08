# -*- coding: utf-8 -*-
"""
Hidradenitis suppurativa (HS) onarim sayfasi.

KAPSAM NOTU — bu sayfa neden yazilabilir:
  HS'nin ILERI EVRESI (Hurley 3) cerrahi bir hastaliktir; genis eksizyon ve
  ardindan flep/greft ile rekonstruksiyon plastik cerrahinin alanidir. Yani
  lenfoma orneginin aksine burada uzmanlik-icerik uyumu var.

  ANCAK medikal tedavi (antibiyotik, biyolojik ajanlar, hormonal tedavi)
  DERMATOLOJININ alanidir. Sayfa bunu acikca soyler ve erken evre hastayi
  dermatolojiye yonlendirir. Hasta yanlis kapiya gitmesin.

Semrush TR: hidradenitis supurativa 6.600/ay (KD 19) · hidradenit 1.000 (16)
            hidradenit nedir 720 (15) · ter bezi iltihabi 590 (25)
            koltuk alti ciban 390 (23) · akne inversa 110 (21)
"""

HIDRADENIT = [{
 "key": "hidradenit",
 "authority": "Hidradenitis süpürativanın ileri evresinde tek kalıcı çözüm geniş eksizyon ve ardından yapılan rekonstrüksiyondur. Bu, tekrarlayan apse drenajından tamamen farklı bir cerrahidir: hastalıklı ter bezi alanının bütünüyle çıkarılması ve oluşan geniş defektin flep ya da greftle kapatılması gerekir. Doç. Dr. Acartürk'ün serbest doku aktarımı ve flep cerrahisindeki pratiği, koltuk altı ve kasık gibi hareketli bölgelerde kontraktür bırakmayan kapama planlaması için belirleyicidir.",
 "creds": ["University of Pittsburgh'da 300+ mikrocerrahi ve flep vakası",
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
   "follow": "Bölgeye göre 2–6 hafta hareket kısıtlaması, yara bakımı, kontraktür önleyici egzersiz ve dermatoloji ile ortak takip.",
   "body": "Koltuk altı, kasık, meme altı, kalça"},
 "keyfacts": [("Evreleme", "Hurley 1–2–3"),
              ("Cerrahi kararı", "Genellikle Hurley 2–3"),
              ("Yöntem", "Geniş eksizyon + flep/greft"),
              ("Kritik", "Erken evre dermatolojinin alanı")],
 "sections": [
  {"id": "nedir", "tag": "Tanım", "h2": "Hidradenitis süpürativa nedir?", "body": [
   "Hidradenitis süpürativa (HS), tıp literatüründe <strong>akne inversa</strong> olarak da geçen kronik ve tekrarlayıcı bir deri hastalığıdır. Halk arasında \"ter bezi iltihabı\" ya da \"koltuk altı çıbanı\" denilen tablonun tekrarlayan ve tünelleşen biçimi çoğunlukla budur.",
   "Hastalık kıl folikülünün tıkanmasıyla başlar. Tıkanan folikül şişer, iltihaplanır ve patlar; iyileşirken deri altında <strong>sinüs traktı</strong> denilen tüneller bırakır. Bu tüneller birbirine bağlanır, akıntı yapar ve her atakta nedbe dokusu artar.",
   ("note", "<strong>Sık yapılan hata:</strong> her atakta apsenin ayrı ayrı boşaltılması. Drenaj o günkü ağrıyı geçirir ama tünelleri ve hastalıklı ter bezi alanını yerinde bırakır — bu yüzden şikâyet birkaç ay sonra aynı yerde geri döner. Tekrarlayan drenaj, hastalığın tedavisi değildir."),
   ("h3", "En sık tutulan bölgeler"),
   ("ul", ["Koltuk altı",
           "Kasık ve genital bölge",
           "Meme altı ve memeler arası",
           "Kalça ve makat çevresi",
           "Ense ve bel"])]},

  {"id": "evre", "tag": "Evreleme", "h2": "Hurley evrelemesi: cerrahi hangi evrede gerekir?", "body": [
   "Tedavi kararı, hastalığın evresine göre verilir. Kullanılan sınıflama <strong>Hurley evrelemesi</strong>dir ve üç basamaklıdır.",
   ("table", ["Evre", "Tablo", "Öncelikli tedavi"],
    [["Hurley 1", "Tek tek apseler, tünel ve nedbe yok", "Medikal tedavi — dermatoloji"],
     ["Hurley 2", "Tekrarlayan apseler, ayrı ayrı tüneller ve nedbeler", "Medikal tedavi + sınırlı cerrahi"],
     ["Hurley 3", "Bölgenin tamamına yayılmış birleşik tüneller", "Geniş eksizyon ve rekonstrüksiyon"]]),
   ("note", "<strong>Erken evrede cerrah değil, dermatolog.</strong> Hurley 1'de doğru adres dermatolojidir; antibiyotik, hormonal tedavi ve biyolojik ajanlarla hastalık kontrol altına alınabilir ve ameliyat gerekmeyebilir. Bu sayfa, medikal tedaviye rağmen ilerlemiş ya da başlangıçta ileri evrede olan tabloları anlatır.")]},

  {"id": "ameliyat", "tag": "Cerrahi", "h2": "Ameliyat nasıl yapılır?", "body": [
   "İleri evre HS cerrahisinin mantığı basittir ve tek cümleyle özetlenir: <strong>hastalıklı ter bezi alanının tamamı çıkarılmadan hastalık durmaz.</strong> Sınırlı çıkarma, kalan dokuda nüks demektir.",
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
   "Dürüst cevap: <strong>nüks mümkündür.</strong> Geniş eksizyon, çıkarılan alandaki hastalığı bitirir; ancak HS sistemik yatkınlığı olan bir hastalıktır ve başka bir bölgede yeniden başlayabilir.",
   "Buna karşılık literatürde net olan şey şudur: geniş eksizyon, sınırlı cerrahi ve tekrarlayan drenaja kıyasla aynı bölgede belirgin biçimde daha düşük nüks oranı verir. Yani \"kesin çözüm\" sözü verilemez, ama doğru cerrahi ile tekrar tekrar apse boşaltma döngüsünden çıkılır.",
   ("ul", ["<strong>Sigara</strong> hem hastalığın seyrini hem yara iyileşmesini kötüleştirir; bırakmak tedavinin parçasıdır.",
           "<strong>Kilo kontrolü</strong> özellikle kasık ve meme altı tutulumunda atak sıklığını azaltır.",
           "<strong>Dermatoloji takibi</strong> ameliyattan sonra da sürer; cerrahi medikal tedavinin yerine geçmez."]),
   ("note", "Hiçbir cerrahi teknik HS'de %100 kalıcı sonuç garanti etmez. Size garanti veren bir yaklaşım varsa, o yaklaşımın kendisini sorgulayın.")]}],

 "faqs": [
  ("Hidradenitis süpürativa hangi doktora gidilir?",
   "Başlangıçta dermatolojiye. Hurley 1 ve çoğu Hurley 2 olguda medikal tedavi yeterli olabilir. Tünelleşme, kalıcı nedbe ve tekrarlayan akıntı varsa plastik ve rekonstrüktif cerrahi devreye girer. En doğru yol ikisinin birlikte çalışmasıdır."),
  ("Apsemi boşalttırıyorum ama sürekli tekrarlıyor, neden?",
   "Drenaj yalnızca içerideki iltihabı boşaltır; hastalığı oluşturan tünelleri ve hastalıklı ter bezi alanını yerinde bırakır. Bu yüzden şikâyet birkaç ay içinde aynı yerde geri döner. Kalıcı sonuç için hastalıklı alanın bütünüyle çıkarılması gerekir."),
  ("Ameliyat izi büyük olur mu?",
   "Çıkarılan alan geniş olduğu için iz de belirgindir; bunu küçültmeye çalışmak nüksü davet eder. Buradaki öncelik iz değil, hastalığın durması ve bölgenin hareketinin korunmasıdır. Flep ile kapama, izin hareket kısıtlamayacak şekilde yerleşmesini sağlar."),
  ("Hidradenitis süpürativa bulaşıcı mı?",
   "Hayır. Akıntı ve iltihap görüntüsü bulaşıcı bir enfeksiyon izlenimi verse de HS bulaşmaz. Kıl folikülünün tıkanmasıyla başlayan, bağışıklık sisteminin de rol oynadığı kronik bir deri hastalığıdır."),
  ("İyileşme ne kadar sürer?",
   "Bölgeye ve kapama yöntemine göre değişir. Koltuk altı flep onarımında hareket kısıtlaması genellikle 2–4 hafta, tam iyileşme 6–8 haftadır. Greftle kapatılan geniş alanlarda süre uzar ve fizyoterapi gerekebilir."),
  ("Ameliyat sonrası ilaç tedavisi devam eder mi?",
   "Çoğu hastada evet. Cerrahi, çıkarılan bölgedeki hastalığı bitirir ama sistemik yatkınlığı ortadan kaldırmaz. Dermatoloji takibi ve gerekiyorsa medikal tedavi ameliyattan sonra da sürer.")],

 "related": ["yanik", "meme-rek", "el-cerrahisi"],
 "ctah": "Hidradenitis süpürativa için değerlendirme",
 "ctap": "Hangi bölgelerin tutulduğunu, kaç yıldır şikâyetinizin olduğunu ve daha önce uygulanan tedavileri yazın. Varsa fotoğraf ekleyin — evre değerlendirmesi ve cerrahi gerekip gerekmediği için bunlar yeterli olur.",
 "sources": [("Hidradenitis Suppurativa — StatPearls, NCBI Bookshelf",
              "https://www.ncbi.nlm.nih.gov/books/NBK534867/")],
}]
