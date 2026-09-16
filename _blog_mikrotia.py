# -*- coding: utf-8 -*-
"""
Blog — mikrotia (dogustan kulak gelismemesi) kumesi, 9 yazi.
Yayin: 30 Eylul - 8 Ekim 2026, gunde 1.

KAPSAM SINIRI: Isitme degerlendirmesi ve atrezi cerrahisi KBB/odyoloji
alanidir. Bu kumede kulak kepcesi onarimi anlatilir; isitme kismi dogru
brimse yonlendirilir. Fiyat, once/sonra gorseli, garanti vaadi yoktur.
"""

SRC_SP = ("Ear Microtia — StatPearls, NCBI Bookshelf",
          "https://www.ncbi.nlm.nih.gov/books/NBK563243/")
SRC_ATR = ("External Ear Aural Atresia — StatPearls, NCBI Bookshelf",
           "https://www.ncbi.nlm.nih.gov/books/NBK563257/")
SRC_CDC = ("Anotia / Microtia — ABD Hastalık Kontrol ve Önleme Merkezleri (CDC)",
           "https://www.cdc.gov/birth-defects/about/anotia-microtia.html")
SRC_WHO = ("Deafness and hearing loss — Dünya Sağlık Örgütü (WHO)",
           "https://www.who.int/news-room/fact-sheets/detail/deafness-and-hearing-loss")

K_TEMEL = [SRC_SP, SRC_CDC]
K_ISITME = [SRC_ATR, SRC_WHO, SRC_SP]
K_CERRAHI = [SRC_SP, SRC_ATR]

