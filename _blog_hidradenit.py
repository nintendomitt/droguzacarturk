# -*- coding: utf-8 -*-
"""
Blog — hidradenitis suppurativa kumesi (13 yazi).
Yayin: 17-29 Eylul 2026, gunde 1.

KAPSAM SINIRI: Erken evre (Hurley 1) dermatolojinin alanidir. Bu kumedeki
yazilar hastayi dogru brimse yonlendirir; cerrahi kisim yalnizca ileri
evre icin anlatilir. Fiyat, once/sonra gorseli, garanti vaadi yoktur.
"""

SRC_SP = ("Hidradenitis Suppurativa — StatPearls, NCBI Bookshelf",
          "https://www.ncbi.nlm.nih.gov/books/NBK534867/")
SRC_AAD = ("Hidradenitis suppurativa: Overview — American Academy of Dermatology",
           "https://www.aad.org/public/diseases/a-z/hidradenitis-suppurativa-overview")
KAYNAK = [SRC_SP, SRC_AAD]

BLOG_HIDRADENIT = [

# ------------------------------------------------------------------ 1
{"slug": "hidradenit-nedir", "sources": KAYNAK,
 "date": "2026-09-17",
 "cat": "Hidradenit",
 "title": "Hidradenit Nedir? Koltuk Altı ve Kasıkta Tekrarlayan Çıban",
 "ogtitle": "Hidradenit nedir, neden tekrar eder?",
 "desc": "Hidradenit, koltuk altı ve kasıkta tekrarlayan ağrılı şişlik ve akıntıyla giden kronik bir deri hastalığıdır. Neden tekrar eder, ne zaman cerrahi gerekir?",
 "h1": "Hidradenit nedir?",
 "lead": "Hidradenit — tam adıyla <strong>hidradenitis suppurativa</strong> — koltuk altı, kasık ve göğüs altında tekrar tekrar ortaya çıkan ağrılı şişlikler, apseler ve akıntılı kanallarla giden <strong>kronik bir deri hastalığıdır</strong>. Halk arasında \"geçmeyen koltuk altı çıbanı\" denen tablo çoğu zaman budur. Sıradan bir çıban değildir: her boşaltmadan sonra aynı yere geri döner, çünkü sorun iltihabın kendisi değil, deri altında kalan kanallardır.",
 "watopic": "hidradenit değerlendirmesi",
 "related": ["hidradenit"],
 "sections": [
  {"id": "nedir", "tag": "Tanım", "h2": "Hidradenit tam olarak ne demek?", "body": [
   "Hidradenit, tıp literatüründe <strong>hidradenitis suppurativa</strong> ya da <strong>akne inversa</strong> olarak geçer. Uzun yıllar \"ter bezi iltihabı\" diye anlatıldı, ancak bugün hastalığın ter bezlerinden değil <strong>kıl folikülünün tıkanmasından</strong> başladığı biliniyor.",
   "Tıkanan folikül şişer, iltihaplanır ve açılır. İyileşirken deri altında bir tünel bırakır. Bu tünellere <strong>sinüs traktı</strong> denir. Zamanla tüneller birbirine bağlanır, akıntı yapar ve her alevlenmede biraz daha nedbe dokusu birikir.",
   ("note", "<strong>Hastalığın mantığı tek cümlede:</strong> sorun o anki iltihap değil, deri altında kalıcı hale gelmiş kanal ağıdır. Bu yüzden iltihabı boşaltmak bugünün ağrısını dindirir ama hastalığı durdurmaz."),
   ("h3", "En sık tutulan bölgeler"),
   ("ul", ["Koltuk altları",
           "Kasık ve genital bölge",
           "Göğüs altı ve göğüsler arası",
           "Kalça ve makat çevresi",
           "Ense ve bel"])]},

  {"id": "kim", "tag": "Kimlerde", "h2": "Kimlerde daha sık görülür?", "body": [
   "Hidradenit genellikle <strong>ergenlikten sonra</strong> başlar ve yirmili-otuzlu yaşlarda en yoğun seyreder. Kadınlarda erkeklere göre daha sık görülür.",
   ("ul", ["<strong>Aile öyküsü:</strong> hastaların bir bölümünde ailede benzer tablo vardır",
           "<strong>Sigara:</strong> hem hastalığın seyrini hem yara iyileşmesini belirgin şekilde kötüleştirir",
           "<strong>Fazla kilo:</strong> sürtünen ve nemli kalan kıvrımlar alevlenmeyi artırır",
           "<strong>Hormonal dalgalanmalar:</strong> bazı hastalarda adet döngüsüyle ilişkili alevlenme olur"]),
   ("note", "Bu etkenlerin hiçbiri \"hastanın suçu\" değildir. Hidradenit hijyen eksikliğinden olmaz — bu, hastaların en sık maruz kaldığı ve en yanlış olan yakıştırmadır.")]},

  {"id": "seyir", "tag": "Seyir", "h2": "Neden hep aynı yere geri dönüyor?", "body": [
   "Çünkü apse boşaltıldığında içerideki irin çıkar, ama <strong>onu üreten kanal ağı ve etkilenmiş ter bezi bölgesi yerinde kalır</strong>. Birkaç hafta ya da ay sonra aynı kanal yeniden dolar.",
   ("steps", [
    ("İLK DÖNEM", "Tek tük, sivilceye benzeyen ağrılı şişlikler. Kendiliğinden geçebilir. Bu evrede ilaç tedavisi çoğu zaman yeterlidir."),
    ("TEKRARLAMA", "Aynı bölgede yılda birkaç kez alevlenme. Deri altında ilk tüneller oluşur, ilk nedbeler görünür."),
    ("KANAL AĞI", "Tüneller birleşir, sürekli akıntı başlar. Bölge sertleşir, hareket kısıtlanır."),
    ("İLERİ TABLO", "Geniş bir alan boyunca birbirine bağlı kanallar ve yaygın nedbe. Bu aşamada ilaç tek başına yetmez.")]),
   "Bu ilerleyiş herkeste aynı hızda olmaz. Bazı hastalarda yıllarca ilk dönemde kalır; bazılarında birkaç yıl içinde ileri tabloya ulaşır."]},

  {"id": "ne-yapmali", "tag": "Yol haritası", "h2": "Ne yapmak gerekir?", "body": [
   "İlk adım <strong>doğru tanı ve evrelemedir</strong>. Hidradenit, sıradan apse, kist ve fronkülden ayrılmalıdır — çünkü tedavileri farklıdır.",
   ("h3", "Erken evrede"),
   "Antibiyotikler, hormonal tedaviler ve gerektiğinde biyolojik ilaçlar hastalığı kontrol altında tutabilir. <strong>Bu dönem dermatolojinin alanıdır</strong> ve cerrahi gerekmeyebilir.",
   ("h3", "İleri evrede"),
   "Kalıcı kanallar ve nedbe oluştuysa, bölgenin tamamının çıkarılıp <strong>flep ya da greft ile onarılması</strong> gerekir. Plastik ve rekonstrüktif cerrahinin devreye girdiği yer burasıdır.",
   ("note", "Hidradenitte en sık yapılan hata, her apsenin ayrı ayrı boşaltılmasıdır. Tekrarlayan drenaj bir tedavi yöntemi değildir; hastalığı yıllarca aynı noktada tutar.")]}],

 "faqs": [
  ("Hidradenit ile normal çıban aynı şey mi?",
   "Değil. Normal çıban (fronkül) tek seferlik bir folikül enfeksiyonudur, tedaviyle geçer ve genellikle tekrarlamaz. Hidradenit ise kronik bir hastalıktır; aynı bölgede tekrar tekrar ortaya çıkar, deri altında kalıcı kanallar ve nedbe bırakır."),
  ("Hidradenit hijyen eksikliğinden mi olur?",
   "Hayır. Hidradenit temizlikle ilgili bir hastalık değildir; kıl folikülünün tıkanmasıyla başlayan ve bağışıklık sisteminin de rol aldığı kronik bir süreçtir. Aşırı yıkama ve sert antiseptikler deriyi tahriş ederek tabloyu kötüleştirebilir."),
  ("Hangi doktora gitmeliyim?",
   "Önce dermatoloji. Erken ve orta evrede ilaç tedavisi çoğu hastada yeterli olur. Deri altında kalıcı kanallar, sürekli akıntı ve sertleşmiş nedbe varsa plastik ve rekonstrüktif cerrahi devreye girer. En iyi sonuç iki branşın birlikte çalışmasıyla alınır."),
  ("Hidradenit geçer mi?",
   "Kronik bir hastalıktır, yani tamamen ortadan kalkacağının garantisi verilemez. Ancak erken evrede ilaçla kontrol altına alınabilir; ileri evrede etkilenmiş bölgenin tamamen çıkarılmasıyla o bölgedeki hastalık durdurulur. \"Kesin şifa\" vaat eden yaklaşımlara temkinli yaklaşın."),
  ("Hidradenit kanser yapar mı?",
   "Hidradenitin kendisi kanser değildir. Çok uzun yıllar tedavi edilmeden süren, sürekli akıntılı ve nedbeli tablolarda nadiren deri kanseri gelişebildiği bildirilmiştir. Bu, hastalığı yıllarca kontrolsüz bırakmamak için bir nedendir — panik nedeni değil."),
  ("Sigarayı bırakmam gerçekten fark yaratır mı?",
   "Evet, hidradenitte sigaranın etkisi net biçimde gösterilmiştir. Hem alevlenme sıklığını artırır hem de ameliyat gerekirse yara iyileşmesini bozar. Sigarayı bırakmak, tedavinin yardımcı bir parçası değil, doğrudan bir parçasıdır.")]},

# ------------------------------------------------------------------ 2
{"slug": "koltuk-altinda-tekrarlayan-ciban", "sources": KAYNAK,
 "date": "2026-09-18",
 "cat": "Hidradenit",
 "title": "Koltuk Altında Tekrarlayan Çıban: Ne Zaman Hidradenittir?",
 "ogtitle": "Koltuk altındaki çıban hep aynı yere dönüyorsa",
 "desc": "Koltuk altındaki çıban boşaltılıyor ama birkaç ay sonra aynı yere dönüyorsa, bu sıradan bir apse değil hidradenit olabilir. Ayırt edici bulgular.",
 "h1": "Koltuk altında tekrarlayan çıban",
 "lead": "Koltuk altındaki şişlik boşaltılıyor, birkaç hafta rahatlıyorsunuz, sonra <strong>aynı noktada yeniden başlıyor</strong>. Bu döngü iki-üç kez tekrarladıysa artık sıradan bir çıbandan söz etmiyoruz. Tekrarlayan koltuk altı apsesinin en sık nedeni <strong>hidradenitis suppurativa</strong>dır ve bu hastalıkta tedavi mantığı tamamen farklıdır.",
 "watopic": "tekrarlayan koltuk altı şişliği",
 "related": ["hidradenit"],
 "sections": [
  {"id": "ayrim", "tag": "Ayrım", "h2": "Sıradan çıban mı, hidradenit mi?", "body": [
   "İkisi ilk bakışta benzer görünür: ağrılı, kırmızı, şiş bir kabartı. Ayrım <strong>zaman içindeki davranışta</strong> ortaya çıkar.",
   ("table", ["", "Sıradan çıban (fronkül)", "Hidradenit"],
    [["Tekrarlama", "Genellikle tek seferlik", "Aynı bölgede tekrar tekrar"],
     ["Yerleşim", "Vücudun her yerinde", "Koltuk altı, kasık, göğüs altı"],
     ["Deri altı kanal", "Yok", "Zamanla oluşur"],
     ["Nedbe", "Genelde iz bırakmaz", "Sertleşmiş nedbe birikir"],
     ["Akıntı", "Boşalınca biter", "Aralıklarla sürer"],
     ["Tedavi", "Antibiyotik, drenaj", "Kronik hastalık yönetimi"]]),
   ("note", "<strong>Pratik ölçüt:</strong> aynı bölgede bir yıl içinde iki veya daha fazla alevlenme olduysa, hidradenit ihtimali ciddi biçimde düşünülmelidir.")]},

  {"id": "bulgular", "tag": "Bulgular", "h2": "Hidradenite işaret eden bulgular", "body": [
   ("ul", ["Aynı bölgede <strong>tekrarlayan</strong> ağrılı şişlikler",
           "Deri altında elle hissedilen <strong>sert bantlar</strong> — birbirine bağlanan kanallar",
           "Birbirine yakın, siyah uçlu <strong>ikili komedonlar</strong> (\"tombstone\" görünümü)",
           "Aralıklı, kötü kokulu akıntı",
           "Gömük, çekintili nedbeler",
           "Kolu kaldırırken takılma ya da gerginlik hissi"]),
   "Bu bulguların hepsinin birden olması gerekmez. Özellikle <strong>ikili komedon</strong> ve <strong>deri altı sert bant</strong>, hidradenit için oldukça tipiktir."]},

  {"id": "yanlis", "tag": "Sık hata", "h2": "Neden boşaltmak yetmiyor?", "body": [
   "Apsenin boşaltılması içerideki basıncı ve ağrıyı azaltır — bu doğru ve bazen gereklidir. Ama boşaltma, <strong>iltihabı üreten yapıyı</strong> ortadan kaldırmaz.",
   "Deri altındaki kanal ağı ve etkilenmiş folikül bölgesi yerinde kaldığı sürece, süreç yeniden başlar. Bu yüzden bazı hastalar yıllar içinde onlarca kez drenaj olur ve her seferinde \"geçti\" sanır.",
   ("note", "Her drenaj biraz daha nedbe bırakır. Uzun vadede tekrarlayan drenaj, ileride yapılacak onarımı da zorlaştırır. Tekrarlayan tabloda asıl soru \"bunu nasıl boşaltırız\" değil, \"bu neden tekrar ediyor\" olmalıdır.")]},

  {"id": "ne-zaman", "tag": "Başvuru", "h2": "Ne zaman hekime gitmeli?", "body": [
   ("ul", ["Aynı bölgede <strong>ikinci kez</strong> alevlenme olduğunda",
           "Deri altında sertlik ya da bant hissedildiğinde",
           "Akıntı aralıklarla sürüyorsa",
           "Kol hareketi kısıtlanmaya başladıysa",
           "Ateş, yaygın kızarıklık ve genel halsizlik varsa — bu acil değerlendirme gerektirir"]),
   "İlk başvuru adresi <strong>dermatolojidir</strong>. Erken evrede ilaç tedavisi çoğu hastada yeterlidir ve cerrahi gerekmeyebilir. Kalıcı kanal ve nedbe oluştuysa plastik cerrahi devreye girer."]},
 ],

 "faqs": [
  ("Koltuk altındaki çıban kaç kez tekrarlarsa hidradenit sayılır?",
   "Yaygın kullanılan ölçüt, aynı bölgede altı ay içinde iki veya daha fazla alevlenmedir. Tek bir atak hidradenit tanısı koydurmaz; tekrarlama ve deri altı kanal oluşumu tanının temelidir."),
  ("Deodorant ya da tıraş hidradenite yol açar mı?",
   "Hastalığın nedeni değildir. Ancak tahriş eden ürünler ve derin tıraş, mevcut hastalıkta alevlenmeyi tetikleyebilir. Bölgeyi tahriş etmeyen, alkolsüz ürünler tercih edilmesi genellikle önerilir."),
  ("Antibiyotik kullanıyorum ama yine dönüyor, neden?",
   "Antibiyotik o anki iltihabı baskılar; deri altındaki kanal ağını ortadan kaldırmaz. Erken evrede uzun süreli tedavi şemaları işe yarayabilir, ancak kalıcı kanal oluşmuş bölgede tek başına kalıcı çözüm sağlamaz."),
  ("Ameliyat olmadan kurtulmak mümkün mü?",
   "Erken evrede evet — birçok hasta ilaç tedavisiyle kontrol altına alınır ve ameliyat gerekmez. Geniş kanal ağı ve sertleşmiş nedbe oluştuysa, o bölge için cerrahi dışında kalıcı bir seçenek yoktur."),
  ("Hidradenit başkasına bulaşır mı?",
   "Hayır. Akıntı ve iltihap bulaşıcı bir enfeksiyon izlenimi verse de hidradenit bulaşıcı değildir. Ortak havlu, kıyafet ya da temasla geçmez.")]},

# ------------------------------------------------------------------ 3
{"slug": "hidradenit-belirtileri", "sources": KAYNAK,
 "date": "2026-09-19",
 "cat": "Hidradenit",
 "title": "Hidradenit Belirtileri: İlk Bulgular ve Uyarı İşaretleri",
 "ogtitle": "Hidradenit belirtileri nelerdir?",
 "desc": "Hidradenitin ilk belirtisi koltuk altı veya kasıkta tekrarlayan ağrılı şişliktir. Deri altı sert bant, ikili komedon ve akıntı tanıyı güçlendirir.",
 "h1": "Hidradenit belirtileri",
 "lead": "Hidradenitin ilk belirtisi genellikle koltuk altı ya da kasıkta beliren, <strong>bezelye büyüklüğünde, ağrılı ve derin bir şişliktir</strong>. Sivilceye benzer ama daha derindedir ve başı yoktur. Haftalar içinde kendiliğinden gerileyebilir; asıl uyarı işareti, aynı bölgede <strong>yeniden ortaya çıkmasıdır</strong>.",
 "watopic": "hidradenit belirtileri değerlendirmesi",
 "related": ["hidradenit"],
 "sections": [
  {"id": "erken", "tag": "Erken bulgular", "h2": "İlk dönemde ne görülür?", "body": [
   ("ul", ["Deri altında, dokunmakla ağrıyan <strong>derin şişlik</strong>",
           "Şişliğin üzerinde kızarıklık ve ısı artışı",
           "Başı olmayan, sıkmakla açılmayan kabartı",
           "Günler içinde büyüyüp gerileyen seyir",
           "Bölgede zonklama ya da yanma hissi"]),
   ("note", "Bu dönemde hastaların çoğu \"iltihaplı sivilce\" ya da \"çıban\" diye düşünür ve hekime gitmez. Oysa tanının en değerli olduğu dönem tam olarak burasıdır — ilaç tedavisiyle hastalık kontrol altına alınabilir ve kanal oluşumu önlenebilir.")]},

  {"id": "tipik", "tag": "Tipik bulgular", "h2": "Hidradenite özgü işaretler", "body": [
   "Aşağıdaki bulgular, tabloyu sıradan bir apseden ayıran işaretlerdir.",
   ("h3", "İkili komedon"),
   "Yan yana duran, siyah uçlu iki açıklık. Tek bir noktadan çıkan çift siyah nokta görünümü hidradenit için oldukça tipiktir.",
   ("h3", "Deri altı sert bant"),
   "Parmakla bastırıldığında hissedilen, cilt altında uzanan sert şerit. Bu, birleşmiş kanalların (sinüs traktı) elle alınan karşılığıdır.",
   ("h3", "Aralıklı akıntı"),
   "Kendiliğinden açılan noktalardan gelen, berrak ya da irinli, çoğu zaman kokulu akıntı. Kapanır, bir süre sonra yeniden başlar.",
   ("h3", "Çekintili nedbe"),
   "İyileşen bölgede oluşan, içe doğru çekilmiş, sert iz. Zamanla bölgenin esnekliğini azaltır."]},

  {"id": "ilerleyen", "tag": "İleri bulgular", "h2": "İleri evrede ne değişir?", "body": [
   ("ul", ["Alevlenmeler sıklaşır, aralar kısalır",
           "Birden fazla bölge aynı anda tutulur",
           "Akıntı sürekli hale gelir, günlük ped kullanımı gerekebilir",
           "Bölge sertleşir; kol ya da bacak hareketi kısıtlanır",
           "Ağrı arka planda sürekli hale gelir",
           "Uyku, iş ve sosyal yaşam etkilenir"]),
   ("note", "Hidradenitin en az konuşulan tarafı ruhsal yüküdür. Sürekli akıntı, koku kaygısı ve görünür nedbe, hastaların kendini geri çekmesine yol açar. Bu, hastalığın \"yan etkisi\" değil, doğrudan bir parçasıdır ve tedavi planında yer almalıdır.")]},

  {"id": "acil", "tag": "Uyarı", "h2": "Hangi durumda beklememeli?", "body": [
   ("ul", ["<strong>Ateş</strong> ve titreme",
           "Şişliğin etrafında hızla yayılan kızarıklık",
           "Belirgin ısı artışı ve şiddetli ağrı",
           "Genel halsizlik, kendini kötü hissetme"]),
   "Bu tablo, yayılan bir deri enfeksiyonuna (selülit) işaret edebilir ve <strong>gecikmeden değerlendirilmelidir</strong>. Hidradenitin olağan alevlenmesi genellikle ateş yapmaz."]},
 ],

 "faqs": [
  ("Hidradenitin ilk belirtisi nedir?",
   "Genellikle koltuk altı ya da kasıkta beliren, başı olmayan, dokunmakla ağrıyan derin bir şişliktir. Sivilceden farkı, daha derin olması ve sıkmakla açılmamasıdır. Aynı bölgede tekrarlaması en önemli uyarı işaretidir."),
  ("Hidradenit ağrılı mıdır?",
   "Alevlenme dönemlerinde belirgin ağrı olur; hastaların çoğu zonklayıcı bir ağrı tarif eder. Sessiz dönemlerde ağrı azalır ya da kaybolur. İleri evrede bölgede sürekli bir rahatsızlık hissi yerleşebilir."),
  ("Akıntının kokması normal mi?",
   "Hidradenitte akıntının kokulu olması sık görülür ve hijyen eksikliğinden kaynaklanmaz. Kokunun kaynağı, kapalı kanallarda biriken salgı ve bakteri karışımıdır. Bu, hastaların en çok utandığı ama en yaygın bulgulardan biridir."),
  ("Belirtiler kendiliğinden geçer mi?",
   "Tek bir alevlenme kendiliğinden gerileyebilir. Ancak hastalık kendiliğinden ortadan kalkmaz; sessiz dönemlerin ardından yeniden alevlenir. Bu dalgalı seyir, hastaların tanıyı geciktirmesinin başlıca nedenidir."),
  ("Hangi bölgelerde görülür?",
   "En sık koltuk altları, kasık ve genital bölge, göğüs altı, kalça ve makat çevresi. Bu bölgelerin ortak özelliği, deri kıvrımı olmaları ve sürtünmeye maruz kalmalarıdır."),
  ("Belirtiler için hangi bölüme başvurmalıyım?",
   "Dermatolojiye. Tanı, evreleme ve ilaç tedavisi bu branşın alanıdır. Deri altında kalıcı kanallar ve nedbe oluştuysa, onarım için plastik ve rekonstrüktif cerrahi değerlendirmesi gerekir.")]},

# ------------------------------------------------------------------ 4
{"slug": "hidradenit-hangi-doktor-bakar", "sources": KAYNAK,
 "date": "2026-09-20",
 "cat": "Hasta Rehberi",
 "title": "Hidradenite Hangi Doktor Bakar? Dermatoloji mi, Cerrahi mi",
 "ogtitle": "Hidradenite hangi bölüm bakar?",
 "desc": "Hidradenitte ilk adres dermatolojidir. Deri altında kalıcı kanal ve nedbe oluştuysa plastik ve rekonstrüktif cerrahi devreye girer. Hangi durumda hangisi?",
 "h1": "Hidradenite hangi doktor bakar?",
 "lead": "Hidradenitte <strong>iki branş birlikte çalışır</strong>. İlk başvuru adresi <strong>dermatolojidir</strong>: tanı, evreleme ve ilaç tedavisi oradadır ve hastaların önemli bir bölümü bu aşamada kontrol altına alınır. Deri altında kalıcı kanallar, sürekli akıntı ve sertleşmiş nedbe oluştuysa <strong>plastik ve rekonstrüktif cerrahi</strong> devreye girer. Doğru sıra budur — tersi değil.",
 "watopic": "hidradenit için hangi bölüme başvuracağım",
 "related": ["hidradenit"],
 "sections": [
  {"id": "derma", "tag": "İlk adres", "h2": "Neden önce dermatoloji?", "body": [
   "Çünkü hidradenit her şeyden önce <strong>kronik bir deri hastalığıdır</strong>. Tanının konması, diğer hastalıklardan ayrılması ve evrelenmesi dermatolojinin işidir.",
   ("ul", ["Tanıyı koyar ve apse, kist, fronkül gibi tablolardan ayırır",
           "Hurley evrelemesini yapar — tedavi planı buna göre kurulur",
           "Antibiyotik, hormonal tedavi ve gerektiğinde biyolojik ilaç tedavisini yürütür",
           "Alevlenme sıklığını azaltacak günlük bakım düzenini kurar"]),
   ("note", "Hurley 1 ve birçok Hurley 2 hastasında ilaç tedavisi yeterlidir ve <strong>ameliyat hiç gerekmeyebilir</strong>. Cerrahiye erken koşmak, gereksiz nedbe anlamına gelir.")]},

  {"id": "cerrahi", "tag": "Ne zaman cerrahi", "h2": "Plastik cerrahi ne zaman devreye girer?", "body": [
   "İlaç tedavisi iltihabı baskılar ama <strong>oluşmuş kanalları ve nedbeyi geri döndürmez</strong>. Doku içinde kalıcı yapı oluştuysa, o yapının çıkarılması gerekir.",
   ("h3", "Cerrahiyi gündeme getiren bulgular"),
   ("ul", ["Deri altında elle hissedilen, birbirine bağlı kanal ağı",
           "Aylardır süren, kapanmayan akıntı",
           "Sertleşmiş, çekintili, geniş nedbe alanları",
           "İlaç tedavisine rağmen sıklaşan alevlenmeler",
           "Kol ya da bacak hareketini kısıtlayan doku sertliği"]),
   "Bu noktada yapılan işlem, apse boşaltmak değildir. <strong>Etkilenmiş bölgenin bütünüyle çıkarılması</strong> ve oluşan açıklığın flep ya da greftle onarılmasıdır.",
   ("note", "Koltuk altı ve kasık hareket eden bölgelerdir. Buradaki onarımın yalnızca yarayı kapatması yetmez — <strong>hareketi kısıtlamaması</strong> da gerekir. Flep seçiminin önemi buradan gelir.")]},

  {"id": "birlikte", "tag": "Birlikte çalışma", "h2": "İki branş nasıl birlikte yürür?", "body": [
   ("steps", [
    ("TANI VE EVRELEME", "Dermatoloji tanıyı koyar, Hurley evresini belirler, ilaç tedavisini başlatır."),
    ("YANITIN DEĞERLENDİRİLMESİ", "Tedaviye yanıt izlenir. Alevlenme sıklığı ve kanal oluşumu takip edilir."),
    ("CERRAHİ DEĞERLENDİRME", "Kalıcı yapı oluştuysa plastik cerrahi bölgeyi haritalar, çıkarma ve kapatma planını yapar."),
    ("AMELİYAT SONRASI", "Dermatoloji takibi devam eder. Cerrahi o bölgeyi durdurur, sistemik yatkınlığı ortadan kaldırmaz.")]),
   ("note", "Ameliyat sonrası dermatoloji takibinin kesilmesi sık yapılan bir hatadır. Hidradenit bölgesel bir sorun gibi görünse de sistemik bir yatkınlıkla ilişkilidir; başka bir bölgede yeniden başlayabilir.")]},

  {"id": "diger", "tag": "Diğer branşlar", "h2": "Başka hangi branşlar işin içinde olabilir?", "body": [
   ("ul", ["<strong>Genel cerrahi:</strong> makat çevresi tutulumunda, fistül ayrımı gerektiğinde",
           "<strong>Endokrinoloji:</strong> hormonal düzensizlik ya da metabolik sendrom eşlik ediyorsa",
           "<strong>Romatoloji:</strong> eşlik eden eklem tutulumu varsa",
           "<strong>Psikiyatri ve psikolojik destek:</strong> kronik ağrı, sosyal geri çekilme ve beden algısı için"]),
   "Bu branşların hepsi her hastada gerekmez. Belirleyici olan, hastalığın hangi sistemleri etkilediğidir."]},
 ],

 "faqs": [
  ("Hidradenit için ilk olarak hangi bölüme gitmeliyim?",
   "Dermatolojiye. Tanının konması, hastalığın evrelenmesi ve ilaç tedavisinin yürütülmesi bu branşın alanıdır. Erken ve orta evrede hastaların önemli bir bölümü cerrahiye gerek kalmadan kontrol altına alınır."),
  ("Doğrudan cerraha gitsem olmaz mı?",
   "Erken evrede önerilmez. Kalıcı kanal oluşmamış bir bölgede cerrahi, gereksiz nedbe bırakır ve hastalığın sistemik seyrini değiştirmez. Cerrahi, ilaç tedavisinin yetmediği ve dokuda kalıcı yapı oluşmuş durumlar için anlamlıdır."),
  ("Plastik cerrahi mi genel cerrahi mi?",
   "Geniş çıkarma sonrası oluşan açıklığın flep ya da greftle kapatılması gerekiyorsa plastik ve rekonstrüktif cerrahi. Özellikle koltuk altı ve kasık gibi hareketli bölgelerde kapatma planı, sonucu belirleyen asıl adımdır. Makat çevresi tutulumunda genel cerrahi ile birlikte değerlendirme gerekebilir."),
  ("Devlet hastanesinde tedavi olabilir miyim?",
   "Hidradenit tedavisi hem dermatoloji hem plastik cerrahi kliniklerinde yürütülebilen bir tedavidir. Önemli olan kurumun adı değil, hastalığın doğru evrelenmesi ve tedavinin bu evreye uygun planlanmasıdır."),
  ("Tedavi ne kadar sürer?",
   "Hidradenit kronik bir hastalıktır; takip uzun sürelidir. İlaç tedavileri aylarla ölçülür. Cerrahi gerekiyorsa, bölge ve yöntem değişmekle birlikte iyileşme genellikle birkaç haftadan birkaç aya uzanır. Ameliyat sonrası dermatoloji takibi devam eder.")]},

# ------------------------------------------------------------------ 5
{"slug": "hidradenit-evreleri-hurley", "sources": KAYNAK,
 "date": "2026-09-21",
 "cat": "Hidradenit",
 "title": "Hidradenit Evreleri: Hurley 1, 2, 3 Nasıl Ayrılır",
 "ogtitle": "Hurley evreleri: hidradenit hangi aşamada?",
 "desc": "Hidradenit üç Hurley evresine ayrılır. Evre 1'de ilaç, evre 3'te cerrahi öne çıkar. Hangi evrede hangi tedavi, hangi bulgular hangi evreyi gösterir?",
 "h1": "Hidradenit evreleri (Hurley)",
 "lead": "Hidradenitte tedavi kararı <strong>evreye göre</strong> verilir. Kullanılan sistem <strong>Hurley evrelemesi</strong>dir ve üç basamaklıdır. Ayrımı yapan tek şey iltihabın şiddeti değil, <strong>deri altında kalıcı kanal (sinüs traktı) ve nedbe olup olmadığıdır</strong>. Evre 1'de ilaç öndedir; evre 3'te cerrahi kaçınılmaz hale gelir.",
 "watopic": "hidradenit evresinin belirlenmesi",
 "related": ["hidradenit"],
 "sections": [
  {"id": "tablo", "tag": "Evreleme", "h2": "Üç evre bir arada", "body": [
   ("table", ["Evre", "Bulgu", "Öne çıkan tedavi"],
    [["Hurley 1", "Tek tük apse; kanal ve nedbe yok", "İlaç tedavisi — dermatoloji"],
     ["Hurley 2", "Tekrarlayan apseler; ayrı ayrı kanal ve nedbe", "İlaç + sınırlı cerrahi"],
     ["Hurley 3", "Bölge boyunca birleşmiş kanal ağı", "Geniş çıkarma ve onarım"]]),
   ("note", "Evreler tek yönlü ilerlemez zorunlu olarak — erken tedaviyle birçok hasta yıllarca Hurley 1'de kalır. Evrenin yükselmesini engelleyen en güçlü etken, erken tanı ve düzenli takiptir.")]},

  {"id": "evre1", "tag": "Evre 1", "h2": "Hurley 1: tek tük apse", "body": [
   "Bir ya da birkaç ağrılı şişlik vardır. <strong>Deri altında kanal yoktur, belirgin nedbe yoktur.</strong> Alevlenmeler seyrektir ve kendiliğinden gerileyebilir.",
   ("ul", ["Tedavi ağırlıklı olarak ilaçla yürütülür",
           "Bölgesel ve gerektiğinde ağızdan antibiyotikler",
           "Kadın hastalarda hormonal tedavi seçenekleri",
           "Tahriş etmeyen günlük bakım düzeni",
           "Sigaranın bırakılması ve kilo yönetimi"]),
   ("note", "Bu evrede cerrahi genellikle gerekmez. Hastaların büyük bölümü doğru ilaç tedavisiyle kontrol altına alınır. <strong>Amaç, evrenin ilerlemesini durdurmaktır.</strong>")]},

  {"id": "evre2", "tag": "Evre 2", "h2": "Hurley 2: tekrarlayan apseler ve ilk kanallar", "body": [
   "Aynı bölgede tekrarlayan alevlenmeler vardır. Deri altında <strong>birbirinden ayrı</strong> kanallar ve nedbe alanları oluşmuştur, ancak bunlar henüz tüm bölgeyi kaplamaz.",
   ("ul", ["İlaç tedavisi sürer ve genellikle daha uzun süreli planlanır",
           "Biyolojik tedaviler bu evrede gündeme gelebilir",
           "Tek tek kanalların açılması (deroofing) gibi sınırlı cerrahi işlemler uygulanabilir",
           "Geniş çıkarma, yalnızca sınırlı bir alan sürekli sorun çıkarıyorsa düşünülür"]),
   ("note", "Hurley 2, tedavi kararının en tartışmalı olduğu evredir. Aynı hastada bir bölge ilaçla kontrol altına alınırken, başka bir bölge cerrahi gerektirebilir. Karar bölge bölge verilir.")]},

  {"id": "evre3", "tag": "Evre 3", "h2": "Hurley 3: birleşmiş kanal ağı", "body": [
   "Kanallar birbirine bağlanmış, bölgenin tamamı etkilenmiştir. Sürekli akıntı, yaygın nedbe ve hareket kısıtlılığı vardır.",
   "Bu evrede ilaç tedavisi iltihabı azaltabilir ama <strong>yapıyı geri döndüremez</strong>. Kalıcı çözüm, etkilenmiş bölgenin bütünüyle çıkarılması ve oluşan açıklığın onarılmasıdır.",
   ("h3", "Onarım seçenekleri"),
   ("ul", ["<strong>Lokal flep:</strong> komşu sağlıklı dokunun kaydırılması — hareketli bölgelerde tercih edilir",
           "<strong>Perforatör flep:</strong> geniş açıklıklarda, kendi damarıyla taşınan doku bloğu",
           "<strong>Deri grefti:</strong> çok geniş alanlarda; eklem üzerinde tek başına kullanıldığında kontraktür riski taşır",
           "<strong>İkincil iyileşme:</strong> yaranın kendiliğinden kapanmasının beklenmesi; uzun sürer, nedbe kalitesi düşüktür"]),
   ("note", "Hurley 3'te amaç nedbeyi küçültmek değil, hastalığı durdurmak ve bölgenin hareketini korumaktır. Çıkarma alanını küçük tutma çabası, hastalığın geride kalan dokuda sürmesi anlamına gelir.")]}],

 "faqs": [
  ("Hangi evrede olduğumu nasıl anlarım?",
   "Ayrımı yapan asıl bulgu, deri altında kalıcı kanal ve nedbe olup olmadığıdır. Bu, muayeneyle değerlendirilir. Tek tük apse ve iz yoksa Hurley 1; ayrı ayrı sert bantlar ve izler varsa Hurley 2; bölge boyunca birleşmiş kanal ağı varsa Hurley 3 düşünülür."),
  ("Evre geri döner mi?",
   "Oluşmuş kanal ve nedbe kendiliğinden kaybolmaz, yani evre geriye gitmez. Ancak tedaviyle alevlenme sıklığı azaltılabilir ve evrenin ilerlemesi durdurulabilir. Cerrahi ile çıkarılan bölgede hastalık durdurulmuş olur."),
  ("Hurley 1'de ameliyat gerekir mi?",
   "Genellikle gerekmez. Bu evrede ilaç tedavisi çoğu hastada yeterlidir ve gereksiz cerrahi, kalıcı iz bırakır. Cerrahi, dokuda kalıcı yapı oluştuğunda anlamlı hale gelir."),
  ("Hurley 3'te ilaç tedavisi işe yaramaz mı?",
   "Yaramaz demek doğru olmaz; ilaç tedavisi iltihabı azaltır, ameliyat öncesi bölgeyi sakinleştirir ve ameliyat sonrası yeni odakların çıkmasını geciktirir. Ancak oluşmuş kanal ağını ortadan kaldırmaz — bu yüzden tek başına yeterli olmaz."),
  ("Her bölgem aynı evrede mi olur?",
   "Hayır. Aynı hastada koltuk altı Hurley 1, kasık Hurley 3 olabilir. Bu yüzden tedavi kararı hasta için tek seferde değil, bölge bölge verilir.")]},

# ------------------------------------------------------------------ 6
{"slug": "hidradenit-neden-olur", "sources": KAYNAK,
 "date": "2026-09-22",
 "cat": "Hidradenit",
 "title": "Hidradenit Neden Olur? Ter Bezi Değil, Kıl Folikülü",
 "ogtitle": "Hidradenit neden olur?",
 "desc": "Hidradenit ter bezi iltihabı değildir. Kıl folikülünün tıkanmasıyla başlar; bağışıklık yanıtı, genetik yatkınlık, sigara ve hormonlar seyri belirler.",
 "h1": "Hidradenit neden olur?",
 "lead": "Hidradenit uzun yıllar \"ter bezi iltihabı\" olarak anlatıldı. Bugün bildiğimiz şu: hastalık ter bezinden değil, <strong>kıl folikülünün tıkanmasından</strong> başlar. Tıkanan folikül şişer, çevresine iltihap yayılır ve bağışıklık sisteminin aşırı yanıtıyla süreç kronikleşir. Genetik yatkınlık, sigara, hormonal dalgalanmalar ve kilo, bu sürecin <strong>hızını</strong> belirler — ama tek başına nedeni değildir.",
 "watopic": "hidradenit nedeni ve seyri",
 "related": ["hidradenit"],
 "sections": [
  {"id": "mekanizma", "tag": "Mekanizma", "h2": "Hastalık nasıl başlar?", "body": [
   ("steps", [
    ("TIKANMA", "Kıl folikülünün ağzı tıkanır. Foliküldeki salgı dışarı çıkamaz."),
    ("ŞİŞME VE PATLAMA", "Folikül genişler ve çevre dokuya açılır. İçerik dokuya yayılır."),
    ("BAĞIŞIKLIK YANITI", "Vücut bu içeriği yabancı olarak algılar; yoğun bir iltihap yanıtı başlar."),
    ("KANAL OLUŞUMU", "İyileşme sırasında deri altında tünel benzeri kanallar kalır. Her alevlenme bu ağı genişletir.")]),
   ("note", "Bu zincirin en kritik halkası <strong>bağışıklık yanıtıdır</strong>. Hidradenitte iltihap, mikroba karşı verilen olağan bir tepkiden daha güçlü ve daha uzun sürelidir. Biyolojik tedavilerin işe yaramasının nedeni de budur.")]},

  {"id": "etkenler", "tag": "Etkenler", "h2": "Seyri belirleyen etkenler", "body": [
   ("h3", "Genetik yatkınlık"),
   "Hastaların bir bölümünde ailede benzer tablo bulunur. Bu, hastalığın doğrudan kalıtsal olduğu anlamına gelmez; yatkınlığın aktarılabildiğini gösterir.",
   ("h3", "Sigara"),
   "Hidradenitle ilişkisi en güçlü gösterilmiş etkendir. Hem alevlenme sıklığını artırır hem de cerrahi gerekirse yara iyileşmesini bozar. Bırakmak tedavinin doğrudan bir parçasıdır.",
   ("h3", "Kilo ve sürtünme"),
   "Deri kıvrımlarında sürtünme ve nem, folikül tıkanmasını kolaylaştırır. Kilo vermek hastalığı ortadan kaldırmaz ama alevlenme sıklığını azaltabilir.",
   ("h3", "Hormonal dalgalanmalar"),
   "Bazı kadın hastalarda alevlenmeler adet döngüsüyle ilişkilidir. Hastalığın ergenlikten sonra başlaması da hormonal bir bileşene işaret eder.",
   ("note", "Bu etkenlerin hiçbiri hastanın \"yapmadığı bir şey\" değildir. Hidradenit temizlik, ihmal ya da irade meselesi değildir — bu yanlış inanç, hastaların hekime başvurmasını yıllarca geciktiriyor.")]},

  {"id": "yanlis", "tag": "Yanlış bilinen", "h2": "Doğru bilinen yanlışlar", "body": [
   ("ul", ["<strong>\"Ter bezi iltihabıdır\":</strong> hastalık kıl folikülünden başlar. Eski adlandırma yanlış bir zihinsel model kurmuştur.",
           "<strong>\"Hijyen eksikliğidir\":</strong> değildir. Aşırı yıkama ve sert antiseptikler deriyi tahriş ederek tabloyu kötüleştirebilir.",
           "<strong>\"Bulaşıcıdır\":</strong> değildir. Akıntı ve iltihap bulaşıcı bir enfeksiyon izlenimi verse de temasla geçmez.",
           "<strong>\"Boşaltınca geçer\":</strong> geçmez. Drenaj basıncı azaltır; kanal ağını ortadan kaldırmaz.",
           "<strong>\"Antibiyotik yetmiyorsa çare yok\":</strong> yanlış. İleri evrede cerrahi ile o bölgedeki hastalık durdurulabilir."]),
   ]},

  {"id": "eslik", "tag": "Eşlik edenler", "h2": "Hidradenite eşlik edebilen durumlar", "body": [
   "Hidradenit yalnızca deriyle sınırlı kalmayabilir. Bazı hastalarda başka sistemleri ilgilendiren durumlar birlikte görülür.",
   ("ul", ["Metabolik sendrom ve insülin direnci",
           "Polikistik over sendromu",
           "İnflamatuar bağırsak hastalıkları",
           "Eklem tutulumu",
           "Kronik ağrıya bağlı uyku bozukluğu ve depresif belirtiler"]),
   ("note", "Bunlar her hastada görülmez. Ancak tanı konduğunda genel bir değerlendirme yapılması, yalnızca deriye odaklanmaktan daha doğru bir yaklaşımdır.")]}],

 "faqs": [
  ("Hidradenit ter bezi iltihabı mı?",
   "Hayır. Eski adlandırma bu yönde olsa da hastalık kıl folikülünün tıkanmasıyla başlar. Ter bezleri süreçte ikincil olarak etkilenir. Bu ayrım önemlidir çünkü tedavi mantığını doğrudan değiştirir."),
  ("Hidradenit genetik mi?",
   "Hastaların bir bölümünde ailede benzer tablo bulunur, yani genetik yatkınlık rol oynar. Ancak ailede kimse yoksa da hastalık görülebilir. Yatkınlık tek başına hastalığı başlatmaz; başka etkenlerle birleşir."),
  ("Sigarayı bırakırsam hastalık geçer mi?",
   "Geçmesini beklemek doğru olmaz, ancak alevlenme sıklığının azalması sık görülür. Ayrıca cerrahi gerekirse yara iyileşmesini belirgin biçimde iyileştirir. Sigarayı bırakmak, tedavinin yardımcı değil doğrudan bir parçasıdır."),
  ("Kilo verirsem düzelir mi?",
   "Kilo vermek hastalığı ortadan kaldırmaz ama özellikle kasık ve göğüs altı tutulumunda sürtünme ve nemi azaltarak alevlenme sıklığını düşürebilir. Beklentiyi doğru kurmak gerekir: bu bir kontrol aracıdır, tedavi değil."),
  ("Beslenme hidradeniti etkiler mi?",
   "Bazı hastalar süt ürünleri ve yüksek glisemik indeksli besinlerle alevlenme tarif eder, ancak bu konuda kesin ve herkes için geçerli bir diyet önerisi yoktur. Beslenme düzenlemesi ilaç tedavisinin yerini almaz."),
  ("Stres hastalığı tetikler mi?",
   "Stresin doğrudan neden olduğu gösterilmemiştir, ancak birçok hasta yoğun stres dönemlerinde alevlenme bildirir. Kronik ağrı ve sosyal geri çekilme de stresi artırarak bir döngü kurabilir.")]},

# ------------------------------------------------------------------ 7
{"slug": "hidradenit-bulasici-mi", "sources": KAYNAK,
 "date": "2026-09-23",
 "cat": "Hidradenit",
 "title": "Hidradenit Bulaşıcı mı? Akıntı ve Temas Konusunda Netlik",
 "ogtitle": "Hidradenit bulaşıcı mı?",
 "desc": "Hidradenit bulaşıcı değildir. Akıntı, temas, ortak havlu veya cinsel yolla geçmez. Neden bulaşıcı sanıldığı ve gerçekte ne olduğu.",
 "h1": "Hidradenit bulaşıcı mı?",
 "lead": "<strong>Hayır, hidradenit bulaşıcı değildir.</strong> Ne temasla, ne ortak havlu ya da kıyafetle, ne havuz veya hamamla, ne de cinsel yolla geçer. Hastalık bir mikrobun vücuda girmesiyle başlamaz; <strong>kıl folikülünün tıkanması</strong> ve buna verilen aşırı bağışıklık yanıtıyla gelişir. Akıntının varlığı bulaşıcılık anlamına gelmez.",
 "watopic": "hidradenit hakkında bilgi",
 "related": ["hidradenit"],
 "sections": [
  {"id": "neden-sanilir", "tag": "Yanlış algı", "h2": "Neden bulaşıcı sanılıyor?", "body": [
   "Üç görünür özellik bu yanlış algıyı besliyor.",
   ("ul", ["<strong>Akıntı:</strong> irinli akıntı, bulaşıcı bir enfeksiyon izlenimi verir",
           "<strong>Koku:</strong> kapalı kanallarda biriken salgı kokabilir ve bu, hijyenle ilişkilendirilir",
           "<strong>Tekrarlama:</strong> geçmeyen bir tablo, \"bulaşıyor olmalı\" düşüncesini doğurur"]),
   "Oysa akıntının içeriği, dışarıdan gelen bir mikrop değil, <strong>tıkanmış folikülün dokuya boşalan içeriği ve buna verilen iltihap yanıtıdır</strong>. İkincil olarak bakteri ürese bile, hastalığı başlatan etken bu değildir."]},

  {"id": "gunluk", "tag": "Günlük yaşam", "h2": "Günlük yaşamda ne yapmak gerekir?", "body": [
   "Hiç kimseyi hastalıktan koruma amaçlı bir önlem almanız gerekmez. Alınacak önlemler <strong>kendi konforunuz</strong> içindir.",
   ("ul", ["Akıntı varsa emici ped ya da gazlı bez kullanmak kıyafeti korur",
           "Nefes alan, pamuklu ve bol kıyafetler sürtünmeyi azaltır",
           "Bölgeyi tahriş etmeyen, alkolsüz temizleyicilerle yıkamak yeterlidir",
           "Sert fırçalama ve antiseptik dezenfektanlar deriyi tahriş eder, yarar sağlamaz"]),
   ("note", "Hastaların en sık sorduğu şey çocuklarına ya da eşine bulaştırma korkusudur. Bu korkunun tıbbi bir karşılığı yoktur — evde ayrı havlu, ayrı çamaşır ya da mesafe gerekmez.")]},

  {"id": "kalitim", "tag": "Aile", "h2": "Bulaşmıyorsa neden ailede birden fazla kişide var?", "body": [
   "Çünkü bulaşma değil, <strong>yatkınlık paylaşımı</strong> söz konusudur. Hastaların bir bölümünde ailede benzer tablo bulunur; bu genetik yatkınlığın aktarılmasıyla ilgilidir, mikrop geçişiyle değil.",
   "Aynı evde yaşayan kişilerin sigara, beslenme ve kilo gibi ortak etkenleri paylaşması da tabloyu benzer kılabilir.",
   ("note", "Ailede hidradenit varsa, gençlerde erken bulgular ciddiye alınmalıdır. Erken tanı, hastalığın ileri evreye geçmesini engelleyen en güçlü etkendir.")]},

  {"id": "enfeksiyon", "tag": "Ayrım", "h2": "Peki ya enfeksiyon eklenirse?", "body": [
   "Hidradenit bölgesine ikincil bir bakteriyel enfeksiyon eklenebilir. Bu, hastalığın kendisinin bulaşıcı olduğu anlamına gelmez — açık bir yaraya bakteri yerleşmesi her yarada olabilecek bir durumdur.",
   ("h3", "Hekime başvurulması gereken bulgular"),
   ("ul", ["Ateş ve titreme",
           "Hızla yayılan kızarıklık",
           "Belirgin ısı artışı ve ani şiddetlenen ağrı",
           "Genel halsizlik"]),
   ("note", "Bu tablo yayılan bir deri enfeksiyonuna işaret edebilir ve gecikmeden değerlendirilmelidir. Hidradenitin olağan alevlenmesi genellikle ateş yapmaz.")]}],

 "faqs": [
  ("Hidradenit cinsel yolla bulaşır mı?",
   "Hayır. Kasık ve genital bölge tutulumu sık olduğu için bu soru çok sorulur, ancak hidradenit cinsel yolla bulaşan bir hastalık değildir. Partnere geçmez."),
  ("Aynı havluyu kullanmak sorun olur mu?",
   "Hastalığın bulaşması açısından sorun oluşturmaz. Yine de akıntılı bir yara varsa, temiz ve kuru tutmak yara bakımı açısından iyi bir alışkanlıktır."),
  ("Havuza veya hamama girebilir miyim?",
   "Açık akıntılı bir yara yoksa engel yoktur. Açık yara varsa, yara bakımı ve tahriş açısından beklemek daha uygundur; bu bir bulaştırma endişesi değil, kendi yaranızı koruma meselesidir."),
  ("Çocuğuma geçer mi?",
   "Temasla geçmez. Ancak genetik yatkınlık aktarılabilir; yani çocuğunuzda da ileride hidradenit görülme olasılığı, genel topluma göre bir miktar yüksek olabilir. Bu, erken bulguları ciddiye almak için bir nedendir."),
  ("Akıntı kokuyorsa mikrop mudur?",
   "Koku, kapalı kanallarda biriken salgı ve ikincil bakteri karışımından kaynaklanır; hastalığın bulaşıcı olduğunu göstermez. Hijyen eksikliğiyle de ilgisi yoktur.")]},

# ------------------------------------------------------------------ 8
{"slug": "hidradenit-ameliyati-nasil-yapilir", "sources": KAYNAK,
 "date": "2026-09-24",
 "cat": "Tedavi",
 "title": "Hidradenit Ameliyatı Nasıl Yapılır? Geniş Eksizyon ve Flep",
 "ogtitle": "Hidradenit ameliyatı nasıl yapılır?",
 "desc": "İleri evre hidradenitte etkilenmiş bölge bütünüyle çıkarılır ve oluşan açıklık flep ya da greftle onarılır. Ameliyatın adımları ve kapatma seçenekleri.",
 "h1": "Hidradenit ameliyatı nasıl yapılır?",
 "lead": "İleri evre hidradenitte ameliyatın mantığı tek cümleye sığar: <strong>hastalıklı ter bezi bölgesinin tamamı çıkarılmadan hastalık durmaz</strong>. Bu nedenle yapılan işlem apse boşaltmak değil, etkilenmiş alanın sağlam dokuya kadar bütünüyle çıkarılması (geniş eksizyon) ve oluşan açıklığın <strong>flep ya da greftle onarılmasıdır</strong>. Sınırlı çıkarma, geride kalan dokuda nüks demektir.",
 "watopic": "hidradenit ameliyatı planlaması",
 "related": ["hidradenit"],
 "sections": [
  {"id": "hazirlik", "tag": "Hazırlık", "h2": "Ameliyat öncesi hazırlık", "body": [
   ("ul", ["<strong>Evreleme:</strong> Hurley evresi belirlenir, tedavi kararı buna göre verilir",
           "<strong>Haritalama:</strong> etkilenmiş bölgenin sınırları çizilir; kanal ağı görünen deliklerin ötesine uzanır",
           "<strong>Aktif enfeksiyonun söndürülmesi:</strong> yaygın iltihap varsa önce ilaçla sakinleştirilir",
           "<strong>Sigaranın bırakılması:</strong> yara iyileşmesini doğrudan etkiler",
           "<strong>Eşlik eden durumların değerlendirilmesi:</strong> kan şekeri, kilo, beslenme"]),
   ("note", "Haritalama bu ameliyatın en belirleyici adımıdır. Kanal ağının dışarıdan görünen açıklıklardan daha geniş olması kuraldır, istisna değil. Eksik haritalama, eksik çıkarma ve kaçınılmaz nüks demektir.")]},

  {"id": "adimlar", "tag": "Ameliyat", "h2": "Ameliyatın adımları", "body": [
   ("steps", [
    ("SINIRLARIN BELİRLENMESİ", "Etkilenmiş alanın sınırları, muayene ve gerektiğinde ameliyat sırasında değerlendirmeyle çizilir."),
    ("GENİŞ EKSİZYON", "Bölge, sağlıklı dokuya ulaşılana dek bütünüyle çıkarılır. Amaç izi küçültmek değil, hastalıklı doku bırakmamaktır."),
    ("KAPATMA PLANI", "Oluşan açıklığın boyutu ve bölgenin hareketliliği değerlendirilir; buna göre kapatma yöntemi seçilir."),
    ("ONARIM", "Lokal flep, perforatör flep ya da deri grefti ile açıklık kapatılır."),
    ("İYİLEŞME DÖNEMİ", "Bölgeye göre 2-6 hafta hareket kısıtlaması, ardından kontraktüre karşı egzersiz programı.")])]},

  {"id": "kapatma", "tag": "Onarım", "h2": "Kapatma seçenekleri ve hangisi ne zaman", "body": [
   ("h3", "Doğrudan kapatma"),
   "Açıklık küçükse kenarlar birbirine yaklaştırılarak kapatılır. Hareketli bölgelerde gerginlik yaratırsa kontraktür riski taşır.",
   ("h3", "Lokal flep"),
   "Komşu sağlıklı doku kaydırılarak açıklık örtülür. Koltuk altı gibi hareketli bölgelerde tercih edilir — deri kalitesi ve hareket korunur.",
   ("h3", "Perforatör flep"),
   "Geniş açıklıklarda, kendi damarıyla taşınan doku bloğu kullanılır. Kontraktür riskini belirgin şekilde azaltır.",
   ("h3", "Deri grefti"),
   "Çok geniş alanlar için bir seçenektir. Ancak eklem üzerinde tek başına kullanıldığında hareket kısıtlılığı riski taşır.",
   ("h3", "İkincil iyileşme"),
   "Yaranın kendiliğinden kapanmasının beklenmesi. Uzun sürer, pansuman yükü fazladır ve nedbe kalitesi düşüktür; hareketli bölgelerde önerilmez.",
   ("note", "Koltuk altı ve kasık, kolun ve bacağın hareket ettiği bölgelerdir. Buradaki kapatmanın yalnızca yarayı örtmesi yetmez — <strong>hareketi kısıtlamaması</strong> da gerekir. Flep seçiminin özü budur.")]},

  {"id": "beklenti", "tag": "Beklenti", "h2": "Ne beklemeli, ne beklememeli?", "body": [
   ("ul", ["<strong>Beklenebilir:</strong> o bölgedeki tekrarlayan apse döngüsünün durması",
           "<strong>Beklenebilir:</strong> sürekli akıntının sona ermesi",
           "<strong>Beklenebilir:</strong> hareket ve günlük yaşam kalitesinde belirgin düzelme",
           "<strong>Beklenmemeli:</strong> izsiz bir sonuç — çıkarılan alan geniş olduğu için iz belirgindir",
           "<strong>Beklenmemeli:</strong> tüm vücutta hastalığın sona ermesi — başka bölgede yeni odak çıkabilir"]),
   ("note", "Hidradenitte hiçbir cerrahi yöntem yüzde yüz kalıcı sonuç garantisi vermez. Size garanti veren bir yaklaşımla karşılaşırsanız, yaklaşımın kendisinden şüphelenin.")]}],

 "faqs": [
  ("Hidradenit ameliyatı genel anestezi ile mi yapılır?",
   "Bölgenin genişliğine bağlıdır. Sınırlı alanlarda lokal anestezi yeterli olabilir; geniş eksizyon ve flep onarımı genellikle genel anestezi altında yapılır. Karar, çıkarılacak alanın boyutuna ve kapatma yöntemine göre verilir."),
  ("Ameliyat izi büyük olur mu?",
   "Çıkarılan alan geniş olduğu için iz belirgindir. Bunu küçültmeye çalışmak, hastalıklı doku bırakmak anlamına gelir ve nüksü davet eder. Önceliğimiz iz değil, hastalığın durması ve bölgenin hareketinin korunmasıdır. Flep planlaması, izi hareketi kısıtlamayacak şekilde konumlandırmayı sağlar."),
  ("Tek ameliyatla biter mi?",
   "Birden fazla bölge etkilenmişse ameliyatlar aşamalı planlanır; her bölge kendi iyileşme süresine ihtiyaç duyar. Tek bölge için genellikle tek ameliyat yeterlidir, ancak iyileşme sürecinde küçük düzeltmeler gerekebilir."),
  ("Ameliyattan sonra ilaç tedavisi devam eder mi?",
   "Hastaların çoğunda evet. Cerrahi, çıkarılan bölgedeki hastalığı durdurur; sistemik yatkınlığı ortadan kaldırmaz. Dermatoloji takibi ve gerektiğinde ilaç tedavisi ameliyat sonrası da sürer."),
  ("Lazer ile tedavi mümkün mü?",
   "Lazer epilasyon, erken evrede folikül sayısını azaltarak alevlenmeleri seyreltmede yardımcı olabilir ve bazı hastalarda kullanılır. Ancak oluşmuş kanal ağı ve nedbe için lazer bir çözüm değildir; ileri evrede cerrahinin yerini almaz."),
  ("Ameliyat sonrası ne kadar sürede işe dönerim?",
   "Bölgeye ve yapılan onarıma göre değişir. Koltuk altı flep onarımında hareket kısıtlaması genellikle 2-4 hafta, tam iyileşme 6-8 haftadır. Masa başı işlere dönüş daha erken olabilir; fiziksel güç gerektiren işler için süre uzar.")]},

# ------------------------------------------------------------------ 9
{"slug": "hidradenit-ameliyati-sonrasi-iyilesme", "sources": KAYNAK,
 "date": "2026-09-25",
 "cat": "Hasta Rehberi",
 "title": "Hidradenit Ameliyatı Sonrası İyileşme: Haftalara Göre Süreç",
 "ogtitle": "Hidradenit ameliyatı sonrası iyileşme süreci",
 "desc": "Hidradenit ameliyatı sonrası ilk günden üçüncü aya kadar ne olur? Hareket kısıtlaması, yara bakımı, kontraktür egzersizleri ve işe dönüş.",
 "h1": "Hidradenit ameliyatı sonrası iyileşme",
 "lead": "Hidradenit ameliyatından sonraki iyileşme, çıkarılan alanın genişliğine ve kapatma yöntemine göre değişir. Genel çerçeve şudur: <strong>ilk 2-4 hafta hareket kısıtlaması</strong>, ardından <strong>kontraktüre karşı egzersiz dönemi</strong> ve <strong>6-8 haftada büyük ölçüde iyileşme</strong>. Bu sürecin en kritik parçası yaranın kapanması değil, bölgenin <strong>hareketinin geri kazanılmasıdır</strong>.",
 "watopic": "hidradenit ameliyatı sonrası süreç",
 "related": ["hidradenit"],
 "sections": [
  {"id": "takvim", "tag": "Takvim", "h2": "Haftalara göre ne olur?", "body": [
   ("steps", [
    ("İLK GÜNLER", "Ağrı kontrolü ve drenaj takibi. Bölge sargılı tutulur. Hareket sınırlıdır; kolu ya da bacağı zorlamamak esastır."),
    ("1-2. HAFTA", "Pansuman düzeni oturur. Dikişler ve varsa drenler bu dönemde alınır. Şişlik ve morluk gerilemeye başlar."),
    ("2-4. HAFTA", "Hareket kısıtlaması kademeli olarak gevşetilir. Hekim onayıyla kontraktür egzersizleri başlar."),
    ("4-8. HAFTA", "Yara büyük ölçüde kapanmıştır. Egzersiz programı sürer. Günlük yaşam normale döner."),
    ("3-6. AY", "Nedbe olgunlaşır; kızarıklık ve sertlik azalır. Nihai görünüm bu dönemde oturur.")]),
   ("note", "Bu takvim bir ortalamadır. Greft ile kapatılan geniş alanlarda süre uzar ve fizyoterapi desteği gerekebilir. Sigara içiliyorsa her aşama gecikir.")]},

  {"id": "bakim", "tag": "Yara bakımı", "h2": "Yara bakımında neye dikkat etmeli?", "body": [
   ("ul", ["Pansuman sıklığına hekiminizin verdiği düzene uyun — fazlası da azı da iyileşmeyi bozar",
           "Bölgeyi kuru ve temiz tutun; nem yara kenarlarını yumuşatır",
           "Sürtünmeyen, pamuklu, bol kıyafet tercih edin",
           "Deodorant, parfüm ve alkollü ürünleri yara bölgesine uygulamayın",
           "Duş için hekiminizin verdiği zamanı bekleyin; erken ıslatma greft ve flep için risklidir"]),
   ("h3", "Hemen bildirilmesi gerekenler"),
   ("ul", ["Ateş",
           "Yara kenarında artan kızarıklık ve ısı",
           "Kötü kokulu ya da artan akıntı",
           "Flep bölgesinde renk değişikliği — morarma ya da solma",
           "Ani artan, ilaçla geçmeyen ağrı"])]},

  {"id": "egzersiz", "tag": "Hareket", "h2": "Kontraktür egzersizleri neden bu kadar önemli?", "body": [
   "Koltuk altı ve kasık, hareket eden bölgelerdir. İyileşen nedbe doğal olarak <strong>büzüşme eğilimindedir</strong>. Hareket geri kazandırılmazsa, nedbe kolu ya da bacağı kısıtlayan bir bant haline gelir. Buna <strong>kontraktür</strong> denir.",
   ("ul", ["Egzersizlere hekiminizin belirttiği günde başlayın — erken başlamak yarayı açabilir, geç başlamak kontraktüre yol açar",
           "Hareketi zorlamadan, ağrı sınırının hemen altında çalışın",
           "Günde birkaç kısa seans, tek uzun seanstan iyidir",
           "Geniş greft uygulanan hastalarda fizyoterapi desteği alınması yararlıdır"]),
   ("note", "Ameliyatın başarısı çoğu zaman yaranın kapanmasıyla değil, <strong>üç ay sonra kolunuzu ne kadar rahat kaldırabildiğinizle</strong> ölçülür. Egzersiz dönemi, ameliyatın devamıdır.")]},

  {"id": "sonrasi", "tag": "Uzun vade", "h2": "İyileştikten sonra ne olacak?", "body": [
   "Çıkarılan bölgede hastalık durdurulmuştur. Ancak hidradenit sistemik bir yatkınlıkla ilişkilidir; <strong>başka bir bölgede yeniden başlayabilir</strong>.",
   ("ul", ["Dermatoloji takibi devam eder",
           "Yeni bölgelerde erken bulgular ciddiye alınmalıdır",
           "Sigaranın bırakılmış olması uzun vadeli seyri etkiler",
           "Kilo ve sürtünme yönetimi önemini korur"]),
   ("note", "Ameliyat sonrası dermatoloji takibinin kesilmesi en sık yapılan hatalardan biridir. Cerrahi bir bölgeyi çözer; hastalığın kendisini takip etmeyi bırakmak için bir gerekçe değildir.")]}],

 "faqs": [
  ("İyileşme ne kadar sürer?",
   "Bölgeye ve kapatma yöntemine göre değişir. Koltuk altı flep onarımında hareket kısıtlaması genellikle 2-4 hafta, büyük ölçüde iyileşme 6-8 haftadır. Geniş greft uygulanan alanlarda süre uzar ve fizyoterapi gerekebilir."),
  ("Ne zaman duş alabilirim?",
   "Kapatma yöntemine bağlıdır ve mutlaka hekiminizin verdiği tarihe uyulmalıdır. Flep ve greft bölgelerinin erken ıslatılması ciddi sorunlara yol açabilir. Genellikle ilk günlerde bölge korunarak yıkanma önerilir."),
  ("Ne zaman işe dönebilirim?",
   "Masa başı işlerde çoğu hasta 1-2 hafta içinde dönebilir. Kol ya da bacağın aktif kullanıldığı, fiziksel güç gerektiren işlerde süre 4-6 haftaya uzayabilir. Karar, yapılan onarıma göre verilir."),
  ("Ameliyattan sonra spor yapabilir miyim?",
   "Hekim onayıyla, genellikle 6-8 hafta sonra kademeli olarak. Erken dönemde ter ve sürtünme yara iyileşmesini zorlar. Yüzme, yara tam kapanmadan önerilmez."),
  ("Nedbe zamanla düzelir mi?",
   "Nedbe ilk aylarda kızarık ve sert olur; 3-6 ay içinde solar ve yumuşar. Nihai görünüm genellikle bir yılı bulur. Silikon ürünler ve masaj, hekim önerisiyle nedbenin olgunlaşmasına yardımcı olabilir."),
  ("Aynı bölgede tekrar çıkar mı?",
   "Bölge bütünüyle çıkarıldıysa aynı yerde nüks olasılığı belirgin biçimde düşüktür. Sınırlı çıkarma yapıldıysa risk yüksektir. Başka bir bölgede yeni odak çıkması ise ayrı bir konudur ve mümkündür.")]},

# ------------------------------------------------------------------ 10
{"slug": "hidradenit-nuks-eder-mi", "sources": KAYNAK,
 "date": "2026-09-26",
 "cat": "Hidradenit",
 "title": "Hidradenit Nüks Eder mi? Ameliyat Sonrası Gerçekçi Beklenti",
 "ogtitle": "Hidradenit ameliyattan sonra tekrarlar mı?",
 "desc": "Geniş eksizyon yapılan bölgede nüks oranı düşüktür; ancak başka bölgede yeni odak çıkabilir. Nüksü belirleyen etkenler ve gerçekçi beklenti.",
 "h1": "Hidradenit nüks eder mi?",
 "lead": "Dürüst cevap: <strong>nüks mümkündür.</strong> Ancak burada iki farklı şeyi ayırmak gerekir. Bütünüyle çıkarılmış bir bölgede hastalığın <strong>aynı yerde</strong> tekrarlaması belirgin biçimde nadirdir. Buna karşılık hidradenit sistemik bir yatkınlıkla ilişkili olduğu için <strong>başka bir bölgede</strong> yeni bir odak başlayabilir. \"Nüks etti\" denen durumların çoğu aslında ikincisidir.",
 "watopic": "hidradenit nüks riski",
 "related": ["hidradenit"],
 "sections": [
  {"id": "iki-tur", "tag": "Ayrım", "h2": "İki farklı \"tekrarlama\"", "body": [
   ("table", ["", "Aynı bölgede nüks", "Yeni bölgede odak"],
    [["Nedeni", "Eksik çıkarma — geride hastalıklı doku kalması", "Sistemik yatkınlığın sürmesi"],
     ["Sıklık", "Geniş eksizyon sonrası düşük", "Mümkün; ilaç tedavisiyle azaltılabilir"],
     ["Önlenebilir mi", "Büyük ölçüde — doğru haritalama ve yeterli sınır ile", "Tümüyle değil; risk azaltılabilir"],
     ["Ne yapılır", "Yeniden değerlendirme ve gerekirse ek cerrahi", "Dermatoloji takibi ve erken tedavi"]]),
   ("note", "Bu ayrım önemlidir çünkü hastanın yaşadığı deneyim aynı görünür: \"yine çıktı\". Oysa nedenleri ve çözümleri farklıdır.")]},

  {"id": "etkenler", "tag": "Risk", "h2": "Nüks riskini artıran etkenler", "body": [
   ("ul", ["<strong>Sınırlı çıkarma:</strong> izi küçültmek için dar sınırla yapılan eksizyon, en güçlü nüks nedenidir",
           "<strong>Eksik haritalama:</strong> kanal ağı görünen açıklıkların ötesine uzanır; haritalanmayan kısım geride kalır",
           "<strong>Sigara:</strong> hem hastalığın seyrini hem yara iyileşmesini bozar",
           "<strong>İleri Hurley evresi:</strong> yaygın tutulumda birden fazla bölge risk altındadır",
           "<strong>Takibin kesilmesi:</strong> yeni odakların erken yakalanmaması ilerlemesine izin verir"]),
   ("note", "Bu listedeki ilk iki madde tamamen <strong>cerrahi planlamayla</strong> ilgilidir. Hidradenit cerrahisinde \"az kesip az iz bırakma\" yaklaşımı, iyi niyetli ama yanlış bir tercihtir.")]},

  {"id": "azaltma", "tag": "Ne yapılabilir", "h2": "Nüks riski nasıl azaltılır?", "body": [
   ("h3", "Cerrahi tarafında"),
   ("ul", ["Bölgenin ameliyat öncesi ayrıntılı haritalanması",
           "Sağlıklı dokuya kadar yeterli sınırla çıkarma",
           "Hareketli bölgede kontraktür bırakmayan kapatma planı"]),
   ("h3", "Hasta tarafında"),
   ("ul", ["Sigaranın bırakılması",
           "Kilo yönetimi ve sürtünen bölgelerin korunması",
           "Dermatoloji takibinin sürdürülmesi",
           "Yeni bölgedeki ilk bulgunun ertelenmemesi"]),
   ("note", "Yeni bir bölgede ilk şişlik çıktığında beklemek, o bölgenin de yıllar içinde ileri evreye ilerlemesine izin vermek demektir. Erken müdahale, ikinci bir ameliyatı gereksiz kılabilir.")]},

  {"id": "beklenti", "tag": "Beklenti", "h2": "Gerçekçi beklenti nedir?", "body": [
   "Hidradenitte hiçbir yöntem <strong>ömür boyu hastalıksızlık</strong> garantisi vermez. Verilebilecek en dürüst çerçeve şudur:",
   ("ul", ["Bütünüyle çıkarılan bölgede tekrarlayan apse döngüsü durur",
           "Sürekli akıntı ve o bölgeye bağlı ağrı sona erer",
           "Hareket ve günlük yaşam kalitesi belirgin şekilde düzelir",
           "Başka bir bölgede yeni odak çıkma olasılığı devam eder",
           "Dermatoloji takibi ve gerektiğinde ilaç tedavisi sürer"]),
   ("note", "Size \"kesin şifa\" ya da \"bir daha asla çıkmaz\" diyen bir yaklaşımla karşılaşırsanız, o yaklaşımın kendisini sorgulayın. Hidradenitte dürüst beklenti yönetimi, tedavinin bir parçasıdır.")]}],

 "faqs": [
  ("Ameliyattan sonra aynı yerde tekrar çıkma ihtimali nedir?",
   "Bölge sağlıklı dokuya kadar bütünüyle çıkarıldıysa aynı yerde nüks olasılığı belirgin biçimde düşüktür. Literatürde geniş eksizyonun, sınırlı işlemlere ve tekrarlayan drenaja kıyasla çok daha düşük nüks oranı verdiği tutarlı biçimde gösterilmiştir."),
  ("Neden başka bir bölgede çıkıyor?",
   "Çünkü hidradenit yalnızca o bölgeye ait bir sorun değil, sistemik bir yatkınlığın deri üzerindeki yansımasıdır. Cerrahi bir bölgedeki hastalıklı dokuyu ortadan kaldırır; vücudun genel eğilimini değiştirmez."),
  ("Nüks olursa yeniden ameliyat gerekir mi?",
   "Her zaman değil. Yeni bölgedeki bulgular erken evredeyse ilaç tedavisi yeterli olabilir. Kalıcı kanal ve nedbe oluştuysa o bölge için de cerrahi değerlendirme gerekir."),
  ("İlaç tedavisi nüksü önler mi?",
   "Tümüyle önlemez, ancak yeni odak çıkma sıklığını azaltabilir. Özellikle yaygın tutulumu olan hastalarda ameliyat sonrası sistemik tedavinin sürdürülmesi tercih edilir."),
  ("Sigara gerçekten nüksü etkiliyor mu?",
   "Evet. Sigaranın hidradenitin seyrini kötüleştirdiği ve yara iyileşmesini bozduğu net biçimde gösterilmiştir. Ameliyat öncesi ve sonrası sigarasız dönem, hem iyileşmeyi hem uzun vadeli sonucu etkiler.")]},

# ------------------------------------------------------------------ 11
{"slug": "hidradenit-ve-sigara", "sources": KAYNAK,
 "date": "2026-09-27",
 "cat": "Hidradenit",
 "title": "Hidradenit ve Sigara: Bırakmak Gerçekten Fark Yaratır mı?",
 "ogtitle": "Hidradenitte sigaranın etkisi",
 "desc": "Sigara, hidradenitle ilişkisi en güçlü gösterilmiş etkendir. Alevlenme sıklığını artırır, ameliyat sonrası yara iyileşmesini bozar. Bırakmanın etkisi.",
 "h1": "Hidradenit ve sigara",
 "lead": "Hidradenitte <strong>sigara, ilişkisi en güçlü gösterilmiş çevresel etkendir</strong>. İki ayrı yerden zarar verir: hastalığın kendi seyrini ağırlaştırır ve ameliyat gerekirse <strong>yara iyileşmesini doğrudan bozar</strong>. Bu yüzden sigarayı bırakmak, tedaviye eşlik eden bir öneri değil, <strong>tedavinin kendisinin bir parçasıdır</strong>.",
 "watopic": "hidradenit ve sigara ilişkisi",
 "related": ["hidradenit"],
 "sections": [
  {"id": "nasil", "tag": "Mekanizma", "h2": "Sigara nasıl zarar veriyor?", "body": [
   ("h3", "Folikül tıkanmasını artırır"),
   "Sigara dumanındaki bileşenler, kıl folikülünün ağzındaki hücrelerin davranışını değiştirir ve tıkanmayı kolaylaştırır. Hidradenitin başlangıç noktası tam olarak burasıdır.",
   ("h3", "İltihap yanıtını güçlendirir"),
   "Hidradenitte sorun yalnızca tıkanma değil, ona verilen aşırı bağışıklık yanıtıdır. Sigara bu yanıtı destekleyerek alevlenmeleri sıklaştırır.",
   ("h3", "Dokuya giden kanı azaltır"),
   "Nikotin damarları daraltır. Daralan damar, dokuya daha az oksijen taşır. Bu, hem mevcut iltihabın çözülmesini geciktirir hem de ameliyat sonrası iyileşmeyi zorlaştırır.",
   ("note", "Üçüncü madde, cerrahi planlamada belirleyicidir. Flep ve greft, kanlanmaya bağımlı yapılardır. Sigara içen bir hastada flep kaybı ve yara ayrılması riski belirgin biçimde yükselir.")]},

  {"id": "seyir", "tag": "Seyir", "h2": "Sigara içen hastalarda ne değişiyor?", "body": [
   ("ul", ["Alevlenmeler daha sık ve daha uzun sürer",
           "Daha fazla bölge tutulma eğilimindedir",
           "İlaç tedavisine yanıt daha zayıf olabilir",
           "Ameliyat sonrası yara ayrılması ve enfeksiyon riski artar",
           "Nüks olasılığı yükselir"]),
   ("note", "Bunlar bir suçlama listesi değil, bir <strong>kaldıraç listesidir</strong>. Hidradenitte hastanın kendi elinde olan, etkisi en büyük tek değişken sigaradır.")]},

  {"id": "birakinca", "tag": "Bırakınca", "h2": "Bırakmak ne kadar fark yaratır?", "body": [
   "Sigarayı bırakmak hidradeniti ortadan kaldırmaz — bunu açıkça söylemek gerekir. Ama iki somut kazanım sağlar:",
   ("ul", ["<strong>Alevlenme sıklığında azalma:</strong> hastaların önemli bir bölümü aylar içinde fark eder",
           "<strong>Ameliyat sonucunda iyileşme:</strong> yara iyileşmesi belirgin biçimde düzelir, flep ve greft başarısı artar"]),
   ("h3", "Ameliyat planlanıyorsa zamanlama"),
   "Ameliyattan önceki dönemde sigarasız geçen süre, yara iyileşmesini doğrudan etkiler. Cerrahınız size bu konuda bir süre önerecektir; bu öneri keyfi değil, doku kanlanmasının toparlanma süresiyle ilgilidir.",
   ("note", "Sigara bırakma, ameliyat tarihinden birkaç gün önce alınacak bir karar değildir. Mümkün olan en erken dönemde başlamak, sonucu en çok etkileyen tercihlerden biridir.")]},

  {"id": "destek", "tag": "Destek", "h2": "Bırakmak için destek", "body": [
   "Kronik ağrıyla yaşayan bir kişiden sigarayı tek başına bırakmasını beklemek gerçekçi değildir. Destek almak, iradesizlik göstergesi değil, akılcı bir tercihtir.",
   ("ul", ["Aile hekiminiz sigara bırakma polikliniklerine yönlendirebilir",
           "Nikotin replasman tedavileri ve ilaç seçenekleri mevcuttur",
           "Sağlık Bakanlığı'nın ücretsiz <strong>ALO 171 Sigara Bırakma Danışma Hattı</strong> aranabilir",
           "Ameliyat tarihi, birçok hasta için güçlü bir motivasyon noktasıdır"]),
   ("note", "Elektronik sigara ve ısıtılmış tütün ürünleri, hidradenit açısından güvenli bir alternatif olarak kabul edilmez. Nikotin damar daraltıcı etkisini bu ürünlerde de sürdürür.")]}],

 "faqs": [
  ("Sigarayı bırakırsam hidradenitim geçer mi?",
   "Geçmesini beklemek doğru olmaz. Sigara hastalığın tek nedeni değildir. Ancak alevlenme sıklığının azalması sık görülür ve ameliyat gerekirse iyileşme belirgin şekilde düzelir."),
  ("Ameliyattan ne kadar önce bırakmalıyım?",
   "Ne kadar erken o kadar iyi. Doku kanlanmasının toparlanması zaman aldığı için, ameliyattan haftalar önce bırakılması önerilir. Cerrahınız size kendi planına göre bir süre belirtecektir."),
  ("Elektronik sigara kullanabilir miyim?",
   "Hidradenit açısından güvenli bir alternatif olarak kabul edilmez. Nikotinin damar daraltıcı etkisi bu ürünlerde de devam eder ve yara iyileşmesini etkiler."),
  ("Sigarayı bırakınca kilo aldım, bu hastalığı kötüleştirir mi?",
   "Kilo artışı sürtünen bölgelerde alevlenmeyi tetikleyebilir, bu doğru. Ancak sigaranın hidradenit üzerindeki etkisi kilodan daha güçlüdür. Doğru yaklaşım sigaraya dönmek değil, kilo yönetimi için destek almaktır."),
  ("Ailemde sigara içiliyor, pasif içicilik etkiler mi?",
   "Pasif içiciliğin hidradenit üzerindeki etkisi aktif içiciliğe göre çok daha az incelenmiştir ve net bir sonuç bildirilmemiştir. Yine de dumansız bir ortam, hem yara iyileşmesi hem genel sağlık açısından tercih edilir.")]},

# ------------------------------------------------------------------ 12
{"slug": "hidradenit-mi-ciban-mi-kist-mi", "sources": KAYNAK,
 "date": "2026-09-28",
 "cat": "Ayrım",
 "title": "Hidradenit mi, Çıban mı, Kist mi? Ayırt Etme Rehberi",
 "ogtitle": "Hidradenit, çıban ve kist arasındaki fark",
 "desc": "Hidradenit, fronkül ve epidermal kist benzer görünür ama tedavileri farklıdır. Tekrarlama, yerleşim ve deri altı kanal ayrımı nasıl yapılır?",
 "h1": "Hidradenit mi, çıban mı, kist mi?",
 "lead": "Koltuk altındaki ya da kasıktaki ağrılı bir şişlik üç farklı şey olabilir: <strong>hidradenit</strong>, <strong>çıban (fronkül)</strong> ya da <strong>iltihaplanmış epidermal kist</strong>. İlk bakışta üçü de kırmızı, şiş ve ağrılıdır. Ayrımı yapan asıl ölçüt <strong>zaman içindeki davranıştır</strong>: tekrarlama, deri altında kanal oluşumu ve yerleşim yeri.",
 "watopic": "koltuk altı veya kasıktaki şişliğin değerlendirilmesi",
 "related": ["hidradenit"],
 "sections": [
  {"id": "tablo", "tag": "Karşılaştırma", "h2": "Üçü yan yana", "body": [
   ("table", ["", "Hidradenit", "Çıban (fronkül)", "Epidermal kist"],
    [["Başlangıç", "Derin, başsız şişlik", "Kılın dibinde, başlı", "Yavaş büyüyen yumru"],
     ["Tekrarlama", "Aynı bölgede tekrar tekrar", "Genellikle tek seferlik", "Aynı yerde kalır, iltihaplanabilir"],
     ["Yerleşim", "Koltuk altı, kasık, göğüs altı", "Her yerde", "Sırt, boyun, yüz, gövde"],
     ["Deri altı kanal", "Zamanla oluşur", "Yok", "Yok"],
     ["İkili komedon", "Sık, tipik", "Yok", "Tek bir gözenek (punktum)"],
     ["Nedbe", "Sertleşmiş, çekintili", "Genelde iz bırakmaz", "Sınırlı"],
     ["Tedavi", "Kronik hastalık yönetimi", "Antibiyotik, drenaj", "Kist kesesinin çıkarılması"]])]},

  {"id": "hidradenit", "tag": "Hidradenit", "h2": "Hidradeniti düşündüren", "body": [
   ("ul", ["Aynı bölgede <strong>tekrarlayan</strong> alevlenmeler",
           "Deri altında elle hissedilen sert bantlar",
           "Yan yana duran, siyah uçlu <strong>ikili komedonlar</strong>",
           "Aralıklı akıntı ve çekintili nedbeler",
           "Koltuk altı, kasık ve göğüs altı yerleşimi"]),
   ("note", "<strong>En ayırt edici bulgu ikili komedondur.</strong> Tek bir noktadan çıkan çift siyah nokta görünümü, hidradenit dışında pek görülmez.")]},

  {"id": "ciban", "tag": "Çıban", "h2": "Çıbanı (fronkül) düşündüren", "body": [
   "Fronkül, tek bir kıl folikülünün bakteriyel enfeksiyonudur. Genellikle <strong>stafilokok</strong> kaynaklıdır.",
   ("ul", ["Kılın dibinden başlar, zamanla sarı bir baş oluşur",
           "Açıldığında irin boşalır ve genellikle hızla iyileşir",
           "Vücudun herhangi bir yerinde olabilir",
           "Deri altında kanal bırakmaz",
           "Tedaviden sonra genellikle tekrarlamaz"]),
   ("note", "Birden fazla fronkülün birleşmesine <strong>karbonkül</strong> denir. Bu da hidradenit değildir, ancak daha ağır bir enfeksiyon tablosudur ve tedavi gerektirir.")]},

  {"id": "kist", "tag": "Kist", "h2": "Epidermal kisti düşündüren", "body": [
   "Epidermal kist, deri altında keratin biriken kapalı bir kesedir. İltihaplanmadığı sürece ağrısızdır.",
   ("ul", ["Yavaş büyüyen, hareketli, ağrısız bir yumru olarak başlar",
           "Üzerinde tek bir gözenek (punktum) bulunabilir",
           "İltihaplanınca kızarır, ağrır ve çıbanla karışır",
           "Aynı yerde kalır; başka bölgelerde tekrarlamaz",
           "Kalıcı çözüm, kesenin bütünüyle çıkarılmasıdır"]),
   ("note", "İltihaplı bir kist boşaltıldığında rahatlama olur ama kese yerinde kalırsa yeniden dolar. Bu, hidradenitle karıştırılmasının başlıca nedenidir. Ayrım, kesenin tek ve sınırlı olması ile kanal ağının yaygın olmasıdır.")]},

  {"id": "ne-yapmali", "tag": "Ne yapmalı", "h2": "Ayrım nasıl kesinleşir?", "body": [
   "Üçünün ayrımı genellikle <strong>muayene ve öykü ile</strong> yapılır. Görüntüleme her hastada gerekmez.",
   ("ul", ["Hekiminize <strong>kaç kez tekrarladığını</strong> ve <strong>hangi bölgelerde olduğunu</strong> mutlaka söyleyin",
           "Önceki alevlenmelerin fotoğrafı varsa götürün — sessiz dönemde muayene yanıltıcı olabilir",
           "Daha önce yapılan drenajları ve kullanılan antibiyotikleri not edin",
           "Ailede benzer tablo varsa belirtin"]),
   ("note", "Hidradenit tanısında ortalama gecikme yıllarla ölçülür. Bunun en büyük nedeni, her alevlenmenin ayrı bir \"çıban\" olarak değerlendirilmesidir. Tekrarlama öyküsünü anlatmak, tanıyı hızlandıran en güçlü bilgidir.")]}],

 "faqs": [
  ("Koltuk altımdaki şişlik çıban mı hidradenit mi?",
   "Tek seferlik, başlı, açıldıktan sonra iyileşen ve tekrarlamayan bir şişlik büyük olasılıkla çıbandır. Aynı bölgede tekrar tekrar çıkan, başsız, derin ve deri altında sertlik bırakan şişlikler hidradeniti düşündürür."),
  ("Kist ile hidradenit karışır mı?",
   "İltihaplanmış bir epidermal kist, hidradenit alevlenmesine çok benzeyebilir. Ayrım, kistin tek ve sınırlı bir kese olması, hidradenitin ise yaygın ve birbirine bağlı kanal ağı oluşturmasıdır. Tekrarlama öyküsü ayrımda belirleyicidir."),
  ("Ayrım için tahlil ya da görüntüleme gerekir mi?",
   "Çoğu hastada gerekmez; tanı muayene ve öyküyle konur. Yaygın ve derin tutulumda, kanal ağının sınırlarını belirlemek için ultrason ya da MR kullanılabilir. Akıntıdan kültür alınması ise ikincil enfeksiyon şüphesinde anlamlıdır."),
  ("Yanlış tanı konursa ne olur?",
   "Hidradenit, tekrarlayan çıban olarak değerlendirilirse yıllarca drenaj ve antibiyotik döngüsünde kalınır. Bu süre içinde kanal ağı ve nedbe genişler, hastalık daha ileri bir evreye ilerler. Tanı gecikmesi hidradenitin en büyük sorunudur."),
  ("Hangi bölüme gitmeliyim?",
   "Dermatolojiye. Üç tablonun ayrımı, evreleme ve ilaç tedavisi bu branşın alanıdır. Hidradenit tanısı konur ve deri altında kalıcı kanal oluşmuşsa, onarım için plastik ve rekonstrüktif cerrahi değerlendirmesi gerekir.")]},

# ------------------------------------------------------------------ 13
{"slug": "kasikta-hidradenit", "sources": KAYNAK,
 "date": "2026-09-29",
 "cat": "Hidradenit",
 "title": "Kasıkta Hidradenit: Belirtileri ve Tedavi Yaklaşımı",
 "ogtitle": "Kasıkta hidradenit nasıl seyreder?",
 "desc": "Kasık ve genital bölge hidradeniti, hareket ve mahremiyet nedeniyle ayrı bir yaklaşım gerektirir. Belirtiler, ayrım ve cerrahi planlamada dikkat edilenler.",
 "h1": "Kasıkta hidradenit",
 "lead": "Kasık ve genital bölge, hidradenitin koltuk altından sonra <strong>en sık tuttuğu bölgedir</strong>. Buradaki tablo iki nedenle ayrı ele alınır: bölge sürekli hareket eder ve nemli kalır — bu, hem alevlenmeyi hem de onarım planlamasını zorlaştırır. Ayrıca mahremiyet kaygısı nedeniyle hastalar <strong>en geç bu bölge için başvurur</strong>; tanı gecikmesi burada en yüksektir.",
 "watopic": "kasık bölgesi hidradenit değerlendirmesi",
 "related": ["hidradenit"],
 "sections": [
  {"id": "neden", "tag": "Neden burada", "h2": "Kasık neden bu kadar sık tutulur?", "body": [
   ("ul", ["<strong>Deri kıvrımı:</strong> iki deri yüzeyi sürekli temas halindedir",
           "<strong>Nem:</strong> bölge havalanmaz, terleme kolay kurumaz",
           "<strong>Sürtünme:</strong> yürüme, oturma ve kıyafet baskısı foliküllere sürekli mekanik yük bindirir",
           "<strong>Kıl yoğunluğu:</strong> folikül sayısı yüksektir"]),
   ("note", "Bu etkenler hastalığın nedeni değil, tıkanma sürecini kolaylaştıran zemindir. Hidradenit bu bölgede daha sık başlar ve daha hızlı ilerleyebilir.")]},

  {"id": "belirti", "tag": "Bulgular", "h2": "Kasıkta hangi bulgular görülür?", "body": [
   ("ul", ["Kasık kıvrımında tekrarlayan, ağrılı, derin şişlikler",
           "Bacak arasında yürürken artan ağrı ve sürtünme hissi",
           "Aralıklı, kokulu akıntı ve iç çamaşırında leke",
           "Deri altında hissedilen sert bantlar",
           "İyileşen bölgelerde çekintili, koyu renkli nedbeler",
           "Oturmakta ve bacak açmakta zorlanma"]),
   ("note", "Genital bölge tutulumu, cinsel yaşamı ve beden algısını doğrudan etkiler. Bu, hastaların hekime en zor anlattığı ama tedavi planında mutlaka yer alması gereken bir boyuttur.")]},

  {"id": "ayrim", "tag": "Ayrım", "h2": "Kasıkta neyle karışır?", "body": [
   "Kasık bölgesinde benzer görünen birkaç tablo vardır ve tedavileri farklıdır.",
   ("ul", ["<strong>İltihaplı epidermal kist:</strong> tek ve sınırlı bir kese; tekrarlama başka bölgelere yayılmaz",
           "<strong>Fronkül:</strong> tek seferlik folikül enfeksiyonu; kanal bırakmaz",
           "<strong>Lenf bezi şişmesi:</strong> deri altında daha derin, yuvarlak; deriye açılmaz",
           "<strong>Pilonidal sinüs:</strong> kuyruk sokumu bölgesine özgüdür; kıl içerir",
           "<strong>Anal fistül:</strong> makat kanalıyla bağlantılıdır; genel cerrahi değerlendirmesi gerekir"]),
   ("note", "Makat çevresi tutulumunda hidradenit ile anal fistül ayrımı önemlidir ve bazen ikisi bir arada bulunur. Bu durumda plastik cerrahi ile genel cerrahinin birlikte değerlendirmesi gerekir.")]},

  {"id": "tedavi", "tag": "Tedavi", "h2": "Kasıkta tedavi yaklaşımı", "body": [
   ("h3", "Erken evrede"),
   "İlaç tedavisi ve günlük bakım düzeni önceliklidir. Bölgeyi kuru tutmak, nefes alan pamuklu iç çamaşırı kullanmak ve tahriş eden ürünlerden kaçınmak alevlenme sıklığını azaltır. <strong>Bu dönem dermatolojinin alanıdır.</strong>",
   ("h3", "İleri evrede"),
   "Kanal ağı ve nedbe oluştuysa bölgenin bütünüyle çıkarılması gerekir. Kasıkta kapatma planı, koltuk altından daha zorludur:",
   ("ul", ["Bölge sürekli hareket eder — bacak açma ve yürüme hareketi korunmalıdır",
           "Nem ve kirlenme riski yüksektir; yara bakımı daha titiz yürütülür",
           "Doğrudan kapatma gerginlik yaratırsa kontraktür riski doğar",
           "Perforatör flep, geniş kasık defektlerinde hareketi korumak açısından değerlidir"]),
   ("note", "Kasık onarımında amaç yalnızca yarayı kapatmak değil, <strong>bacağın hareket açıklığını korumaktır</strong>. Kontraktür gelişirse yürüyüş etkilenir ve ikinci bir girişim gerekebilir.")]},

  {"id": "gunluk", "tag": "Günlük yaşam", "h2": "Günlük yaşamda ne yardımcı olur?", "body": [
   ("ul", ["Pamuklu, nefes alan ve sıkmayan iç çamaşırı",
           "Bölgeyi tahriş etmeyen, alkolsüz temizleyicilerle yıkamak",
           "Yıkadıktan sonra bölgeyi ovmadan, kurulayarak tamamen kurutmak",
           "Akıntı varsa emici ped kullanmak",
           "Derin tıraş yerine, tahriş etmeyen kıl kontrolü yöntemlerini hekiminizle konuşmak",
           "Uzun süre oturulan işlerde ara ara ayağa kalkmak"]),
   ("note", "Sert antiseptikler, alkollü mendiller ve sık sıcak su banyoları bu bölgede yarardan çok zarar verir. Deri bariyerini bozar ve alevlenmeyi kolaylaştırır.")]}],

 "faqs": [
  ("Kasıktaki hidradenit cinsel yolla bulaşır mı?",
   "Hayır. Genital bölge tutulumu sık olduğu için bu soru çok sorulur, ancak hidradenit bulaşıcı bir hastalık değildir ve partnere geçmez."),
  ("Kasıkta hidradenit mi, lenf bezi şişmesi mi?",
   "Lenf bezi şişmesi deri altında daha derin, yuvarlak ve hareketli bir yapıdır; deriye açılmaz ve akıntı yapmaz. Hidradenit ise deriye açılır, akıntı yapar ve zamanla kanal ağı oluşturur. Ayrım muayeneyle yapılır."),
  ("Epilasyon kasık hidradenitini tetikler mi?",
   "Derin tıraş ve ağda, foliküllere mekanik yük bindirerek alevlenmeyi tetikleyebilir. Lazer epilasyon ise erken evrede folikül sayısını azaltarak bazı hastalarda yardımcı olabilir. Karar hekiminizle birlikte verilmelidir."),
  ("Kasık ameliyatından sonra yürüyebilir miyim?",
   "İlk günlerde hareket kısıtlıdır ve bacak açma hareketi sınırlandırılır. Kademeli olarak, hekim onayıyla normal yürüyüşe dönülür. Kontraktür egzersizleri bu bölgede özellikle önemlidir; yürüyüşün eski haline dönmesi buna bağlıdır."),
  ("Makat çevresinde de var, aynı ameliyatla olur mu?",
   "Bölgeler birbirine komşu olsa da aşamalı planlama gerekebilir. Ayrıca makat çevresi tutulumunda anal fistül ayrımı yapılmalı ve gerekiyorsa genel cerrahi ile birlikte değerlendirilmelidir."),
  ("Mahremiyet nedeniyle muayeneden çekiniyorum, ne yapabilirim?",
   "Bu çekince çok yaygındır ve tanı gecikmesinin en önemli nedenlerinden biridir. Muayene sırasında yalnızca değerlendirilecek bölge açılır, isterseniz aynı cinsiyetten bir sağlık çalışanının bulunmasını talep edebilirsiniz. Erteleme, hastalığın ilerlemesine izin vermek anlamına gelir.")]},
]
