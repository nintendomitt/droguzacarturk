# -*- coding: utf-8 -*-
"""
Blog — Ekim/Kasim 2026 partisi, 15 yazi.
Yayin: 20 Ekim – 3 Kasim 2026, gunde 1.
Dagilim: 10 lenfodem, 3 hidradenit, 2 mikrotia.

KONU SECIMI: Google otomatik tamamlama (hl=tr, gl=tr; 19 Ekim 2026) uzerinden
halkin yazdigi sorgular toplandi — "lenfodem gecer mi / kendiliginden /
zayiflayinca", "meme kanseri sonrasi kol sismesi", "koltuk alti cibanina ne iyi
gelir", "lenfodemde agri olur mu", "lenfodem ilaclari", "bacakta sislik ve
sertlik", "lenfodemde bandajlama", "kopek memesi hastaligi oldurur mu",
"lenfodemden korunma yollari", "lenfodemde kinezyo bantlama", "mikrotia ameliyati
yapan doktorlar", "lenfodemde suluk tedavisi", "kolda sislik neden olur".
(Semrush API kredisi bitmisti; hacim yerine otomatik tamamlama sirasi esas alindi.)

KANIBALIZASYON: lenfodemde-beslenme, lenfodem-corabi-basi-giysisi,
kompresyon-corabi-nasil-secilir, lenfodem-egzersizleri, hacamat-lenfodem,
ayak-bacak-sismesi-ne-zaman-ciddi, kolda-lenfodem (hizmet) mevcut — yeni yazilar
bunlarin konusunu tekrar etmez, farkli niyeti hedefler.

DIL: Hoca talebi — olculu, kurumsal; kesin sonuc vaadi yok; hidradenitte
dermatoloji vurgusu yok; mikrotia iki asama, arada 12 ay.
"""

SRC_SP = ("Lymphedema — StatPearls, NCBI Bookshelf",
          "https://www.ncbi.nlm.nih.gov/books/NBK537239/")
SRC_NCI = ("Lymphedema and Cancer — National Cancer Institute (NCI)",
           "https://www.cancer.gov/about-cancer/treatment/side-effects/lymphedema")
SRC_NHS = ("Lymphoedema — NHS",
           "https://www.nhs.uk/conditions/lymphoedema/")
SRC_NHS_ONL = ("Lymphoedema: Prevention — NHS",
               "https://www.nhs.uk/conditions/lymphoedema/prevention/")
SRC_MP = ("Lymphedema — MedlinePlus (ABD Ulusal Tıp Kütüphanesi)",
          "https://medlineplus.gov/lymphedema.html")
SRC_ODEM = ("Swollen ankles, feet and legs (oedema) — NHS",
            "https://www.nhs.uk/conditions/oedema/")
SRC_DER = ("Türkiye Lenfödem ve Lipödem Derneği",
           "https://lenfodemdernegi.org.tr/")
SRC_HS_SP = ("Hidradenitis Suppurativa — StatPearls, NCBI Bookshelf",
             "https://www.ncbi.nlm.nih.gov/books/NBK534867/")
SRC_HS_NHS = ("Hidradenitis suppurativa (HS) — NHS",
              "https://www.nhs.uk/conditions/hidradenitis-suppurativa/")
SRC_MIK = ("Ear Microtia — StatPearls, NCBI Bookshelf",
           "https://www.ncbi.nlm.nih.gov/books/NBK563243/")
SRC_MIK_CDC = ("Anotia / Microtia — ABD Hastalık Kontrol ve Önleme Merkezleri (CDC)",
               "https://www.cdc.gov/birth-defects/about/anotia-microtia.html")

K_LEN = [SRC_NCI, SRC_NHS, SRC_SP]
K_LEN_KOR = [SRC_NCI, SRC_NHS_ONL, SRC_SP]
K_HS = [SRC_HS_SP, SRC_HS_NHS]
K_MIK = [SRC_MIK, SRC_MIK_CDC]

