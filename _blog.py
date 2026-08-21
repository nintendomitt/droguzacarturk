# -*- coding: utf-8 -*-
"""
Blog yazilari — icerik kaynagi.

Her yazi bir sozluk. Alanlar:
  slug      : dosya adi (blog/<slug>.html)
  date      : yayin tarihi (YYYY-MM-DD) — gelecek tarihli yazilar uretilmez
  cat       : kategori etiketi
  title     : <title> (60-65 karakter hedef)
  ogtitle   : sosyal paylasim basligi
  desc      : meta description (150-160 karakter)
  h1        : sayfa basligi
  lead      : giris paragrafi (ilk cevap burada olmali — snippet icin)
  sections  : _build.py body_html ile ayni blok yapisi
  faqs      : [(soru, cevap), ...]
  watopic   : WhatsApp mesajinda gececek konu
  related   : ilgili hizmet sayfasi slug'lari (otorite akisi icin)

NOT: Blog anasayfada gorunmez. Kesif yalnizca /blog/ hub, sitemap ve
     footer'daki tek baglanti uzerinden olur.
"""

BLOG = [

{"slug":"fil-hastaligi-nedir",
 "date":"2026-08-21",
 "cat":"Lenfödem",
 "title":"Fil Hastalığı Nedir? Türkiye'de Görülen Tablo | Doç. Dr. T. Oğuz Acartürk",
 "ogtitle":"Fil Hastalığı Nedir? Türkiye'de Görülen Tablo Hangisi?",
 "desc":"Fil hastalığı nedir, Türkiye'de görülen tablo hangisidir? Elefantiyazis ile ileri evre lenfödem arasındaki ilişki, bulgular ve tedavi seçenekleri.",
 "h1":"Fil hastalığı nedir?",
 "lead":"Fil hastalığı, tıptaki adıyla <strong>elefantiyazis</strong>, kol veya bacağın aşırı derecede şişip deri yapısının kalınlaşmasıyla giden ileri bir tablodur. Türkiye'de görülen vakaların neredeyse tamamı <strong>ileri evre lenfödemdir</strong> — yani tropik bölgelerdeki parazit hastalığı değil, lenf dolaşımının bozulmasına bağlı bir durumdur. Ve bu, tedavi edilebilir bir hastalıktır.",
 "watopic":"fil hastalığı (ileri evre lenfödem) değerlendirmesi",
 "related":["lenfodem","lenfodem-evreleri","bacakta-lenfodem"],
 "sections":[
  {"id":"nedir","tag":"Tanım","h2":"Fil hastalığı tıbbi olarak ne demek?","body":[
   "Halk arasında \"fil hastalığı\" denen tablo, tıp literatüründe <strong>elefantiyazis</strong> olarak geçer. Adını, etkilenen uzvun fil ayağına benzeyecek kadar kalınlaşmasından alır.",
   "Bu bir hastalığın adı değil, bir <strong>sonucun</strong> adıdır. Yani elefantiyazis, altta yatan farklı nedenlerin ortak varış noktasıdır. Bu ayrım önemli, çünkü tedavi nedene göre değişir.",
   ("h3","İki farklı tablo, aynı isim"),
   ("ul",["<strong>Lenfatik filariazis:</strong> sivrisinekle bulaşan bir parazitin lenf kanallarına yerleşmesiyle oluşur. Dünya genelinde en sık elefantiyazis nedenidir — ancak <strong>tropik ve subtropik bölgelerde</strong> görülür. Türkiye endemik bölge değildir.",
          "<strong>İleri evre lenfödem:</strong> lenf dolaşımının cerrahi, radyoterapi, tekrarlayan enfeksiyon veya doğuştan yetersizlik nedeniyle bozulmasıyla gelişir. <strong>Türkiye'de görülen tablo budur.</strong>"]),
   ("note","Türkiye'de bir hastada elefantiyazis görüldüğünde, ilk düşünülmesi gereken ileri evre lenfödemdir. Filariazis ancak endemik bir bölgede uzun süre bulunma öyküsü varsa gündeme gelir.")]},
  {"id":"nasil","tag":"Süreç","h2":"Nasıl bu noktaya gelinir?","body":[
   "Elefantiyazis bir günde ortaya çıkmaz. Yılları alan, kademeli bir süreçtir ve her aşamada müdahale şansı vardır.",
   ("steps",[
    ("BAŞLANGIÇ — SIVI BİRİKİMİ","Lenf sıvısı dokuda birikmeye başlar. Şişlik gün içinde artar, sabahları geçer. Bu dönemde tedavi seçenekleri en geniştir."),
    ("İKİNCİ AŞAMA — KALICI ŞİŞLİK","Şişlik uzuv yükseltildiğinde artık geçmez. Doku sertleşmeye başlar."),
    ("ÜÇÜNCÜ AŞAMA — YAĞ VE FİBROZ","Biriken sıvının yerini yağ dokusu ve fibrozis alır. Uzuv belirgin şekilde kalınlaşır."),
    ("ELEFANTİYAZİS","Deri kalınlaşır, siğilimsi değişiklikler ve derin kıvrımlar oluşur. Tekrarlayan enfeksiyonlar tabloyu hızlandırır.")]),
   "Bu ilerleyişi hızlandıran en güçlü etken <strong>tekrarlayan selülit (erizipel) atakları</strong>dır. Her atak lenfatik kanallarda kalıcı hasar bırakır ve bir sonraki atağın riskini artırır — kısır bir döngü kurulur.",
   ("note","Hastaların çoğu ilk yıllarda şişliği ciddiye almaz; çünkü ağrı yoktur ve sabahları geçer. Oysa müdahale için en değerli dönem tam olarak o dönemdir.")]},
  {"id":"belirti","tag":"Bulgular","h2":"Elefantiyazis tablosunda ne görülür?","body":[
   ("ul",["Uzuvda belirgin hacim artışı ve şekil bozukluğu",
          "Derinin kalınlaşması, sertleşmesi ve esnekliğini kaybetmesi",
          "Portakal kabuğu görünümü, siğilimsi çıkıntılar",
          "Derin deri kıvrımları ve bu kıvrımlarda mantar enfeksiyonları",
          "Deriden berrak sıvı sızması (lenfore)",
          "Tekrarlayan ateşli enfeksiyon atakları",
          "Hareket kısıtlılığı ve günlük işlerde zorlanma"]),
   ("note","Bu tabloda ağrı genellikle ön planda değildir; hastaların asıl şikâyeti ağırlık, hareket kısıtlılığı ve enfeksiyonlardır. Ağrının baskın olduğu durumlarda lipödem ya da başka bir tanı düşünülmelidir.")]},
  {"id":"tedavi","tag":"Tedavi","h2":"Fil hastalığı tedavi edilebilir mi?","body":[
   "Evet. Bu tabloyu \"çaresiz\" olarak tanımlayan bilgi güncel değil. İleri evrede bile hacmi azaltmak, enfeksiyonları seyreltmek ve hareketi geri kazandırmak mümkündür.",
   ("h3","Konservatif tedavi"),
   "Kompleks boşaltıcı fizyoterapi — manuel lenf drenajı, bandajlama, bası giysisi — tedavinin temelidir ve cerrahi sonrasında da sürer. İleri evrede tek başına yeterli olmaz ama vazgeçilmezdir.",
   ("h3","Azaltıcı cerrahi"),
   "Hacim yağ dokusu ve fibrozla arttığı için, liposuction ve eksizyon teknikleriyle uzuv hacmi belirgin şekilde küçültülebilir. İleri evrede en çok fark yaratan yöntemdir.",
   ("h3","Vaskülarize lenf nodu transferi"),
   "Sağlıklı bir bölgeden alınan lenf nodları, besleyici damarlarıyla birlikte etkilenen bölgeye taşınır. Zamanla yeni lenfatik bağlantılar kurar. Işınlanmış ve skarlaşmış dokuya canlı doku getirmesi ayrıca değerlidir.",
   ("h3","Lenfatikovenöz anastomoz (LVA)"),
   "Çalışan lenf kanalları mikroskop altında venlere bağlanır. İleri evrede tek başına yeterli olmayabilir ancak görüntülemede çalışan kanal saptanırsa diğer yöntemlerle birlikte planlanır.",
   ("note","İleri evrede genellikle tek bir yöntem yetmez. Azaltıcı cerrahi + lenf nodu transferi kombinasyonu, aşamalı olarak planlanır. Tedavi bir ameliyatla bitmez; bir program olarak yürütülür.")]},
  {"id":"enfeksiyon","tag":"Kritik","h2":"Enfeksiyonları önlemek neden bu kadar önemli?","body":[
   "Elefantiyazis tablosunda en acil ve en çok fark yaratan müdahale, <strong>selülit ataklarını azaltmak</strong>tır. Bu, hacim küçültmekten bile öncelikli olabilir.",
   ("ul",["Her atak lenfatik rezervi biraz daha azaltır",
          "Bir atak geçirmek bir sonrakinin riskini artırır",
          "Ataklar hastaneye yatış ve iş gücü kaybına yol açar",
          "Sık atak, cerrahi planlamayı da zorlaştırır"]),
   ("h3","Korunmanın temeli"),
   ("ul",["<strong>Günlük cilt bakımı:</strong> kuru deri çatlar, çatlaktan bakteri girer",
          "<strong>Mantar tedavisi:</strong> parmak araları selülitin en sık giriş kapısıdır",
          "<strong>Yaralanmalardan korunma:</strong> çıplak ayakla yürümemek, tırnakları çok kısa kesmemek",
          "<strong>Erken antibiyotik:</strong> ateş, kızarıklık ve ısı artışında beklememek"]),
   ("note","Ateş, uzuvda yaygın kızarıklık ve ısı artışı selülit habercisidir. Bu tablo gecikmeden antibiyotik gerektirir — ertelemek hem atağı ağırlaştırır hem kalıcı lenfatik hasarı artırır.")]}],
 "faqs":[
  ("Fil hastalığı Türkiye'de görülür mü?","Evet, ancak neredeyse tamamı ileri evre lenfödem tablosudur. Tropik bölgelerdeki parazit hastalığı olan lenfatik filariazis Türkiye'de endemik değildir."),
  ("Fil hastalığı bulaşıcı mı?","Türkiye'de görülen tablo — ileri evre lenfödem — <strong>bulaşıcı değildir</strong>. Ne temasla ne de başka bir yolla geçer. Bulaşıcı olan, tropik bölgelerdeki parazit hastalığıdır ve o da sivrisinek aracılığıyla, doğrudan insandan insana değil."),
  ("Fil hastalığı tedavi edilir mi?","Edilir. İleri evrede bile azaltıcı cerrahi ve lenf nodu transferi ile hacim belirgin şekilde küçültülebilir, enfeksiyonlar seyrelir ve hareket geri kazanılır. Tam şifa vaadi doğru olmaz, ancak tablo kontrol altına alınabilir."),
  ("Hangi bölüme başvurmalıyım?","Cerrahi tedavi için Plastik ve Rekonstrüktif Cerrahi, konservatif tedavi için Fiziksel Tıp ve Rehabilitasyon. İkisi birlikte çalıştığında sonuç en iyi olur."),
  ("Fil hastalığı genetik mi?","İleri evre lenfödemin çoğu sekonderdir — yani cerrahi, radyoterapi veya enfeksiyon sonrası gelişir ve kalıtsal değildir. Primer lenfödemde ise genetik yatkınlık rol oynayabilir ve aile öyküsü bulunabilir."),
  ("Bu noktaya gelmeden önce ne yapılabilirdi?","Erken evrede — şişlik henüz gün içinde artıp sabahları geçerken — mikrocerrahi ile müdahale seçenekleri çok daha geniştir. Bu yüzden ilk aylardaki şişliği ciddiye almak, sonraki yılların tablosunu belirler.")]},

{"slug":"fil-hastaligi-bulasici-mi",
 "date":"2026-08-24",
 "cat":"Lenfödem",
 "title":"Fil Hastalığı Bulaşıcı mı? Sivrisinek Efsanesi | Doç. Dr. T. Oğuz Acartürk",
 "ogtitle":"Fil Hastalığı Bulaşıcı mı? Gerçek Nedir?",
 "desc":"Fil hastalığı bulaşıcı mı, sivrisinekle geçer mi? Türkiye'de görülen tablonun bulaşıcı olmadığını ve gerçek nedenini açıklıyoruz.",
 "h1":"Fil hastalığı bulaşıcı mı?",
 "lead":"Kısa cevap: <strong>Türkiye'de görülen fil hastalığı bulaşıcı değildir.</strong> Ne temasla, ne aynı evde yaşamakla, ne de sivrisinekle geçer. Bu tablonun Türkiye'deki karşılığı ileri evre lenfödemdir — yani lenf dolaşımının bozulmasıyla ortaya çıkan, bulaşıcı olmayan bir durumdur. Karışıklık, dünyanın başka bölgelerinde görülen bambaşka bir hastalıktan kaynaklanıyor.",
 "watopic":"fil hastalığı ve lenfödem değerlendirmesi",
 "related":["lenfodem","lenfodem-neden-olur","lenfodem-hangi-doktor"],
 "sections":[
  {"id":"karisiklik","tag":"Kaynak","h2":"Karışıklık nereden geliyor?","body":[
   "İnternette \"fil hastalığı\" araması yapıldığında karşımıza çıkan bilgilerin çoğu <strong>lenfatik filariazis</strong> hakkındadır. Bu, sivrisinekle bulaşan bir parazit hastalığıdır ve dünya genelinde elefantiyazisin en sık nedenidir.",
   "Ancak bu hastalık <strong>tropik ve subtropik bölgelerde</strong> görülür: Güney Asya, Afrika'nın bazı bölgeleri, Pasifik adaları ve Güney Amerika'nın kimi kesimleri. <strong>Türkiye endemik bölge değildir.</strong>",
   ("note","Yani ekranda okuduğunuz \"sivrisinekle bulaşır\" bilgisi yanlış değil — ama sizin durumunuzla ilgili olmayabilir. Türkiye'de bir hastada elefantiyazis görüldüğünde ilk düşünülmesi gereken ileri evre lenfödemdir.")]},
  {"id":"turkiye","tag":"Türkiye","h2":"Türkiye'de bu tablo neden oluşur?","body":[
   "Türkiye'de fil hastalığı görünümüne yol açan tablo, <strong>uzun süre tedavi edilmemiş veya kontrol altına alınamamış lenfödemdir</strong>. En sık nedenler:",
   ("ul",["<strong>Kanser tedavileri:</strong> meme, jinekolojik, ürolojik kanserlerde lenf nodu diseksiyonu ve radyoterapi",
          "<strong>Tekrarlayan selülit atakları:</strong> her atak lenfatik yapıyı biraz daha bozar",
          "<strong>Doğuştan lenfatik yetersizlik:</strong> primer lenfödem",
          "<strong>Travma ve büyük cerrahiler</strong>",
          "<strong>Kronik venöz yetmezlik:</strong> zamanla lenfatik yükü artırır"]),
   "Bu nedenlerin hiçbiri bulaşıcı değildir. Hiçbiri başka bir insana geçmez."]},
  {"id":"sorular","tag":"Yakınlarınız","h2":"Aile ve yakın çevre için ne anlama geliyor?","body":[
   "Bu sorunun cevabını netleştirmek önemli, çünkü hastaların sosyal olarak en çok zorlandığı nokta burası.",
   ("table",["Soru","Cevap"],[
     ["Aynı evde yaşamak risk mi?","Hayır"],
     ["Aynı havluyu, çarşafı kullanmak?","Hayır"],
     ["Sarılmak, tokalaşmak, dokunmak?","Hayır"],
     ["Aynı havuz veya hamamı kullanmak?","Hayır"],
     ["Sivrisinek ısırığıyla geçer mi?","Türkiye'deki tabloda hayır"],
     ["Çocuklarıma geçer mi?","Hayır — sekonder lenfödem kalıtsal değildir"]]),
   ("note","Primer lenfödemde genetik yatkınlık rol oynayabilir ve ailede benzer durum görülebilir. Ancak bu \"bulaşma\" değil, kalıtımla ilgili bir durumdur ve vakaların küçük bir kısmını oluşturur.")]},
  {"id":"enfeksiyon-farki","tag":"Önemli Ayrım","h2":"Peki bu ataklar neden enfeksiyon gibi görünüyor?","body":[
   "Lenfödemli hastalarda sık görülen <strong>selülit (erizipel)</strong> atakları kafa karıştırabilir. Ateş, kızarıklık, ısı artışı — bunlar gerçekten bir enfeksiyondur.",
   "Ancak burada enfeksiyon <strong>hastalığın nedeni değil, sonucudur</strong>. Lenf dolaşımı bozulduğu için dokunun mikroplara karşı savunması zayıflar; deri çatlaklarından giren bakteri kolayca yerleşir.",
   ("ul",["Selülit bulaşıcı bir hastalık değildir — kişinin kendi cildindeki bakterilerden kaynaklanır",
          "Başkasına geçmez",
          "Ancak hastanın kendisi için tehlikelidir: her atak lenfatik hasarı artırır",
          "Ateş ve yaygın kızarıklıkta gecikmeden antibiyotik gerekir"]),
   ("note","Bu ayrım hem hasta hem yakınları için rahatlatıcı olmalı: ataklar sizin için ciddi ama çevrenizdekiler için risk taşımıyor.")]}],
 "faqs":[
  ("Fil hastalığı bulaşıcı mı?","Türkiye'de görülen tablo — ileri evre lenfödem — bulaşıcı değildir. Temasla, ortak eşya kullanımıyla veya başka bir yolla geçmez."),
  ("Sivrisinek ısırığıyla fil hastalığı olur mu?","Türkiye'de hayır. Sivrisinekle bulaşan lenfatik filariazis tropik bölgelerde görülür; Türkiye endemik bölge değildir. Endemik bir bölgede uzun süre bulunma öyküsü yoksa bu ihtimal gündeme gelmez."),
  ("Ailemdekilere geçer mi?","Hayır. Sekonder lenfödem — yani cerrahi, radyoterapi veya enfeksiyon sonrası gelişen tablo — bulaşıcı da değildir, kalıtsal da değildir."),
  ("Aynı evde yaşamak sakıncalı mı?","Hiçbir sakıncası yok. Ortak yaşam alanı, havlu, çarşaf, banyo kullanımı risk oluşturmaz."),
  ("Selülit atakları başkasına bulaşır mı?","Hayır. Selülit, kişinin kendi cildindeki bakterilerin deri çatlaklarından girmesiyle oluşur ve bulaşıcı değildir. Ancak hastanın kendisi için ciddidir ve erken antibiyotik gerektirir."),
  ("Bu tablo tedavi edilebilir mi?","Evet. İleri evrede bile azaltıcı cerrahi ve lenf nodu transferi ile hacim küçültülebilir, enfeksiyonlar seyrelir. Erken evrede müdahale edilirse seçenekler çok daha geniştir.")]},

{"slug":"fil-hastaligi-hangi-bolum-bakar",
 "date":"2026-08-28",
 "cat":"Hasta Rehberi",
 "title":"Fil Hastalığına Hangi Bölüm Bakar? | Doç. Dr. T. Oğuz Acartürk",
 "ogtitle":"Fil Hastalığına Hangi Bölüm Bakar?",
 "desc":"Fil hastalığı (ileri evre lenfödem) için hangi bölüme başvurulmalı? Plastik cerrahi ve fizik tedavinin rolleri, randevu hazırlığı ve doğru yönlendirme.",
 "h1":"Fil hastalığına hangi bölüm bakar?",
 "lead":"Cerrahi tedavi için <strong>Plastik ve Rekonstrüktif Cerrahi</strong>, konservatif tedavi için <strong>Fiziksel Tıp ve Rehabilitasyon</strong>. Bu iki bölüm birbirinin alternatifi değil, tamamlayıcısıdır. Fil hastalığı görünümündeki bir tabloda — yani ileri evre lenfödemde — en iyi sonuç, iki branşın birlikte çalıştığı merkezlerde alınır.",
 "watopic":"fil hastalığı için doğru bölüm",
 "related":["lenfodem-hangi-doktor","lenfodem","lenfodem-evreleri"],
 "sections":[
  {"id":"neden-karisik","tag":"Sorun","h2":"Neden bu kadar çok bölüm dolaşılıyor?","body":[
   "Fil hastalığı görünümüyle başvuran hastalar sıklıkla dahiliye, kardiyoloji, damar cerrahisi ve dermatoloji arasında dolaşır. Bunun iki sebebi var:",
   ("ul",["<strong>Tablo çok branşı ilgilendiriyor gibi görünür.</strong> Şişlik akla kalp ve böbreği, deri değişiklikleri dermatolojiyi, damar görünümü damar cerrahisini getirir.",
          "<strong>Lenfödem cerrahisi görece yeni bir alan.</strong> Mikrocerrahi ile lenfatik onarım yapan merkez sayısı Türkiye'de sınırlı; bu yüzden hastaya \"yapılacak bir şey yok\" denebiliyor."]),
   ("note","\"Yapacak bir şey yok\" bilgisi güncel değil. İleri evrede bile hacmi azaltmak, enfeksiyonları seyreltmek ve hareketi geri kazandırmak mümkündür.")]},
  {"id":"kim-ne-yapar","tag":"Roller","h2":"Hangi bölüm ne yapar?","body":[
   ("table",["Bölüm","Rolü"],[
     ["Plastik ve Rekonstrüktif Cerrahi","Cerrahi tedavi: azaltıcı cerrahi, lenf nodu transferi, LVA"],
     ["Fiziksel Tıp ve Rehabilitasyon","Kompleks boşaltıcı fizyoterapi, bandajlama, bası giysisi planlaması"],
     ["Enfeksiyon Hastalıkları","Tekrarlayan selülit ataklarının yönetimi"],
     ["Dermatoloji","Deri komplikasyonları, mantar enfeksiyonları"],
     ["Radyoloji","Lenfosintigrafi, ICG lenfografi, MR lenfanjiyografi"],
     ["Kardiyoloji / Nefroloji","Sistemik ödem nedenlerinin dışlanması"],
     ["Damar Cerrahisi","Venöz yetmezlik ve tromboz ayrımı"]]),
   ("note","İlk başvuru için doğru adres, tabloyu bütün olarak değerlendirebilecek olan plastik cerrahi veya fizik tedavidir. Diğer branşlar gerektiğinde devreye girer.")]},
  {"id":"ne-zaman","tag":"Yönlendirme","h2":"Hangi durumda kime?","body":[
   ("table",["Durumunuz","Başvuru"],[
     ["Şişlik ileri boyutta, hareket kısıtlı","Plastik cerrahi — cerrahi değerlendirme"],
     ["Fizyoterapi görüyor, yeterli gelmiyor","Plastik cerrahi"],
     ["Bası giysisi ve fizyoterapi planı gerekiyor","Fizik tedavi ve rehabilitasyon"],
     ["Sık selülit atağı geçiriyor","Enfeksiyon hastalıkları + lenfödem ekibi"],
     ["Deriden sızıntı, açık yara var","Plastik cerrahi — öncelikli"],
     ["Ani başlayan ağrılı şişlik","Acil servis — damar tıkanıklığı dışlanmalı"]]),
   ("note","Ani başlayan, ağrılı ve tek taraflı şişlik derin ven trombozunu düşündürebilir ve acildir. Lenfödem değerlendirmesi bu ihtimal dışlandıktan sonra yapılır.")]},
  {"id":"hazirlik","tag":"Hazırlık","h2":"Randevuya ne götürmeli?","body":[
   ("ul",["<strong>Ameliyat raporları:</strong> lenf nodu diseksiyonu yapıldı mı, kaç nod çıkarıldı",
          "<strong>Radyoterapi bilgisi:</strong> hangi bölgeye, kaç seans",
          "<strong>Görüntüleme kayıtları:</strong> lenfosintigrafi veya MR yapıldıysa",
          "<strong>Enfeksiyon öyküsü:</strong> kaç selülit atağı, ne zaman, hastaneye yatış oldu mu",
          "<strong>Fotoğraflar:</strong> şişliğin yıllar içindeki değişimi",
          "<strong>Kullandığınız bası giysisi bilgisi</strong>",
          "<strong>İlaç listesi</strong>"]),
   ("note","Şişliğin <strong>ne zaman başladığı</strong> ve <strong>kaç yıldır sürdüğü</strong>, cerrahi planlamada en belirleyici bilgilerden biridir. Bu iki soruya net cevap verebilmek randevunuzun verimini doğrudan artırır.")]},
  {"id":"cerrah-secimi","tag":"Cerrah Seçimi","h2":"Cerrah seçerken nelere bakmalı?","body":[
   "Lenfatik cerrahi, plastik cerrahinin ayrı deneyim gerektiren bir alt alanıdır. Her plastik cerrah bu ameliyatları yapmaz. Sorulabilecek makul sorular:",
   ("ul",["Lenfödem cerrahisinde kaç vaka deneyimi var?",
          "Merkezde ICG lenfografi veya lenfosintigrafi yapılabiliyor mu?",
          "Fizyoterapi ekibiyle birlikte mi çalışılıyor?",
          "İleri evrede hangi yöntemlerin önerildiği açıkça anlatılıyor mu?",
          "Kaç aşamada planlanıyor?",
          "Gerçekçi beklenti konuşuluyor mu?"]),
   ("note","Tam şifa vaadi uyarı işaretidir. Dürüst bir değerlendirme; hacim azalması, enfeksiyonların seyrelmesi ve hareketin geri kazanılması gibi ölçülebilir hedefler üzerinden konuşur.")]}],
 "faqs":[
  ("Fil hastalığına hangi bölüm bakar?","Cerrahi tedavi için Plastik ve Rekonstrüktif Cerrahi, konservatif tedavi için Fiziksel Tıp ve Rehabilitasyon. İkisi tamamlayıcıdır."),
  ("Önce hangisine gitmeliyim?","İleri evre bir tabloda plastik cerrahi değerlendirmesi öncelikli olmalıdır, çünkü cerrahi seçenekler burada belirlenir. Fizyoterapi paralel olarak yürür ve cerrahi sonrasında da sürer."),
  ("Dahiliye veya kardiyoloji gerekli mi?","Sistemik bir ödem nedeninden şüpheleniliyorsa evet. Ancak lenfödem tanısı konmuş bir hastada tedaviyi bu bölümler yürütmez."),
  ("Devlet hastanesinde yapılıyor mu?","Bazı üniversite ve eğitim-araştırma hastanelerinde lenfatik cerrahi uygulanmaktadır. Merkez sayısı sınırlıdır; başvurmadan önce teyit etmek zaman kazandırır."),
  ("Her plastik cerrah bu ameliyatı yapar mı?","Hayır. Lenfatik cerrahi ayrı deneyim gerektirir. Cerrahın bu alandaki vaka deneyimini ve merkezin görüntüleme imkânlarını sormak makuldür."),
  ("İkinci görüş almalı mıyım?","Özellikle \"yapılacak bir şey yok\" cevabı aldıysanız evet. Bu bilgi güncel değil ve ileri evrede bile uygulanabilir yöntemler var.")]},

{"slug":"fil-hastaligi-neden-olur",
 "date":"2026-08-31",
 "cat":"Lenfödem",
 "title":"Fil Hastalığı Neden Olur? Nedenleri ve İlerleme | Doç. Dr. T. Oğuz Acartürk",
 "ogtitle":"Fil Hastalığı Neden Olur? Gerçek Nedenleri",
 "desc":"Fil hastalığı neden olur? Türkiye'de görülen tablonun nedenleri, lenfödemin neden bu noktaya kadar ilerlediği ve hangi faktörlerin değiştirilebildiği.",
 "h1":"Fil hastalığı neden olur?",
 "lead":"Fil hastalığı görünümü, <strong>lenf sıvısının dokuda uzun yıllar boyunca birikmesi</strong> sonucu ortaya çıkar. Türkiye'de bunun nedeni neredeyse her zaman <strong>tedavi edilmemiş veya kontrol altına alınamamış lenfödemdir</strong> — en sık kanser cerrahisi ve radyoterapi sonrası, ardından tekrarlayan enfeksiyonlar ve doğuştan lenfatik yetersizlik gelir. Tropik bölgelerde ise neden farklıdır: sivrisinekle bulaşan bir parazit. Aynı görüntü, iki ayrı hikâye.",
 "watopic":"fil hastalığının nedeni ve tedavi seçenekleri",
 "related":["lenfodem-neden-olur","lenfodem-evreleri","lenfodem"],
 "sections":[
  {"id":"iki-neden","tag":"Ayrım","h2":"Aynı görüntünün iki farklı nedeni","body":[
   "Fil hastalığı — tıptaki adıyla elefantiyazis — tek bir hastalığın değil, bir <strong>son görüntünün</strong> adıdır. Farklı nedenler aynı noktaya varır. Bu yüzden \"neden olur\" sorusunun cevabı, hastanın nerede yaşadığına ve öyküsüne göre değişir.",
   ("table",["","Lenfatik filariazis","İleri evre lenfödem"],[
     ["Neden","Sivrisinekle bulaşan parazit","Lenf dolaşımının bozulması"],
     ["Görüldüğü yer","Tropik ve subtropik bölgeler","Dünya genelinde, Türkiye dahil"],
     ["Bulaşıcılık","Sivrisinek aracılığıyla","Bulaşıcı değil"],
     ["Türkiye'deki payı","Endemik değil; çok nadir","Vakaların neredeyse tamamı"],
     ["Tedaviyi yürüten","Enfeksiyon hastalıkları + cerrahi","Plastik cerrahi + fizik tedavi"]]),
   ("note","İnternette \"fil hastalığı\" araması yapıldığında çıkan bilgilerin çoğu filariazis hakkındadır. Bu bilgi yanlış değil, ancak Türkiye'deki bir hastanın durumunu genellikle açıklamaz.")]},
  {"id":"turkiyede","tag":"Nedenler","h2":"Türkiye'de fil hastalığına yol açan nedenler","body":[
   "Lenf sistemi, dokular arasında biriken protein yüklü sıvıyı toplayıp dolaşıma geri veren bir ağdır. Bu ağın taşıma kapasitesi, yükün altına düştüğünde sıvı dokuda kalır. Elefantiyazis, bu dengesizliğin yıllarca sürmesinin sonucudur.",
   ("h3","Sekonder nedenler — en sık grup"),
   ("ul",["<strong>Kanser cerrahisi:</strong> meme, jinekolojik, ürolojik kanserler ve melanomda lenf nodu diseksiyonu. Çıkarılan nod sayısı arttıkça risk artar.",
          "<strong>Radyoterapi:</strong> ışınlanan bölgede lenfatik kanallar zamanla fibrozla daralır. Etkisi yıllar sonra da ortaya çıkabilir.",
          "<strong>Tekrarlayan selülit (erizipel) atakları:</strong> her atak lenfatik kanallarda kalıcı hasar bırakır.",
          "<strong>Travma ve büyük cerrahiler:</strong> kasık, koltuk altı gibi lenfatik yoğunluğun yüksek olduğu bölgelerdeki yaralanmalar.",
          "<strong>Kronik venöz yetmezlik:</strong> venöz sistemin taşıyamadığı yükü lenfatik sistem üstlenir; zamanla o da yorulur (flebolenfödem).",
          "<strong>İleri obezite:</strong> çok yüksek vücut kitle indeksinde lenfatik akım mekanik olarak engellenir."]),
   ("h3","Primer nedenler"),
   "Primer lenfödemde lenfatik yapı doğuştan yetersizdir — kanal sayısı az, kapak yapısı bozuk veya nodlar gelişmemiştir. Doğumda, ergenlikte veya erişkin dönemde ortaya çıkabilir. Vakaların küçük bir kısmını oluşturur ancak tedavi edilmediğinde ileri evreye ilerleme eğilimi belirgindir.",
   ("note","Nedeni ayrıntılı olarak ele alan hizmet sayfamız için: <a href=\"../lenfodem-neden-olur.html\">lenfödem neden olur</a>. Bu yazı, nedenin ötesinde <strong>ilerlemenin</strong> neden olduğuna odaklanıyor.")]},
  {"id":"ilerleme","tag":"İlerleme","h2":"Asıl soru: neden bu noktaya kadar ilerliyor?","body":[
   "Lenf nodu diseksiyonu geçiren her hastada fil hastalığı görünümü gelişmez. Aynı ameliyatı olan iki hastadan biri hafif bir şişlikle yıllarca yaşarken diğerinde tablo ağırlaşabilir. Farkı yaratan, başlangıç nedeni değil <strong>sonraki yıllarda olan bitendir</strong>.",
   ("steps",[
    ("BİRİKEN SIVI DOKUYU DEĞİŞTİRİR","Lenf sıvısı protein yüklüdür. Dokuda kaldığında kronik bir inflamasyon başlatır; bağ dokusu ve yağ dokusu artar. Bu noktadan sonra hacim yalnızca sıvıdan değil, kalıcı dokudan kaynaklanır."),
    ("SERTLEŞEN DOKU AKIMI DAHA DA BOZAR","Fibrozis, kalan sağlam lenf kanallarını dışarıdan sıkıştırır. Taşıma kapasitesi bir kez daha düşer."),
    ("ENFEKSİYON DÖNGÜSÜ KURULUR","Savunması zayıflamış dokuda selülit kolay gelişir. Her atak biraz daha lenfatik kanal kaybettirir; kayıp bir sonraki atağı kolaylaştırır."),
    ("HAREKETSİZLİK EKLENİR","Ağırlaşan uzuv daha az kullanılır. Kas pompası devreden çıkınca lenfatik akımın en önemli mekanik desteği kaybolur."),
    ("ELEFANTİYAZİS","Deri kalınlaşır, kıvrımlar derinleşir, siğilimsi değişiklikler ve sızıntı görülür.")]),
   "Bu zincirin her halkası bir öncekini besler. Kritik nokta şu: <strong>halkalardan birini kırmak zinciri yavaşlatır.</strong> En çok fark yaratan halka, çoğu hastada enfeksiyon döngüsüdür.",
   ("h3","Zamanlama neden bu kadar belirleyici?"),
   "Lenfödemde dokunun yapısı, tablo ilerledikçe değişir. İlk dönemde hacim büyük ölçüde sıvıdan kaynaklanır; sıvı, drenaj ve bası ile yer değiştirebilir. Yıllar geçtikçe sıvının yerini yağ dokusu ve fibrozis alır ve bu doku artık yer değiştirmez — çıkarılması gerekir.",
   "Bu, tedavi seçeneklerinin zamanla nasıl daraldığını açıklar. Erken dönemde mikrocerrahi ile lenfatik akımı yeniden yönlendirmek gündeme gelebilirken, ileri evrede öncelik hacmi azaltmaya kayar. İki yaklaşım da uygulanabilir; ancak sıralamayı ve beklentiyi belirleyen, kaç yıl geçtiğidir.",
   ("note","Hastaların çoğu ilk yıllarda şişliği ciddiye almaz, çünkü ağrı yoktur ve sabahları geriler. Oysa doku henüz yumuşakken müdahale seçenekleri en geniştir. Bu bir suçlama değil — tablonun sessiz başlaması hastalığın doğasında var.")]},
  {"id":"ayirici","tag":"Ayırıcı Tanı","h2":"Bu görünüm her zaman lenfödem mi?","body":[
   "Şişmiş ve kalınlaşmış bir uzuv gördüğünde ilk düşünülen lenfödemdir, ancak benzer görünüme yol açan başka tablolar da vardır. Nedeni doğru koymak, tedavinin tamamını belirlediği için bu ayrım atlanmamalıdır.",
   ("table",["Tablo","Ayırt eden özellik"],[
     ["Lenfödem","Genellikle tek taraflı, ayak sırtı dahil, parmaklar kalın (Stemmer bulgusu)"],
     ["Lipödem","Çift taraflı ve simetrik, ayaklar korunur, dokunmakla ağrı belirgin"],
     ["Kronik venöz yetmezlik","Akşamları artan şişlik, varis, ayak bileğinde renk değişikliği"],
     ["Kalp veya böbrek kaynaklı ödem","Çift taraflı, gode bırakan, sistemik bulgular eşlik eder"],
     ["Derin ven trombozu","Ani başlangıç, ağrı, ısı artışı — acil değerlendirme gerektirir"],
     ["Lipo-lenfödem","İki tablonun birlikte bulunması; zamanla lipödeme lenfödem eklenir"]]),
   "Bu tabloların bir kısmı bir arada bulunabilir. Örneğin uzun süreli venöz yetmezlik zeminde lenfatik yükü artırarak lenfödemi başlatabilir; ileri lipödeme yıllar içinde lenfödem eklenebilir. Bu durumlarda tedavi de katmanlı planlanır.",
   ("note","Ani başlayan, ağrılı ve tek taraflı şişlik derin ven trombozunu düşündürür ve acildir. Lenfödem değerlendirmesi bu ihtimal dışlandıktan sonra yapılır.")]},
  {"id":"faktorler","tag":"Risk","h2":"Hangi faktörler değiştirilebilir, hangileri değil?","body":[
   "Bu ayrım pratik olarak önemli, çünkü enerjinin nereye harcanacağını belirler.",
   ("table",["Faktör","Değiştirilebilir mi?","Ne yapılabilir"],[
     ["Çıkarılan lenf nodu sayısı","Hayır","Geçmiş cerrahi değiştirilemez"],
     ["Radyoterapi öyküsü","Hayır","Etkisi takiple izlenir"],
     ["Genetik yatkınlık","Hayır","Erken tanı ve düzenli izlem"],
     ["Selülit atakları","Evet","Cilt bakımı, mantar tedavisi, erken antibiyotik"],
     ["Bası giysisi kullanımı","Evet","Doğru sınıf, doğru ölçü, düzenli yenileme"],
     ["Vücut ağırlığı","Kısmen","Kontrollü ve sürdürülebilir azalma"],
     ["Hareketsizlik","Evet","Düzenli, uzuvu yormayan egzersiz"],
     ["Tanıdaki gecikme","Evet","Şişliği ilk yılında değerlendirtmek"]]),
   "Tablonun sağ sütunundaki dört kalem, ileri evreye gidişi belirleyen asıl kalemlerdir. Hiçbiri tek başına hastalığı geri döndürmez; ancak birlikte uygulandığında ilerleme hızı ölçülebilir şekilde yavaşlar.",
   ("note","Kilo başlığı hassas bir konu ve dikkatle konuşulmalı. Lenfödem kilo alımının sonucu değildir; ancak ileri obezite mevcut tabloyu mekanik olarak ağırlaştırır. Amaç estetik değil, lenfatik yükü azaltmaktır.")]},
  {"id":"neden-onemli","tag":"Sonuç","h2":"Nedeni bilmek tedaviyi nasıl değiştirir?","body":[
   "Nedeni netleştirmek akademik bir ayrıntı değil; doğrudan tedavi planını belirler.",
   ("ul",["<strong>Kanser tedavisi sonrasıysa:</strong> hangi nodların çıkarıldığı ve hangi bölgenin ışınlandığı, lenf nodu transferinde verici ve alıcı bölge seçimini belirler.",
          "<strong>Enfeksiyon ağırlıklıysa:</strong> önce atak sıklığını düşürmek gerekir; sık atak varken cerrahi planlamak riskli olur.",
          "<strong>Primer lenfödemse:</strong> lenfatik anatominin görüntülemeyle haritalanması öne çıkar; çalışan kanal varsa LVA gündeme gelir.",
          "<strong>Venöz yetmezlik eşlik ediyorsa:</strong> venöz sorun ele alınmadan lenfatik tedavi eksik kalır.",
          "<strong>Doku ağırlıklı olarak yağ ve fibrozsa:</strong> drenaj ve bası tek başına hacmi düşürmez; azaltıcı cerrahi gündeme gelir."]),
   "Bu yüzden ilk değerlendirmede öykü, görüntülemeden önce gelir. Şişliğin ne zaman başladığı, kaç yıldır sürdüğü ve kaç enfeksiyon atağı geçirildiği — bu üç bilgi, planın büyük kısmını şekillendirir.",
   ("note","İleri evrede bile tablo yönetilebilir. Hacmi azaltmak, enfeksiyonları seyreltmek ve hareketi geri kazandırmak mümkündür. Tam şifa vaadi doğru olmaz; ancak \"yapılacak bir şey yok\" bilgisi de güncel değildir.")]}],
 "faqs":[
  ("Fil hastalığı neden olur?","Lenf sıvısının dokuda uzun yıllar birikmesiyle. Türkiye'de bunun nedeni genellikle kanser cerrahisi ve radyoterapi sonrası gelişen lenfödem, tekrarlayan enfeksiyonlar veya doğuştan lenfatik yetersizliktir. Tropik bölgelerde ise sivrisinekle bulaşan bir parazit hastalığı söz konusudur."),
  ("Lenf nodu ameliyatı olan herkeste gelişir mi?","Hayır. Lenf nodu diseksiyonu riski artırır ancak çoğu hastada ileri evre tablo gelişmez. Belirleyici olan, sonraki yıllarda enfeksiyon ataklarının, bası giysisi kullanımının ve tanı zamanlamasının nasıl seyrettiğidir."),
  ("Neden bazı hastalarda hızlı ilerliyor?","En güçlü hızlandırıcı, tekrarlayan selülit ataklarıdır. Her atak lenfatik kanallarda kalıcı hasar bırakır. Buna hareketsizlik, bası giysisinin kullanılmaması ve tanıdaki gecikme eklendiğinde ilerleme belirgin şekilde hızlanır."),
  ("Fil hastalığı genetik mi?","Çoğu vaka sekonderdir — yani cerrahi, radyoterapi veya enfeksiyon sonrası gelişir ve kalıtsal değildir. Primer lenfödemde genetik yatkınlık rol oynayabilir ve ailede benzer durum bulunabilir."),
  ("Kilo vermek tabloyu düzeltir mi?","Tek başına düzeltmez, ancak ileri obezite varsa lenfatik yükü azaltarak tedavinin etkisini artırır. Lenfödem kilo alımının sonucu değildir; bu iki durumu karıştırmamak gerekir."),
  ("İlerlemesini durdurmak mümkün mü?","İlerlemeyi tümüyle durdurma garantisi verilemez, ancak hızını yavaşlatmak mümkündür. Enfeksiyon ataklarını azaltmak, düzenli bası giysisi kullanmak ve uzuvu hareketli tutmak bu konuda en çok fark yaratan üç başlıktır.")]},

]