BLOG_MIKROTIA = [

# ------------------------------------------------------------------ 1
{"slug": "mikrotia-nedir", "sources": K_TEMEL,
 "date": "2026-09-30",
 "cat": "Mikrotia",
 "title": "Mikrotia Nedir? Doğuştan Küçük veya Gelişmemiş Kulak",
 "ogtitle": "Mikrotia nedir, nasıl tedavi edilir?",
 "desc": "Mikrotia, kulak kepçesinin doğuştan küçük veya gelişmemiş olmasıdır. İşitmeyle ilişkisi, onarım seçenekleri ve mikrotia ameliyatının zamanlaması.",
 "h1": "Mikrotia nedir?",
 "lead": "Mikrotia, <strong>kulak kepçesinin doğuştan küçük, şekilsiz ya da hiç gelişmemiş olmasıdır</strong>. Çoğunlukla tek taraflıdır ve sıklıkla dış kulak yolunun da kapalı olmasıyla (atrezi) birlikte görülür. İki ayrı konu vardır ve karıştırılmamalıdır: <strong>kulağın görünümü</strong> plastik cerrahinin, <strong>işitme</strong> ise KBB ve odyolojinin alanıdır. İkisi birlikte planlanır ama aynı ameliyat değildir.",
 "watopic": "mikrotia değerlendirmesi",
 "related": ["mikrotia"],
 "sections": [
  {"id": "nedir", "tag": "Tanım", "h2": "Mikrotia tam olarak ne demek?", "body": [
   "\"Mikrotia\" kelime olarak <strong>küçük kulak</strong> demektir. Kulak kepçesinin gebeliğin erken haftalarında tam gelişmemesi sonucu ortaya çıkar. Kulağın hiç olmamasına ise <strong>anotia</strong> denir.",
   "Etkilenen kulak, normalin küçültülmüş bir kopyası değildir. Kıvrımlar, çukurluk ve kenar yapısı çoğu zaman yoktur; yerinde küçük bir doku parçası ve kulak memesi benzeri bir yapı bulunur.",
   ("note", "Mikrotia bir hastalık değil, bir <strong>gelişim farklılığıdır</strong>. Ağrı yapmaz, ilerlemez, bulaşıcı değildir. Sorun görünüm ve — atrezi eşlik ediyorsa — işitmedir."),
   ("h3", "Sık görülen özellikler"),
   ("ul", ["Çoğunlukla tek taraflıdır; sağ kulak daha sık etkilenir",
           "Erkeklerde biraz daha sık görülür",
           "Yaklaşık yarısında dış kulak yolu da kapalıdır (atrezi)",
           "Çoğu vakada iç kulak ve işitme siniri normaldir",
           "Bir bölümünde yüzün aynı tarafında gelişim farklılıkları eşlik eder"])]},

  {"id": "isitme", "tag": "İşitme", "h2": "Mikrotiada işitme nasıl etkilenir?", "body": [
   "Kulak kepçesi sesi toplar ama işitmenin asıl işi iç kulaktadır. Mikrotiada işitme kaybının nedeni kepçenin küçüklüğü değil, çoğu zaman ona eşlik eden <strong>dış kulak yolu kapalılığıdır</strong>.",
   ("ul", ["Dış kulak yolu kapalıysa sesin iç kulağa iletimi azalır — buna <strong>iletim tipi işitme kaybı</strong> denir",
           "İç kulak ve işitme siniri genellikle sağlamdır",
           "Tek taraflı vakalarda diğer kulak normalse konuşma gelişimi genellikle etkilenmez",
           "Çift taraflı vakalarda işitme desteği <strong>erken dönemde</strong> gereklidir"]),
   ("note", "<strong>Çift taraflı mikrotiada işitme değerlendirmesi ertelenemez.</strong> Konuşma gelişimi ilk yıllarda şekillendiği için, kemik yolu işitme cihazı gibi çözümler bebeklik döneminde gündeme gelir. Bu, kepçe onarımını beklemez.")]},

  {"id": "onarim", "tag": "Onarım", "h2": "Kulak kepçesi nasıl onarılır?", "body": [
   "İki ana yol vardır ve ikisi de aşamalı planlanır.",
   ("h3", "Kendi kaburga kıkırdağıyla onarım"),
   "Çocuğun kendi kaburga kıkırdağından bir kulak iskeleti şekillendirilir ve deri altına yerleştirilir. Genellikle 2-4 aşamada tamamlanır. Kendi dokusu olduğu için ömür boyu kalıcıdır ve büyümeyle uyumludur.",
   ("h3", "Sentetik iskelet (implant) ile onarım"),
   "Hazır gözenekli bir iskelet kullanılır ve ince bir doku örtüsüyle kaplanır. Daha az aşama gerektirir ve daha erken yaşta yapılabilir; buna karşılık darbe ve enfeksiyona karşı daha hassastır.",
   ("h3", "Protez kulak"),
   "Cerrahi onarımın uygun olmadığı ya da tercih edilmediği durumlarda, yapıştırılan veya implanta tutturulan protez kulak bir seçenektir.",
   ("note", "Hangi yolun seçileceği; çocuğun yaşı, kaburga gelişimi, derinin durumu, daha önce yapılmış girişimler ve ailenin tercihine göre belirlenir. Tek bir \"en iyi yöntem\" yoktur.")]},

  {"id": "zamanlama", "tag": "Zamanlama", "h2": "Ne zaman ameliyat edilir?", "body": [
   "Zamanlamayı belirleyen iki etken vardır: <strong>kaburga kıkırdağının yeterli boyuta ulaşması</strong> ve <strong>çocuğun sürece katılabilmesi</strong>.",
   ("ul", ["Kendi kıkırdağıyla onarımda genellikle <strong>okul çağı ve sonrası</strong> beklenir",
           "Sentetik iskelet daha erken yaşta uygulanabilir",
           "İşitme değerlendirmesi ise <strong>doğumdan hemen sonra</strong> yapılmalıdır — beklemez",
           "Atrezi cerrahisi düşünülüyorsa sıralama önemlidir; kepçe onarımı genellikle önce planlanır"]),
   ("note", "Sıklıkla sorulan \"bir an önce yapılsın\" isteği anlaşılırdır, ancak erken girişim yeterli kıkırdak olmadan yapılırsa sonucu kalıcı olarak sınırlayabilir. Buna karşılık <strong>işitmenin değerlendirilmesi hiç ertelenmemelidir</strong>.")]}],

 "faqs": [
  ("Mikrotia neden olur?",
   "Çoğu vakada tek bir neden gösterilemez. Gebeliğin erken haftalarında kulak kepçesini oluşturan yapıların gelişimindeki bir aksama sonucu ortaya çıkar. Bazı ilaçlar ve sendromlarla ilişkisi bilinmekle birlikte, vakaların büyük bölümünde bilinen bir neden ya da ailede benzer öykü yoktur."),
  ("Mikrotia işitme kaybına yol açar mı?",
   "Kulak kepçesinin kendisi işitmeyi belirleyen yapı değildir. İşitme kaybı, çoğunlukla ona eşlik eden dış kulak yolu kapalılığından kaynaklanır ve iletim tipindedir. İç kulak genellikle sağlamdır. Her mikrotia vakasında işitme mutlaka değerlendirilmelidir."),
  ("Tek kulakta mikrotia varsa çocuğum normal duyar mı?",
   "Diğer kulak normalse çocuk genellikle konuşmayı zamanında geliştirir. Ancak sesin geldiği yönü ayırt etme ve gürültülü ortamda anlama güçlüğü olabilir. Bu nedenle okul döneminde oturma düzeni gibi basit düzenlemeler yararlı olur."),
  ("Ameliyat kaç yaşında yapılır?",
   "Kendi kaburga kıkırdağıyla yapılan onarımda genellikle okul çağı ve sonrası beklenir, çünkü kıkırdağın yeterli boyuta ulaşması gerekir. Sentetik iskeletle daha erken yaşta yapılabilir. İşitme değerlendirmesi ise doğumdan hemen sonra yapılmalıdır."),
  ("Mikrotia ilerler mi, kötüleşir mi?",
   "Hayır. Mikrotia doğuştan var olan bir gelişim farklılığıdır; zamanla ilerlemez ya da kötüleşmez. Bu nedenle acil bir cerrahi durum değildir ve zamanlama sakin biçimde planlanabilir."),
  ("Hangi bölüme başvurmalıyım?",
   "Kulak kepçesinin onarımı için plastik ve rekonstrüktif cerrahi; işitme değerlendirmesi ve dış kulak yolu ile ilgili girişimler için KBB ve odyoloji. İki branşın birlikte planlama yapması en doğru yaklaşımdır.")]},

# ------------------------------------------------------------------ 2
{"slug": "bebegin-kulagi-dogustan-yok", "sources": K_TEMEL,
 "date": "2026-10-01",
 "cat": "Mikrotia",
 "title": "Bebeğimin Kulağı Doğuştan Yok: İlk Haftalarda Ne Yapmalı?",
 "ogtitle": "Bebeğin kulağı doğuştan yoksa ilk ne yapılır?",
 "desc": "Bebeğinizin kulağı doğuştan yok ya da küçükse ilk yapılması gereken işitme değerlendirmesidir. Ailelerin ilk haftalarda izlemesi gereken yol.",
 "h1": "Bebeğimin kulağı doğuştan yok, ne yapmalıyım?",
 "lead": "Bebeğinizin kulağı doğuştan yoksa ya da çok küçükse, ilk günlerin telaşı içinde sorulacak doğru soru \"ne zaman ameliyat olur\" değildir. Kulağın hiç olmamasına <strong>anotia</strong>, küçük ya da şekilsiz olmasına <strong>mikrotia</strong> denir. İkisi de aynı gelişim farklılığının farklı dereceleridir. Ailelerin doğumdan sonraki ilk haftalarda yapması gereken tek acil şey vardır: <strong>işitmenin değerlendirilmesi</strong>. Kulağın görünümüne yönelik onarım ise aylar, çoğu zaman yıllar sonra planlanır ve acele gerektirmez.",
 "watopic": "doğuştan kulak gelişmemesi hakkında bilgi",
 "related": ["mikrotia"],
 "sections": [
  {"id": "ayrim", "tag": "Ayrım", "h2": "Anotia mı, mikrotia mı?", "body": [
   ("table", ["", "Mikrotia", "Anotia"],
    [["Tanım", "Kulak küçük ya da şekilsiz", "Kulak kepçesi hiç yok"],
     ["Görünüm", "Kıvrımlar kısmen olabilir", "Yerinde doku parçası olabilir ya da hiç olmayabilir"],
     ["Sıklık", "Daha sık", "Daha nadir"],
     ["Dış kulak yolu", "Sıklıkla kapalı", "Genellikle kapalı"],
     ["Onarım", "Aşamalı cerrahi ya da protez", "Aşamalı cerrahi ya da protez"]]),
   ("note", "Adlandırma farklı olsa da yaklaşım aynı mantıkta ilerler: önce işitme, sonra görünüm. Anotia daha az doku demektir; bu, onarım planlamasını etkiler ama seçenekleri ortadan kaldırmaz.")]},

  {"id": "ilk-adim", "tag": "İlk adımlar", "h2": "Doğumdan sonraki ilk haftalarda ne yapılmalı?", "body": [
   ("steps", [
    ("İŞİTME TARAMASI", "Her yenidoğana yapılan tarama, mikrotia varlığında ayrıca dikkatle değerlendirilir. Çift taraflıysa ileri odyolojik inceleme gecikmeden yapılır."),
    ("GENEL DEĞERLENDİRME", "Mikrotiaya eşlik edebilecek durumlar açısından çocuk hekimi tarafından genel muayene yapılır."),
    ("KBB DEĞERLENDİRMESİ", "Dış kulak yolunun durumu ve orta kulak yapıları incelenir. Gerekirse görüntüleme planlanır."),
    ("PLASTİK CERRAHİ GÖRÜŞMESİ", "Acil değildir, ancak aileye yol haritasını anlatmak için erken bir görüşme yararlıdır.")]),
   ("note", "<strong>Çift taraflı tutulumda işitme desteği ertelenemez.</strong> Konuşma ve dil gelişimi ilk yıllarda şekillenir; kemik yolu işitme cihazı gibi çözümler bebeklik döneminde değerlendirilir ve kepçe onarımını beklemez.")]},

  {"id": "beklemek", "tag": "Zamanlama", "h2": "Neden hemen ameliyat edilmiyor?", "body": [
   "Ailelerin en sık sorduğu soru budur ve tamamen anlaşılırdır. Cevap, beklemenin ihmal değil <strong>teknik bir gereklilik</strong> olmasıdır.",
   ("ul", ["Kendi kaburga kıkırdağıyla onarımda, kıkırdağın bir kulak iskeleti çıkaracak boyuta ulaşması gerekir",
           "Sağlıklı kulak da büyümeye devam eder; iki kulağın uyumu için gelişimin belli bir noktaya gelmesi beklenir",
           "Çocuğun ameliyat sonrası bakım kurallarına uyabilecek olgunlukta olması sonucu doğrudan etkiler",
           "Erken ve yetersiz bir girişim, deriyi ve dokuyu bozarak ileride yapılacak onarımı zorlaştırabilir"]),
   ("note", "Bekleme dönemi boş geçmez: işitme takibi, konuşma gelişiminin izlenmesi ve gerekiyorsa destek bu dönemde yürütülür.")]},

  {"id": "aile", "tag": "Aile", "h2": "Aileler için birkaç not", "body": [
   ("ul", ["<strong>Kendinizi suçlamayın:</strong> mikrotianın vakaların büyük bölümünde bilinen bir nedeni yoktur ve gebelikte yapılan bir şeyden kaynaklanmaz",
           "<strong>Kardeş riski düşüktür:</strong> çoğu vaka tek başınadır; yine de genetik danışmanlık istenebilir",
           "<strong>Okul döneminden önce plan yapın:</strong> çocuklar farklılığı okul çağında fark eder; hazırlık yapmak süreci kolaylaştırır",
           "<strong>Saç kesimi ve kıyafet:</strong> çocuğun kendini rahat hissettiği seçimler, cerrahi zamanlamasına kadar destekleyicidir"]),
   ("note", "Çocuğun psikolojik hazırlığı, cerrahi planlamanın bir parçasıdır. Ameliyat kararında çocuğun kendi isteği — yaşı uygunsa — mutlaka dikkate alınmalıdır.")]}],

 "faqs": [
  ("Doğuştan kulak olmaması tedavi edilebilir mi?",
   "Kulak kepçesi, kendi kaburga kıkırdağından ya da sentetik bir iskeletten şekillendirilerek onarılabilir. Bu aşamalı bir cerrahi süreçtir. Cerrahinin uygun olmadığı durumlarda protez kulak bir seçenektir. İşitme ise ayrı bir konudur ve KBB tarafından değerlendirilir."),
  ("Bebeğimin işitmesi normal mi, nasıl anlarım?",
   "Yenidoğan işitme taraması ilk adımdır, ancak mikrotia varlığında bu tarama tek başına yeterli sayılmaz. KBB ve odyoloji tarafından ayrıntılı değerlendirme yapılmalıdır. Özellikle çift taraflı tutulumda bu değerlendirme geciktirilmemelidir."),
  ("Kardeşinde de olur mu?",
   "Vakaların büyük bölümü tek başınadır ve kardeşte görülme olasılığı düşüktür. Ailede birden fazla etkilenen kişi varsa ya da bir sendrom düşünülüyorsa genetik danışmanlık önerilir."),
  ("Gebelikte yaptığım bir şeyden mi kaynaklandı?",
   "Vakaların büyük bölümünde bilinen bir neden yoktur. Bazı ilaçlarla ilişkisi bilinse de, tipik bir mikrotia vakası annenin gebelikte yaptığı ya da yapmadığı bir şeyden kaynaklanmaz."),
  ("Protez kulak kalıcı bir çözüm müdür?",
   "Protez, günlük olarak takılıp çıkarılan ya da implanta tutturulan bir seçenektir. Görünüm açısından oldukça başarılı sonuçlar verebilir, ancak kendi dokusuyla yapılan onarımdan farklı olarak bakım ve düzenli yenileme gerektirir.")]},

# ------------------------------------------------------------------ 3
{"slug": "mikrotia-tipleri", "sources": K_TEMEL,
 "date": "2026-10-02",
 "cat": "Mikrotia",
 "title": "Mikrotia Tipleri ve Dereceleri: Grade 1, 2, 3 ve Anotia",
 "ogtitle": "Mikrotia tipleri nasıl ayrılır?",
 "desc": "Mikrotia dört tipe ayrılır. Grade 1'de kulak küçük ama şekli belli, Grade 3'te sadece doku parçası vardır. Tip, onarım planını nasıl değiştirir?",
 "h1": "Mikrotia tipleri ve dereceleri",
 "lead": "Mikrotia, kulak kepçesinde ne kadar yapı kaldığına göre <strong>dört tipe</strong> ayrılır; literatürde bunlara <strong>Grade 1, 2, 3 ve anotia</strong> denir. Grade 1'de kulak küçüktür ama biçimi tanınabilir; Grade 3'te yalnızca küçük bir doku parçası ve memeye benzer bir yapı bulunur; anotiada kepçe hiç yoktur. Bu ayrım yalnızca bir tanımlama değildir — <strong>hangi onarım yönteminin uygun olacağını doğrudan belirler</strong>.",
 "watopic": "mikrotia derecesinin belirlenmesi",
 "related": ["mikrotia"],
 "sections": [
  {"id": "tablo", "tag": "Derecelendirme", "h2": "Dört derece bir arada", "body": [
   ("table", ["Derece", "Görünüm", "Onarımda öne çıkan"],
    [["Grade 1", "Kulak küçük; kıvrımların çoğu var", "Sınırlı düzeltme yeterli olabilir"],
     ["Grade 2", "Kulağın alt bölümü var; üst kısım eksik", "Kısmi iskelet ve şekillendirme"],
     ["Grade 3", "Yalnızca doku parçası ve meme benzeri yapı", "Tam iskelet ile aşamalı onarım"],
     ["Anotia", "Kepçe hiç yok", "Tam iskelet ya da protez"]]),
   ("note", "Derecelendirme, görünümü tarif eder — işitmeyi tarif etmez. Grade 1 bir kulakta da dış kulak yolu kapalı olabilir. <strong>İşitme her derecede ayrıca değerlendirilir.</strong>")]},

  {"id": "grade12", "tag": "Grade 1-2", "h2": "Grade 1 ve 2: yapı kısmen var", "body": [
   ("h3", "Grade 1"),
   "Kulak normalden küçüktür ama kıvrımlar, çukurluk ve kenar büyük ölçüde tanınabilir. Dış kulak yolu açık olabilir. Onarımda çoğu zaman <strong>tam bir iskelet gerekmez</strong>; boyut ve şekil düzeltmeleriyle sonuç alınabilir.",
   ("h3", "Grade 2"),
   "Kulağın alt bölümü ve memesi genellikle vardır, üst kısım eksiktir. Onarımda eksik bölüm için <strong>kısmi bir iskelet</strong> hazırlanır ve mevcut yapıyla birleştirilir.",
   ("note", "Grade 1 ve 2'de mevcut dokunun korunması önemlidir. Bu bölgeye yapılan gereksiz girişimler, ileride kullanılacak deriyi ve kan dolaşımını bozabilir.")]},

  {"id": "grade3", "tag": "Grade 3", "h2": "Grade 3: en sık görülen tablo", "body": [
   "Mikrotianın en sık görülen biçimidir. Kulak yerinde, öne ya da yukarı doğru duran küçük bir doku parçası ve kulak memesine benzeyen bir yapı bulunur. Kıvrımlar yoktur.",
   ("ul", ["Dış kulak yolu genellikle kapalıdır",
           "Onarımda <strong>tam bir kulak iskeleti</strong> hazırlanması gerekir",
           "Süreç genellikle 2-4 aşamada tamamlanır",
           "Mevcut doku parçası, onarımda meme yapısı olarak değerlendirilebilir"]),
   ("note", "Grade 3, \"en ağır\" derece değildir — en sık görülenidir ve onarım sonuçları genellikle yüz güldürücüdür. Derecenin yüksek olması sonucun kötü olacağı anlamına gelmez.")]},

  {"id": "anotia", "tag": "Anotia", "h2": "Anotia: kepçe hiç yok", "body": [
   "Kulak kepçesinin hiç bulunmamasıdır. Daha nadirdir ve genellikle dış kulak yolu da kapalıdır.",
   ("ul", ["Onarımda tam iskelet gerekir",
           "Bölgede kullanılabilir doku daha az olduğu için planlama daha titizdir",
           "Deri örtüsü için ek yöntemler (doku genişletici, fasyal flep) gerekebilir",
           "Protez kulak, özellikle doku yetersizliğinde güçlü bir seçenektir"]),
   ("note", "Anotiada da onarım mümkündür. \"Hiç kulak yok, yapılacak bir şey yok\" bilgisi güncel değildir.")]},

  {"id": "karar", "tag": "Karar", "h2": "Derece tedavi kararını nasıl değiştirir?", "body": [
   ("ul", ["<strong>Aşama sayısı:</strong> derece yükseldikçe genellikle daha fazla aşama gerekir",
           "<strong>Kıkırdak miktarı:</strong> tam iskelet daha fazla kaburga kıkırdağı gerektirir; bu, yaş beklentisini etkiler",
           "<strong>Deri örtüsü:</strong> mevcut deri yetersizse ek yöntemler planlanır",
           "<strong>Protez seçeneği:</strong> doku çok yetersizse ya da aile tercih ederse öne çıkar"]),
   "Derece tek başına karar vermez. Çocuğun yaşı, kaburga gelişimi, daha önce yapılmış girişimler ve ailenin beklentisi de plana girer."]}],

 "faqs": [
  ("Mikrotia derecesi nasıl belirlenir?",
   "Muayeneyle belirlenir; kulakta ne kadar yapı kaldığına bakılır. Ek görüntüleme genellikle kepçe için değil, dış kulak yolu ve orta kulak yapılarını değerlendirmek için istenir."),
  ("Grade 3 ağır bir durum mu?",
   "Grade 3, mikrotianın en sık görülen biçimidir ve onarım sonuçları genellikle iyidir. Derecenin yüksek olması daha fazla aşama gerektirebilir, ancak sonucun kötü olacağı anlamına gelmez."),
  ("Grade 1'de ameliyat gerekir mi?",
   "Her zaman değil. Kulak küçük ama biçimi tanınabilir durumdaysa, aile ve çocuk görünümden rahatsız değilse girişim gerekmeyebilir. Karar, tıbbi bir zorunluluktan çok kişisel tercihle verilir. İşitme ayrıca değerlendirilir."),
  ("Derece işitme kaybının şiddetini gösterir mi?",
   "Hayır. Derecelendirme yalnızca kulak kepçesinin görünümünü tanımlar. Dış kulak yolunun açık ya da kapalı olması ile orta kulak yapılarının durumu, dereceden bağımsız olarak değerlendirilir."),
  ("İki kulağın derecesi farklı olabilir mi?",
   "Evet. Çift taraflı vakalarda iki kulak farklı derecelerde olabilir ve her biri için ayrı plan yapılır. Çift taraflı tutulumda işitme desteği önceliklidir.")]},

# ------------------------------------------------------------------ 4
{"slug": "mikrotia-ameliyati-kac-yasinda-yapilir", "sources": K_CERRAHI,
 "date": "2026-10-03",
 "cat": "Mikrotia",
 "title": "Mikrotia Ameliyatı Kaç Yaşında Yapılır?",
 "ogtitle": "Mikrotia ameliyatı için doğru yaş",
 "desc": "Kendi kıkırdağıyla onarımda okul çağı beklenir, sentetik iskelet daha erken yapılabilir. İşitme değerlendirmesi ise ertelenmez. Zamanlamayı belirleyenler.",
 "h1": "Mikrotia ameliyatı ne zaman yapılır?",
 "lead": "\"Mikrotia ameliyatı kaç yaşında yapılır?\" sorusunun tek bir sayıyla cevabı yoktur, ama net bir kural vardır: <strong>işitme değerlendirmesi beklemez, kepçe onarımı bekler</strong>. Kendi kaburga kıkırdağıyla yapılan onarımda genellikle <strong>okul çağı ve sonrası</strong> beklenir, çünkü kıkırdağın bir kulak iskeleti çıkaracak boyuta ulaşması gerekir. Sentetik iskeletle daha erken yaşta girişim mümkündür.",
 "watopic": "mikrotia ameliyatı zamanlaması",
 "related": ["mikrotia"],
 "sections": [
  {"id": "iki-saat", "tag": "İki ayrı takvim", "h2": "Kaç yaşında? İşitme ve görünüm için iki ayrı takvim", "body": [
   ("table", ["", "İşitme", "Kulak kepçesi"],
    [["Değerlendirme zamanı", "Doğumdan hemen sonra", "Okul öncesi dönemde planlama"],
     ["Aciliyet", "Çift taraflıysa acil", "Acil değil"],
     ["Sorumlu branş", "KBB ve odyoloji", "Plastik ve rekonstrüktif cerrahi"],
     ["Gecikmenin bedeli", "Konuşma ve dil gelişimi", "Yok — bekleme sonucu iyileştirir"]]),
   ("note", "Bu tablo, ailelerin en sık karıştırdığı noktayı netleştirmek içindir. Kepçe onarımını beklemek bir ihmal değildir; işitme değerlendirmesini ertelemek ise telafisi zor sonuçlar doğurabilir.")]},

  {"id": "kikirdak", "tag": "Kıkırdak", "h2": "Neden kaburga gelişimi bekleniyor?", "body": [
   "Kendi dokusuyla yapılan onarımda kulak iskeleti, çocuğun <strong>kendi kaburga kıkırdağından</strong> elde edilir. Bu iskeletin sağlıklı kulakla uyumlu boyutta olabilmesi için yeterli kıkırdak gerekir.",
   ("ul", ["Yetersiz kıkırdakla yapılan iskelet, küçük ve zayıf kalır",
           "Kıkırdağın alındığı bölgede göğüs duvarı gelişiminin belli bir noktaya gelmesi tercih edilir",
           "Sağlıklı kulak da büyümeye devam eder; iki kulağın uyumu için gelişim hızının yavaşlaması beklenir"]),
   ("note", "Beklemenin karşılığı somuttur: yeterli kıkırdakla yapılan iskelet, kıvrımları belirgin ve kalıcı bir kulak verir. Erken yapılan ve yetersiz kalan bir onarımı düzeltmek, sıfırdan yapmaktan zordur.")]},

  {"id": "sentetik", "tag": "Alternatif", "h2": "Sentetik iskelet daha erken yapılabilir mi?", "body": [
   "Evet. Hazır gözenekli iskelet kullanıldığında kaburga gelişimi beklenmez ve girişim daha erken yaşta yapılabilir. Aşama sayısı da genellikle daha azdır.",
   ("ul", ["<strong>Avantajı:</strong> erken yaş, daha az aşama, göğüsten kıkırdak alınmaması",
           "<strong>Dezavantajı:</strong> darbe ve enfeksiyona karşı daha hassas, uzun vadeli açığa çıkma riski",
           "<strong>Gereklilik:</strong> iskeletin ince bir doku örtüsüyle güvenle kaplanması şarttır"]),
   ("note", "İki yöntemin de savunucuları vardır ve ikisi de dünyada yaygın olarak uygulanır. Karar, çocuğun durumu ve ailenin bilgilendirilmiş tercihiyle verilmelidir — tek doğru bir yöntem yoktur.")]},

  {"id": "sira", "tag": "Sıralama", "h2": "Atrezi ameliyatı da gerekiyorsa sıra ne olmalı?", "body": [
   "Dış kulak yolunun açılması (atrezi cerrahisi) düşünülüyorsa, sıralama önem kazanır.",
   ("ul", ["Kepçe onarımı genellikle <strong>önce</strong> planlanır",
           "Çünkü atrezi cerrahisi bölgedeki deriyi ve dokuyu değiştirir; bu, kepçe onarımını zorlaştırabilir",
           "Sıralama, KBB ve plastik cerrahinin birlikte kararıyla belirlenir",
           "Her çocukta atrezi cerrahisi uygun olmayabilir; iç kulak ve orta kulak yapıları belirleyicidir"]),
   ("note", "Atrezi cerrahisi bir işitme ameliyatıdır ve her hastada uygun değildir. Uygun olmadığı durumlarda kemik yolu işitme çözümleri gündeme gelir. Bu karar KBB'ye aittir.")]},

  {"id": "cocuk", "tag": "Çocuğun rolü", "h2": "Çocuğun hazır olması ne demek?", "body": [
   ("ul", ["Ameliyat sonrası sargı ve bakım kurallarına uyabilmesi",
           "Kulağın üzerine yatmamak gibi kısıtlamaları anlayabilmesi",
           "Sürecin neden yapıldığını kavrayabilmesi",
           "Kendi isteğinin sorulabileceği bir yaşta olması"]),
   ("note", "Onarım, çocuğun kendisi için yapılır. Yaşı uygunsa kararın bir parçası olması, hem uyumu hem de sonuçtan duyduğu memnuniyeti artırır.")]}],

 "faqs": [
  ("Mikrotia ameliyatı için en uygun yaş kaçtır?",
   "Kendi kaburga kıkırdağıyla yapılan onarımda genellikle okul çağı ve sonrası tercih edilir; belirleyici olan yaş değil, kıkırdağın yeterli boyuta ulaşmış olmasıdır. Sentetik iskeletle daha erken yaşta girişim mümkündür. Kesin yaş, muayene ve değerlendirmeyle belirlenir."),
  ("Erken yaptırsak daha iyi olmaz mı?",
   "Kepçe onarımı için hayır. Yetersiz kıkırdakla yapılan iskelet küçük ve zayıf kalır; bunu sonradan düzeltmek sıfırdan yapmaktan zordur. Buna karşılık işitme değerlendirmesi ve gerekiyorsa işitme desteği asla ertelenmemelidir."),
  ("Okul döneminde çocuğum zorlanır mı?",
   "Çocuklar farklılığı okul çağında fark eder ve bu dönem zorlayıcı olabilir. Bu nedenle onarımın okul çağına yakın planlanması sık tercih edilir. Bekleme döneminde çocuğun psikolojik olarak desteklenmesi, planın bir parçası sayılmalıdır."),
  ("Yetişkin yaşta yaptırabilir miyim?",
   "Evet. Mikrotia onarımı yetişkin yaşta da yapılabilir ve sonuçları başarılıdır. Kıkırdak gelişimi tamamlandığı için zamanlama açısından bir engel yoktur. Daha önce yapılmış girişimler varsa planlama buna göre yapılır."),
  ("Ameliyat kaç aşamada biter?",
   "Kendi kıkırdağıyla yapılan onarımda genellikle 2-4 aşama gerekir ve aşamalar arasında birkaç ay beklenir. Sentetik iskeletle aşama sayısı daha azdır. Toplam süre, derece ve seçilen yönteme göre değişir.")]},

# ------------------------------------------------------------------ 5
{"slug": "mikrotia-ameliyati-nasil-yapilir", "sources": K_CERRAHI,
 "date": "2026-10-04",
 "cat": "Tedavi",
 "title": "Mikrotia Ameliyatı Nedir, Nasıl Yapılır? Aşamalar",
 "ogtitle": "Mikrotia ameliyatı nasıl yapılır?",
 "desc": "Mikrotia ameliyatında kulak iskeleti kaburga kıkırdağından şekillendirilir ve deri altına yerleştirilir. Aşamalar, kulağın kaldırılması ve beklenen sonuç.",
 "h1": "Mikrotia ameliyatı nasıl yapılır?",
 "lead": "Mikrotia ameliyatı nedir? Kısaca: gelişmemiş kulak kepçesinin yerine yeni bir kulak yapılmasıdır. Bu, <strong>tek bir ameliyat değil, aşamalı bir süreçtir</strong>. En yaygın yöntemde çocuğun kendi kaburga kıkırdağından bir kulak iskeleti şekillendirilir, kulak bölgesindeki derinin altına yerleştirilir ve sonraki aşamalarda kulak baştan ayrılarak doğal açısı verilir. Süreç genellikle <strong>2-4 aşamada</strong> tamamlanır ve aşamalar arasında birkaç ay beklenir.",
 "watopic": "mikrotia ameliyatı planlaması",
 "related": ["mikrotia"],
 "sections": [
  {"id": "hazirlik", "tag": "Hazırlık", "h2": "Ameliyat öncesi hazırlık", "body": [
   ("ul", ["<strong>İşitme değerlendirmesi:</strong> KBB ve odyoloji tarafından tamamlanmış olmalıdır",
           "<strong>Şablon çıkarma:</strong> sağlıklı kulağın ölçüsü alınarak iskelet için şablon hazırlanır",
           "<strong>Kaburga değerlendirmesi:</strong> kıkırdağın yeterliliği kontrol edilir",
           "<strong>Deri durumu:</strong> daha önce yapılmış girişimler ve nedbeler değerlendirilir",
           "<strong>Saç çizgisi planlaması:</strong> kulak bölgesindeki saç dağılımı sonucu etkiler"]),
   ("note", "Sağlıklı kulaktan çıkarılan şablon, bu ameliyatın en belirleyici hazırlık adımıdır. Simetri, ameliyat masasında değil, bu şablonda kazanılır.")]},

  {"id": "asamalar", "tag": "Aşamalar", "h2": "Ameliyatın aşamaları", "body": [
   ("steps", [
    ("1. AŞAMA — İSKELETİN YERLEŞTİRİLMESİ", "Kaburga kıkırdağı alınır, şablona göre bir kulak iskeleti oyularak şekillendirilir ve kulak bölgesinde hazırlanan deri cebine yerleştirilir. Bu aşama sonucun temelini belirler."),
    ("2. AŞAMA — MEME AKTARIMI", "Mevcut doku parçası, yeni kulağın meme bölgesini oluşturacak şekilde konumlandırılır. Bazı planlamalarda bu adım birinci aşamayla birleştirilir."),
    ("3. AŞAMA — KULAĞIN KALDIRILMASI", "Kulak, baştan ayrılarak doğal açısı verilir. Arkada oluşan alan bir doku örtüsü ve deri greftiyle kapatılır."),
    ("4. AŞAMA — İNCE DÜZELTMELER", "Simetri, kıvrım derinliği ve çukurluk için küçük düzeltmeler yapılır. Her hastada gerekmez.")]),
   ("note", "Aşamalar arasında genellikle 3-6 ay beklenir. Bu süre, dokunun iyileşmesi ve iskeletin yerleşmesi için gereklidir — acele edildiğinde sonuç kalıcı olarak etkilenir.")]},

  {"id": "kaburga", "tag": "Kaburga", "h2": "Kaburgadan kıkırdak alınması sorun yaratır mı?", "body": [
   "Ailelerin en çok endişelendiği konudur. Alınan kıkırdak, göğüs kafesinin ön alt bölümündendir ve <strong>kemik değil kıkırdak</strong> kısmıdır.",
   ("ul", ["Alınan bölgede zamanla bir miktar yeniden kıkırdak oluşumu görülebilir",
           "Göğüs duvarında hafif bir kontur farkı kalabilir",
           "İlk günlerde derin nefes alırken ağrı olur; bu birkaç haftada geriler",
           "Nefes alma kapasitesinde kalıcı bir kısıtlama beklenmez"]),
   ("note", "Kıkırdağın yeterli gelişime ulaşmasının beklenmesinin bir nedeni de budur: yeterli boyutta kıkırdak, göğüs duvarından daha az doku alınarak elde edilebilir.")]},

  {"id": "sonuc", "tag": "Beklenti", "h2": "Ne beklemeli, ne beklememeli?", "body": [
   ("ul", ["<strong>Beklenebilir:</strong> saç kesimi ve günlük yaşamda dikkat çekmeyen, doğal konumlu bir kulak",
           "<strong>Beklenebilir:</strong> kalıcı bir sonuç — kendi dokusu olduğu için büyümeyle uyumludur",
           "<strong>Beklenebilir:</strong> gözlük ve maske takabilme",
           "<strong>Beklenmemeli:</strong> sağlıklı kulağın birebir kopyası — hedef benzerlik ve doğallıktır",
           "<strong>Beklenmemeli:</strong> işitmenin düzelmesi — kepçe onarımı bir işitme ameliyatı değildir"]),
   ("note", "Bu ameliyatta başarı ölçütü, kulağın yakından incelendiğinde kusursuz olması değil; <strong>çocuğun günlük yaşamda fark edilmeden dolaşabilmesidir</strong>.")]}],

 "faqs": [
  ("Mikrotia ameliyatı işitmeyi düzeltir mi?",
   "Hayır. Kulak kepçesinin onarımı görünüme yöneliktir. İşitme, dış kulak yolunun ve orta kulak yapılarının durumuna bağlıdır ve KBB tarafından ayrıca değerlendirilir. İki süreç birlikte planlanır ama aynı ameliyat değildir."),
  ("Kaç ameliyat gerekecek?",
   "Kendi kaburga kıkırdağıyla yapılan onarımda genellikle 2-4 aşama gerekir. Sentetik iskeletle aşama sayısı daha azdır. Kesin sayı, mikrotianın derecesine ve seçilen yönteme göre belirlenir."),
  ("Aşamalar arasında ne kadar beklenir?",
   "Genellikle 3-6 ay. Bu süre dokunun iyileşmesi ve iskeletin yerleşmesi için gereklidir. Aceleyle yapılan ikinci aşama, ilk aşamada elde edilen sonucu bozabilir."),
  ("Kaburgadan kıkırdak almak çocuğuma zarar verir mi?",
   "Alınan bölge kemik değil kıkırdaktır. İlk haftalarda derin nefes alırken ağrı olur ve bu geriler. Göğüs duvarında hafif bir kontur farkı kalabilir, ancak nefes alma kapasitesinde kalıcı bir kısıtlama beklenmez."),
  ("Ameliyattan sonra spor yapabilir mi?",
   "İyileşme tamamlandıktan sonra çoğu spora dönülebilir. Ancak kulağa doğrudan darbe gelme riski olan sporlarda — özellikle sentetik iskelet kullanıldıysa — dikkatli olunması önerilir. Yüzme, hekim onayıyla belirlenen tarihte başlar."),
  ("Yapılan kulak zamanla değişir mi?",
   "Kendi kıkırdağından yapılan iskelet canlı dokudur ve çocukla birlikte uyumlu biçimde kalır. Sentetik iskelet ise büyümez; bu nedenle boyutlandırma planlaması farklı yapılır.")]},

# ------------------------------------------------------------------ 6
{"slug": "mikrotia-kaburga-kikirdagi-mi-implant-mi", "sources": K_CERRAHI,
 "date": "2026-10-05",
 "cat": "Tedavi",
 "title": "Mikrotia Ameliyatında Kaburga Kıkırdağı mı, İmplant mı?",
 "ogtitle": "Mikrotia onarımında iki yöntem karşılaştırması",
 "desc": "Kendi kaburga kıkırdağı kalıcıdır ama daha ileri yaş ve daha fazla aşama ister. Sentetik iskelet erken yapılır ama darbeye hassastır. Karşılaştırma.",
 "h1": "Kaburga kıkırdağı mı, sentetik iskelet mi?",
 "lead": "Mikrotia onarımında iki ana yol vardır ve ikisi de dünyada yaygın olarak uygulanır. <strong>Kendi kaburga kıkırdağı</strong> kalıcıdır ve büyümeyle uyumludur; buna karşılık daha ileri yaş ve daha fazla aşama gerektirir. <strong>Sentetik iskelet</strong> daha erken yaşta ve daha az aşamada sonuç verir; ancak darbeye ve enfeksiyona karşı daha hassastır. Tek bir doğru yöntem yoktur — karar bilgilendirilmiş bir tercihtir.",
 "watopic": "mikrotia onarımında yöntem seçimi",
 "related": ["mikrotia"],
 "sections": [
  {"id": "tablo", "tag": "Karşılaştırma", "h2": "İki yöntem yan yana", "body": [
   ("table", ["", "Kendi kaburga kıkırdağı", "Sentetik iskelet"],
    [["Uygulama yaşı", "Kaburga gelişimi beklenir", "Daha erken mümkün"],
     ["Aşama sayısı", "Genellikle 2-4", "Genellikle daha az"],
     ["Göğüsten doku alınması", "Var", "Yok"],
     ["Büyümeyle uyum", "Canlı doku; uyumlu kalır", "Büyümez; boyut baştan planlanır"],
     ["Darbeye dayanıklılık", "Daha dayanıklı", "Daha hassas"],
     ["Enfeksiyon ve açığa çıkma", "Daha düşük risk", "Daha yüksek risk"],
     ["Doku örtüsü gereksinimi", "Deri cebi yeterli olabilir", "İnce fasya örtüsü şart"]])]},

  {"id": "kaburga", "tag": "Kendi kıkırdağı", "h2": "Kendi kaburga kıkırdağıyla onarım", "body": [
   "Uzun yıllardır uygulanan ve en çok uzun dönem verisi bulunan yöntemdir. İskelet, çocuğun kendi kıkırdağından oyularak şekillendirilir.",
   ("h3", "Güçlü yanları"),
   ("ul", ["Canlı, kendi dokusudur — reddedilme ya da yabancı cisim sorunu olmaz",
           "Darbeye ve enfeksiyona karşı daha dayanıklıdır",
           "Uzun vadede açığa çıkma riski belirgin şekilde düşüktür",
           "Çocukla birlikte uyumlu kalır"]),
   ("h3", "Zorlukları"),
   ("ul", ["Kaburga gelişiminin beklenmesi gerekir",
           "Göğüsten kıkırdak alınması ek bir iyileşme süreci demektir",
           "Daha fazla aşama ve daha uzun toplam süre",
           "Sonuç, iskeletin oyulmasındaki ustalığa doğrudan bağlıdır"])]},

  {"id": "sentetik", "tag": "Sentetik", "h2": "Sentetik iskeletle onarım", "body": [
   "Hazır, gözenekli bir iskelet — hastaların sıklıkla <strong>implant</strong> dediği yapı — kullanılır. İskeletin çevre dokuyla bütünleşebilmesi için ince bir fasya örtüsüyle kaplanması ve üzerine deri grefti uygulanması gerekir.",
   ("h3", "Güçlü yanları"),
   ("ul", ["Daha erken yaşta uygulanabilir",
           "Göğüsten doku alınmaz",
           "Genellikle daha az aşama gerektirir",
           "İskelet hazır olduğu için kıvrım ayrıntısı baştan bellidir"]),
   ("h3", "Zorlukları"),
   ("ul", ["Darbeye karşı daha hassastır",
           "Zaman içinde deriden açığa çıkma riski taşır",
           "Enfeksiyon gelişirse iskeletin çıkarılması gerekebilir",
           "Büyümez; boyutlandırma baştan ileriye dönük planlanır"]),
   ("note", "Sentetik iskelette fasya örtüsünün kalitesi, uzun vadeli sonucu belirleyen en kritik unsurdur. Bu, yöntemin kendisinden çok uygulanışıyla ilgili bir konudur.")]},

  {"id": "karar", "tag": "Karar", "h2": "Karar nasıl verilir?", "body": [
   "Aşağıdaki başlıklar, görüşmede birlikte değerlendirilir:",
   ("ul", ["<strong>Çocuğun yaşı:</strong> beklemek mümkün mü, okul dönemi ne zaman başlıyor",
           "<strong>Kaburga gelişimi:</strong> yeterli kıkırdak var mı",
           "<strong>Deri durumu:</strong> daha önce girişim yapılmış mı, nedbe var mı",
           "<strong>Yaşam biçimi:</strong> temaslı spor yapıyor mu",
           "<strong>Ailenin beklentisi:</strong> aşama sayısı, toplam süre, göğüsten doku alınması"]),
   ("note", "İki yöntemden birini kesin olarak üstün gösteren bir sonuç yoktur; ikisi de deneyimli ellerde yüz güldürücü sonuçlar verir. Size tek bir yöntemi \"tek doğru\" olarak sunan bir yaklaşımla karşılaşırsanız, ikinci bir görüş almak yerinde olur.")]}],

 "faqs": [
  ("Hangi yöntem daha iyi sonuç verir?",
   "İkisi de deneyimli ellerde doğal görünümlü sonuçlar verir. Kendi kıkırdağı uzun vadede daha dayanıklıdır; sentetik iskelet daha erken ve daha az aşamada sonuç sağlar. Seçim, çocuğun durumu ve ailenin önceliklerine göre yapılır."),
  ("Sentetik iskelet vücut tarafından reddedilir mi?",
   "Bu malzemeler bağışıklık sistemi tarafından reddedilmez; asıl risk, zamanla deriden açığa çıkması ve enfeksiyondur. Bu riski azaltan en önemli etken, iskeletin ince bir fasya örtüsüyle güvenle kaplanmasıdır."),
  ("Sentetik iskelet çocukla birlikte büyür mü?",
   "Hayır, büyümez. Bu nedenle boyutlandırma ileriye dönük planlanır. Kendi kıkırdağından yapılan iskelet ise canlı dokudur ve uyumlu kalır."),
  ("Çocuğum futbol oynuyor, hangisi daha uygun?",
   "Kulağa darbe gelme olasılığı yüksekse kendi kıkırdağıyla yapılan onarım daha dayanıklıdır. Bu, tek başına karar verdiren bir etken değildir, ancak değerlendirmede ağırlığı vardır."),
  ("Sonradan yöntem değiştirilebilir mi?",
   "Sentetik iskelet çıkarılmak zorunda kalırsa, sonrasında kendi kıkırdağıyla onarım genellikle mümkündür. Ancak bölgedeki deri ve nedbe durumu planlamayı zorlaştırır. Bu nedenle ilk kararın dikkatli verilmesi önemlidir.")]},

# ------------------------------------------------------------------ 7
{"slug": "mikrotia-isitme-kaybi", "sources": K_ISITME,
 "date": "2026-10-06",
 "cat": "Mikrotia",
 "title": "Mikrotiada İşitme Kaybı: Atrezi ve Çözüm Seçenekleri",
 "ogtitle": "Mikrotiada işitme kaybı nasıl değerlendirilir?",
 "desc": "Mikrotiada işitme kaybı genellikle dış kulak yolu kapalılığından kaynaklanır. Değerlendirme zamanı, kemik yolu cihazları ve atrezi cerrahisi seçenekleri.",
 "h1": "Mikrotiada işitme kaybı",
 "lead": "Mikrotiada işitmeyi belirleyen şey kulak kepçesinin küçüklüğü değil, çoğu zaman ona eşlik eden <strong>dış kulak yolu kapalılığıdır (atrezi)</strong>. Bu durumda ses iç kulağa yeterince iletilemez — buna <strong>iletim tipi işitme kaybı</strong> denir. İyi haber şu: vakaların büyük bölümünde <strong>iç kulak ve işitme siniri sağlamdır</strong>, yani sesi iç kulağa ulaştıracak bir yol bulunduğunda işitme sağlanabilir.",
 "watopic": "mikrotiada işitme değerlendirmesi",
 "related": ["mikrotia"],
 "sections": [
  {"id": "neden", "tag": "Mekanizma", "h2": "İşitme neden etkileniyor?", "body": [
   "Ses, dış kulak yolundan geçip kulak zarına ulaşır; oradan orta kulak kemikçikleriyle iç kulağa iletilir. Dış kulak yolu kapalıysa bu zincirin ilk halkası eksiktir.",
   ("ul", ["Kulak kepçesi sesi toplar ve yönlendirir, ama işitmenin asıl işini yapmaz",
           "Dış kulak yolu kapalıysa sesin iletimi belirgin şekilde azalır",
           "Orta kulak kemikçikleri de gelişim farklılığı gösterebilir",
           "İç kulak ve işitme siniri genellikle normaldir"]),
   ("note", "Bu ayrım umut vericidir: sorun sesin <strong>algılanmasında</strong> değil, <strong>iletilmesinde</strong> olduğu için, sesi iç kulağa başka bir yoldan ulaştırmak çözüm sağlar.")]},

  {"id": "degerlendirme", "tag": "Değerlendirme", "h2": "İşitme ne zaman ve nasıl değerlendirilir?", "body": [
   ("steps", [
    ("YENİDOĞAN TARAMASI", "Her bebeğe yapılan tarama ilk adımdır. Mikrotia varlığında sonuç tek başına yeterli sayılmaz."),
    ("İLERİ ODYOLOJİK İNCELEME", "Beyin sapı işitsel yanıt testi gibi yöntemlerle işitme eşikleri belirlenir."),
    ("GÖRÜNTÜLEME", "Orta ve iç kulak yapılarını değerlendirmek için tomografi istenebilir. Zamanlaması KBB tarafından belirlenir."),
    ("DÜZENLİ TAKİP", "İşitme, çocukluk boyunca belirli aralıklarla yeniden değerlendirilir.")]),
   ("note", "<strong>Çift taraflı mikrotiada bu süreç ertelenemez.</strong> Konuşma ve dil gelişimi ilk yıllarda şekillenir; işitme desteğinin erken sağlanması, çocuğun gelişimini doğrudan etkiler.")]},

  {"id": "cozumler", "tag": "Çözümler", "h2": "Hangi çözümler var?", "body": [
   ("h3", "Kemik yolu işitme cihazları"),
   "Sesi kafatası kemiği üzerinden doğrudan iç kulağa ileten cihazlardır. Bebeklik döneminde bir bantla, ileri yaşlarda implantla kullanılabilir. Cerrahi gerektirmeyen bant seçeneği sayesinde <strong>çok erken dönemde başlanabilir</strong>.",
   ("h3", "Atrezi cerrahisi"),
   "Dış kulak yolunun cerrahi olarak açılmasıdır. Her hastada uygun değildir; orta ve iç kulak yapılarının durumu belirleyicidir. Uygunluk kararı KBB tarafından, görüntüleme sonrası verilir.",
   ("h3", "Sınıf içi düzenlemeler"),
   "Tek taraflı vakalarda basit düzenlemeler büyük fark yaratır: çocuğun sağlıklı kulağının sınıfa dönük olacak şekilde oturtulması, öğretmenin bilgilendirilmesi, gürültülü ortamlarda öne alınması.",
   ("note", "Tek taraflı mikrotiada da işitme \"sorunsuz\" değildir. Sesin yönünü ayırt etme ve gürültüde anlama güçlüğü olabilir; bu, okul başarısını sessizce etkileyebilir.")]},

  {"id": "sira", "tag": "Sıralama", "h2": "İşitme ve kepçe onarımı nasıl sıralanır?", "body": [
   ("ul", ["<strong>İşitme desteği</strong> en erken dönemde başlar — kepçe onarımını beklemez",
           "<strong>Kepçe onarımı</strong> genellikle atrezi cerrahisinden önce planlanır",
           "Çünkü atrezi cerrahisi bölgedeki deri ve dokuyu değiştirir",
           "İmplantlı kemik yolu cihazı düşünülüyorsa, implantın konumu kepçe onarımıyla birlikte planlanmalıdır"]),
   ("note", "Bu sıralama, KBB ve plastik cerrahinin <strong>birlikte</strong> karar vermesini gerektirir. İki branşın birbirinden habersiz planlama yapması, ileride ikisini de zorlayan sonuçlar doğurabilir.")]}],

 "faqs": [
  ("Mikrotiası olan çocuk duyar mı?",
   "Tek taraflı vakalarda diğer kulak normalse çocuk duyar ve konuşmayı zamanında geliştirir. Etkilenen kulakta ise dış kulak yolu kapalıysa iletim tipi işitme kaybı olur. Çift taraflı vakalarda işitme desteği erken dönemde gereklidir."),
  ("İşitme cihazı ne zaman takılabilir?",
   "Bantla kullanılan kemik yolu cihazları bebeklik döneminde, cerrahi gerektirmeden kullanılabilir. Bu, özellikle çift taraflı vakalarda konuşma gelişimini desteklemek için erken dönemde gündeme gelir."),
  ("Atrezi ameliyatı her çocukta yapılabilir mi?",
   "Hayır. Uygunluk, orta ve iç kulak yapılarının durumuna bağlıdır ve görüntüleme sonrası KBB tarafından değerlendirilir. Uygun olmayan hastalarda kemik yolu işitme çözümleri tercih edilir."),
  ("Kepçe onarımı işitmeye katkı sağlar mı?",
   "Doğrudan bir işitme kazancı beklenmez. Kulak kepçesinin sesi toplama işlevi vardır, ancak dış kulak yolu kapalıyken bu katkı sınırlı kalır. Kepçe onarımı görünüme yönelik bir işlemdir."),
  ("Tek taraflı işitme kaybı okulda sorun yaratır mı?",
   "Yaratabilir. Sesin yönünü ayırt etme ve gürültülü ortamda konuşmayı anlama güçlüğü, derse odaklanmayı etkileyebilir. Oturma düzeni ve öğretmenin bilgilendirilmesi gibi basit düzenlemeler belirgin fark yaratır."),
  ("İşitme için hangi bölüme başvurmalıyım?",
   "KBB ve odyoloji. İşitme değerlendirmesi, cihaz seçimi ve atrezi cerrahisi kararı bu branşların alanıdır. Kulak kepçesinin onarımı ise plastik ve rekonstrüktif cerrahinin alanıdır.")]},

# ------------------------------------------------------------------ 8
{"slug": "mikrotia-neden-olur", "sources": K_TEMEL,
 "date": "2026-10-07",
 "cat": "Mikrotia",
 "title": "Mikrotia Neden Olur? Bilinen Nedenler ve Yanlış İnanışlar",
 "ogtitle": "Mikrotia neden olur?",
 "desc": "Mikrotia vakalarının çoğunda tek bir neden gösterilemez. Bilinen risk etkenleri, sendromlarla ilişkisi ve ailelerin sıkça sorduğu suçluluk sorusu.",
 "h1": "Mikrotia neden olur?",
 "lead": "Ailelerin ilk sorusu genellikle budur ve dürüst cevap şudur: <strong>vakaların büyük bölümünde tek bir neden gösterilemez.</strong> Mikrotia, gebeliğin erken haftalarında kulak kepçesini oluşturan yapıların gelişimindeki bir aksama sonucu ortaya çıkar. Bazı ilaçlar ve bazı sendromlarla ilişkisi bilinmektedir, ancak tipik bir vakada ailede benzer öykü ya da belirlenebilir bir neden yoktur.",
 "watopic": "mikrotia nedenleri hakkında bilgi",
 "related": ["mikrotia"],
 "sections": [
  {"id": "gelisim", "tag": "Gelişim", "h2": "Kulak nasıl gelişir, nerede aksar?", "body": [
   "Kulak kepçesi, gebeliğin erken haftalarında altı ayrı kabartının birleşip kaynaşmasıyla oluşur. Bu birleşme sürecindeki bir aksama, kepçenin eksik ya da şekilsiz kalmasına yol açar.",
   ("ul", ["Süreç gebeliğin çok erken döneminde tamamlanır",
           "Bu nedenle çoğu anne, henüz gebeliğinin farkında olmadığı bir dönemde gerçekleşmiş olur",
           "Aynı dönemde gelişen yüz yapıları da etkilenebilir; bu, bazı vakalarda eşlik eden farklılıkları açıklar"]),
   ("note", "Sürecin bu kadar erken tamamlanması önemli bir bilgidir: gebeliğin ilerleyen aylarında yapılan ya da yapılmayan hiçbir şey mikrotiaya yol açmaz.")]},

  {"id": "etkenler", "tag": "Etkenler", "h2": "Bilinen risk etkenleri", "body": [
   "Aşağıdakiler <strong>ilişkili bulunmuş</strong> etkenlerdir; her vakada bulunmaları gerekmez ve çoğu vakada hiçbiri yoktur.",
   ("ul", ["<strong>Bazı ilaçlar:</strong> gebeliğin erken döneminde kullanılan belirli ilaçlarla ilişki bildirilmiştir",
           "<strong>Sendromlar:</strong> mikrotia bazı genetik sendromların bir parçası olarak görülebilir",
           "<strong>Ailede öykü:</strong> vakaların küçük bir bölümünde ailede benzer tablo vardır",
           "<strong>Bazı gebelik koşulları:</strong> araştırmalarda bazı ilişkiler bildirilmiş olmakla birlikte, nedensellik gösterilememiştir"]),
   ("note", "\"İlişkili bulunmuş\" ile \"neden olur\" aynı şey değildir. Bir etkenin vakalarda daha sık görülmesi, o etkenin hastalığa yol açtığını kanıtlamaz. Mikrotia araştırmalarında bu ayrım özellikle önemlidir.")]},

  {"id": "sendrom", "tag": "Sendromlar", "h2": "Mikrotia bir sendromun parçası olabilir mi?", "body": [
   "Evet, bazı vakalarda mikrotia tek başına değil, başka gelişim farklılıklarıyla birlikte görülür.",
   ("ul", ["Yüzün aynı tarafında çene ve yanak gelişiminde farklılık",
           "Göz, omurga ya da böbrek gelişiminde eşlik eden durumlar",
           "Yüz sinirinin işlevinde farklılıklar"]),
   "Bu nedenle mikrotia tanısı konan her bebeğin <strong>genel bir değerlendirmeden geçmesi</strong> önerilir. Amaç kaygı yaratmak değil, varsa eşlik eden durumları erken saptamaktır.",
   ("note", "Vakaların çoğunda mikrotia tek başınadır ve başka bir sorun eşlik etmez. Genel değerlendirme, bunu teyit etmek için de yapılır.")]},

  {"id": "sucluluk", "tag": "Aileye", "h2": "Yanlış inanışlar: \"benim yüzümden mi oldu?\"", "body": [
   "Bu soru neredeyse her ailede sorulur ve cevabı nettir: <strong>hayır.</strong>",
   ("ul", ["Mikrotia, annenin gebelikte yaptığı ya da yapmadığı bir şeyden kaynaklanmaz",
           "Beslenme, stres, çalışma ya da hareket etmekle ilgisi yoktur",
           "Süreç, çoğu annenin gebeliğinin farkına varmadığı kadar erken bir dönemde gerçekleşir",
           "Vakaların büyük bölümünde belirlenebilir bir neden yoktur"]),
   ("note", "Suçluluk duygusu, ailenin sürece odaklanmasını zorlaştıran gerçek bir engeldir. Enerjinin doğru yeri, nedeni aramak değil; işitme değerlendirmesini zamanında yaptırmak ve onarım planını sakin biçimde kurmaktır.")]}],

 "faqs": [
  ("Mikrotianın kesin nedeni nedir?",
   "Vakaların büyük bölümünde kesin bir neden gösterilemez. Gebeliğin erken haftalarında kulak kepçesini oluşturan yapıların birleşme sürecindeki bir aksama sonucu ortaya çıkar. Bazı ilaçlar ve sendromlarla ilişkisi bilinmektedir."),
  ("Mikrotia kalıtsal mı?",
   "Vakaların küçük bir bölümünde ailede benzer öykü bulunur. Çoğu vaka tek başınadır ve kalıtsal değildir. Ailede birden fazla etkilenen kişi varsa genetik danışmanlık önerilir."),
  ("İkinci çocuğumda da olur mu?",
   "Tekrarlama olasılığı genel olarak düşüktür. Ancak ailede birden fazla vaka varsa ya da bir sendrom söz konusuysa bu oran değişir. Kesin bilgi için genetik danışmanlık alınması en doğrusudur."),
  ("Gebelikte kullandığım ilaçlar neden olmuş olabilir mi?",
   "Gebeliğin erken döneminde kullanılan belirli ilaçlarla ilişki bildirilmiştir, ancak tipik bir mikrotia vakasında bu ilişki kurulamaz. Kullandığınız ilaçlar konusunda endişeniz varsa hekiminizle paylaşmanız, hem sizi rahatlatır hem de varsa takip gerektiren bir durumu ortaya çıkarır."),
  ("Mikrotia gebelikte fark edilebilir mi?",
   "Bazı vakalarda ileri düzey ultrason ile fark edilebilir, ancak kulak kepçesi küçük bir yapı olduğu için rutin taramalarda gözden kaçabilir. Doğumdan sonra fark edilmesi sık görülen bir durumdur.")]},

# ------------------------------------------------------------------ 9
{"slug": "mikrotia-ameliyati-sonrasi", "sources": K_CERRAHI,
 "date": "2026-10-08",
 "cat": "Hasta Rehberi",
 "title": "Mikrotia Ameliyatı Sonrası: Aileler İçin Bakım Rehberi",
 "ogtitle": "Mikrotia ameliyatı sonrası süreç",
 "desc": "Mikrotia ameliyatı sonrası hastane süreci, kulağa baskı yapmama kuralı, göğüs bölgesi ağrısı, okula ve spora dönüş hakkında bilmeniz gerekenler.",
 "h1": "Mikrotia ameliyatı sonrası süreç",
 "lead": "Mikrotia onarımından sonraki dönemin tek bir altın kuralı vardır: <strong>yeni kulağa baskı uygulanmaması</strong>. İskelet yerleştirildikten sonra deri ile iskelet arasındaki uyum haftalar içinde oturur; bu dönemde üzerine yatmak, sıkı bere takmak ya da darbe almak sonucu doğrudan etkiler. İkinci konu, kıkırdağın alındığı göğüs bölgesidir — ilk haftalarda derin nefes alırken ağrı olması beklenir.",
 "watopic": "mikrotia ameliyatı sonrası bakım",
 "related": ["mikrotia"],
 "sections": [
  {"id": "ilk-gunler", "tag": "İlk günler", "h2": "Hastanede ve ilk günlerde", "body": [
   ("ul", ["Kulak koruyucu bir sargıyla kapatılır; sargı hekimin belirlediği zamana kadar açılmaz",
           "Ağrı kontrolü hem kulak hem göğüs bölgesi için planlanır",
           "Bazı planlamalarda küçük bir dren kullanılır ve birkaç gün içinde alınır",
           "Çocuğun sırtüstü ya da sağlıklı kulak üzerine yatması sağlanır",
           "Derin nefes ve öksürük sırasında göğüs bölgesinin desteklenmesi rahatlatır"]),
   ("note", "Ameliyattan çıkan çocuğun en çok yakındığı yer genellikle kulak değil, <strong>göğüs bölgesidir</strong>. Aileleri bu konuda önceden bilgilendirmek, ilk günleri belirgin biçimde kolaylaştırır.")]},

  {"id": "kulak", "tag": "Kulak bakımı", "h2": "Yeni kulağın korunması", "body": [
   ("ul", ["<strong>Üzerine yatılmaz.</strong> Gerekirse yastık düzeni bunu engelleyecek şekilde kurulur",
           "<strong>Sıkı bere, bandana, kulaklık takılmaz.</strong> Baskı, iskeletin üzerindeki derinin beslenmesini bozar",
           "<strong>Darbeden korunur.</strong> Kalabalık oyun ortamları ilk dönemde sınırlandırılır",
           "<strong>Islatılmaz.</strong> Duş ve saç yıkama için hekiminizin verdiği tarihi bekleyin",
           "<strong>Kaşınırsa kaşınmaz.</strong> İyileşme döneminde kaşıntı olağandır; hekiminize bildirin"]),
   ("h3", "Hemen bildirilmesi gerekenler"),
   ("ul", ["Ateş",
           "Sargıda artan ya da kötü kokulu akıntı",
           "Kulak çevresinde artan kızarıklık, ısı ve şişlik",
           "Deride renk değişikliği — morarma ya da beyazlama",
           "İlaçla geçmeyen, artan ağrı"])]},

  {"id": "gogus", "tag": "Göğüs bölgesi", "h2": "Kıkırdak alınan bölge", "body": [
   "Kaburga kıkırdağının alındığı bölge, ilk haftalarda kulaktan daha fazla rahatsızlık verir. Bu beklenen bir durumdur.",
   ("ul", ["Derin nefes, öksürük ve gülme sırasında ağrı olur; birkaç hafta içinde geriler",
           "Yastıkla göğsü desteklemek öksürük sırasında rahatlatır",
           "Solunum egzersizleri, akciğerlerin iyi havalanması için önemlidir",
           "Bölgede ince bir iz kalır; zamanla solar",
           "Göğüs duvarında hafif bir kontur farkı kalabilir"]),
   ("note", "Ağrı korkusuyla yüzeysel nefes almak, ilk günlerde akciğer havalanmasını azaltır. Ağrı kontrolünün iyi yapılması, yalnızca konfor için değil, bu nedenle de önemlidir.")]},

  {"id": "donus", "tag": "Dönüş", "h2": "Okula, spora ve günlük yaşama dönüş", "body": [
   ("steps", [
    ("1-2. HAFTA", "Evde dinlenme dönemi. Sargı bakımı ve ağrı kontrolü ön planda."),
    ("2-4. HAFTA", "Çoğu çocuk okula dönebilir. Beden eğitimi ve temaslı oyunlardan uzak durulur."),
    ("6-8. HAFTA", "Hekim onayıyla çoğu günlük etkinliğe dönülür."),
    ("3-6. AY", "Şişlik tamamen geriler, kıvrımlar belirginleşir. Bir sonraki aşama bu dönemde planlanır.")]),
   ("ul", ["<strong>Yüzme:</strong> yara tam kapanmadan başlanmaz; tarihi hekiminiz belirler",
           "<strong>Temaslı sporlar:</strong> daha uzun süre beklenir; sentetik iskelet varsa uzun vadede de dikkat gerekir",
           "<strong>Gözlük:</strong> kulağın üzerine oturan çerçeveler için hekim onayı beklenir",
           "<strong>Saç kesimi:</strong> ilk dönemde bölgeye dokunulmaması istenir"]),
   ("note", "Okula dönüş, çocuk için teknik olduğu kadar duygusal bir eşiktir. Öğretmenin durumdan haberdar edilmesi ve ilk günlerde beden eğitiminden muafiyet, geçişi kolaylaştırır.")]}],

 "faqs": [
  ("Ameliyattan sonra hastanede ne kadar kalınır?",
   "Yapılan aşamaya ve çocuğun durumuna göre değişir; ilk aşamada genellikle birkaç gün kalınır. Sonraki aşamalar daha kısa sürelidir. Kesin süreyi cerrahınız planına göre belirtir."),
  ("Çocuğum ne zaman okula dönebilir?",
   "Çoğu çocuk 2-4 hafta içinde okula döner. Beden eğitimi ve temaslı oyunlardan bir süre daha uzak durulması istenir. Karar, iyileşmenin seyrine göre hekiminiz tarafından verilir."),
  ("Ne zaman saçını yıkayabilirim?",
   "Sargı düzeni ve yara durumu belirleyicidir; mutlaka hekiminizin verdiği tarihi bekleyin. Erken ıslatma, iskeletin üzerindeki ince deri için risk oluşturur."),
  ("Kulak şişliği ne zaman geçer?",
   "İlk haftalarda belirgin şişlik olur ve kıvrımlar tam görünmez. Şişliğin büyük bölümü 4-6 haftada geriler, nihai görünüm birkaç ayı bulur. Erken dönemde sonuç hakkında yargıya varmamak önemlidir."),
  ("Kulağına yanlışlıkla baskı uygulanırsa ne olur?",
   "Kısa süreli hafif bir baskı genellikle sorun yaratmaz. Ancak uzun süreli baskı — özellikle üzerine yatmak — iskeletin üzerindeki derinin beslenmesini bozabilir. Böyle bir durumda hekiminizi bilgilendirin."),
  ("Sonraki aşama ne zaman yapılır?",
   "Genellikle 3-6 ay sonra. Bu süre dokunun iyileşmesi ve iskeletin yerleşmesi için gereklidir. Aceleyle yapılan ikinci aşama, ilk aşamada elde edilen sonucu bozabilir.")]},
]