BLOG_EKIM2 = [

# ------------------------------------------------------------------ 1
{"slug": "lenfodem-gecer-mi", "sources": K_LEN,
 "date": "2026-10-20",
 "cat": "Lenfödem",
 "title": "Lenfödem Geçer mi? Kendiliğinden, Sporla veya Zayıflayınca",
 "ogtitle": "Lenfödem geçer mi, tamamen iyileşir mi?",
 "desc": "Lenfödem kendiliğinden geçmez; ancak erken başlanan tedaviyle şişlik büyük ölçüde kontrol altına alınabilir. Spor, kilo verme ve cerrahinin rolü.",
 "h1": "Lenfödem geçer mi?",
 "lead": "Kısa yanıt: <strong>lenfödem kendiliğinden geçmez</strong>, ancak doğru ve erken başlanan tedaviyle şişlik büyük ölçüde kontrol altına alınabilir. Ameliyattan sonraki ilk haftalarda görülen geçici şişlik ile kalıcı lenfödem farklı şeylerdir. Lenf damarlarındaki akış bozukluğu sürdükçe sıvı birikmeye devam eder; bu yüzden tedavi, bozukluğu ya yönetmeyi ya da cerrahi olarak düzeltmeyi hedefler.",
 "watopic": "lenfödem tedavi seçenekleri",
 "related": ["lenfodem", "lenfodem-evreleri"],
 "sections": [
  {"id": "kendiliginden", "tag": "Seyir", "h2": "Kendiliğinden geçer mi?", "body": [
   "Ameliyat ya da radyoterapi sonrasındaki ilk haftalarda kolda veya bacakta hafif bir şişlik olabilir ve bu çoğu zaman kendiliğinden geriler. Ancak şişlik <strong>aylarca sürüyorsa, gün içinde artıp gece azalıyorsa ve uzvun bir kısmında ağırlık hissi varsa</strong>, bu artık geçici bir tablo değildir.",
   ("ul", ["Erken evrede şişlik yumuşaktır, bastırınca iz kalır ve bacak yükseltildiğinde azalır",
           "Tedavi edilmezse doku zamanla sertleşir; yükseltme artık yeterli olmaz",
           "İleri evrede deri kalınlaşır, kıvrımlar ve tekrarlayan enfeksiyonlar görülebilir"]),
   ("note", "Lenfödemde zaman önemlidir. Erken evrede başlanan tedavi, hem konservatif yöntemlerin hem de cerrahinin etkisini artırır.")]},

  {"id": "spor-kilo", "tag": "Yaşam tarzı", "h2": "Sporla veya zayıflayınca geçer mi?", "body": [
   "Egzersiz ve kilo kontrolü lenfödemin yönetiminde önemlidir, ancak tek başlarına hastalığı ortadan kaldırmaz.",
   ("ul", ["<strong>Egzersiz:</strong> kasların kasılması lenf akışına yardım eder; bası giysisiyle yapılan düzenli egzersiz şişliğin kontrolünü kolaylaştırır",
           "<strong>Kilo verme:</strong> fazla kilo lenf sistemine ek yük bindirir; kilo vermek şişliği azaltabilir ve tedavinin etkisini artırır",
           "<strong>Sınır:</strong> lenf damarlarında yapısal bir tıkanıklık varsa, spor ve diyet bu tıkanıklığı açmaz"]),
   ("note", "Obeziteye bağlı lenfödem ayrı bir tablodur. Bu hastalarda belirgin kilo kaybı şişlikte anlamlı düzelme sağlayabilir; değerlendirme buna göre yapılır.")]},

  {"id": "tedavi", "tag": "Tedavi", "h2": "Tamamen iyileşmesi mümkün mü?", "body": [
   "Lenfödem tedavisi iki basamaklıdır. İlk basamak konservatif tedavidir: manuel lenf drenajı, bandajlama, bası giysisi, egzersiz ve cilt bakımı. Bu yöntemler şişliği kontrol eder ama nedeni ortadan kaldırmaz.",
   "İkinci basamak cerrahidir. <strong>Lenf damarını toplardamara bağlama (LVA)</strong> ve <strong>lenf bezi nakli</strong>, sıvının çıkışı için yeni yollar oluşturmayı hedefler. Uygun hastalarda bası giysisi ihtiyacının azalması ve enfeksiyon ataklarının seyrekleşmesi bildirilmektedir.",
   ("note", "Hiçbir yöntem her hastada lenfödemin tamamen ortadan kalkacağını garanti etmez. Gerçekçi hedef, şişliğin azalması, uzvun hafiflemesi ve günlük yaşamın rahatlamasıdır. Uygun yöntem muayene ve görüntüleme sonrası belirlenir.")]}],

 "faqs": [
  ("Lenfödem kendiliğinden geçer mi?",
   "Ameliyat sonrası ilk haftalardaki geçici şişlik kendiliğinden gerileyebilir. Ancak aylarca süren, gün içinde artan ve ağırlık hissi yapan şişlik lenfödemdir ve tedavi edilmeden kendiliğinden geçmez."),
  ("Lenfödem sporla geçer mi?",
   "Düzenli egzersiz lenf akışına yardım eder ve şişliğin kontrolünü kolaylaştırır; ancak lenf damarlarındaki tıkanıklığı ortadan kaldırmaz. Egzersiz, bası giysisiyle birlikte ve kademeli olarak yapılmalıdır."),
  ("Zayıflayınca lenfödem geçer mi?",
   "Fazla kilo lenf sistemine yük bindirir; kilo vermek şişliği azaltabilir. Obeziteye bağlı lenfödemde belirgin düzelme görülebilir. Kanser tedavisi sonrası gelişen lenfödemde ise kilo kaybı tek başına yeterli değildir."),
  ("Lenfödem ameliyatla tamamen iyileşir mi?",
   "Cerrahi, uygun hastalarda şişliği ve bası giysisi ihtiyacını azaltabilir. Sonuçlar kişiden kişiye değişir; tamamen iyileşme garantisi verilemez. En iyi sonuçlar genellikle erken evrede yapılan cerrahide görülür.")]},

# ------------------------------------------------------------------ 2
{"slug": "meme-kanseri-sonrasi-kol-sismesi", "sources": [SRC_NCI, SRC_NHS, SRC_SP],
 "date": "2026-10-21",
 "cat": "Lenfödem",
 "title": "Meme Kanseri Ameliyatı Sonrası Kol ve Koltuk Altı Şişmesi: Lenfödem mi?",
 "ogtitle": "Meme kanseri ameliyatı sonrası kol şişmesi",
 "desc": "Meme kanseri ameliyatından sonra kolda ve koltuk altında şişlik neden olur? Sıvı toplanması (seroma) ile lenfödem farkı, erken belirtiler ve ne zaman başvurulmalı.",
 "h1": "Meme kanseri ameliyatı sonrası kol şişmesi",
 "lead": "Meme kanseri ameliyatından sonra kolda veya koltuk altında şişlik sık görülen bir şikâyettir. Bunların bir kısmı ameliyata bağlı <strong>geçici sıvı toplanmasıdır</strong> ve kendiliğinden geriler. Ancak koltuk altı lenf bezleri alınmış ya da bölgeye radyoterapi uygulanmışsa, aylar hatta yıllar sonra gelişen kalıcı şişlik <strong>kol lenfödemi</strong> olabilir. İkisini ayırt etmek tedavinin zamanlaması için önemlidir.",
 "watopic": "meme kanseri sonrası kol lenfödemi",
 "related": ["kolda-lenfodem", "lenfodem"],
 "sections": [
  {"id": "neden", "tag": "Nedenler", "h2": "Ameliyattan sonra kol neden şişer?", "body": [
   ("ul", ["<strong>Seroma (sıvı toplanması):</strong> ameliyat bölgesinde, genellikle koltuk altında biriken sıvı; ilk haftalarda görülür ve çoğu zaman geriler",
           "<strong>Ameliyat sonrası ödem:</strong> doku iyileşirken oluşan geçici şişlik",
           "<strong>Lenfödem:</strong> lenf bezlerinin alınması veya radyoterapiye bağlı kalıcı akış bozukluğu; aylar ya da yıllar sonra başlayabilir",
           "<strong>Enfeksiyon:</strong> kızarıklık, ısı artışı ve ateşle birlikte şişlik",
           "<strong>Toplardamarda pıhtı:</strong> ani başlayan, ağrılı şişlik — acil değerlendirme gerektirir"]),
   ("note", "Koltuk altından çıkarılan lenf bezi sayısı arttıkça ve radyoterapi eklendikçe lenfödem riski artar. Yalnızca nöbetçi (sentinel) lenf bezi alınan hastalarda risk daha düşüktür.")]},

  {"id": "belirti", "tag": "Belirtiler", "h2": "Lenfödemi düşündüren erken bulgular", "body": [
   ("ul", ["Kolda ağırlık, dolgunluk ya da gerginlik hissi",
           "Yüzük, saat veya bilezik sıkmaya başlaması",
           "Gömlek kolunun bir tarafta daha dar gelmesi",
           "Elin ya da parmakların gün sonunda şişmesi",
           "Bastırınca iz kalan yumuşak şişlik"]),
   "Bu bulgular başlangıçta gelip gidebilir. Erken dönemde fark edilen lenfödem, tedaviye daha iyi yanıt verir.",
   ("note", "<strong>Kızarıklık, sıcaklık ve ateşle birlikte artan şişlik</strong> enfeksiyon (selülit) belirtisi olabilir ve aynı gün değerlendirilmelidir.")]},

  {"id": "ne-zaman", "tag": "Başvuru", "h2": "Ne zaman başvurmalı?", "body": [
   "Ameliyattan sonraki ilk haftalarda koltuk altında sıvı toplanması genellikle cerrahi ekip tarafından takip edilir. Şu durumlarda lenfödem açısından değerlendirme önerilir:",
   ("ul", ["Şişlik ameliyattan aylar sonra başladıysa",
           "Kol ölçümleri iki taraf arasında belirgin fark gösteriyorsa",
           "Şişlik birkaç haftadır geçmiyor ya da artıyorsa",
           "Tekrarlayan enfeksiyon atakları oluyorsa"]),
   ("note", "Kol lenfödeminde tedavi; bası giysisi, lenf drenajı ve egzersizle başlar. Uygun hastalarda lenf damarını toplardamara bağlama (LVA) ya da lenf bezi nakli gibi mikrocerrahi yöntemler planlanabilir; bazı hastalarda meme rekonstrüksiyonu ile aynı ameliyatta yapılabilir.")]}],

 "faqs": [
  ("Meme kanseri ameliyatından sonra kol şişmesi normal mi?",
   "İlk haftalarda hafif şişlik ve koltuk altında sıvı toplanması sık görülür ve çoğu zaman geriler. Aylar sonra başlayan ya da geçmeyen şişlik ise lenfödem açısından değerlendirilmelidir."),
  ("Koltuk altı şişmesi lenfödem mi?",
   "Ameliyattan sonraki ilk haftalarda koltuk altındaki şişlik genellikle seromadır, yani ameliyat bölgesinde biriken sıvıdır. Lenfödem ise daha çok kol ve elde, zamanla gelişen kalıcı şişlik olarak görülür."),
  ("Lenfödem ameliyattan ne kadar sonra başlar?",
   "Aylar içinde başlayabileceği gibi yıllar sonra da ortaya çıkabilir. Bu nedenle lenf bezleri alınmış ya da radyoterapi almış hastaların kol değişikliklerini uzun süre takip etmesi önerilir."),
  ("Meme kanseri sonrası kol lenfödemi tedavi edilebilir mi?",
   "Evet. Konservatif tedavi ile şişlik kontrol altına alınabilir. Uygun hastalarda mikrocerrahi yöntemlerle lenf akışı için yeni yollar oluşturulabilir. Tedavi seçimi muayene ve görüntüleme sonrası yapılır.")]},

# ------------------------------------------------------------------ 3
{"slug": "koltuk-alti-cibanina-ne-iyi-gelir", "sources": K_HS,
 "date": "2026-10-22",
 "cat": "Hidradenit",
 "title": "Koltuk Altı Çıbanına Ne İyi Gelir? Evde Yapılabilecekler ve Sınırları",
 "ogtitle": "Koltuk altı çıbanına ne iyi gelir?",
 "desc": "Koltuk altı çıbanında ılık kompres, gevşek giysi ve hijyen rahatlatabilir; sıkmak ve iğneyle açmak zarar verir. Tekrarlıyorsa hidradenit olabilir.",
 "h1": "Koltuk altı çıbanına ne iyi gelir?",
 "lead": "Tek seferlik bir koltuk altı çıbanı çoğu zaman basit önlemlerle geriler. <strong>Ilık kompres, bölgeyi kuru ve temiz tutmak, gevşek giysiler</strong> rahatlatıcı olabilir. Ancak çıban aynı bölgede tekrar tekrar çıkıyor, akıntı yapan kanallar oluşuyor ya da iz bırakıyorsa, bu basit bir çıban değil <strong>hidradenitis süpürativa</strong> olabilir ve evde uygulanan yöntemlerin bir sınırı vardır.",
 "watopic": "tekrarlayan koltuk altı çıbanı",
 "related": ["hidradenit"],
 "sections": [
  {"id": "evde", "tag": "Evde", "h2": "Evde yapılabilecekler", "body": [
   ("ul", ["<strong>Ilık kompres:</strong> günde birkaç kez 10–15 dakika uygulanan ılık ve temiz bez, ağrıyı azaltabilir ve iltihabın kendiliğinden boşalmasına yardım edebilir",
           "<strong>Bölgeyi kuru tutmak:</strong> nem ve sürtünme şikâyeti artırır",
           "<strong>Gevşek, pamuklu giysiler:</strong> sıkı giysiler sürtünmeyi artırır",
           "<strong>Antiseptik yıkama:</strong> hekim önerisiyle antiseptik içerikli temizleyiciler kullanılabilir",
           "<strong>Tıraşa ara vermek:</strong> iltihaplı bölgede tıraş tahrişi artırabilir"]),
   ("note", "Bu önlemler şikâyeti hafifletir; tekrarlayan hastalığın nedenini ortadan kaldırmaz.")]},

  {"id": "yapilmamasi", "tag": "Dikkat", "h2": "Yapılmaması gerekenler", "body": [
   ("ul", ["Çıbanı sıkmak ya da iğneyle açmak — iltihabı derine ve çevreye yayabilir",
           "Bilinçsiz antibiyotik kullanımı — tekrarlayan tabloda kalıcı çözüm sağlamaz",
           "Bitkisel macun, merhem veya sıcak yakı uygulamak — deride yanık ve tahriş yapabilir",
           "Aynı bölgede tekrarlayan şikâyeti yıllarca \"basit çıban\" diye beklemek"]),
   ("note", "Yüksek ateş, hızla yayılan kızarıklık ya da çok şiddetli ağrı varsa evde beklenmemeli, aynı gün değerlendirme yapılmalıdır.")]},

  {"id": "hidradenit", "tag": "Tekrarlıyorsa", "h2": "Tekrarlıyorsa hidradenit olabilir", "body": [
   "Hidradenitis süpürativa, koltuk altı, kasık ve meme altı gibi bölgelerde tekrarlayan ağrılı şişlikler, apseler ve deri altında tüneller oluşturan kronik bir hastalıktır. Bulaşıcı değildir ve hijyen eksikliğinden kaynaklanmaz.",
   ("ul", ["Aynı bölgede yılda birkaç kez tekrarlayan şişlikler",
           "Deri altında birbirine bağlanan, akıntı yapan kanallar",
           "İyileşen alanlarda kalan sert izler"]),
   "Erken evrede ilaç tedavisiyle kontrol sağlanabilir. Deri altında tünelleşme ve kalıcı iz oluştuysa, hastalıklı alanın çıkarılıp onarılması için cerrahi değerlendirme gerekir.",
   ("note", "Tekrarlayan çıbanların her seferinde boşaltılması o anki ağrıyı geçirir; ancak tünelleri yerinde bıraktığı için şikâyet aynı bölgede geri dönebilir.")]}],

 "faqs": [
  ("Koltuk altı çıbanına sıcak kompres iyi gelir mi?",
   "Ilık ve temiz bir kompres ağrıyı azaltabilir ve iltihabın kendiliğinden boşalmasına yardımcı olabilir. Çok sıcak uygulamalardan kaçınılmalıdır; deri yanabilir."),
  ("Koltuk altı çıbanı kendiliğinden geçer mi?",
   "Tek seferlik çıbanlar çoğu zaman kendiliğinden geriler. Aynı bölgede tekrar tekrar çıkıyorsa hidradenit olabilir ve değerlendirme gerekir."),
  ("Çıbanı sıkmak zararlı mı?",
   "Evet. Sıkmak iltihabın derine ve çevre dokuya yayılmasına, iz oluşumunun artmasına yol açabilir."),
  ("Koltuk altı çıbanı için krem var mı?",
   "Bazı antiseptik ve antibiyotikli kremler hekim önerisiyle kullanılabilir. Ancak tekrarlayan ve tünel oluşturan tabloda kremler tek başına yeterli değildir; tedavi hastalığın evresine göre planlanır.")]},

# ------------------------------------------------------------------ 4
{"slug": "lenfodemde-agri-olur-mu", "sources": K_LEN,
 "date": "2026-10-23",
 "cat": "Lenfödem",
 "title": "Lenfödemde Ağrı Olur mu? Ağrının Nedenleri ve Uyarı İşaretleri",
 "ogtitle": "Lenfödemde ağrı olur mu?",
 "desc": "Lenfödem genellikle keskin ağrı değil, ağırlık ve gerginlik yapar. Ani ve şiddetli ağrı enfeksiyon ya da pıhtı işareti olabilir. Ne zaman acil?",
 "h1": "Lenfödemde ağrı olur mu?",
 "lead": "Lenfödemin tipik şikâyeti keskin bir ağrı değil, <strong>ağırlık, dolgunluk ve gerginlik hissidir</strong>. Şişlik arttıkça bu his bir sızıya dönüşebilir. Ancak <strong>ani başlayan, şiddetli ya da kızarıklıkla birlikte olan ağrı</strong> lenfödemin olağan seyri değildir; enfeksiyon veya toplardamarda pıhtı gibi acil durumların işareti olabilir.",
 "watopic": "lenfödem ve ağrı",
 "related": ["lenfodem-belirtileri", "lenfodem"],
 "sections": [
  {"id": "nasil", "tag": "Karakter", "h2": "Lenfödemdeki rahatsızlık nasıl hissedilir?", "body": [
   ("ul", ["Uzuvda ağırlık ve yorgunluk, özellikle gün sonunda",
           "Deride gerginlik ve dolgunluk hissi",
           "Eklemlerde hareket kısıtlılığına bağlı sızı",
           "Uyuşma ya da karıncalanma",
           "Ağır şişlikte omuz, bel veya kalçaya yansıyan yük ağrısı"]),
   ("note", "Lipödemde ön planda olan dokunma hassasiyeti ve kendiliğinden morarma, lenfödemin tipik bulgusu değildir. Bu fark, iki hastalığın ayırt edilmesinde yardımcı olur.")]},

  {"id": "neden", "tag": "Nedenler", "h2": "Ağrıyı artıran durumlar", "body": [
   ("ul", ["<strong>Şişliğin artması:</strong> sıcak hava, uzun süre ayakta kalmak veya bası giysisinin bırakılması",
           "<strong>Enfeksiyon (selülit, erizipel):</strong> kızarıklık, sıcaklık, ateş ve hızla artan ağrı",
           "<strong>Doku sertleşmesi:</strong> ileri evrede eklem hareketinin kısıtlanması",
           "<strong>Uygun olmayan bası giysisi:</strong> çok sıkı ya da kıvrılan giysi ağrı ve uyuşma yapabilir",
           "<strong>Sinir hasarı:</strong> kanser ameliyatı veya radyoterapiye bağlı ağrı"]),
   ("note", "Kanser tedavisi görmüş hastalarda yeni başlayan ve geçmeyen ağrı, hastalığın tekrarı açısından da onkoloji ekibine bildirilmelidir.")]},

  {"id": "acil", "tag": "Acil", "h2": "Ne zaman acil değerlendirme gerekir?", "body": [
   ("ul", ["Kızarıklık ve sıcaklıkla birlikte artan ağrı",
           "Titreme ve ateş",
           "Ciltte kırmızı çizgi şeklinde yayılan iz",
           "Tek uzuvda ani başlayan şişlik ve ağrı",
           "Nefes darlığı ya da göğüs ağrısı"]),
   ("note", "Bu bulgular enfeksiyon ya da pıhtı belirtisi olabilir ve aynı gün, nefes darlığı varsa hemen acil serviste değerlendirilmelidir.")]}],

 "faqs": [
  ("Lenfödem ağrı yapar mı?",
   "Genellikle keskin ağrı değil, ağırlık, gerginlik ve sızı yapar. Şişlik arttıkça bu rahatsızlık belirginleşebilir."),
  ("Lenfödemli bacakta ani ağrı neden olur?",
   "Ani ve şiddetli ağrı çoğu zaman enfeksiyon veya toplardamarda pıhtı gibi lenfödem dışı bir nedene bağlıdır. Aynı gün değerlendirme gerekir."),
  ("Bası giysisi ağrı yapar mı?",
   "Doğru ölçüde seçilmiş giysi ağrı yapmamalıdır. Uyuşma, morarma veya ağrı oluyorsa giysinin ölçüsü ve basınç sınıfı kontrol edilmelidir."),
  ("Lenfödemde ağrı için ne yapılabilir?",
   "Şişliği azaltan yöntemler — bası giysisi, lenf drenajı, egzersiz ve uzvu yükseltmek — rahatsızlığı da azaltır. Ağrı kesici kullanımı hekimle planlanmalıdır.")]},

# ------------------------------------------------------------------ 5
{"slug": "lenfodem-ilaclari", "sources": [SRC_SP, SRC_NCI, SRC_NHS],
 "date": "2026-10-24",
 "cat": "Tedavi",
 "title": "Lenfödem İlaçları: Hangi İlaç Kullanılır, İlaçla Geçer mi?",
 "ogtitle": "Lenfödem ilaçla geçer mi?",
 "desc": "Lenfödemi tedavi eden bir ilaç yoktur. İdrar söktürücüler önerilmez; antibiyotik yalnızca enfeksiyonda kullanılır. Etkili tedavi seçenekleri neler?",
 "h1": "Lenfödem ilaçla geçer mi?",
 "lead": "Lenfödem için en sık sorulan sorulardan biri \"hangi ilaç iyi gelir\" sorusudur. Kısa yanıt: <strong>bugün lenfödemi ortadan kaldıran bir ilaç yoktur</strong>. Lenfödemde sorun damar dışında biriken proteinden zengin sıvı ve bozulmuş lenf akışıdır; bunu ilaçla çözmek mümkün olmamıştır. İlaçların lenfödemdeki yeri sınırlıdır ve belirli durumlarla ilgilidir.",
 "watopic": "lenfödem tedavi seçenekleri",
 "related": ["lenfodem", "lenfodem-hangi-doktor"],
 "sections": [
  {"id": "idrar", "tag": "Ödem söktürücü", "h2": "İdrar söktürücüler (ödem atıcılar) işe yarar mı?", "body": [
   "İdrar söktürücüler kalp, böbrek veya karaciğer kaynaklı ödemde kullanılır. Lenfödemde ise <strong>uzun süreli tedavi olarak önerilmez</strong>.",
   ("ul", ["Damar içinden su çeker; dokudaki proteinden zengin lenf sıvısını uzaklaştırmaz",
           "Geçici bir azalmadan sonra şişlik geri döner",
           "Uzun kullanımda tuz-su dengesi bozuklukları gibi yan etkiler görülebilir"]),
   ("note", "Lenfödemle birlikte kalp veya böbrek hastalığı varsa idrar söktürücü bu hastalık için gerekebilir. Bu karar ilgili hekim tarafından verilir; kendi başınıza başlamayın ya da bırakmayın.")]},

  {"id": "antibiyotik", "tag": "Enfeksiyon", "h2": "Antibiyotikler ne zaman kullanılır?", "body": [
   "Lenfödemde dokuda biriken sıvı enfeksiyon riskini artırır. <strong>Selülit veya erizipel</strong> gelişirse antibiyotik tedavisi gerekir ve gecikmemelidir.",
   ("ul", ["Kızarıklık, sıcaklık, artan şişlik ve ateş enfeksiyonu düşündürür",
           "Sık tekrarlayan ataklarda hekim koruyucu antibiyotik planlayabilir",
           "Antibiyotik enfeksiyonu tedavi eder; lenfödemin kendisini geçirmez"])]},

  {"id": "diger", "tag": "Diğer", "h2": "Bitkisel ürünler ve takviyeler", "body": [
   "Benzopiron grubu bazı ilaçlar ve çeşitli bitkisel takviyeler lenfödem için denenmiştir. Bugünkü kanıtlar bu ürünlerin şişliği anlamlı ölçüde azalttığını göstermemektedir; bazıları karaciğer yan etkileri nedeniyle dikkat gerektirir.",
   ("ul", ["Takviye kullanmadan önce hekiminize danışın",
           "\"Lenfödemi geçiren\" iddiasıyla satılan ürünlere temkinli yaklaşın",
           "Kanser tedavisi sürenlerde bitkisel ürünler ilaçlarla etkileşebilir"]),
   ("note", "Lenfödemde etkinliği kanıtlanmış tedaviler ilaç dışı yöntemlerdir: bası tedavisi, manuel lenf drenajı, egzersiz, cilt bakımı ve uygun hastalarda mikrocerrahi.")]}],

 "faqs": [
  ("Lenfödem için hangi ilaç kullanılır?",
   "Lenfödemi tedavi eden bir ilaç yoktur. İlaçlar, enfeksiyon gelişirse antibiyotik ya da eşlik eden hastalıkların tedavisi gibi özel durumlarda kullanılır."),
  ("Ödem söktürücü lenfödemde işe yarar mı?",
   "Lenfödemde uzun süreli tedavi olarak önerilmez. Geçici azalma sağlayabilir ama şişlik geri döner ve yan etki riski vardır."),
  ("Lenfödem ilaçla geçer mi?",
   "Hayır. Lenfödemin yönetimi bası tedavisi, lenf drenajı, egzersiz ve cilt bakımıyla yapılır; uygun hastalarda mikrocerrahi seçenekler değerlendirilir."),
  ("Bitkisel takviyeler lenfödeme iyi gelir mi?",
   "Bugünkü kanıtlar bitkisel takviyelerin şişliği anlamlı azalttığını göstermemektedir. Kullanmadan önce hekiminize danışmanız önerilir.")]},

# ------------------------------------------------------------------ 6
{"slug": "kulak-sekil-bozukluklari", "sources": K_MIK,
 "date": "2026-10-25",
 "cat": "Mikrotia",
 "title": "Bebekte Kulak Şekil Bozuklukları: Mikrotia mı, Kepçe Kulak mı?",
 "ogtitle": "Mikrotia mı, kepçe kulak mı? Kulak şekil bozuklukları",
 "desc": "Kepçe kulak, kıvrık kulak, gömük kulak ve mikrotia farklı durumlardır. Hangisinde ameliyat gerekir, hangisi bebeklikte düzeltilebilir? Ayırt etme rehberi.",
 "h1": "Kulak şekil bozuklukları: mikrotia mı, kepçe kulak mı?",
 "lead": "Bebeğin kulağının farklı görünmesi ailelerde haklı bir endişe yaratır. Ancak her kulak şekil bozukluğu mikrotia değildir. <strong>Kepçe kulak, kıvrık kulak, gömük kulak</strong> gibi durumlarda kulak kepçesinin dokusu tamdır, yalnızca şekli farklıdır. <strong>Mikrotiada</strong> ise kulak kepçesinin kendisi eksik gelişmiştir. Bu ayrım, tedavinin zamanlamasını ve yöntemini belirler.",
 "watopic": "bebekte kulak şekil bozukluğu",
 "related": ["mikrotia", "lip-lift"],
 "sections": [
  {"id": "turler", "tag": "Türler", "h2": "Sık görülen kulak şekil bozuklukları", "body": [
   ("table", ["Durum", "Görünüm", "Kulak dokusu"],
    [["Kepçe kulak", "Kulak başa göre fazla açılı durur", "Tam"],
     ["Kıvrık (bükük) kulak", "Kulağın üst kenarı öne doğru kıvrılmıştır", "Tam"],
     ["Gömük kulak", "Kulağın üst kısmı deri altına gömülü gibidir", "Tam"],
     ["Mikrotia", "Kulak küçük, eksik veya yalnızca bir doku parçası şeklindedir", "Eksik"],
     ["Anotia", "Kulak kepçesi hiç yoktur", "Yok"]]),
   ("note", "Kulak önünde küçük deri çıkıntıları veya delikler de görülebilir. Bunlar çoğu zaman tek başına bulunur, ancak işitme değerlendirmesi önerilir.")]},

  {"id": "bebeklik", "tag": "Bebeklik", "h2": "Bebeklikte düzeltilebilenler", "body": [
   "Kulak kepçesinin dokusu tam olan şekil bozukluklarında, doğumdan sonraki ilk haftalarda kıkırdak hâlâ yumuşaktır. Bu dönemde uygulanan <strong>kalıplama yöntemleri</strong> bazı bebeklerde ameliyata gerek kalmadan şekli düzeltebilir.",
   ("ul", ["En iyi sonuç ilk haftalarda başlandığında alınır",
           "Kıkırdak sertleştikçe kalıplamanın etkisi azalır",
           "Kalıplama mikrotiada eksik dokuyu tamamlamaz"])]},

  {"id": "mikrotia", "tag": "Mikrotia", "h2": "Mikrotiada süreç nasıl ilerler?", "body": [
   "Mikrotiada kulak kepçesinin bir kısmı ya da tamamı gelişmemiştir. Sıklıkla dış kulak yolu da dar veya kapalıdır; bu nedenle <strong>işitme değerlendirmesi ilk aylarda</strong> yapılmalıdır.",
   "Kulak kepçesinin onarımı, kaburga kıkırdağının yeterli büyüklüğe ulaştığı dönemde, genellikle okul çağı civarında planlanır. Kendi kaburga kıkırdağıyla yapılan onarım <strong>iki aşamada</strong> tamamlanır ve aşamalar arasında <strong>12 ay</strong> beklenir.",
   ("note", "Kepçe kulak ameliyatı (otoplasti) ile mikrotia onarımı tamamen farklı ameliyatlardır. İlkinde mevcut kulak yeniden şekillendirilir; ikincisinde yeni bir kulak iskeleti oluşturulur.")]}],

 "faqs": [
  ("Bebeğimin kulağı kıvrık, mikrotia mı?",
   "Kulak dokusu tam ama kıvrık görünüyorsa bu genellikle mikrotia değil, şekil bozukluğudur ve ilk haftalarda kalıplamayla düzelebilir. Kesin ayrım muayene ile yapılır."),
  ("Kepçe kulak kaç yaşında ameliyat edilir?",
   "Kepçe kulak ameliyatı genellikle kulağın büyük ölçüde geliştiği okul öncesi veya okul çağında planlanır. Bebeklik döneminde kalıplama bir seçenek olabilir."),
  ("Mikrotia kalıplamayla düzelir mi?",
   "Hayır. Mikrotiada kulak dokusu eksik olduğu için kalıplama yeterli olmaz. Onarım kendi kaburga kıkırdağıyla, iki aşamada yapılır."),
  ("Kulak şekil bozukluğunda işitme etkilenir mi?",
   "Kepçe kulak ve kıvrık kulakta işitme genellikle normaldir. Mikrotiada dış kulak yolu dar veya kapalı olabileceği için işitme testi yapılmalıdır.")]},

# ------------------------------------------------------------------ 7
{"slug": "bacakta-sislik-ve-sertlik", "sources": [SRC_ODEM, SRC_NCI, SRC_SP],
 "date": "2026-10-26",
 "cat": "Lenfödem",
 "title": "Bacakta Şişlik ve Sertlik Neden Olur? Lenfödemde Sertleşme Evresi",
 "ogtitle": "Bacakta şişlik ve sertlik neden olur?",
 "desc": "Bacakta şişliğe sertlik eşlik ediyorsa lenfödemin ilerlediğini gösterebilir. Diğer nedenler, acil durumlar ve sertleşmiş dokuda tedavi seçenekleri.",
 "h1": "Bacakta şişlik ve sertlik neden olur?",
 "lead": "Bacakta şişlik pek çok nedene bağlı olabilir; ancak şişliğe <strong>deri ve deri altında sertleşme</strong> eşlik ediyorsa, bu genellikle sıvının uzun süredir dokuda kaldığını gösterir. Lenfödemde zamanla biriken sıvı, dokuda yağ birikimine ve <strong>fibrozise (sertleşme)</strong> yol açar. Bu evrede bacak yükseltmekle şişlik artık inmez.",
 "watopic": "bacakta şişlik ve sertlik",
 "related": ["bacakta-lenfodem", "lenfodem-evreleri"],
 "sections": [
  {"id": "nedenler", "tag": "Nedenler", "h2": "Şişlik ve sertliğin olası nedenleri", "body": [
   ("ul", ["<strong>Lenfödem:</strong> yavaş ilerleyen, ayak sırtı ve parmakları da tutan şişlik; zamanla sertleşir",
           "<strong>Toplardamar yetmezliği:</strong> varis, akşama doğru artan şişlik, ayak bileği çevresinde renk değişikliği ve sertlik",
           "<strong>Geçirilmiş enfeksiyonlar:</strong> tekrarlayan selülit atakları lenf damarlarına zarar verip sertleşmeyi artırır",
           "<strong>Lipödem:</strong> iki bacakta simetrik, ağrılı yağ birikimi; ayaklar korunur",
           "<strong>Kalp, böbrek, tiroit hastalıkları:</strong> genellikle iki bacakta birden şişlik yapar"]),
   ("note", "<strong>Tek bacakta ani başlayan şişlik, ağrı ve kızarıklık</strong> toplardamarda pıhtı belirtisi olabilir ve acil değerlendirme gerektirir.")]},

  {"id": "evre", "tag": "Evre", "h2": "Sertlik lenfödemde neyi gösterir?", "body": [
   ("table", ["Evre", "Bulgu"],
    [["Erken evre", "Yumuşak şişlik, bastırınca iz kalır, yükseltince azalır"],
     ["Orta evre", "Doku sertleşmeye başlar, bastırınca iz bırakmaz, yükseltmek yetmez"],
     ["İleri evre", "Deri kalınlaşır, kıvrımlar ve siğil benzeri değişiklikler görülebilir"]]),
   "Sertleşme, sıvının yerini zamanla yağ ve bağ dokusunun aldığını gösterir. Bu dokular yalnızca lenf drenajı ve bası tedavisiyle tamamen geri dönmez."]},

  {"id": "tedavi", "tag": "Tedavi", "h2": "Sertleşmiş bacakta tedavi seçenekleri", "body": [
   ("ul", ["<strong>Yoğun bası tedavisi:</strong> bandajlama ve uygun bası giysisi ile şişlik ve sertlik bir ölçüde azaltılabilir",
           "<strong>Enfeksiyonların önlenmesi:</strong> cilt bakımı ve ataklarının erken tedavisi ilerlemeyi yavaşlatır",
           "<strong>Fizyolojik cerrahi:</strong> uygun hastalarda lenf damarını toplardamara bağlama (LVA) veya lenf bezi nakli",
           "<strong>Azaltıcı cerrahi:</strong> birikmiş yağ ve sertleşmiş dokunun liposuction veya eksizyonla azaltılması"]),
   ("note", "İleri evrede tek bir yöntem yerine birden fazla yöntemin aşamalı planlanması gerekebilir. Plan, muayene ve görüntüleme bulgularına göre kişiye özel yapılır.")]}],

 "faqs": [
  ("Bacakta şişlik ve sertlik nasıl geçer?",
   "Neden belirlenmeden önerilecek tek bir yöntem yoktur. Lenfödeme bağlı sertlikte bası tedavisi ve lenf drenajı şişliği azaltabilir; birikmiş dokunun azaltılması için cerrahi gerekebilir."),
  ("Bacakta şişlik ve sertlik için hangi bölüme gidilir?",
   "Ani başlayan şişlikte acil servise başvurulmalıdır. Uzun süredir devam eden ve sertleşen şişlikte lenfödem açısından değerlendirme için lenfödem tedavisiyle ilgilenen hekimlere başvurulabilir."),
  ("Bacaktaki sertlik kalıcı mı?",
   "Erken dönemde sertlik bir ölçüde geriler. Uzun süredir devam eden sertlikte yağ ve bağ dokusu birikmiş olabilir; bu durumda cerrahi seçenekler değerlendirilir."),
  ("Bacakta şişlik ve kızarıklık tehlikeli mi?",
   "Kızarıklık, sıcaklık ve ateşle birlikte olan şişlik enfeksiyon, tek bacakta ani şişlik ise pıhtı belirtisi olabilir. Her iki durumda da aynı gün değerlendirme gerekir.")]},

# ------------------------------------------------------------------ 8
{"slug": "lenfodemde-bandajlama", "sources": [SRC_NCI, SRC_NHS, SRC_MP],
 "date": "2026-10-27",
 "cat": "Tedavi",
 "title": "Lenfödemde Bandajlama Nasıl Yapılır? Kısa Gerimli Bandaj Rehberi",
 "ogtitle": "Lenfödemde bandajlama nasıl yapılır?",
 "desc": "Lenfödemde bandajlama, şişliği azaltma döneminde kısa gerimli bandajlarla yapılır. Neden elastik bandaj kullanılmaz, kim uygular, nelere dikkat edilir?",
 "h1": "Lenfödemde bandajlama nasıl yapılır?",
 "lead": "Bandajlama, lenfödem tedavisinin <strong>şişliği azaltma döneminde</strong> kullanılan temel yöntemlerden biridir. Amaç, uzva katmanlı ve kademeli bir basınç uygulayarak sıvının birikmesini önlemek ve lenf akışına yardım etmektir. Doğru uygulandığında etkilidir; yanlış uygulandığında ise şişliği artırabilir. Bu nedenle bandajlama <strong>eğitimli bir terapist tarafından</strong> başlatılmalı ve hastaya öğretilmelidir.",
 "watopic": "lenfödem bandajlama",
 "related": ["lenfodem", "bacakta-lenfodem"],
 "sections": [
  {"id": "neden", "tag": "Amaç", "h2": "Bandaj neden kullanılır?", "body": [
   ("ul", ["Şişliği azaltma döneminde hacmi hızla düşürmek",
           "Dokudaki sertleşmeyi yumuşatmaya yardımcı olmak",
           "Kasların çalışırken lenf akışını desteklemesini sağlamak",
           "Hacim azaldıktan sonra bası giysisine geçişe hazırlamak"]),
   ("note", "Bandajlama genellikle manuel lenf drenajı, egzersiz ve cilt bakımıyla birlikte, birkaç haftalık yoğun tedavi döneminde uygulanır.")]},

  {"id": "nasil", "tag": "Uygulama", "h2": "Bandajlama nasıl yapılır?", "body": [
   ("steps", [
    ("CİLT BAKIMI", "Deri temizlenir ve nemlendirilir; yara veya enfeksiyon varsa önce o ele alınır."),
    ("ALT KATMAN", "Deri korunur, kıvrımlar ve çukurlar yumuşak dolgu malzemesiyle düzlenir."),
    ("KISA GERİMLİ BANDAJ", "Bandaj parmaklardan başlayarak yukarı doğru, uçta daha fazla, yukarıda daha az basınç olacak şekilde katmanlı sarılır."),
    ("KONTROL", "Parmakların rengi, hissi ve hareketi kontrol edilir; uyuşma veya morarma olursa bandaj gevşetilir.")]),
   ("note", "Lenfödemde <strong>kısa gerimli bandaj</strong> kullanılır. Spor yaralanmalarında kullanılan uzun gerimli (elastik) bandajlar dinlenirken de yüksek basınç uyguladığı için uygun değildir.")]},

  {"id": "dikkat", "tag": "Dikkat", "h2": "Nelere dikkat edilmeli?", "body": [
   ("ul", ["Bandaj ağrı, uyuşma, karıncalanma veya renk değişikliği yapmamalıdır",
           "Kalp yetmezliği, ağır damar tıkanıklığı veya aktif enfeksiyon varsa hekim değerlendirmesi olmadan uygulanmaz",
           "Kayan veya kıvrılan bandaj yeniden sarılmalıdır",
           "Bandaj altında ciltte yara oluşursa uygulama durdurulup kontrole gidilmelidir"]),
   ("note", "Bandajlama şişliği kontrol eder; lenf akışındaki bozukluğu ortadan kaldırmaz. Konservatif tedaviye rağmen ilerleyen lenfödemde cerrahi seçenekler değerlendirilebilir.")]}],

 "faqs": [
  ("Lenfödem bandajı evde yapılabilir mi?",
   "Evet, ancak önce eğitimli bir terapistten doğru tekniği öğrenmek gerekir. Yanlış sarılan bandaj şişliği artırabilir."),
  ("Lenfödemde elastik bandaj kullanılır mı?",
   "Hayır. Lenfödemde kısa gerimli bandajlar kullanılır. Elastik bandajlar dinlenirken de yüksek basınç uyguladığı için uygun değildir."),
  ("Bandaj ne kadar süre takılır?",
   "Yoğun tedavi döneminde genellikle gün boyu ve terapistin önerisine göre gece de takılır. Süre ve düzen hastaya göre belirlenir."),
  ("Bandaj mı, bası çorabı mı?",
   "Bandaj daha çok şişliği azaltma döneminde, bası çorabı ise azalan hacmi korumak için kullanılır. İkisi tedavinin farklı aşamalarıdır.")]},

# ------------------------------------------------------------------ 9
{"slug": "kopek-memesi-hastaligi-tehlikeli-mi", "sources": K_HS,
 "date": "2026-10-28",
 "cat": "Hidradenit",
 "title": "Köpek Memesi Hastalığı Tehlikeli mi, Öldürür mü?",
 "ogtitle": "Köpek memesi hastalığı tehlikeli mi?",
 "desc": "Köpek memesi hastalığı (hidradenit) öldürücü bir hastalık değildir; ancak tedavi edilmezse ilerleyebilir. Hangi durumlar ciddidir, ne zaman başvurulmalı?",
 "h1": "Köpek memesi hastalığı tehlikeli mi?",
 "lead": "Halk arasında <strong>köpek memesi</strong> olarak bilinen hidradenitis süpürativa, koltuk altı, kasık ve meme altında tekrarlayan ağrılı şişlikler yapan kronik bir hastalıktır. Ailelerin ve hastaların sık sorduğu \"öldürür mü\" sorusunun yanıtı: <strong>hayır, hidradenit öldürücü bir hastalık değildir</strong>. Ancak tedavi edilmediğinde ilerleyebilir, yaşam kalitesini belirgin biçimde etkileyebilir ve nadiren ciddi komplikasyonlara yol açabilir.",
 "watopic": "köpek memesi (hidradenit) tedavisi",
 "related": ["hidradenit"],
 "sections": [
  {"id": "seyir", "tag": "Seyir", "h2": "Hastalık nasıl seyreder?", "body": [
   ("ul", ["Başlangıçta tek tük, ağrılı şişlikler olur",
           "Tedavi edilmezse ataklar sıklaşır, deri altında tüneller oluşur",
           "İleri evrede tüneller birleşir, akıntı ve kalıcı izler gelişir",
           "Koltuk altı ve kasıkta hareket kısıtlılığı görülebilir"]),
   ("note", "Hidradenit bulaşıcı değildir ve hijyen eksikliğinden kaynaklanmaz. Sigara ve fazla kilo hastalığın seyrini kötüleştiren başlıca etkenlerdir.")]},

  {"id": "ciddi", "tag": "Ciddi durumlar", "h2": "Hangi durumlar ciddidir?", "body": [
   ("ul", ["<strong>Yaygın enfeksiyon:</strong> yüksek ateş, titreme ve hızla yayılan kızarıklık",
           "<strong>Ağır ağrı ve hareket kısıtlılığı:</strong> günlük yaşamı ve çalışmayı engelleyen tablo",
           "<strong>Uzun yıllar süren, iyileşmeyen yaralar:</strong> özellikle kalça ve makat çevresinde, nadiren deri kanseri gelişebileceği bildirilmiştir",
           "<strong>Ruhsal etkiler:</strong> ağrı, akıntı ve koku nedeniyle sosyal yaşamdan çekilme ve depresyon"]),
   ("note", "Uzun süredir iyileşmeyen, şekil değiştiren ya da kolay kanayan bir yara varsa mutlaka muayene edilmelidir.")]},

  {"id": "tedavi", "tag": "Tedavi", "h2": "Tedavi seçenekleri", "body": [
   "Tedavi hastalığın evresine göre planlanır. Erken evrede ilaç tedavisiyle ataklar kontrol altına alınabilir. Deri altında tünelleşme ve kalıcı iz oluşmuşsa, hastalıklı alanın bütünüyle çıkarılması ve bölgenin flep ya da greftle onarılması gündeme gelir.",
   ("note", "Her atakta apsenin boşaltılması o günkü ağrıyı geçirir; ancak tünelleri yerinde bıraktığı için şikâyet aynı bölgede geri dönebilir. Tekrarlayan tabloda kalıcı plan için değerlendirme önerilir.")]}],

 "faqs": [
  ("Köpek memesi hastalığı öldürür mü?",
   "Hayır. Hidradenit öldürücü bir hastalık değildir. Ancak tedavi edilmezse ilerleyebilir ve yaşam kalitesini ciddi biçimde etkileyebilir."),
  ("Köpek memesi hastalığı kansere dönüşür mü?",
   "Çok nadiren, özellikle kalça ve makat çevresinde uzun yıllar iyileşmeyen yaralarda deri kanseri gelişebileceği bildirilmiştir. Bu nedenle uzun süredir iyileşmeyen yaralar muayene edilmelidir."),
  ("Köpek memesi bulaşıcı mı?",
   "Hayır. Akıntı ve iltihap görüntüsü bulaşıcı izlenimi verse de hastalık kişiden kişiye geçmez."),
  ("Köpek memesi hastalığının kesin çözümü var mı?",
   "Erken evrede ilaçla kontrol sağlanabilir; ileri evrede hastalıklı alanın çıkarılıp onarılması aynı bölgede nüksü belirgin biçimde azaltır. Ancak hastalık başka bölgelerde yeniden başlayabileceği için kesin sonuç vaadi verilemez.")]},

# ------------------------------------------------------------------ 10
{"slug": "lenfodemden-korunma-yollari", "sources": K_LEN_KOR,
 "date": "2026-10-29",
 "cat": "Hasta Rehberi",
 "title": "Lenfödemden Korunma Yolları: Koldan Kan Alınır mı, Uçağa Binilir mi?",
 "ogtitle": "Lenfödemden korunma yolları",
 "desc": "Lenf bezi alınan veya radyoterapi gören hastalar lenfödem riskini nasıl azaltır? Koldan kan alma, tansiyon ölçümü, uçak yolculuğu, sıcak ve cilt bakımı.",
 "h1": "Lenfödemden korunma yolları",
 "lead": "Lenf bezleri alınmış ya da radyoterapi görmüş kişilerde lenfödem riskini sıfırlayan bir yöntem yoktur; ancak <strong>riski azaltan ve erken fark etmeyi sağlayan</strong> önlemler vardır. Hastaların en çok sorduğu sorular günlük yaşamla ilgilidir: koldan kan alınabilir mi, tansiyon ölçülebilir mi, uçağa binilir mi, hamama girilir mi? Güncel öneriler, eskiden olduğu kadar kısıtlayıcı değildir.",
 "watopic": "lenfödemden korunma",
 "related": ["kolda-lenfodem", "lenfodem-belirtileri"],
 "sections": [
  {"id": "cilt", "tag": "Cilt", "h2": "Cildi korumak", "body": [
   ("ul", ["Cildi her gün nemlendirmek; kuruma ve çatlaklar enfeksiyona kapı açar",
           "Bahçe ve mutfak işlerinde eldiven kullanmak",
           "Böcek ısırığı ve güneş yanığından korunmak",
           "Küçük kesik ve sıyrıkları temizleyip takip etmek",
           "Kızarıklık, sıcaklık veya ateş olursa aynı gün başvurmak"]),
   ("note", "Enfeksiyon, lenfödemi başlatan ya da kötüleştiren en önemli tetikleyicilerden biridir. Cilt bakımı korunmanın temelidir.")]},

  {"id": "gunluk", "tag": "Günlük yaşam", "h2": "Sık sorulan günlük durumlar", "body": [
   ("ul", ["<strong>Koldan kan alma ve tansiyon ölçümü:</strong> mümkünse risk altındaki kol yerine diğer kol kullanılır",
           "<strong>Uçak yolculuğu:</strong> çoğu hasta uçak yolculuğu yapabilir; lenfödem varsa uçuşta bası giysisi giyilmesi ve hareket edilmesi önerilir",
           "<strong>Sıcak, sauna ve hamam:</strong> aşırı sıcak şişliği artırabilir; uzun süre kalmaktan kaçınılmalıdır",
           "<strong>Takı ve giysiler:</strong> sıkı yüzük, saat ve lastikli kol ağızlarından kaçınılmalıdır",
           "<strong>Ağır yük:</strong> kademeli olarak artırılan egzersiz güvenlidir; ani ve aşırı yüklenmeden kaçınılır"]),
   ("note", "Eski önerilerde risk altındaki kolun neredeyse hiç kullanılmaması istenirdi. Güncel yaklaşımda kontrollü egzersizin riski artırmadığı, aksine faydalı olduğu kabul edilmektedir.")]},

  {"id": "erken", "tag": "Erken fark etme", "h2": "Erken fark etmek için neler yapılabilir?", "body": [
   ("ul", ["Kolda veya bacakta ağırlık, dolgunluk hissine dikkat etmek",
           "Yüzük ve saatin sıkmaya başlamasını not etmek",
           "Kontrollerde iki uzvun çevre ölçümlerinin karşılaştırılmasını istemek",
           "Sağlıklı kiloyu korumak"]),
   ("note", "Lenfödem erken evrede fark edildiğinde tedaviye daha iyi yanıt verir. Ameliyat sonrası takipte şüpheli bir değişiklik fark ederseniz beklemeden bildirin.")]}],

 "faqs": [
  ("Lenfödemli koldan kan alınır mı?",
   "Mümkünse risk altındaki ya da lenfödemli kol yerine diğer koldan kan alınması ve tansiyon ölçülmesi önerilir. Her iki kol da etkilenmişse hekiminizle uygun yöntemi konuşun."),
  ("Lenfödem hastası uçağa binebilir mi?",
   "Evet. Lenfödem varsa uçuş sırasında bası giysisi giyilmesi, bol su içilmesi ve uzun süre hareketsiz kalınmaması önerilir."),
  ("Lenfödemde hamama veya saunaya girilir mi?",
   "Aşırı sıcak şişliği artırabilir. Hamam ve saunada uzun süre kalmaktan kaçınılması önerilir."),
  ("Lenfödem tamamen önlenebilir mi?",
   "Tamamen önleyen bir yöntem yoktur. Cilt bakımı, kilo kontrolü, düzenli egzersiz ve erken fark etme riski azaltır.")]},

# ------------------------------------------------------------------ 11
{"slug": "lenfodemde-kinezyo-bantlama", "sources": [SRC_SP, SRC_NCI, SRC_DER],
 "date": "2026-10-30",
 "cat": "Tedavi",
 "title": "Lenfödemde Kinezyo Bantlama İşe Yarar mı?",
 "ogtitle": "Lenfödemde kinezyo bantlama işe yarar mı?",
 "desc": "Kinezyo bant lenfödemde bazı hastalarda yardımcı olabilir; ancak bandajlama ve bası giysisinin yerini tutmaz. Kanıtlar, kimlere uygun, cilt riskleri.",
 "h1": "Lenfödemde kinezyo bantlama işe yarar mı?",
 "lead": "Kinezyo bant, deriye yapıştırılan elastik bir banttır ve son yıllarda lenfödemde de sıkça kullanılmaktadır. Bandın deriyi hafifçe kaldırarak deri altındaki lenf akışını kolaylaştırdığı düşünülür. Çalışmalar <strong>bazı hastalarda yardımcı olabileceğini</strong> göstermektedir; ancak <strong>bandajlama ve bası giysisinin yerini tutmaz</strong>.",
 "watopic": "lenfödem tedavi seçenekleri",
 "related": ["lenfodem", "kolda-lenfodem"],
 "sections": [
  {"id": "nasil", "tag": "Mekanizma", "h2": "Kinezyo bant nasıl etki eder?", "body": [
   ("ul", ["Bant, deriyi hafifçe kaldırarak deri altındaki alanı genişletir",
           "Bu etkinin yüzeysel lenf kanallarında akışı kolaylaştırdığı düşünülür",
           "Hareket sırasında deri üzerinde hafif bir masaj etkisi oluşturur",
           "Bası giysisi giyilemeyen bölgelerde (göğüs duvarı, gövde, yüz) tercih edilebilir"])]},

  {"id": "kanit", "tag": "Kanıtlar", "h2": "Bilimsel kanıtlar ne söylüyor?", "body": [
   "Kinezyo bantla yapılan çalışmalar küçük ve farklı yöntemlerle yürütülmüştür. Genel tablo şöyledir:",
   ("ul", ["Bazı hastalarda şişlik ve ağırlık hissinde azalma bildirilmiştir",
           "Bandajlamaya göre üstün olduğu gösterilmemiştir",
           "Tedavinin tamamlayıcı bir parçası olarak kullanılması daha uygundur"]),
   ("note", "Kinezyo bant, bandajlama veya bası giysisine uyum sağlayamayan hastalarda ya da bu yöntemlerin uygulanamadığı bölgelerde bir seçenek olarak düşünülebilir.")]},

  {"id": "dikkat", "tag": "Dikkat", "h2": "Kimlere uygun değil?", "body": [
   ("ul", ["Bant yapıştırıcısına alerjisi olanlar",
           "Aktif enfeksiyon veya açık yarası olanlar",
           "Çok ince, kırılgan veya radyoterapi sonrası hassas deride dikkatli olunmalıdır",
           "Kaşıntı, kızarıklık veya kabarcık gelişirse bant hemen çıkarılmalıdır"]),
   ("note", "Bantlama, lenfödem tedavisinde deneyimli bir terapist tarafından uygulanmalıdır. Bantlama da diğer konservatif yöntemler gibi şişliği yönetir; lenf akışındaki bozukluğu ortadan kaldırmaz.")]}],

 "faqs": [
  ("Kinezyo bant lenfödemi geçirir mi?",
   "Hayır. Bazı hastalarda şişlik ve ağırlık hissini azaltabilir; ancak lenfödemi ortadan kaldırmaz ve bandajlama ile bası giysisinin yerini tutmaz."),
  ("Kinezyo bant kaç gün kalır?",
   "Genellikle birkaç gün kalabilir. Süre, cildin durumuna ve terapistin önerisine göre belirlenir. Kaşıntı veya kızarıklık olursa erken çıkarılmalıdır."),
  ("Kinezyo bantı kendim yapabilir miyim?",
   "Bandın yönü ve gerginliği etkiyi belirler. İlk uygulamaların lenfödem konusunda eğitimli bir terapist tarafından yapılması önerilir."),
  ("Meme kanseri sonrası göğüs şişliğinde kinezyo bant kullanılır mı?",
   "Bası giysisinin iyi oturmadığı göğüs duvarı ve gövde bölgesinde kinezyo bant bir seçenek olabilir. Radyoterapi görmüş deride dikkatli olunmalıdır.")]},

# ------------------------------------------------------------------ 12
{"slug": "mikrotia-doktoru-nasil-secilir", "sources": K_MIK,
 "date": "2026-10-31",
 "cat": "Mikrotia",
 "title": "Mikrotia Ameliyatı Yapan Doktor Nasıl Seçilir? Ailelerin Soracağı Sorular",
 "ogtitle": "Mikrotia ameliyatı yapan doktor nasıl seçilir?",
 "desc": "Mikrotia ameliyatı için doktor seçerken nelere bakılmalı? Deneyim, yöntem, iki aşamalı plan, işitme ekibiyle çalışma ve ilk görüşmede sorulacak sorular.",
 "h1": "Mikrotia ameliyatı yapan doktor nasıl seçilir?",
 "lead": "Mikrotia onarımı, plastik cerrahinin el becerisi ve deneyim gerektiren alanlarından biridir. Kulak iskeleti kaburga kıkırdağından elle oyulur ve sonucun doğal görünmesi bu işçiliğe bağlıdır. Bu nedenle ailelerin doktor seçerken <strong>yöntemi, deneyimi ve süreç planını</strong> açıkça sorması önemlidir. Aşağıdaki sorular ilk görüşmeye hazırlanmanıza yardımcı olabilir.",
 "watopic": "mikrotia ameliyatı planlaması",
 "related": ["mikrotia"],
 "sections": [
  {"id": "uzmanlik", "tag": "Uzmanlık", "h2": "Hangi uzmanlık alanı?", "body": [
   "Kulak kepçesinin onarımı <strong>plastik, rekonstrüktif ve estetik cerrahi</strong> alanına girer. İşitme ise kulak burun boğaz ve odyoloji ekibiyle birlikte değerlendirilir. İki ekibin birbiriyle uyumlu çalışması, özellikle işitme cerrahisi de planlanıyorsa, ameliyatların sırası açısından önemlidir.",
   ("note", "Kulak kepçesi onarımı genellikle işitme cerrahisinden önce yapılır; çünkü işitme ameliyatı, yeni kulak için gereken deri ve damar yapısını etkileyebilir.")]},

  {"id": "sorular", "tag": "Sorular", "h2": "İlk görüşmede sorulabilecek sorular", "body": [
   ("ul", ["Hangi yöntemi uyguluyorsunuz: kendi kaburga kıkırdağı mı, sentetik iskelet mi? Neden?",
           "Çocuğumun yaşı ve kıkırdak gelişimi ameliyat için uygun mu?",
           "Ameliyat kaç aşamada yapılacak ve aşamalar arasında ne kadar beklenecek?",
           "Kaburgadan kıkırdak alınan bölgede ne beklemeliyiz?",
           "Ameliyat sonrası bakım ve kontroller nasıl planlanıyor?",
           "İşitme değerlendirmesi ve tedavisi için hangi ekiple birlikte çalışıyorsunuz?",
           "Olası komplikasyonlar nelerdir ve nasıl yönetilir?"]),
   ("note", "Kendi kaburga kıkırdağıyla yapılan onarım <strong>iki aşamada</strong> tamamlanır: birinci aşamada kulak iskeleti yerleştirilir ve kulak memesi doğru konuma taşınır; <strong>12 ay sonraki</strong> ikinci aşamada kulak baştan ayrılarak doğal açısı verilir.")]},

  {"id": "dikkat", "tag": "Dikkat", "h2": "Nelere dikkat edilmeli?", "body": [
   ("ul", ["Gerçekçi beklenti: hedef sağlıklı kulağın birebir kopyası değil, doğal ve uyumlu bir kulaktır",
           "Aceleci zamanlama: kıkırdak yeterli gelişmeden yapılan onarım sonucu sınırlayabilir",
           "Daha önce girişim yapılmış bölgeler: revizyon ameliyatları ilk onarımdan daha zor olabilir",
           "Süreç boyunca aynı ekiple takip: aşamalı bir tedavide süreklilik önemlidir"]),
   ("note", "İzmir'de Doç. Dr. Tahsin Oğuz Acartürk, kaburga kıkırdağıyla kulak rekonstrüksiyonu ve mikrotia onarımı konusunda deneyimlidir; ilk görüşmede mikrotianın derecesi ve karşı kulağın yapısı değerlendirilerek iki aşamalı plan çıkarılır.")]}],

 "faqs": [
  ("Mikrotia ameliyatını hangi doktor yapar?",
   "Kulak kepçesi onarımı plastik, rekonstrüktif ve estetik cerrahi uzmanları tarafından yapılır. İşitme değerlendirmesi kulak burun boğaz ekibiyle birlikte planlanır."),
  ("Mikrotia ameliyatı kaç aşamada yapılır?",
   "Kendi kaburga kıkırdağıyla yapılan onarım iki aşamada tamamlanır ve aşamalar arasında 12 ay beklenir."),
  ("Yetişkinlikte mikrotia ameliyatı yapılabilir mi?",
   "Evet. Kıkırdak gelişimi tamamlandığı için zamanlama açısından engel yoktur. Daha önce girişim yapılmışsa planlama buna göre yapılır."),
  ("İlk görüşmeye ne götürmeliyim?",
   "Varsa işitme testi sonuçları, tomografi raporları, önceki ameliyat bilgileri ve kulakların farklı açılardan çekilmiş fotoğrafları değerlendirmeyi kolaylaştırır.")]},

# ------------------------------------------------------------------ 13
{"slug": "lenfodemde-suluk-tedavisi", "sources": [SRC_SP, SRC_NHS, SRC_NCI],
 "date": "2026-11-01",
 "cat": "Lenfödem",
 "title": "Lenfödemde Sülük Tedavisi İşe Yarar mı? Riskler ve Kanıtlar",
 "ogtitle": "Lenfödemde sülük tedavisi işe yarar mı?",
 "desc": "Sülük tedavisinin lenfödemi azalttığını gösteren güvenilir kanıt yoktur. Lenfödemli dokuda enfeksiyon riski yüksektir. Kanıtlanmış tedaviler neler?",
 "h1": "Lenfödemde sülük tedavisi işe yarar mı?",
 "lead": "Sülük tedavisi, lenfödem için en sık araştırılan alternatif yöntemlerden biridir. Ancak bugün <strong>sülüğün lenfödemi azalttığını gösteren güvenilir bir kanıt yoktur</strong>. Üstelik lenfödemli dokuda bağışıklık savunması zayıfladığı için, deriyi delen her uygulama <strong>enfeksiyon riskini</strong> artırır. Lenfödemde enfeksiyon, hastalığı ilerleten en önemli etkenlerden biridir.",
 "watopic": "lenfödem tedavi seçenekleri",
 "related": ["lenfodem", "lenfodem-evreleri"],
 "sections": [
  {"id": "neden", "tag": "Neden tercih ediliyor", "h2": "Neden sülük tedavisi deneniyor?", "body": [
   "Sülüğün salgıladığı maddelerin kanın pıhtılaşmasını geçici olarak engellediği bilinir. Bu özellik nedeniyle tıpta, bazı mikrocerrahi ameliyatlardan sonra <strong>toplardamar dönüşü bozulmuş dokularda</strong> kontrollü koşullarda kullanılır. Ancak bu durum lenfödemden farklıdır: lenfödemde sorun kan dolaşımı değil, lenf akışıdır.",
   ("note", "Bir yöntemin başka bir hastalıkta işe yaraması, lenfödemde de etkili olacağı anlamına gelmez.")]},

  {"id": "risk", "tag": "Riskler", "h2": "Lenfödemde riskleri nelerdir?", "body": [
   ("ul", ["<strong>Enfeksiyon:</strong> sülük ısırığı deride açık bir yara oluşturur; sülüklerin taşıdığı bakteriler ciddi enfeksiyonlara yol açabilir",
           "<strong>Selülit atakları:</strong> lenfödemde her enfeksiyon lenf damarlarına ek zarar verebilir",
           "<strong>Uzun süren kanama:</strong> ısırık yeri saatlerce sızabilir",
           "<strong>Alerjik tepkiler ve iz:</strong> bazı kişilerde görülebilir"]),
   ("note", "Lenfödemli bir uzuvda deriyi delen uygulamalardan — sülük, hacamat, iğneli yöntemler — kaçınılması önerilir.")]},

  {"id": "alternatif", "tag": "Kanıtlanmış yöntemler", "h2": "Etkinliği gösterilmiş tedaviler", "body": [
   ("ul", ["Bası tedavisi: bandajlama ve bası giysisi",
           "Manuel lenf drenajı",
           "Düzenli egzersiz",
           "Cilt bakımı ve enfeksiyonların önlenmesi",
           "Uygun hastalarda mikrocerrahi: lenf damarını toplardamara bağlama (LVA) ve lenf bezi nakli"]),
   ("note", "Konservatif tedaviye rağmen ilerleyen lenfödemde, alternatif yöntemlerle zaman kaybetmek yerine cerrahi seçeneklerin değerlendirilmesi önerilir.")]}],

 "faqs": [
  ("Sülük lenfödeme iyi gelir mi?",
   "Sülüğün lenfödemi azalttığını gösteren güvenilir bir kanıt yoktur. Lenfödemli dokuda enfeksiyon riskini artırabileceği için önerilmez."),
  ("Sülük tedavisinden sonra şişlik arttı, neden?",
   "Isırık yerinden gelişen bir enfeksiyon şişliği artırabilir. Kızarıklık, sıcaklık veya ateş varsa aynı gün değerlendirme yapılmalıdır."),
  ("Lenfödemde hacamat ve sülük aynı risk mi taşır?",
   "Her ikisi de deride açık yara oluşturduğu için lenfödemli dokuda enfeksiyon riski taşır ve önerilmez."),
  ("Lenfödemde hangi tedaviler gerçekten işe yarar?",
   "Bası tedavisi, manuel lenf drenajı, egzersiz ve cilt bakımı temel tedavilerdir. Uygun hastalarda mikrocerrahi yöntemler değerlendirilir.")]},

# ------------------------------------------------------------------ 14
{"slug": "kolda-sislik-neden-olur", "sources": [SRC_NCI, SRC_NHS, SRC_ODEM],
 "date": "2026-11-02",
 "cat": "Hasta Rehberi",
 "title": "Kolda Şişlik Neden Olur? Ne Zaman Acil, Hangi Bölüme Gidilir?",
 "ogtitle": "Kolda şişlik neden olur?",
 "desc": "Kolda şişlik; darbe, enfeksiyon, pıhtı, lenfödem veya kalp-böbrek kaynaklı olabilir. Ağrı, kızarıklık ve sertlikle birlikte olan şişlikte ne yapılmalı?",
 "h1": "Kolda şişlik neden olur?",
 "lead": "Kolda şişliğin pek çok nedeni vardır ve bunların bir kısmı kendiliğinden geçerken bir kısmı <strong>acil değerlendirme</strong> gerektirir. Şişliğin ne zaman başladığı, tek kolda mı iki kolda mı olduğu, <strong>ağrı, kızarıklık veya sertliğin</strong> eşlik edip etmediği nedeni tahmin etmede yol gösterir. Meme kanseri tedavisi görmüş kişilerde kolda gelişen kalıcı şişlik ise öncelikle lenfödem açısından değerlendirilmelidir.",
 "watopic": "kolda şişlik değerlendirmesi",
 "related": ["kolda-lenfodem", "el-cerrahisi"],
 "sections": [
  {"id": "nedenler", "tag": "Nedenler", "h2": "Kolda şişliğin sık nedenleri", "body": [
   ("table", ["Neden", "Tipik özellik"],
    [["Darbe, burkulma, kırık", "Yaralanma sonrası ağrı, morarma ve hareket kısıtlılığı"],
     ["Enfeksiyon (selülit)", "Kızarıklık, sıcaklık, ağrı, bazen ateş"],
     ["Toplardamarda pıhtı", "Tek kolda ani şişlik, ağrı, morumsu renk; damar yolu veya kateter sonrası görülebilir"],
     ["Lenfödem", "Yavaş başlayan, ağırlık hissi yapan şişlik; meme kanseri tedavisi sonrası sık"],
     ["Böcek ısırığı, alerji", "Kaşıntı, kızarıklık, hızlı başlayan lokal şişlik"],
     ["Kalp, böbrek, karaciğer hastalıkları", "Genellikle iki taraflı, vücudun başka bölgelerinde de ödem"]]),
   ("note", "Tek kolda nedeni bilinmeyen ani şişlik, kızarıklık ve ağrı birlikteyse aynı gün değerlendirme gerekir.")]},

  {"id": "acil", "tag": "Acil", "h2": "Ne zaman acile gidilmeli?", "body": [
   ("ul", ["Nefes darlığı, göğüs ağrısı veya çarpıntı",
           "Hızla artan şişlik ve şiddetli ağrı",
           "Kızarıklıkla birlikte ateş ve titreme",
           "Kolda uyuşma, soğukluk veya renk değişikliği",
           "Ciddi bir yaralanma sonrası şekil bozukluğu"]),
   ("note", "Nefes darlığı veya göğüs ağrısı akciğerde pıhtı belirtisi olabilir; bu durumda vakit kaybetmeden acil yardım istenmelidir.")]},

  {"id": "bolum", "tag": "Başvuru", "h2": "Hangi bölüme başvurulmalı?", "body": [
   ("ul", ["<strong>Ani başlayan şişlik, ağrı, ateş:</strong> acil servis",
           "<strong>Yaralanma sonrası şişlik:</strong> acil servis veya ortopedi",
           "<strong>Meme kanseri tedavisi sonrası yavaş gelişen şişlik:</strong> onkoloji ekibine bildirim ve lenfödem değerlendirmesi",
           "<strong>Uzun süredir devam eden, ağırlık yapan şişlik:</strong> lenfödem tedavisiyle ilgilenen fizik tedavi ve plastik cerrahi hekimleri"]),
   ("note", "Kol lenfödeminde tedavi bası giysisi, lenf drenajı ve egzersizle başlar. Uygun hastalarda lenf damarını toplardamara bağlama (LVA) ve lenf bezi nakli gibi mikrocerrahi yöntemler değerlendirilebilir.")]}],

 "faqs": [
  ("Kolda şişlik ve ağrı neden olur?",
   "Darbe, enfeksiyon, toplardamarda pıhtı ve lenfödem en sık nedenlerdir. Ani başlayan, ağrılı ve kızarık şişlik aynı gün değerlendirilmelidir."),
  ("Kolda şişlik hangi bölüme bakar?",
   "Ani ve ağrılı şişlikte acil servise başvurulmalıdır. Meme kanseri tedavisi sonrası yavaş gelişen şişlikte lenfödem değerlendirmesi için fizik tedavi veya plastik cerrahi hekimlerine başvurulabilir."),
  ("Kolda şişlik ve sertlik neyin belirtisi?",
   "Uzun süredir devam eden şişliğe sertlik eklenmesi lenfödemin ilerlediğini gösterebilir. Kızarıklık ve sıcaklıkla birlikte olan sertlik ise enfeksiyon belirtisi olabilir."),
  ("Kolda şişlik kendiliğinden geçer mi?",
   "Küçük darbe ve böcek ısırığına bağlı şişlik çoğu zaman günler içinde geçer. Haftalarca süren ya da artan şişlik değerlendirilmelidir.")]},

# ------------------------------------------------------------------ 15
{"slug": "meme-alti-ve-kalcada-ciban", "sources": K_HS,
 "date": "2026-11-03",
 "cat": "Hidradenit",
 "title": "Meme Altında ve Kalçada Tekrarlayan Çıban: Hidradenit Olabilir mi?",
 "ogtitle": "Meme altında ve kalçada tekrarlayan çıban",
 "desc": "Meme altında, kalçada veya makat çevresinde tekrarlayan çıbanlar hidradenit belirtisi olabilir. Kıl dönmesi ve basit çıbandan farkı, tedavi seçenekleri.",
 "h1": "Meme altında ve kalçada tekrarlayan çıban",
 "lead": "Hidradenitis süpürativa yalnızca koltuk altında görülmez. <strong>Meme altı, memeler arası, kalça ve makat çevresi</strong> de hastalığın sık yerleştiği bölgelerdir. Bu bölgelerde aynı yerde tekrar tekrar çıkan, iz bırakan ya da akıntılı kanallar oluşturan şişlikler, basit bir çıbandan farklı olarak hidradenit belirtisi olabilir.",
 "watopic": "tekrarlayan çıban (hidradenit)",
 "related": ["hidradenit"],
 "sections": [
  {"id": "bolgeler", "tag": "Bölgeler", "h2": "Hangi bölgelerde görülür?", "body": [
   ("ul", ["Koltuk altı",
           "Kasık ve iç uyluk",
           "Meme altı ve memeler arası",
           "Kalça ve makat çevresi",
           "Ense ve bel çevresi"]),
   "Ortak özellik, bu bölgelerin <strong>sürtünmenin fazla olduğu ve kıl köklerinin yoğun bulunduğu</strong> alanlar olmasıdır. Hastalık kıl kökünün tıkanmasıyla başlar.",
   ("note", "Fazla kilo ve sigara, özellikle meme altı ve kalça tutulumunda atakların sıklığını artırır.")]},

  {"id": "ayrim", "tag": "Ayrım", "h2": "Basit çıban, kıl dönmesi ve hidradenit farkı", "body": [
   ("table", ["Durum", "Tipik özellik"],
    [["Basit çıban", "Tek seferlik, birkaç günde boşalıp iyileşir; aynı yerde tekrarlamaz"],
     ["Kıl dönmesi (pilonidal sinüs)", "Kuyruk sokumunun üst kısmında, kalça yarığında delik veya şişlik"],
     ["Hidradenit", "Birden fazla bölgede, aynı yerde tekrarlayan şişlikler; tüneller ve iz bırakır"]]),
   ("note", "Hidradenit hastalarında kıl dönmesi de birlikte görülebilir. Kesin ayrım muayene ile yapılır.")]},

  {"id": "tedavi", "tag": "Tedavi", "h2": "Tedavi nasıl planlanır?", "body": [
   "Erken evrede ilaç tedavisi ve yaşam tarzı düzenlemeleriyle ataklar kontrol altına alınabilir. Deri altında tünelleşme ve kalıcı iz oluşmuşsa, hastalıklı alanın bütünüyle çıkarılması ve bölgenin onarılması gündeme gelir.",
   ("ul", ["Meme altı ve kalça gibi bölgelerde onarım yöntemi, deri gerginliği ve hareket dikkate alınarak seçilir",
           "Geniş alanlarda lokal flep veya greft kullanılabilir",
           "Kilo kontrolü ve sigaranın bırakılması tedavinin parçasıdır"]),
   ("note", "Tekrarlayan apselerin her seferinde boşaltılması o anki ağrıyı geçirir; ancak tünelleri yerinde bıraktığı için şikâyet aynı bölgede geri dönebilir.")]}],

 "faqs": [
  ("Meme altında çıban neden çıkar?",
   "Sürtünme, nem ve kıl kökü tıkanması meme altında çıban oluşumunu kolaylaştırır. Aynı bölgede tekrarlıyorsa hidradenit olabilir."),
  ("Kalçada tekrarlayan çıban hidradenit mi?",
   "Olabilir. Kalça ve makat çevresinde aynı yerde tekrarlayan, iz bırakan ve akıntılı kanallar oluşturan şişlikler hidradenit açısından değerlendirilmelidir."),
  ("Kıl dönmesi ile hidradenit aynı şey mi?",
   "Hayır, farklı hastalıklardır; ancak bazı hastalarda birlikte görülebilir. Ayrım muayene ile yapılır."),
  ("Meme altındaki hidradenit ameliyat edilir mi?",
   "Tünelleşme ve kalıcı iz oluşmuşsa hastalıklı alanın çıkarılıp onarılması değerlendirilebilir. Karar hastalığın evresine ve tutulan alanın genişliğine göre verilir.")]},
]
