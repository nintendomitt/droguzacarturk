# -*- coding: utf-8 -*-
"""
Blog — lipodem kumesi ikinci parti, 8 yazi.
Yayin: 9-16 Ekim 2026, gunde 1.

KAPSAM NOTU: Mevcut hizmet sayfalariyla cakismamasi icin konular
uzun kuyruk secildi. "lipodem belirtileri", "lipodem evreleri",
"lipodem nedir", "lipodem diyeti", "lipodem hangi doktor" basliklari
zaten hizmet sayfalarinda — burada tekrarlanmaz.
"""

SRC_SP = ("Lipedema — StatPearls, NCBI Bookshelf",
          "https://www.ncbi.nlm.nih.gov/books/NBK573066/")
SRC_DER = ("Türkiye Lenfödem ve Lipödem Derneği",
           "https://lenfodemdernegi.org.tr/")
KAYNAK = [SRC_SP, SRC_DER]

BLOG_LIPODEM2 = [

# ------------------------------------------------------------------ 1
{"slug": "lipodemde-agri-neden-olur", "sources": KAYNAK,
 "date": "2026-10-09",
 "cat": "Lipödem",
 "title": "Lipödemde Ağrı Neden Olur? Dokunma Hassasiyeti ve Morarma",
 "ogtitle": "Lipödemde bacak ağrısı neden olur?",
 "desc": "Lipödemde ağrı, yağ dokusundaki iltihabi değişiklik ve sinir uçlarına baskıdan kaynaklanır. Dokunma hassasiyeti ve kolay morarma neden olur?",
 "h1": "Lipödemde ağrı neden olur?",
 "lead": "Lipödemi basit bir kilo fazlalığından ayıran en güçlü bulgu <strong>ağrıdır</strong>. Hastalar bacaklarına hafifçe dokunulduğunda bile acı duyduklarını, çarpmadıkları halde morluklar oluştuğunu ve gün sonunda bacaklarında derin bir sızı hissettiklerini anlatır. Bunun nedeni yağ dokusunun fazlalığı değil, o dokudaki <strong>iltihabi değişiklik, artmış sıvı ve sinir uçlarına binen baskıdır</strong>.",
 "watopic": "lipödem ağrısı değerlendirmesi",
 "related": ["lipodem", "lipodem-belirtileri"],
 "sections": [
  {"id": "neden", "tag": "Mekanizma", "h2": "Ağrının kaynağı nedir?", "body": [
   "Lipödemdeki yağ dokusu, olağan yağ dokusundan farklı davranır. Üç ayrı mekanizma ağrıya katkı verir.",
   ("ul", ["<strong>İltihabi değişiklik:</strong> lipödem dokusunda düşük düzeyli, süregen bir iltihap tablosu bildirilmiştir",
           "<strong>Sıvı birikimi:</strong> doku arasında biriken sıvı basıncı artırır ve gerginlik yaratır",
           "<strong>Sinir uçlarına baskı:</strong> genişleyen yağ lobülleri ince sinir uçlarına baskı yapar",
           "<strong>Kılcal damar kırılganlığı:</strong> küçük damarların kolay zedelenmesi morluk oluşumunu açıklar"]),
   ("note", "Bu mekanizmalar, ağrının neden <strong>kilo vermekle geçmediğini</strong> de açıklar. Sorun yağın miktarı değil, dokunun kendisidir.")]},

  {"id": "nasil", "tag": "Ağrının biçimi", "h2": "Lipödem ağrısı nasıl tarif edilir?", "body": [
   ("ul", ["Hafif dokunuşla bile ortaya çıkan hassasiyet",
           "Gün ilerledikçe artan derin sızı ve ağırlık hissi",
           "Uzun süre ayakta kalmak ya da oturmakla artan rahatsızlık",
           "Sıcak havada belirginleşen şikâyetler",
           "Çarpmadan oluşan, açıklanamayan morluklar",
           "Bacaklarda gerginlik ve dolgunluk hissi"]),
   ("note", "Ağrının varlığı, lipödemi <strong>obeziteden ve lenfödemden</strong> ayırmada en değerli bulgulardan biridir. Lenfödemde ön planda ağrı değil, ağırlık ve hareket kısıtlılığı vardır.")]},

  {"id": "ayrim", "tag": "Ayrım", "h2": "Bu ağrı başka neyin işareti olabilir?", "body": [
   "Bacak ağrısının tek nedeni lipödem değildir. Aşağıdaki tablolar ayrıca değerlendirilmelidir.",
   ("ul", ["<strong>Venöz yetmezlik:</strong> akşama doğru artan şişlik, varis, bacakta dolgunluk",
           "<strong>Derin ven trombozu:</strong> tek bacakta ani başlayan şişlik, kızarıklık ve ağrı — <strong>acil değerlendirme gerektirir</strong>",
           "<strong>Fibromiyalji:</strong> yaygın kas-iskelet ağrısı, uyku bozukluğu",
           "<strong>Lenfödem:</strong> ayak sırtı ve parmaklarda şişlik, Stemmer bulgusu",
           "<strong>Romatolojik tablolar:</strong> eklem tutulumu ve sabah tutukluğu"]),
   ("note", "<strong>Tek bacakta ani başlayan şişlik ve ağrı, lipödemin olağan tablosu değildir</strong> ve gecikmeden değerlendirilmelidir. Lipödem tipik olarak iki taraflı ve simetriktir.")]},

  {"id": "rahatlama", "tag": "Ne yardımcı olur", "h2": "Ağrıyı azaltmak için ne yapılabilir?", "body": [
   ("ul", ["<strong>Bası giysileri:</strong> doku basıncını dengeleyerek gün içi ağrıyı azaltabilir",
           "<strong>Suda egzersiz:</strong> suyun basıncı ve eklem yükünün azalması iki yönlü fayda sağlar",
           "<strong>Bacak yükseltme:</strong> gün sonunda birikmiş sıvının boşalmasına yardımcı olur",
           "<strong>Manuel lenf drenajı:</strong> hekim önerisiyle, ödem bileşeni olan hastalarda rahatlatıcı olabilir",
           "<strong>Sıcaktan korunma:</strong> aşırı sıcak, damar genişlemesiyle şikâyeti artırır"]),
   ("note", "Bu yöntemler ağrıyı <strong>yönetir</strong>, hastalığı ortadan kaldırmaz. Lipödem dokusunun kendisi ancak cerrahi ile azaltılabilir; buna karar vermeden önce konservatif yöntemlerin denenmesi standart yaklaşımdır.")]}],

 "faqs": [
  ("Lipödem ağrısı neden kilo verince geçmiyor?",
   "Çünkü ağrının kaynağı yağın miktarı değil, lipödem dokusunun kendine özgü yapısıdır: iltihabi değişiklik, doku arası sıvı ve sinir uçlarına baskı. Kilo verildiğinde yüz ve gövde incelir, lipödem bölgeleri büyük ölçüde aynı kalır ve ağrı sürer."),
  ("Çarpmadığım halde neden morarıyorum?",
   "Lipödemde küçük damarların kırılganlığı arttığı için hafif temaslarla bile kılcal damarlar zedelenebilir ve morluk oluşur. Bu, hastaların en sık bildirdiği ve en çok şaşırdığı bulgulardan biridir."),
  ("Ağrı her lipödem hastasında olur mu?",
   "Şiddeti kişiden kişiye değişir; bazı hastalarda hafif bir hassasiyet düzeyinde kalır, bazılarında günlük yaşamı kısıtlar. Ancak dokunma hassasiyeti, lipödemin tanımlayıcı bulgularından biri kabul edilir."),
  ("Ağrı kesici kullanmalı mıyım?",
   "Ağrı kesiciler geçici rahatlama sağlayabilir ancak lipödem ağrısı kronik olduğu için sürekli kullanım uygun değildir. Bası giysisi, egzersiz ve bacak yükseltme gibi yöntemler daha sürdürülebilir bir yönetim sağlar. İlaç kullanımı hekiminizle planlanmalıdır."),
  ("Ameliyat ağrıyı azaltır mı?",
   "Lipödem cerrahisinin hastalarda ağrı ve dokunma hassasiyetinde azalma sağladığı bildirilmektedir. Ancak bu, her hastada aynı ölçüde olmaz ve tam ağrısızlık vaat edilemez. Karar, konservatif yöntemler denendikten sonra verilmelidir.")]},

# ------------------------------------------------------------------ 2
{"slug": "lipodem-mi-selulit-mi", "sources": KAYNAK,
 "date": "2026-10-10",
 "cat": "Ayrım",
 "title": "Lipödem mi, Selülit mi? Portakal Kabuğu Görünümü Ayrımı",
 "ogtitle": "Lipödem ile selülit arasındaki fark",
 "desc": "Selülit yaygın ve zararsız bir cilt görünümüdür; lipödem ise ağrı, morarma ve simetrik yağ birikimiyle giden bir hastalıktır. Ayırt edici bulgular.",
 "h1": "Lipödem mi, selülit mi?",
 "lead": "Bacaklardaki pütürlü görünüm çoğu kadında bulunur ve <strong>selülit</strong> adı verilen bu tablo bir hastalık değildir. Lipödem ise farklıdır: bacaklarda <strong>simetrik yağ birikimi</strong>, <strong>ağrı ve dokunma hassasiyeti</strong>, <strong>kolay morarma</strong> ve en tipik olarak <strong>bileklerde biten şişlik</strong> ile gider. Ayrımı yapan tek soru şudur: rahatsızlık görünümle mi sınırlı, yoksa ağrı da var mı?",
 "watopic": "lipödem mi selülit mi ayrımı",
 "related": ["lipodem-belirtileri", "lipodem-nedir"],
 "sections": [
  {"id": "tablo", "tag": "Karşılaştırma", "h2": "İkisi yan yana", "body": [
   ("table", ["", "Selülit", "Lipödem"],
    [["Nedir", "Cilt altı yağın bağ dokusu arasından kabarması", "Yağ dokusunun kendine özgü hastalığı"],
     ["Ağrı", "Yok", "Var — dokunma hassasiyeti tipik"],
     ["Morarma", "Beklenmez", "Çarpmadan morluk sık"],
     ["Dağılım", "Kalça ve uyluk yüzeyinde", "Kalça, uyluk ve baldırda simetrik hacim"],
     ["Bilek sınırı", "Yok", "Şişlik bilekte biter; ayaklar normal"],
     ["Kilo vermeyle", "Bir miktar azalabilir", "Bölge büyük ölçüde aynı kalır"],
     ["Tıbbi önemi", "Kozmetik bir görünüm", "Hastalık — takip ve tedavi gerektirir"]]),
   ("note", "Selülit kadınların büyük çoğunluğunda görülür ve kilo ile doğrudan ilişkili değildir. Zayıf bir kişide de olabilir. Tek başına bir hastalık göstergesi sayılmaz.")]},

  {"id": "lipodem", "tag": "Lipödem", "h2": "Lipödemi düşündüren bulgular", "body": [
   ("ul", ["Şişlik ve hacim artışı <strong>iki bacakta simetrik</strong>",
           "Şişlik <strong>bilekte biter</strong>, ayak sırtı ve parmaklar normal görünür",
           "Dokunmakla ağrı ve hassasiyet",
           "Çarpmadan oluşan morluklar",
           "Üst gövde ile alt gövde arasında belirgin orantısızlık",
           "Kilo verildiğinde yüz ve bel incelirken bacakların aynı kalması",
           "Ergenlik, gebelik ya da menopoz dönemlerinde başlaması"]),
   ("note", "<strong>Bilek sınırı, lipödemin en ayırt edici bulgusudur.</strong> Şişlik ayak sırtına ve parmaklara uzanıyorsa, lipödem yerine lenfödem düşünülmelidir.")]},

  {"id": "selulit", "tag": "Selülit", "h2": "Selülit neden olur?", "body": [
   "Cilt altındaki yağ hücreleri, deriyi alttaki dokuya bağlayan bağ dokusu bantları arasından yukarı doğru kabarır. Bu, deride pütürlü bir yüzey oluşturur.",
   ("ul", ["Kadınlarda bağ dokusunun dizilimi bu görünümü kolaylaştırır",
           "Kilo, yaş, hormonlar ve kalıtım görünümün belirginliğini etkiler",
           "Zayıf kişilerde de görülebilir",
           "Ağrı, hassasiyet ya da morarma yapmaz"]),
   ("note", "Selülit için pazarlanan kremlerin ve cihazların çoğu, geçici ödem azalmasıyla kısa süreli bir görünüm değişikliği yaratır. Kalıcı bir çözüm vaat eden yaklaşımlara temkinli olun.")]},

  {"id": "ne-zaman", "tag": "Ne zaman hekime", "h2": "Ne zaman hekime başvurmalı?", "body": [
   ("ul", ["Bacaklarda dokunmakla ağrı varsa",
           "Çarpmadan morluklar oluşuyorsa",
           "Kilo verdiğinizde bacaklarınız değişmiyorsa",
           "Üst ve alt gövde arasında belirgin orantısızlık varsa",
           "Şikâyetler ergenlik, gebelik ya da menopozla birlikte başladıysa"]),
   "Bu bulgular varsa değerlendirme gerekir. <strong>Yalnızca pütürlü görünüm</strong> varsa ve ağrı yoksa, tıbbi bir sorundan söz etmiyoruz demektir.",
   ("note", "Lipödemi olan birçok kadın yıllarca \"kilolu\" ya da \"selülitli\" olarak değerlendirildiği için hekime başvurmaz. Ağrı ve morarma, bu iki tabloyu ayıran en pratik iki bulgudur.")]}],

 "faqs": [
  ("Selülit lipödemin erken belirtisi mi?",
   "Hayır. Selülit yaygın bir cilt görünümüdür ve tek başına lipödem göstergesi değildir. Lipödemi düşündüren şey görünüm değil, ağrı, dokunma hassasiyeti, kolay morarma ve bilekte biten simetrik şişliktir."),
  ("Lipödemli bacakta selülit görünümü olur mu?",
   "Olabilir; ikisi aynı kişide birlikte bulunabilir. Ancak selülitin varlığı ya da yokluğu lipödem tanısını değiştirmez. Tanıyı belirleyen bulgular ağrı, morarma ve dağılım biçimidir."),
  ("Selülit kremi lipödeme iyi gelir mi?",
   "Lipödem dokusu üzerinde kalıcı bir etkisi beklenmez. Bu ürünler geçici ödem azalmasıyla kısa süreli görünüm değişikliği sağlayabilir, ancak hastalığın seyrini etkilemez."),
  ("Spor yaparsam bacaklarım incelir mi?",
   "Egzersiz genel sağlık, dolaşım ve ağrı yönetimi açısından önemlidir ve önerilir. Ancak lipödem bölgelerindeki yağ dokusu egzersize dirençlidir; bacakların belirgin şekilde incelmesini beklemek gerçekçi değildir. Bu, motivasyon kırıcı değil, beklentiyi doğru kuran bir bilgidir."),
  ("Ayrım için hangi tetkik yapılır?",
   "Lipödem tanısı temel olarak muayene ve öyküyle konur; spesifik bir kan testi ya da görüntüleme yöntemi yoktur. Lenfödem ya da venöz yetmezlik şüphesinde ek tetkikler istenebilir.")]},

# ------------------------------------------------------------------ 3
{"slug": "lipodem-mi-obezite-mi", "sources": KAYNAK,
 "date": "2026-10-11",
 "cat": "Ayrım",
 "title": "Lipödem mi, Obezite mi? Kilo Vermeyen Bacakların Nedeni",
 "ogtitle": "Lipödem ile obezite arasındaki fark",
 "desc": "Obezitede kilo verilince tüm vücut incelir; lipödemde bacaklar aynı kalır. Orantısızlık, ağrı ve bilek sınırı ayrımın üç anahtarıdır.",
 "h1": "Lipödem mi, obezite mi?",
 "lead": "İkisi bir arada bulunabilir, ama aynı şey değildir. Obezitede kilo verildiğinde <strong>vücudun her yeri</strong> incelir. Lipödemde ise yüz, kollar, bel ve göğüs incelirken <strong>bacaklar büyük ölçüde aynı kalır</strong> — hastaların en çok bildirdiği ve en çok yıpratan durum budur. Ayrımı yapan üç bulgu vardır: <strong>orantısızlık</strong>, <strong>ağrı</strong> ve <strong>bilekte biten şişlik</strong>.",
 "watopic": "lipödem mi obezite mi değerlendirmesi",
 "related": ["lipodem-nedir", "lipodem-belirtileri", "lipodem-diyeti"],
 "sections": [
  {"id": "tablo", "tag": "Karşılaştırma", "h2": "Üç anahtar bulgu", "body": [
   ("table", ["", "Obezite", "Lipödem"],
    [["Dağılım", "Gövde dahil yaygın", "Alt gövde ağırlıklı, simetrik"],
     ["Orantı", "Üst ve alt gövde benzer", "Belirgin orantısızlık"],
     ["Ağrı", "Beklenmez", "Dokunma hassasiyeti tipik"],
     ["Morarma", "Beklenmez", "Çarpmadan morluk sık"],
     ["Bilek sınırı", "Yok", "Şişlik bilekte biter"],
     ["Kilo vermeyle", "Her bölge incelir", "Bacaklar büyük ölçüde aynı kalır"],
     ["Başlangıç", "Kademeli", "Ergenlik, gebelik, menopoz ile ilişkili"]])]},

  {"id": "orantisizlik", "tag": "Orantısızlık", "h2": "Orantısızlık ne demek?", "body": [
   "Lipödemde yağ birikimi vücuda eşit dağılmaz. Kalça, uyluk ve baldır belirgin şekilde hacimliyken; bel, göğüs ve kollar ince kalabilir.",
   ("ul", ["Üst beden için alınan kıyafet bedeni ile alt beden bedeni arasında iki-üç beden fark olması sık görülür",
           "Pantolon belde bol gelirken bacakta dar kalır",
           "Kilo verildiğinde bu fark <strong>azalmaz, artar</strong>"]),
   ("note", "Kıyafet bedeni farkı basit ama güçlü bir ipucudur. Hastaların çoğu bu durumu yıllardır yaşar ama tıbbi bir anlamı olabileceğini düşünmez.")]},

  {"id": "birlikte", "tag": "Birlikte olabilir", "h2": "İkisi bir arada olabilir mi?", "body": [
   "Evet ve bu sık görülür. Lipödemi olan bir kişide zamanla obezite de gelişebilir; obezitesi olan bir kişide lipödem gözden kaçabilir.",
   ("ul", ["Kilo artışı lipödem bölgelerindeki yükü artırır ve şikâyetleri ağırlaştırır",
           "Kilo verilmesi, lipödemi ortadan kaldırmasa da genel yükü azaltır ve hareketi kolaylaştırır",
           "Kilo verildikten sonra lipödem daha <strong>belirgin</strong> hale gelebilir — çünkü orantısızlık artar"]),
   ("note", "Bu nedenle \"önce kilo verin, sonra bakarız\" yaklaşımı yarım bir yanıttır. Kilo vermek yararlıdır ama lipödemin tedavisi değildir; ikisi ayrı ayrı ele alınmalıdır.")]},

  {"id": "psikoloji", "tag": "Önemli", "h2": "Neden bu ayrım bu kadar önemli?", "body": [
   "Çünkü yanlış değerlendirme, hastaya yıllarca <strong>yetersizlik duygusu</strong> yaşatır.",
   ("ul", ["Diyet ve spor yapıp bacakları değişmeyen hasta, kendini başarısız sayar",
           "Çevreden ve zaman zaman sağlık ortamlarından gelen \"daha çok çalış\" mesajı bu duyguyu pekiştirir",
           "Oysa bacakların yanıt vermemesi irade değil, <strong>doku özelliği</strong> meselesidir"]),
   ("note", "Doğru tanı, tedaviden önce bir şeyi değiştirir: hastanın kendine bakışını. Bu, lipödem tanısının en az tıbbi tarafı kadar önemli bir sonucudur.")]}],

 "faqs": [
  ("Kilo verince bacaklarım niye incelmiyor?",
   "Lipödem dokusu, olağan yağ dokusundan farklı davranır ve kalori kısıtlamasına dirençlidir. Bu nedenle kilo verildiğinde yüz, bel ve göğüs incelirken lipödem bölgeleri büyük ölçüde aynı kalır. Bu bir başarısızlık değil, hastalığın tanımlayıcı özelliğidir."),
  ("Lipödemim varsa diyet yapmamalı mıyım?",
   "Yapmalısınız, ancak beklentiyi doğru kurarak. Kilo yönetimi genel sağlık, eklem yükü ve hareket kabiliyeti açısından değerlidir ve eşlik eden obezite varsa mutlaka ele alınmalıdır. Ancak lipödem bölgelerinde belirgin bir incelme beklemek gerçekçi değildir."),
  ("Vücut kitle indeksim yüksek, lipödem olabilir miyim?",
   "Olabilirsiniz. Vücut kitle indeksi, yağın nasıl dağıldığını göstermez. Lipödem tanısı için bakılan şey indeks değil; orantısızlık, ağrı, morarma ve bilekte biten şişliktir."),
  ("Obezite cerrahisi lipödemi düzeltir mi?",
   "Obezite cerrahisi genel kiloyu azaltır ancak lipödem bölgeleri üzerinde sınırlı etki gösterir. Hatta genel kilo azaldıkça orantısızlık daha belirgin hale gelebilir. İki durum ayrı ayrı planlanmalıdır."),
  ("Hangi bölüme başvurmalıyım?",
   "Cerrahi değerlendirme için plastik ve rekonstrüktif cerrahi; konservatif tedavi ve ödem yönetimi için fiziksel tıp ve rehabilitasyon. Eşlik eden obezite ya da hormonal durum varsa endokrinoloji değerlendirmesi de yararlı olur.")]},

# ------------------------------------------------------------------ 4
{"slug": "lipodem-ve-hormonlar", "sources": KAYNAK,
 "date": "2026-10-12",
 "cat": "Lipödem",
 "title": "Lipödem ve Hormonlar: Ergenlik, Gebelik ve Menopoz",
 "ogtitle": "Lipödem neden hormonal dönemlerde başlıyor?",
 "desc": "Lipödem çoğunlukla ergenlik, gebelik veya menopozla başlar. Hormonal geçişlerin rolü, doğum kontrol hapları ve gebelik planlaması hakkında.",
 "h1": "Lipödem ve hormonlar",
 "lead": "Lipödemin neredeyse tamamen kadınlarda görülmesi ve genellikle <strong>ergenlik, gebelik ya da menopoz</strong> dönemlerinde başlaması tesadüf değildir. Bu üç dönemin ortak noktası, kadın hormonlarındaki büyük geçişlerdir. Hormonlar hastalığın <strong>tek nedeni değildir</strong> — ancak yatkınlığı olan kişilerde tabloyu başlatan ya da belirgin şekilde hızlandıran tetikleyici gibi davranır.",
 "watopic": "lipödem ve hormonal dönemler",
 "related": ["lipodem-nedir", "lipodem-evreleri"],
 "sections": [
  {"id": "donemler", "tag": "Üç dönem", "h2": "Neden bu üç dönem?", "body": [
   ("steps", [
    ("ERGENLİK", "En sık başlangıç dönemidir. Genç kadın, kalça ve uyluklarında hızlı bir hacim artışı fark eder; bu dönemde genellikle \"kilo alıyorsun\" olarak değerlendirilir."),
    ("GEBELİK VE DOĞUM SONRASI", "Var olan tablo belirginleşebilir ya da ilk kez bu dönemde başlayabilir. Gebeliğe bağlı olağan ödemle karışması sık görülür."),
    ("MENOPOZ", "Hormonal geçişle birlikte hem yeni başlangıçlar hem de mevcut tablonun ilerlemesi bildirilir.")]),
   ("note", "Ergenlikte başlayan tablonun \"gelişme çağı\" olarak değerlendirilip yıllarca gözden kaçması, lipödemde tanı gecikmesinin en büyük nedenlerinden biridir.")]},

  {"id": "mekanizma", "tag": "Mekanizma", "h2": "Hormonlar nasıl etkiliyor?", "body": [
   "Kesin mekanizma tam olarak aydınlatılmamıştır; araştırmalar sürmektedir. Bugün bilinenler şunlardır:",
   ("ul", ["Yağ hücreleri hormonlara duyarlıdır ve kadın hormonları yağın alt gövdede birikmesini destekler",
           "Lipödemi olan kişilerde bu duyarlılığın farklı olabileceği düşünülmektedir",
           "Doku arası sıvı dengesi ve kılcal damar geçirgenliği de hormonal etkiye açıktır",
           "Yatkınlık taşıyan kişilerde hormonal geçiş, tabloyu görünür hale getiriyor olabilir"]),
   ("note", "\"Hormonal\" olması, hastalığın hormon tedavisiyle düzeleceği anlamına gelmez. Bugün lipödemi ortadan kaldıran bir hormonal tedavi bulunmamaktadır.")]},

  {"id": "sorular", "tag": "Sık sorular", "h2": "Doğum kontrol hapı, gebelik ve hormon tedavisi", "body": [
   ("h3", "Doğum kontrol hapları"),
   "Bazı hastalar hap kullanımıyla şikâyetlerinde artış bildirir, bazıları hiçbir değişiklik fark etmez. Kesin bir yasak yoktur; karar, kadın hastalıkları uzmanınızla birlikte, kişisel yanıtınıza göre verilmelidir.",
   ("h3", "Gebelik planlaması"),
   "Lipödem gebeliğe engel değildir. Gebelik sırasında şikâyetlerin artması mümkündür; bası giysisi ve bacak yükseltme bu dönemde daha da önem kazanır. Gebelikte cerrahi planlanmaz.",
   ("h3", "Menopoz ve hormon tedavisi"),
   "Menopozda hormon tedavisi kararı, lipödemden bağımsız olarak genel sağlık durumuna göre verilir. Lipödem tek başına bu tedaviyi engelleyen bir durum değildir.",
   ("note", "Bu üç başlıkta da <strong>tek doğru bir yanıt yoktur</strong>. Kararlar, sizi takip eden hekimle birlikte ve kendi yanıtınız gözlenerek verilmelidir.")]},

  {"id": "aile", "tag": "Kalıtım", "h2": "Ailede lipödem varsa", "body": [
   "Lipödemi olan kadınların önemli bir bölümünde annede, teyzede ya da kız kardeşte benzer bir tablo bulunur.",
   ("ul", ["Ailede lipödem varsa, ergenlik döneminde ortaya çıkan orantısızlığı ciddiye almak gerekir",
           "Erken tanı, evrelerin ilerlemesini yavaşlatacak önlemlerin erken alınmasını sağlar",
           "Genç yaşta konan tanı, hastanın kendini yıllarca suçlamasını da önler"]),
   ("note", "Aile öyküsü bir kader değildir; tanıyı hızlandıran bir bilgidir. Ailede lipödem olan genç kadınlarda bacaklardaki değişimi \"gelişme çağı\" diye geçiştirmemek, en değerli erken müdahaledir.")]}],

 "faqs": [
  ("Lipödem neden sadece kadınlarda görülüyor?",
   "Neredeyse tamamen kadınlarda görülür ve bunun kadın hormonlarıyla ilişkili olduğu düşünülmektedir. Erkeklerde çok nadirdir ve genellikle hormonal bir dengesizliğin eşlik ettiği durumlarda bildirilir."),
  ("Doğum kontrol hapı kullanmamalı mıyım?",
   "Genel bir yasak yoktur. Bazı hastalar şikâyetlerinde artış bildirir, bazıları fark etmez. Kararı, kendi yanıtınızı gözleyerek ve kadın hastalıkları uzmanınızla birlikte vermeniz en doğrusudur."),
  ("Gebelikte lipödemim kötüleşir mi?",
   "Şikâyetlerin artması mümkündür; gebelikteki olağan ödem de tabloya eklenir. Bası giysisi, bacak yükseltme ve hareket bu dönemde daha da önemlidir. Gebelik, lipödem için bir engel değildir."),
  ("Menopozda hormon tedavisi alabilir miyim?",
   "Lipödem tek başına hormon tedavisini engelleyen bir durum değildir. Karar, genel sağlık durumunuza göre hekiminiz tarafından verilir. Tedavi sırasında lipödem şikâyetlerinizdeki değişimi not etmeniz yararlı olur."),
  ("Kızımda da olur mu?",
   "Lipödemde aile öyküsü sık bulunur, yani yatkınlık aktarılabilir. Bu kesin bir aktarım anlamına gelmez. Ergenlik döneminde ortaya çıkan orantısızlık ve bacak ağrısını ciddiye almak, erken tanı için en pratik yoldur."),
  ("Hormon tedavisiyle lipödem geçer mi?",
   "Bugün lipödemi ortadan kaldıran bir hormonal tedavi bulunmamaktadır. Hormonların tabloyu tetiklediği düşünülmekle birlikte, hormonal düzenleme hastalığın tedavisi değildir.")]},

# ------------------------------------------------------------------ 5
{"slug": "lipodemde-egzersiz", "sources": KAYNAK,
 "date": "2026-10-13",
 "cat": "Tedavi",
 "title": "Lipödemde Egzersiz: Hangi Hareketler Yardımcı Olur?",
 "ogtitle": "Lipödemde hangi egzersizler yapılmalı?",
 "desc": "Lipödemde egzersiz bacakları inceltmez ama ağrıyı, ödemi ve eklem yükünü azaltır. Su egzersizleri, yürüyüş ve kaçınılması gerekenler.",
 "h1": "Lipödemde egzersiz",
 "lead": "Egzersiz, lipödemde <strong>bacakları inceltmek için</strong> yapılmaz — bu beklenti baştan hayal kırıklığı yaratır. Egzersizin gerçek katkısı başka yerdedir: <strong>ödemi azaltır, ağrıyı hafifletir, eklem yükünü dengeler ve hareket kabiliyetini korur</strong>. En uygun seçenekler, eklem üzerindeki baskıyı azaltan ve dolaşımı destekleyen hareketlerdir; bunların başında da <strong>suda yapılan egzersizler</strong> gelir.",
 "watopic": "lipödemde egzersiz planı",
 "related": ["ameliyatsiz-lipodem-tedavisi", "lipodem"],
 "sections": [
  {"id": "neden", "tag": "Neden", "h2": "Egzersiz lipödemde ne işe yarar?", "body": [
   ("ul", ["<strong>Kas pompası:</strong> bacak kasları kasıldıkça lenf ve venöz dolaşım desteklenir",
           "<strong>Ödem azalması:</strong> gün içi biriken sıvının boşalması kolaylaşır",
           "<strong>Ağrı yönetimi:</strong> düzenli hareket, kronik ağrı algısını azaltır",
           "<strong>Eklem koruması:</strong> güçlenen kaslar diz ve kalça üzerindeki yükü dengeler",
           "<strong>Kilo yönetimi:</strong> eşlik eden obezitenin kontrolü genel yükü azaltır"]),
   ("note", "Lipödem dokusu egzersize dirençlidir; bacak ölçülerinde belirgin bir azalma beklenmemelidir. Bunu baştan bilmek, egzersizi bırakmanın en yaygın nedenini ortadan kaldırır.")]},

  {"id": "onerilen", "tag": "Önerilenler", "h2": "Hangi egzersizler uygun?", "body": [
   ("h3", "Su içi egzersizler"),
   "Lipödemde ilk sırada önerilen seçenektir. Suyun basıncı doğal bir bası etkisi yaratır, kaldırma kuvveti eklem yükünü azaltır ve serin su ödeme iyi gelir. Yüzme, su yürüyüşü ve su aerobiği uygundur.",
   ("h3", "Yürüyüş"),
   "Düz zeminde, orta tempoda ve düzenli yürüyüş dolaşımı destekler. Uzun tek seans yerine güne yayılmış kısa yürüyüşler daha iyi tolere edilir.",
   ("h3", "Bisiklet"),
   "Sabit ya da açık hava bisikleti, eklem yükü düşük bir seçenektir. Sele ve gidon ayarının doğru yapılması önemlidir.",
   ("h3", "Direnç çalışması"),
   "Hafif ağırlık ya da direnç bandıyla yapılan kas güçlendirme, eklem korumasına katkı sağlar. Bacak kaslarının güçlenmesi bacakları kalınlaştırmaz — bu yaygın bir endişedir ve karşılığı yoktur.",
   ("h3", "Esneme ve nefes çalışmaları"),
   "Derin diyafram nefesi, lenf dolaşımını destekleyen basit ve erişilebilir bir yöntemdir."]},

  {"id": "dikkat", "tag": "Dikkat", "h2": "Nelere dikkat etmeli?", "body": [
   ("ul", ["<strong>Bası giysisiyle egzersiz:</strong> hekiminiz önerdiyse, egzersiz sırasında kullanmak ödem kontrolüne katkı sağlar",
           "<strong>Aşırı sıcaktan kaçınma:</strong> sıcak ortam ve sıcak duş damar genişlemesiyle şikâyeti artırır",
           "<strong>Yüksek darbeli hareketler:</strong> koşu ve zıplama, ağrısı olan hastalarda iyi tolere edilmeyebilir",
           "<strong>Aşırıya kaçmama:</strong> ağrıyı belirgin artıran yoğunluk yararlı değildir",
           "<strong>Süreklilik:</strong> haftada birkaç kez düzenli hareket, ara ara yapılan yoğun seanslardan iyidir"]),
   ("note", "Sauna, hamam ve çok sıcak duş lipödemde genellikle şikâyeti artırır. Egzersiz sonrası ılık duş tercih edilmelidir.")]},

  {"id": "baslangic", "tag": "Başlangıç", "h2": "Nereden başlamalı?", "body": [
   ("steps", [
    ("HEKİM ONAYI", "Eşlik eden kalp, eklem ya da damar sorunu varsa program buna göre düzenlenir."),
    ("KÜÇÜK BAŞLA", "Haftada 2-3 kez, 15-20 dakikalık seanslarla başlamak sürdürülebilirliği artırır."),
    ("SUYU ÖNCELİKLENDİR", "Erişim varsa su içi egzersiz, lipödemde en iyi tolere edilen seçenektir."),
    ("KADEMELİ ARTIR", "Süre ve yoğunluk, ağrıyı belirgin artırmayacak şekilde kademeli yükseltilir."),
    ("TAKİP ET", "Ödem, ağrı ve enerji düzeyindeki değişimi not etmek, size uygun düzeni bulmayı kolaylaştırır.")]),
   ("note", "Fiziksel tıp ve rehabilitasyon uzmanı ya da konuya hâkim bir fizyoterapistle hazırlanan kişiye özel program, genel önerilerden çok daha etkili olur.")]}],

 "faqs": [
  ("Egzersizle bacaklarım incelir mi?",
   "Lipödem dokusu egzersize dirençlidir; bacak ölçülerinde belirgin bir azalma beklenmemelidir. Ancak ödem azalmasıyla bacaklarda hafiflik hissi olabilir. Egzersizin asıl kazancı ağrı, dolaşım ve hareket kabiliyeti üzerinedir."),
  ("Ağırlık çalışırsam bacaklarım kalınlaşır mı?",
   "Hafif ve orta düzey direnç çalışması bacakları kalınlaştırmaz; kasları güçlendirerek eklem yükünü dengeler. Bu yaygın endişenin tıbbi bir karşılığı yoktur."),
  ("Koşabilir miyim?",
   "Ağrınız izin veriyorsa ve eklemleriniz uygunsa engel yoktur. Ancak yüksek darbeli hareketler lipödemli hastalarda sıklıkla iyi tolere edilmez. Su içi egzersiz, yürüyüş ve bisiklet genellikle daha uygun seçeneklerdir."),
  ("Egzersiz sırasında bası giysisi giymeli miyim?",
   "Hekiminiz bası giysisi önerdiyse, egzersiz sırasında kullanmak ödem kontrolüne katkı sağlar. Giysinin doğru ölçüde olması ve iz bırakacak kadar sıkı olmaması önemlidir."),
  ("Sauna veya hamam iyi gelir mi?",
   "Genellikle gelmez. Sıcak ortam damar genişlemesine yol açarak ödem ve ağrı şikâyetlerini artırabilir. Serin ya da ılık su, lipödemde daha iyi tolere edilir."),
  ("Ameliyat sonrası ne zaman egzersize dönebilirim?",
   "Yapılan işleme ve iyileşmenin seyrine göre değişir; karar cerrahınıza aittir. Genellikle erken dönemde hafif yürüyüşe izin verilir, daha yoğun egzersiz için birkaç hafta beklenir.")]},

# ------------------------------------------------------------------ 6
{"slug": "lipodemde-basi-giysisi", "sources": KAYNAK,
 "date": "2026-10-14",
 "cat": "Tedavi",
 "title": "Lipödemde Bası Giysisi: Nasıl Seçilir, Nasıl Kullanılır?",
 "ogtitle": "Lipödemde bası giysisi kullanımı",
 "desc": "Bası giysisi lipödemde ödemi ve ağrıyı azaltır. Doğru ölçü, basınç sınıfı, giyme zamanı ve sık yapılan hataların rehberi.",
 "h1": "Lipödemde bası giysisi",
 "lead": "Bası giysisi, lipödemde <strong>en çok işe yarayan ameliyatsız yöntemdir</strong>. Yağ dokusunu eritmez — bunu net söylemek gerekir — ama doku basıncını dengeleyerek <strong>gün içi ödemi, ağırlık hissini ve ağrıyı belirgin şekilde azaltır</strong>. Etkili olmasının tek koşulu vardır: <strong>doğru ölçüde olması ve düzenli kullanılması</strong>. Yanlış ölçüdeki bir giysi fayda sağlamadığı gibi zarar da verebilir.",
 "watopic": "lipödemde bası giysisi seçimi",
 "related": ["ameliyatsiz-lipodem-tedavisi", "lipodem"],
 "sections": [
  {"id": "nasil", "tag": "Nasıl etki eder", "h2": "Bası giysisi ne yapar?", "body": [
   ("ul", ["Doku arasında biriken sıvının geri emilimini destekler",
           "Gün içi ödem artışını sınırlar",
           "Bacaklardaki ağırlık ve gerginlik hissini azaltır",
           "Dokunma hassasiyetine bağlı rahatsızlığı hafifletebilir",
           "Ameliyat sonrası dönemde iyileşmeyi destekler"]),
   ("note", "Bası giysisi lipödem <strong>yağ dokusunu azaltmaz</strong>. Şikâyetleri yönetir ve yaşam kalitesini artırır. Beklentiyi bu çerçevede kurmak, kullanıma devam etmenin en güçlü şartıdır.")]},

  {"id": "secim", "tag": "Seçim", "h2": "Nasıl seçilir?", "body": [
   ("h3", "Ölçü"),
   "Hazır beden yerine <strong>ölçü alınarak</strong> seçilmesi tercih edilir. Ölçüler sabah, ödem en az iken alınmalıdır. Yanlış ölçü, giysinin bir yerde boğum yapmasına ve alttaki bölgede ödemin artmasına yol açar.",
   ("h3", "Basınç sınıfı"),
   "Giysiler farklı basınç sınıflarında üretilir. Hangi sınıfın uygun olduğuna hekiminiz karar verir; kendi başınıza yüksek basınç seçmek yarar değil zarar getirebilir.",
   ("h3", "Uzunluk ve biçim"),
   "Tutulumun yerine göre diz altı, diz üstü, külotlu ya da kol modelleri tercih edilir. Lipödem genellikle bacakların tamamını tuttuğu için külotlu modeller sık kullanılır.",
   ("h3", "Düz örgü mü, yuvarlak örgü mü"),
   "Düz örgü giysiler daha sert yapıdadır ve şekil bozukluğu belirgin olan bacaklarda daha iyi oturur. Yuvarlak örgü daha ince ve esnektir. Seçim, bacağın biçimine göre yapılır.",
   ("note", "Kıyafet mağazasından alınan sıkı taytlar bası giysisi değildir. Tıbbi bası giysileri belirli basınç dağılımına göre üretilir ve bu, ürünün etiketinde belirtilir.")]},

  {"id": "kullanim", "tag": "Kullanım", "h2": "Nasıl kullanılır?", "body": [
   ("ul", ["<strong>Sabah, yataktan kalkar kalkmaz</strong> giyilir — ödem en az iken",
           "Gün boyu kullanılır, gece genellikle çıkarılır",
           "Giymeyi kolaylaştıran ipek çorap ya da giydirme aparatları kullanılabilir",
           "Her gün yıkanır; bu hem hijyen hem de esnekliğin korunması içindir",
           "İki takım bulundurmak, biri yıkanırken diğerinin kullanılmasını sağlar",
           "Esnekliğini yitirdiğinde yenilenir — genellikle 4-6 ayda bir"]),
   ("h3", "Kullanımı bırakmayı gerektiren durumlar"),
   ("ul", ["Bir noktada boğum yapıp altında şişlik oluşturması",
           "Ciltte kızarıklık, yara ya da tahriş",
           "Uyuşma, karıncalanma ya da renk değişikliği",
           "Ağrının belirgin şekilde artması"]),
   ("note", "Bu bulgular giysinin yanlış ölçüde ya da yıpranmış olduğunu gösterir. Kullanmaya devam etmek yerine hekiminize başvurun.")]},

  {"id": "hatalar", "tag": "Sık hatalar", "h2": "Sık yapılan hatalar", "body": [
   ("ul", ["<strong>Akşam ölçü aldırmak:</strong> ödemli bacaktan alınan ölçü, giysiyi bol yapar",
           "<strong>\"Ne kadar sıkı o kadar iyi\" düşüncesi:</strong> aşırı basınç dolaşımı bozar",
           "<strong>Sadece kötü günlerde giymek:</strong> etkisi düzenli kullanımla ortaya çıkar",
           "<strong>Yıpranmış giysiyi kullanmaya devam etmek:</strong> esnekliğini yitiren giysi basınç uygulamaz",
           "<strong>Kıvırarak ya da katlayarak giymek:</strong> katlanan yer boğum yapar"]),
   ("note", "Bası giysisini kullanmayı bırakmanın en sık nedeni, giyme zorluğu ve sıcakta rahatsızlıktır. Bu sorunlar çözülebilir: giydirme aparatı, uygun kumaş seçimi ve doğru ölçü çoğu zaman yeterlidir. Bırakmadan önce hekiminizle konuşun.")]}],

 "faqs": [
  ("Bası giysisi bacaklarımı inceltir mi?",
   "Lipödem yağ dokusunu azaltmaz. Ödemi azalttığı için bacaklarda bir miktar incelme hissi olabilir, ancak bu yağ kaybı değil sıvı kaybıdır. Asıl kazanç ağrı, ağırlık hissi ve gün içi ödem üzerindedir."),
  ("Gece de giymeli miyim?",
   "Genellikle gerekmez; gündüz kullanımı esastır. Bazı özel durumlarda gece için farklı ürünler önerilebilir, ancak bu hekiminizin kararıdır. Gündüz kullanılan giysiyle uyumak önerilmez."),
  ("Yazın çok sıcak oluyor, ne yapabilirim?",
   "Yaz için daha ince ve nefes alan kumaşlar mevcuttur. Ayrıca sabah erken ve akşam serinlikte kullanımı yoğunlaştırmak bir seçenektir. Sıcak nedeniyle tamamen bırakmak yerine, alternatif ürünleri hekiminizle konuşun."),
  ("Ne sıklıkla yenilemeliyim?",
   "Düzenli kullanılan bir giysi genellikle 4-6 ayda esnekliğini yitirir. Giysi kolayca giyilmeye başladıysa ve artık basınç hissi vermiyorsa yenileme zamanı gelmiş demektir."),
  ("Ameliyat sonrası ne kadar süre kullanılır?",
   "Lipödem cerrahisinden sonra bası giysisi kullanımı iyileşmenin önemli bir parçasıdır ve genellikle haftalarca sürer. Süreyi ve giysi tipini cerrahınız belirler."),
  ("Eczaneden hazır alabilir miyim?",
   "Hafif olgularda hazır bedenler uygun olabilir, ancak lipödemde bacak biçimi genellikle standart bedenlere uymaz. Ölçü alınarak üretilen giysiler hem daha etkili hem de boğum yapma riski açısından daha güvenlidir.")]},

# ------------------------------------------------------------------ 7
{"slug": "lipodem-ameliyati-kac-seans", "sources": KAYNAK,
 "date": "2026-10-15",
 "cat": "Tedavi",
 "title": "Lipödem Ameliyatı Kaç Seansta Biter? Aşamalı Planlama",
 "ogtitle": "Lipödem ameliyatı kaç seans sürer?",
 "desc": "Lipödem cerrahisi genellikle birden fazla seansta yapılır. Seans sayısını belirleyen etkenler, seanslar arası süre ve neden tek seferde yapılmadığı.",
 "h1": "Lipödem ameliyatı kaç seansta biter?",
 "lead": "Lipödem cerrahisi çoğu hastada <strong>tek seansta tamamlanmaz</strong>. Tutulan bölgenin genişliğine göre genellikle <strong>2-4 seans</strong> planlanır ve seanslar arasında birkaç ay beklenir. Bunun nedeni cerrahi bir sınırlama değil, <strong>güvenliktir</strong>: tek seansta çıkarılan doku ve sıvı hacminin belirli bir sınırı vardır ve bu sınırın aşılması ciddi riskler doğurur.",
 "watopic": "lipödem ameliyatı seans planlaması",
 "related": ["lipodem", "lipodem-evreleri"],
 "sections": [
  {"id": "neden", "tag": "Neden aşamalı", "h2": "Neden tek seferde yapılmıyor?", "body": [
   ("ul", ["<strong>Hacim sınırı:</strong> bir seansta güvenle çıkarılabilecek doku miktarı sınırlıdır",
           "<strong>Sıvı dengesi:</strong> geniş alan çalışmasında vücudun sıvı dengesi ciddi biçimde etkilenir",
           "<strong>Kanama riski:</strong> işlem alanı büyüdükçe kan kaybı riski artar",
           "<strong>Lenfatik koruma:</strong> geniş ve agresif çalışma lenfatik kanallara zarar verme riskini yükseltir",
           "<strong>İyileşme kalitesi:</strong> aşamalı çalışmada derinin toparlanması daha iyi değerlendirilir"]),
   ("note", "\"Hepsini tek seferde yapalım\" isteği anlaşılırdır ama güvenli değildir. Tek seansta aşırı hacim çıkarılması, lipödem cerrahisinde bilinen en ciddi risklerin kaynağıdır.")]},

  {"id": "belirleyen", "tag": "Seans sayısı", "h2": "Seans sayısını ne belirler?", "body": [
   ("ul", ["<strong>Tutulan bölge:</strong> yalnızca uyluk mu, baldır ve kollar da dahil mi",
           "<strong>Evre:</strong> ileri evrede çıkarılacak hacim daha fazladır",
           "<strong>Vücut ölçüleri:</strong> güvenli hacim sınırı kişiye göre değişir",
           "<strong>Eşlik eden durumlar:</strong> kalp, damar ya da metabolik durumlar planı değiştirir",
           "<strong>Deri kalitesi:</strong> deri toparlanması ek girişim gerektirebilir"]),
   "Tipik bir planlamada bölgeler gruplanır: örneğin bir seansta uylukların ön ve iç yüzü, sonraki seansta arka yüz ve baldırlar çalışılabilir."]},

  {"id": "arasi", "tag": "Seanslar arası", "h2": "Seanslar arasında ne kadar beklenir?", "body": [
   ("steps", [
    ("İLK 2 HAFTA", "Şişlik ve morluk belirgindir. Bası giysisi kullanımı ve hareket ön plandadır."),
    ("4-6. HAFTA", "Şişliğin büyük bölümü geriler. Günlük yaşam normale döner."),
    ("2-3. AY", "Doku toparlanır, sonuç değerlendirilebilir hale gelir. Bir sonraki seans bu dönemde planlanır."),
    ("6. AY", "Nihai sonuç oturur; nedbeler soluklaşır.")]),
   ("note", "Seanslar arasındaki bekleme, dokunun iyileşmesi kadar <strong>sonucun doğru değerlendirilmesi</strong> için de gereklidir. Şişlik varken yapılan planlama yanıltıcı olur.")]},

  {"id": "beklenti", "tag": "Beklenti", "h2": "Ne beklemeli?", "body": [
   ("ul", ["<strong>Beklenebilir:</strong> ağrı ve dokunma hassasiyetinde azalma",
           "<strong>Beklenebilir:</strong> bacak hacminde ve orantısızlıkta belirgin düzelme",
           "<strong>Beklenebilir:</strong> hareket kolaylığı ve kıyafet uyumunda iyileşme",
           "<strong>Beklenmemeli:</strong> hastalığın tamamen ortadan kalkması — lipödem kronik bir durumdur",
           "<strong>Beklenmemeli:</strong> bası giysisi ve konservatif tedavinin tamamen bırakılması"]),
   ("note", "Cerrahi, lipödem dokusunu azaltır ve şikâyetleri hafifletir. Hastalığı ortadan kaldırmaz. Ameliyat sonrası konservatif tedavi ve takip devam eder — bu bir başarısızlık göstergesi değil, tedavinin tasarımının parçasıdır.")]}],

 "faqs": [
  ("Lipödem ameliyatı kaç seans sürer?",
   "Tutulan bölgenin genişliğine göre genellikle 2-4 seans planlanır. Yalnızca sınırlı bir bölge etkilenmişse tek seans yeterli olabilir. Kesin sayı, muayene ve planlama sonrası belirlenir."),
  ("Seanslar arasında ne kadar beklenir?",
   "Genellikle 2-3 ay. Bu süre hem dokunun iyileşmesi hem de sonucun doğru değerlendirilebilmesi için gereklidir. Şişlik devam ederken yapılan planlama yanıltıcı olur."),
  ("Hepsini tek seansta yaptırabilir miyim?",
   "Güvenli değildir. Bir seansta çıkarılabilecek doku ve sıvı hacminin sınırı vardır; bu sınırın aşılması sıvı dengesi ve kanama açısından ciddi riskler doğurur. Aşamalı planlama bir tercih değil, güvenlik gereğidir."),
  ("Ameliyattan sonra kilo alırsam ne olur?",
   "Çıkarılan yağ hücreleri geri gelmez, ancak kalan hücreler kilo alımıyla büyüyebilir. Bu nedenle ameliyat sonrası kilo yönetimi sonucun korunması açısından önemlidir."),
  ("Ameliyat sonrası bası giysisi kullanmaya devam edecek miyim?",
   "Evet. Ameliyat sonrası dönemde bası giysisi iyileşmenin önemli bir parçasıdır. Uzun vadede kullanım gerekliliğini cerrahınız ve takip eden hekiminiz birlikte değerlendirir."),
  ("Ameliyat lenfödeme yol açar mı?",
   "Lenfatik kanalları koruyan tekniklerle çalışıldığında bu risk düşüktür. Agresif ve lenfatik yönü gözetmeyen bir çalışma ise riski artırır. Bu, teknik seçiminin neden önemli olduğunu gösteren en açık örnektir.")]},

# ------------------------------------------------------------------ 8
{"slug": "lipodem-kollarda-gorulur-mu", "sources": KAYNAK,
 "date": "2026-10-16",
 "cat": "Lipödem",
 "title": "Lipödem Kollarda Görülür mü? Kol Tutulumu ve Bulguları",
 "ogtitle": "Lipödem kollarda da olur mu?",
 "desc": "Lipödem hastalarının önemli bir bölümünde kollar da tutulur. Kol lipödeminin bulguları, lenfödemden ayrımı ve tedavi yaklaşımı.",
 "h1": "Lipödem kollarda görülür mü?",
 "lead": "Evet. Lipödem denince akla bacaklar gelir, ancak hastaların <strong>önemli bir bölümünde kollar da tutulur</strong>. Bulgular bacaktakinin aynısıdır: iki kolda <strong>simetrik hacim artışı</strong>, <strong>dokunma hassasiyeti</strong>, <strong>kolay morarma</strong> ve en tipik olarak şişliğin <strong>bileklerde bitmesi</strong> — eller normal görünür. Kol tutulumu sıklıkla gözden kaçar, çünkü hasta da hekim de dikkatini bacaklara yöneltir.",
 "watopic": "kollarda lipödem değerlendirmesi",
 "related": ["lipodem-belirtileri", "lipodem", "kol-uyluk-germe"],
 "sections": [
  {"id": "bulgular", "tag": "Bulgular", "h2": "Kol lipödeminde ne görülür?", "body": [
   ("ul", ["İki kolda <strong>simetrik</strong> hacim artışı",
           "Özellikle kolun üst yarısında belirginleşen dolgunluk",
           "Şişliğin <strong>bilekte bitmesi</strong>; el sırtı ve parmaklar normal",
           "Dokunmakla ağrı ve hassasiyet",
           "Çarpmadan oluşan morluklar",
           "Kolları kaldırırken ağırlık hissi",
           "Üst beden kıyafetlerinde kol bölgesinin dar gelmesi"]),
   ("note", "Bacak tutulumu olan her hastada kol muayenesi de yapılmalıdır. Kol tutulumu hafif olduğunda hasta bunu \"kolum kalın\" diye geçiştirir ve tabloya dahil etmez.")]},

  {"id": "ayrim", "tag": "Ayrım", "h2": "Kol lenfödeminden nasıl ayrılır?", "body": [
   "Kolda şişliğin en bilinen nedeni lenfödemdir — özellikle meme kanseri tedavisi sonrasında. İkisinin ayrımı nettir.",
   ("table", ["", "Kol lipödemi", "Kol lenfödemi"],
    [["Taraf", "İki kol simetrik", "Genellikle tek kol"],
     ["El ve parmaklar", "Normal", "Şişlik ele ve parmaklara uzanır"],
     ["Ağrı", "Dokunma hassasiyeti tipik", "Ağırlık hissi ön planda"],
     ["Morarma", "Sık", "Beklenmez"],
     ["Öykü", "Hormonal dönemlerle başlar", "Ameliyat, ışın tedavisi ya da enfeksiyon öyküsü"],
     ["Stemmer bulgusu", "Negatif", "Pozitif olabilir"]]),
   ("note", "<strong>Tek kolda, meme ameliyatı ya da ışın tedavisi sonrası ortaya çıkan şişlik lipödem değildir</strong> ve lenfödem açısından değerlendirilmelidir.")]},

  {"id": "birlikte", "tag": "Birlikte", "h2": "İkisi bir arada olabilir mi?", "body": [
   "Olabilir. Uzun süren ve ilerleyen lipödemde, zamanla lenfatik dolaşım da etkilenebilir; bu tabloya <strong>lipo-lenfödem</strong> denir.",
   ("ul", ["Şişlik bilek sınırını aşıp ele doğru uzamaya başlar",
           "Deride sertleşme ve kalınlaşma görülebilir",
           "Ödem, gece dinlenmeyle eskisi kadar gerilemez",
           "Tedavi planına ödem yönetimi eklenir"]),
   ("note", "Bilek sınırının kaybolması, lipödemin ilerlediğine ve lenfatik bileşenin eklendiğine işaret eden önemli bir bulgudur. Takipte özellikle izlenmesi gerekir.")]},

  {"id": "tedavi", "tag": "Tedavi", "h2": "Kol tutulumunda tedavi", "body": [
   ("h3", "Konservatif tedavi"),
   "Kol için üretilen bası giysileri, egzersiz ve gerektiğinde manuel lenf drenajı ilk basamaktır. Kol giysilerinde doğru ölçü, bacaktakinden daha kritiktir; yanlış ölçü el sırtında ödem oluşturabilir.",
   ("h3", "Cerrahi"),
   "Şikâyetler konservatif tedaviye rağmen sürüyorsa, kol lipödemi için de hacim azaltıcı cerrahi planlanabilir. Kolda deri toparlanması bacağa göre farklı seyrettiği için, bazı hastalarda deri fazlalığının giderilmesi de gündeme gelebilir.",
   ("ul", ["Kol cerrahisi genellikle bacak seanslarıyla birlikte değil, ayrı planlanır",
           "Lenfatik kanalların yoğun olduğu bölgelerde koruyucu teknik kullanımı önemlidir",
           "Ameliyat sonrası bası giysisi ve kol egzersizleri sürecin parçasıdır"]),
   ("note", "Kolda cerrahi kararı, bacaktan bağımsız verilir. Bacakta ameliyat olmuş olmak, kolda da ameliyat gerektiği anlamına gelmez.")]}],

 "faqs": [
  ("Lipödem kollarda ne sıklıkla görülür?",
   "Lipödemli hastaların önemli bir bölümünde kol tutulumu bildirilmektedir. Bacak tutulumu kadar belirgin olmadığı için sıklıkla gözden kaçar; bu nedenle bacak tanısı konan her hastada kolların da değerlendirilmesi önerilir."),
  ("Kollarımdaki şişlik lipödem mi lenfödem mi?",
   "İki kolda simetrik, eller normal, dokunmakla ağrılı ve kolay morarıyorsa lipödem düşünülür. Tek kolda, el ve parmaklara uzanan, ameliyat ya da ışın tedavisi öyküsü bulunan şişlik ise lenfödemi düşündürür."),
  ("Kol lipödemi için egzersiz yapabilir miyim?",
   "Evet. Kol egzersizleri dolaşımı destekler ve ağırlık hissini azaltır. Hafif direnç çalışması kolları kalınlaştırmaz; kas gücü artışı eklem ve omuz sağlığına katkı sağlar."),
  ("Kol için bası giysisi kullanılır mı?",
   "Kullanılır. Kol için üretilen bası giysileri mevcuttur ve ölçüye göre seçilmelidir. Yanlış ölçüdeki bir kol giysisi, bilekte boğum yaparak el sırtında ödeme yol açabilir; bu nedenle ölçü alımı önemlidir."),
  ("Kol ve bacak aynı ameliyatta yapılabilir mi?",
   "Genellikle ayrı seanslarda planlanır. Bir seansta güvenle çalışılabilecek alan ve çıkarılabilecek hacim sınırlıdır. Planlama, güvenlik sınırları gözetilerek yapılır."),
  ("Kollarımda lipödem varsa bacaklarımda da olur mu?",
   "Lipödem tipik olarak bacaklarda başlar; izole kol tutulumu nadirdir. Kollarında bulgu olan bir hastada bacakların da değerlendirilmesi gerekir.")]},
]
