# -*- coding: utf-8 -*-
"""
Lenfodem sayfasi — artik uretici sisteme dahil.
Turkce cikti: lenfodem-lipodem-cerrahisi.html (mevcut dosyanin uzerine yazilir)
"""

LENFODEM = [{
 "key":"lenfodem", "slug":"lenfodem-lipodem-cerrahisi.html", "prio":"1.0",
 "crumb":"Lenfödem ve Lipödem Cerrahisi",
 # HUB sayfasi: ticari sorguyu ("lenfodem tedavisi/cerrahisi/ameliyati") sahiplenir.
 # "nedir", "evreleri", "belirtileri" ifadeleri bilerek cikarildi — bunlarin
 # adanmis uydu sayfalari var ve hub onlarla ayni sorguda yarisiyordu.
 "title":"Lenfödem Tedavisi: Cerrahi Yöntemler ve LVA | Doç. Dr. T. Oğuz Acartürk",
 "ogtitle":"Lenfödem Tedavisi: Cerrahi Yöntemler ve LVA",
 "desc":"Lenfödem nasıl tedavi edilir? LVA (lenfovenöz anastomoz), vaskülarize lenf nodu transferi ve azaltıcı cerrahi seçenekleri. Pittsburgh Üniversitesi doçenti Doç. Dr. T. Oğuz Acartürk tarafından hazırlanmış cerrahi tedavi rehberi.",
 "eyebrow":"Mikrocerrahi Programı",
 "h1":"Lenfödem tedavisi ve cerrahi seçenekler",
 "lead":"Lenfödem, ömür boyu yalnızca bandaj ve masajla idare edilmesi gereken bir durum değildir. Erken evrelerden itibaren mikrocerrahi ile tedavi edilebilen bir hastalıktır. Bu sayfa; evreleme, tanı yöntemleri, cerrahi seçenekler ve iyileşme sürecine dair sorularınızı yanıtlamak için hazırlanmıştır.",
 "watopic":"lenfödem tedavisi",
 "about":"Lenfödem", "aboutType":"MedicalCondition",
 "card":"Lenfödem cerrahisi", "cardsub":"LVA, lenf nodu transferi ve azaltıcı cerrahi",
 "procedure":{"name":"Lenfatikovenöz Anastomoz (LVA)",
   "how":"Tıkalı lenf kanalları mikroskop altında 0,3–0,8 mm çapındaki komşu toplardamarlara bağlanarak lenf sıvısının venöz dolaşıma yönlendirilmesi sağlanır.",
   "prep":"Muayene, evreleme ve ICG lenfografi veya lenfosintigrafi ile lenfatik haritalama.",
   "follow":"Bası giysisi kullanımı, planlı kontroller ve gerektiğinde lenfödem fizyoterapisi.",
   "body":"Kol ve bacak lenfatik sistemi"},
 "keyfacts":[("Erken evre","LVA — en az invaziv seçenek"),("İleri evre","Lenf nodu transferi + azaltıcı"),
             ("Tanı","ICG lenfografi, lenfosintigrafi"),("Belirleyici","Evre ve geçen süre")],
 "authority":"Lenfödem mikrocerrahisi, plastik cerrahinin en ince teknik gerektiren alanıdır: 0,3–0,8 mm çapındaki lenf kanallarının mikroskop altında damarlara bağlanması. Doç. Dr. Acartürk, Pittsburgh Üniversitesi'nde Baş–Boyun Onarımları Direktörü olarak 300'ün üzerinde mikrocerrahi ameliyat gerçekleştirmiş; Avrupa Lenfatik Mikrocerrahi Grubu'nun çalışmalarına katılmakta ve Dünya Lenfödem Kongresi'nde bildiri sunmaktadır.",
 "creds":["Pittsburgh Üniversitesi Baş–Boyun Onarımları eski Direktörü — 300+ mikrocerrahi vaka",
          "Avrupa Lenfatik Mikrocerrahi Grubu çalışmalarına katılım",
          "Mikrocerrahide doku kaybı oranını %3'e düşürdü — dünya ortalaması %5"],
 "sections":[
  {"id":"nedir","tag":"Temel Bilgi","h2":"Lenfödem nedir, neden oluşur?","body":[
   "Lenf sistemi, dokular arasında biriken protein yüklü sıvıyı toplayıp dolaşıma geri kazandıran ince bir kanal ağıdır. Bu ağda tıkanıklık ya da hasar oluştuğunda sıvı dokuda birikir; ortaya çıkan kalıcı şişliğe <strong>lenfödem</strong> denir.",
   ("h3","Başlıca nedenler"),
   ("ul",["<strong>Sekonder (ikincil) lenfödem:</strong> Kanser cerrahisinde lenf nodlarının çıkarılması, radyoterapi, tekrarlayan enfeksiyonlar veya travma sonrası gelişir. Türkiye'de en sık görülen biçimdir; meme kanseri sonrası kol lenfödemi tipik örnektir.",
          "<strong>Primer (birincil) lenfödem:</strong> Lenfatik sistemin doğuştan yetersiz gelişmesine bağlıdır. Doğumda, ergenlikte veya erişkin dönemde ortaya çıkabilir."]),
   "Şişlik zamanla yalnızca bir görüntü sorunu olmaktan çıkar: dokuda yağlanma ve fibrozis (sertleşme) gelişir, cilt kalınlaşır, tekrarlayan selülit atakları başlar ve hareket kısıtlanır. <strong>Bu nedenle zamanlama, tedavi seçeneklerini doğrudan belirler.</strong>",
   ("note","Erken evrede lenfatik kanallar hâlâ işlev görürken yapılan mikrocerrahi girişimlerden alınan yanıt, doku sertleşmesi yerleştikten sonra elde edilenden belirgin şekilde daha iyidir. Bekleme, seçenekleri daraltır.")]},
  {"id":"fark","tag":"Ayırıcı Tanı","h2":"Lenfödem mi, lipödem mi?","body":[
   "İki durum sıkça karıştırılır; tedavileri ise farklıdır. Aşağıdaki tablo yönlendirici bir çerçeve sunar, ancak kesin ayrım yalnızca muayene ile yapılabilir.",
   ("table",["Bulgu","Lenfödem","Lipödem"],[
     ["Simetri","Genellikle asimetrik; bir taraf belirgin şekilde daha şiş","Tipik olarak simetrik; her iki taraf benzer"],
     ["Ayak tutulumu","Şişlik ayak sırtına ve parmaklara uzanır","Şişlik ayak bileğinde durur — kelepçe belirtisi; ayaklar korunur"],
     ["Cilt ve doku","Cilt gergin; bastırınca çukurlaşma (gode) olabilir","Doku yumuşak ve nodüler; dokunmakla ağrılı olabilir"],
     ["Ağrı","Ağırlık ve gerginlik hissi ön planda","Bası ile ağrı, kolay morarma belirgin"],
     ["Kilo ilişkisi","Diyet ve kilo kaybı şişliği düzeltmez","Kilo kaybına dirençli yağ birikimi"],
     ["Stemmer bulgusu","Genellikle pozitif","Genellikle negatif"],
     ["Başlangıç","Cerrahi, radyoterapi veya enfeksiyon sonrası","Sıklıkla ergenlik, gebelik veya menopoz dönemlerinde"]]),
   "İki tablo bir arada da bulunabilir. Uzun süreli, tedavi edilmemiş lipödem lenfatik yükü artırarak <strong>lipo-lenfödem</strong> adı verilen karma duruma yol açabilir. Ayrıntılar <a href=\"lipodem-cerrahisi.html\">lipödem cerrahisi sayfamızda</a>."]},
  {"id":"evre","tag":"Evreleme","h2":"Lenfödem evreleri","body":[
   "Uluslararası Lenfoloji Derneği (ISL) evrelemesi, hangi cerrahi seçeneğin uygun olduğunu belirleyen temel çerçevedir.",
   ("table",["Evre","Bulgular","Cerrahi yaklaşım"],[
     ["Evre 0","Lenfatik taşıma kapasitesi azalmıştır ancak gözle görülür şişlik yoktur. Görüntülemeyle saptanır.","LVA — önleyici ve en etkili dönem"],
     ["Evre 1","Şişlik gün içinde artar, uzuv yükseltilince kısmen geriler. Bastırınca çukurlaşma olur.","LVA"],
     ["Evre 2","Şişlik yükseltmeyle geçmez. Doku sertleşmeye başlar, enfeksiyon riski artar.","LVA ve/veya lenf nodu transferi"],
     ["Evre 3","Belirgin hacim artışı, kalınlaşmış cilt, tekrarlayan selülit. Elefantiyazis görülebilir.","Lenf nodu transferi + azaltıcı cerrahi"]]),
   ("note","<strong>Genel eğilim:</strong> Evre 0–2'de lenfatik kanallar korunduğu ölçüde LVA öne çıkar. Evre 2–3'te vaskülarize lenf nodu transferi ve azaltıcı cerrahiler tek başına ya da kombine planlanır. Nihai karar, görüntüleme bulgularıyla birlikte verilir.")]},
  {"id":"tani","tag":"Tanı","h2":"Tanı ve lenfatik haritalama","body":[
   "Cerrahi planlama, lenfatik sistemin gerçekte ne durumda olduğunu görmeden yapılamaz. Kullanılan başlıca yöntemler:",
   ("ul",["<strong>ICG lenfografi:</strong> Cilt altına verilen indosiyanin yeşili boyanın kızılötesi kamerayla izlenmesi. Çalışan lenf kanallarının gerçek zamanlı haritasını çıkarır; LVA kesilerinin yerini belirlemede kullanılır.",
          "<strong>Lenfosintigrafi:</strong> Radyoaktif işaretli maddeyle lenfatik akımın ve nod tutulumunun değerlendirilmesi. Evrelemede referans yöntemlerden biridir.",
          "<strong>MR lenfanjiyografi:</strong> Lenfatik kanalların ve sıvı dağılımının ayrıntılı anatomik haritası. İleri evrede ve karmaşık olgularda tercih edilir.",
          "<strong>Klinik değerlendirme:</strong> Çevre ölçümleri, Stemmer bulgusu, cilt kalitesi, enfeksiyon öyküsü ve önceki tedavi yanıtı."])]},
  {"id":"yontem","tag":"Cerrahi Seçenekler","h2":"Cerrahi yöntemler","body":[
   "Lenfödem cerrahisi iki ana felsefeye ayrılır: lenfatik akımı yeniden kuran <strong>fizyolojik</strong> yöntemler ve birikmiş dokuyu uzaklaştıran <strong>azaltıcı</strong> yöntemler. Birçok hastada ikisi aşamalı olarak birlikte kullanılır.",
   ("h3","Lenfatikovenöz anastomoz (LVA)"),
   "Tıkalı lenf kanalları, mikroskop altında yaklaşık 0,3–0,8 mm çapındaki komşu toplardamarlara bağlanır. Lenf sıvısı böylece venöz dolaşıma yönlendirilir. Genellikle birkaç santimetrelik küçük kesilerle uygulanır, erken evrede en az invaziv fizyolojik seçenektir ve çoğu hastada kısa yatış gerektirir.",
   ("h3","Vaskülarize lenf nodu transferi (VLNT)"),
   "Sağlıklı bir donör bölgeden damarlarıyla birlikte alınan lenf nodu paketi, etkilenen bölgeye aktarılır ve mikrocerrahi ile damar bağlantıları kurulur. İleri evre ve yaygın kanal hasarında tercih edilir; <a href=\"meme-rekonstruksiyonu.html\">meme rekonstrüksiyonu</a> ile eş zamanlı planlanabilir.",
   ("h3","Azaltıcı cerrahi"),
   "Lenfatik yapıları koruyan özel liposuction teknikleriyle biriken yağ ve fibrotik dokunun uzaklaştırılması. İleri evrede hacmi ve ağırlığı belirgin şekilde azaltır; sonrasında bası giysisi kullanımı süreklidir.",
   ("h3","Önleyici yaklaşım (LYMPHA)"),
   "Kanser cerrahisi sırasında lenf nodu diseksiyonuyla eş zamanlı yapılan lenfatikovenöz bağlantılar. Amaç, lenfödem daha ortaya çıkmadan riski azaltmaktır. Onkolojik cerrahi ekibiyle birlikte planlanır.",
   ("note","Hiçbir yöntem her hasta için doğru değildir. Aynı evredeki iki hastada bile lenfatik haritalama sonuçları farklı bir plan gerektirebilir. Yöntem seçimi; evre, görüntüleme, önceki tedaviler, cilt kalitesi ve beklentilerin birlikte değerlendirilmesiyle yapılır.")]},
  {"id":"surec","tag":"Süreç","h2":"Ameliyat ve iyileşme süreci","body":[
   ("steps",[
    ("1. ADIM — ÖN GÖRÜŞME","WhatsApp veya form üzerinden ilk temas. Süre, önceki cerrahiler, radyoterapi öyküsü ve varsa görüntüleriniz üzerinden ilk yönlendirme."),
    ("2. ADIM — MUAYENE VE GÖRÜNTÜLEME","Çevre ölçümleri, klinik değerlendirme ve gerekli görüldüğünde ICG lenfografi veya lenfosintigrafi ile lenfatik haritalama."),
    ("3. ADIM — PLANLAMA GÖRÜŞMESİ","Uygulanabilir yöntemler, beklenen kazanım, riskler ve seans sayısı açıkça konuşulur. Karar aceleye getirilmez."),
    ("4. ADIM — AMELİYAT","Tam donanımlı hastane koşullarında. LVA çoğunlukla kısa yatış gerektirir; lenf nodu transferi ve azaltıcı cerrahilerde yatış daha uzundur."),
    ("5. ADIM — İLK 6 HAFTA","Bası giysisi kullanımı, yara bakımı, kademeli hareket. Ödemde ilk değişiklikler bu dönemde fark edilmeye başlar."),
    ("6. ADIM — 3–12 AY TAKİP","Planlı kontroller ve çevre ölçümleriyle yanıtın izlenmesi. Lenfödem fizyoterapisi yoğunluğu kademeli olarak ayarlanır.")]),
   ("note","<strong>Şehir dışı ve yurt dışı hastalar için:</strong> Ön değerlendirme çevrim içi görüşme ve gönderilen görüntülerle yapılır. Ameliyat ve kontrol randevuları tek bir seyahat programında toplanacak şekilde planlanır; sonraki takipler çevrim içi sürdürülür.")]}],
 "faqs":[
  ("Lenfödem ameliyatı kimlere uygundur?","Cerrahi adaylık; evreye, lenfatik sistemin görüntülemedeki durumuna, şişliğin süresine, cilt kalitesine ve genel sağlık durumuna göre belirlenir. Erken evrede (ISL 0–2) LVA öne çıkarken, ileri evrede lenf nodu transferi ve azaltıcı yöntemler gündeme gelir. Aktif kanser tedavisi süreci, kontrolsüz enfeksiyon ve ileri damar hastalığı gibi durumlar zamanlamayı değiştirebilir."),
  ("Ameliyat sonrası bası çorabı kullanmaya devam edecek miyim?","Çoğu hastada ilk dönemde bası giysisi kullanımı sürer. Zaman içinde kullanım süresi ve basınç düzeyi azaltılabilir; tamamen bırakılıp bırakılamayacağı evreye, yönteme ve alınan yanıta göre değişir. Erken evrede yapılan LVA sonrası bağımlılığın azaldığı bildirilmektedir."),
  ("İyileşme süreci ne kadar sürer?","LVA sonrası çoğu hasta birkaç gün içinde günlük yaşamına döner. Lenf nodu transferi ve azaltıcı cerrahilerde iyileşme daha uzundur. Ödemdeki azalma ani değil, haftalar ve aylar içinde kademeli olarak görülür; bu nedenle takip ölçümleri önemlidir."),
  ("Meme kanseri sonrası kolumdaki şişlik için ne zaman başvurmalıyım?","Kol çevresinde artış, ağırlık hissi, yüzük veya saatin sıkmaya başlaması gibi bulgular fark ettiğinizde beklemeden değerlendirilmelisiniz. Erken dönemde yapılan mikrocerrahi girişimler, doku sertleşmesi yerleşmeden çok daha etkilidir."),
  ("Ameliyat olmadan lenfödem geçer mi?","Kompleks boşaltıcı fizyoterapi, bandaj ve bası giysileri şişliği kontrol altında tutmaya yardımcı olur ve tedavinin vazgeçilmez parçasıdır. Ancak bunlar lenfatik akımdaki tıkanıklığı ortadan kaldırmaz. Cerrahi, altta yatan drenaj sorununu hedefleyen tamamlayıcı bir basamaktır."),
  ("Selülit (enfeksiyon) ataklarım azalır mı?","Lenf sıvısının dokuda birikmesi enfeksiyon riskini artırır. Drenajın iyileştirilmesiyle birlikte tekrarlayan selülit ataklarının seyrekleştiği bildirilmektedir. Ancak bu, kişiye ve evreye göre değişen bir sonuçtur ve garanti edilemez."),
  ("İki bacağım da etkilenmiş; tek seansta mı yapılır?","Etkilenen alanın genişliğine ve planlanan yönteme göre değişir. Geniş alanlar genellikle güvenlik ve iyileşme kalitesi açısından birden fazla seansa bölünür."),
  ("Lenfödem ile lenfoma aynı şey mi?","Hayır. Lenfödem, lenf sıvısının dokuda birikmesiyle oluşan bir dolaşım sorunudur. Lenfoma ise lenf sisteminin kanseridir ve hematoloji–onkoloji tarafından tedavi edilir. İsim benzerliği sık karışıklığa yol açar.")],
 "related":["lenfodem-belirtileri","lenfodem-evreleri","lenfodem-neden-olur","bacakta-lenfodem","kolda-lenfodem","lenfodem-hangi-doktor","lipodem"],
 "ctah":"Lenfödem değerlendirmesi için ilk adım",
 "ctap":"Ne kadar süredir devam ettiğini, önceki tedavilerinizi, radyoterapi öykünüzü ve varsa bacak veya kol fotoğraflarınızı gönderin. İlk yönlendirme ve randevu planlaması için size dönüş yapılır."},
]
