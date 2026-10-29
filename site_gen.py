# Yeni EBA sosyal medya onay sayfası (Haberimiz Olsun onay sayfası düzeninde, videolar izlenebilir).
# Kullanım: python site_gen.py <site_klasoru> [APPS_SCRIPT_URL]
import sys, html, os, glob
SITE = sys.argv[1]
URL = sys.argv[2] if len(sys.argv) > 2 else "BURAYA_APPS_SCRIPT_URL"
E = html.escape

PILOTS = [
 dict(no="P1", ad="EBA'DA BU DA VAR · TİYATRO", tur="video", v="p1", sure="19,5 sn", hedef="Herkes",
      kunye="Seri pilotu · Reels 1080×1920 · telefon mock-up'ı, özgün müzik + efekt",
      akis=["“Hey Kâşif!” + “EBA'da tiyatro da var!”", "Şüheda 1915 sahneleri → Cumhuriyete Doğru", "Telefonda izleme: Kütüphane › Tiyatro", "Kapanış: “Perde EBA'da açılıyor!” #BirAdımÖnde"],
      metin="Hey Kâşif! 🎭 EBA'da tiyatro da var!\nŞüheda 1915 ile Çanakkale'nin hikâyesini, Cumhuriyete Doğru ile 100. yılın coşkusunu sahneden izle.\n📍 EBA › Kütüphane › Tiyatro · eba.gov.tr\n#BirAdımÖnde #YeniEBA #EBAdaBuDaVar"),
 dict(no="P2", ad="YAPAY ZEKÂ'YA SORDUM · AY", tur="video", v="p2", sure="20 sn", hedef="Öğrenci",
      kunye="Seri pilotu · Reels 1080×1920 · telefon mock-up'ı, özgün müzik + efekt",
      akis=["Soru: “Ay neden her gece farklı görünüyor?”", "1 Sorunu yaz → 2 Gönder → 3 Sana göre anlatsın", "4 Kısa özet: Yeni ay, Hilal, İlk dördün, Dolunay vurgulanır", "Kapanış: “Sen ne sorardın? Yorumlara yaz!”"],
      metin="Hey Kâşif! 🌙 Ay neden her gece farklı görünüyor?\nEBA Yapay Zekâ'ya sorduk, kısa ve anlaşılır cevapladı. Sıra sende: Sen ne sorardın? Yorumlara yaz, bir sonraki bölümde soralım!\n#BirAdımÖnde #YeniEBA #YapayZekayaSordum",
      kontrol="Cevaptaki “Her hafta bir kez bu şekiller değişir” cümlesi yaklaşık bir anlatım (evreler ~7 günde bir değişir); bir fen öğretmeninin okuması önerilir. Öğrenci adı baş harfler hariç yıldızla gizlendi."),
 dict(no="P3", ad="HAFTANIN OYUNU · HÜCRE KÖY", tur="video", v="p3", sure="16,5 sn", hedef="Öğrenci",
      kunye="Seri pilotu · Reels 1080×1920 · yatay telefon mock-up'ı, özgün müzik + efekt",
      akis=["“Bu haftanın oyunu: Hücre Köy”", "Telefon yan döner → BAŞLA'ya dokunuş → oyun içi", "Hücreni yönet · Görevleri sırayla tamamla · Gün gün ilerle", "Kapanış: “Oyna, keşfet, öğren!”"],
      metin="Hey Kâşif! 🧬 Bu haftanın oyunu: Hücre Köy!\nHücreni yönet, görevleri tamamla, gün gün ilerle. Bilimi oynayarak keşfet.\n📍 EBA › Oyun ve Uygulamalar · eba.gov.tr\n#BirAdımÖnde #YeniEBA #HaftanınOyunu"),
 dict(no="P4", ad="60 SANİYEDE KONU · BİLEŞKE KUVVET", tur="video", v="p4", sure="19,5 sn", hedef="Öğrenci",
      kunye="Seri pilotu · Reels 1080×1920 · tablet mock-up'ı, özgün müzik + efekt",
      akis=["“Bileşke Kuvvet 3 adımda!” · 6. Sınıf Fen Bilimleri", "Konunu seç → 1 Hazır mıyız? → 2 Öğrenelim → 3 Değerlendirelim", "Kapanış: “Her konu 3 adımda!”"],
      metin="Hey Kâşif! ⚡ Bileşke Kuvvet'i 3 adımda öğren:\n1️⃣ Hazır mıyız? ile ön bilgini yokla\n2️⃣ Öğrenelim ile etkileşimli içerik ve videoları izle\n3️⃣ Değerlendirelim ile kendini test et\n📍 EBA › Dersler › Fen Bilimleri · eba.gov.tr\n#BirAdımÖnde #YeniEBA #60SaniyedeKonu",
      kontrol="Ders ekranları öğretmen hesabından alındı (öğretmene özel paneller kırpıldı); istenirse öğrenci hesabından yeniden çekilir."),
 dict(no="P5", ad="KALDIĞIN YERDEN", tur="kare", k="05_KaldiginYerden_*.jpg", sure="5 kare", hedef="Öğrenci",
      kunye="Seri pilotu · Kaydırmalı gönderi 1080×1350",
      akis=["Kapak: “Yarım kalan bir kitabın mı var?”", "Ana sayfada tek dokunuş (Kaldığın Yerden Devam Et vurgulu)", "Seni tam orada bekliyor: Mars Öyküleri · Ara verildi", "Hepsi kaldığın yerden · Kapanış"],
      metin="Hey Kâşif! 📚 Yarım kalan bir kitabın mı var? Merak etme, EBA hatırlıyor.\nAna sayfadaki “Kaldığın Yerden Devam Et” ile tek dokunuşla devam et.\n#BirAdımÖnde #YeniEBA"),
 dict(no="P6", ad="SEN DE ANLAT", tur="kare", k="06_SenDeAnlat_*.jpg", sure="4 kare", hedef="Öğrenci",
      kunye="Seri pilotu · Kaydırmalı gönderi 1080×1350 · etkileşim",
      akis=["Kapak: “Yeni EBA'da en çok neyi sevdin?”", "A Yapay Zekâ · B Tiyatro · C Oyunlar · D Kaldığın Yerden", "“Harfini yorumlara yaz, nedenini de anlat!” · Kapanış"],
      metin="Hey Kâşif! 💬 Yeni EBA'da en çok neyi sevdin?\nA) Yapay Zekâ B) Tiyatro C) Oyunlar D) Kaldığın Yerden\nHarfini yorumlara yaz, nedenini de anlat!\n#BirAdımÖnde #YeniEBA #SenDeAnlat",
      kontrol="Gerçek öğrenci alıntısı kullanılmadı; yorumlardan alıntı yapılacaksa veli onayı gerekir."),
 dict(no="P7", ad="GÜVENLİ EBA · DUYURU / DOĞRULAMA", tur="kare", k="07_GuvenliEBA_*.jpg", sure="5 kare", hedef="Herkes",
      kunye="Seri pilotu · Kaydırmalı gönderi 1080×1350",
      akis=["“EBA'yı güvenle kullanmanın 4 kuralı”", "1 Doğru adres: eba.gov.tr · 2 Şifren sende kalsın", "3 Kişisel bilgilerini yazma (Yapay Zekâ uyarısı)", "4 Duyuruları resmî hesaplardan takip et, paylaşmadan önce doğrula"],
      metin="Hey Kâşif! 🔒 EBA'yı güvenle kullanmanın 4 kuralı:\n✅ Adres çubuğunda eba.gov.tr olsun\n✅ Şifreni kimseyle paylaşma\n✅ Kişisel bilgilerini yazma\n✅ Duyuruları MEB ve YEĞİTEK'in resmî hesaplarından takip et\n#BirAdımÖnde #YeniEBA #GüvenliEBA"),
]
REELS = [
 dict(no="R01", ad="ARTIK DERS ÇALIŞMAK SANA GÖRE", v="r01", sure="22 sn", hedef="Öğrenci, veli", muzik="parlak pop",
      metin="Ders çalışmak artık sana göre! 🎒\nRenkli ana sayfan, kaldığın yerden devam eden derslerin, dijital kitapların, kütüphane ve eğitsel oyunlar… Hepsi Yeni EBA'da bir arada.\n👉 eba.gov.tr\n#YeniEBA #BirAdımÖnde #EBA",
      kontrol="Video yalnızca 1. sınıf arayüzünü gösteriyor; “her kademe” ifadesi kullanılmadı."),
 dict(no="R02", ad="DERS ÇALIŞIRKEN YALNIZ DEĞİLSİN", v="r02", sure="24 sn", hedef="Öğrenci, veli", muzik="synth arp",
      metin="Bir konuda mı takıldın? EBA Yapay Zekâ'ya sor! ✨\nDerslerine odaklı, yaşına uygun ve adım adım açıklamalar Yeni EBA'da seni bekliyor.\nÖrnek: “1. sınıf matematikte toplamayı elma örneğiyle anlatır mısın?” 🍎\n#YeniEBA #EBAYapayZekâ #BirAdımÖnde",
      kontrol="Bu cevapta kaynakça çıkmadığı için “kaynak gösterir” denmedi."),
 dict(no="R03", ad="ÖĞRENCİNİZ EBA'DA NE YAPTI?", v="r03", sure="19 sn", hedef="Veli", muzik="piyano",
      metin="Çocuğunuzun öğrenme yolculuğuna eşlik etmek artık daha kolay. 👨‍👩‍👧\nYeni EBA veli ekranında tamamlanan içerikleri, sınavları, çalışmaları ve ders ilerlemesini tek bakışta görün.\n👉 eba.gov.tr · Veli girişi\n#YeniEBA #EBAVeli #BirAdımÖnde",
      kontrol="Videoda test veli ve öğrenci adları (Rukiye Yıldız, Doğa Yıldız) görünüyor."),
 dict(no="R04", ad="KİM NEREDE ZORLANIYOR?", v="r04", sure="27 sn", hedef="Öğretmen", muzik="lo-fi",
      metin="Hangi öğrenciniz konuyu kavradı, hangisi hangi öğrenme çıktısında zorlanıyor? 📊\nYeni EBA'nın performans haritası ve çalışma sonuçlarıyla sınıfınızı veriye dayalı olarak izleyin.\n#YeniEBA #EBAÖğretmen #BirAdımÖnde"),
 dict(no="R05", ad="DERS PLANI DAKİKALAR İÇİNDE", v="r05", sure="33 sn", hedef="Öğretmen", muzik="piyano",
      metin="Öğrenme çıktısını seçin, içeriği ekleyin; Yeni EBA'nın yapay zekâ destekli ders planı aracı kaynakları adım adım hazırlasın. ⚡\nEtkileşim, keşif, açıklama, detaylandırma ve değerlendirme tek akışta.\n#YeniEBA #EBAÖğretmen #YapayZekâ",
      kontrol="“Dakikalar içinde” bir pazarlama ifadesi; istenirse “Ders planı artık çok daha kolay” kullanılabilir."),
 dict(no="R06", ad="OYNARKEN ÖĞREN", v="r06", sure="21 sn", hedef="Öğrenci", muzik="marimba",
      metin="Oynarken öğrenmeye hazır mısın? 🎮\nHedef X, Laboratuvar Kâşifi, Yörünge Gezgini, Tarih Dedektifleri ve bu haftanın oyunu Hücre Köy… EBA'nın eğitsel oyunları seni bekliyor!\n👉 eba.gov.tr/eba-karsilama-oyun-ve-uygulama\n#YeniEBA #OynarkenÖğren #EBA",
      kontrol="Oyunların ders etiketleri ve açıklamaları kapak görsellerinden çıkarıldı, oynanarak doğrulanmadı. Menüdeki “Oyun ve Uygulamalar” bağlantısı doğrudan adresle 404 veriyor; paylaşımda yukarıdaki adres kullanılmalı."),
 dict(no="R07a", ad="TARİH SAHNEDE CAN BULUYOR", v="r07a", sure="15 sn", hedef="Herkes", muzik="sinematik",
      metin="Tarih sahnede can buluyor! 🎭\nŞüheda 1915 ve Cumhuriyete Doğru tiyatro oyunları EBA Kütüphane'de. Sınıfınızla ya da ailenizle birlikte izleyin.\n#YeniEBA #EBAKütüphane #Şüheda1915 #CumhuriyeteDoğru"),
 dict(no="R07b", ad="BİLİM MERKEZLERİ CEBİNDE", v="r07b", sure="15 sn", hedef="Öğrenci, öğretmen", muzik="synth arp",
      metin="Konya'dan Samsun'a, Türkiye'nin bilim merkezleri EBA Kütüphane'de! 🔭\n13 bilim merkezini videolarla keşfet, sınıfınla birlikte gez.\n#YeniEBA #EBAKütüphane #BilimMerkezleri"),
 dict(no="R07c", ad="OKULDAN ÇIKMADAN MÜZE GEZ", v="r07c", sure="14 sn", hedef="Herkes", muzik="sinematik",
      metin="Okuldan çıkmadan müze gezmeye ne dersiniz? 🏛️\nEfes'ten Seddülbahir'e, Karahantepe'den Anadolu Medeniyetleri Müzesi'ne… EBA Kütüphane'deki sanal müzelerle tarihi yerinde keşfedin.\n#YeniEBA #EBAKütüphane #SanalMüze",
      kontrol="Müze bağlantıları dış sitelere gidiyor."),
 dict(no="R07d", ad="OKUMA ZAMANI BAŞLADI", v="r07d", sure="16 sn", hedef="Öğrenci, veli", muzik="lo-fi",
      metin="Okuma zamanı başladı! 📚\nMEB Yayınları'nın çocuk kitaplarından Tolstoy, Goethe ve Tagore'a uzanan dünya klasikleri EBA Kütüphane'de; sayfa sayfa çevirerek okuyun.\n#YeniEBA #EBAKütüphane #OkumaZamanı"),
 dict(no="R07e", ad="BİLİMİN ÖNCÜLERİ EBA'DA", v="r07e", sure="12 sn", hedef="Öğrenci, öğretmen", muzik="marimba",
      metin="İbn Sina'dan Hârezmî'ye, Bîrûnî'den Cezerî'ye… 🌟\nBilim tarihinin ustalarını EBA Kütüphane'deki videolarla tanıyın.\n#YeniEBA #EBAKütüphane #BilimTarihi"),
]
for r in REELS:
    r.update(tur="video", kunye=f"Tanıtım Reels'i · 1080×1920 · 3B kart, özgün müzik ({r['muzik']}) + efekt", akis=None)

def medya(it):
    if it["tur"] == "video":
        return (f'<div class="medya"><video controls playsinline preload="none" poster="kapak/{it["v"]}.jpg">'
                f'<source src="video/{it["v"]}.mp4" type="video/mp4"></video></div>')
    kareler = sorted(os.path.basename(p) for p in glob.glob(f"{SITE}/kare/{it['k']}"))
    imgs = "".join(f'<img src="kare/{k}" alt="{E(it["ad"])} — {i + 1}. kare" loading="lazy">' for i, k in enumerate(kareler))
    return f'<div class="medya kare"><div class="serit">{imgs}</div><p class="ipucu">Kareleri yana kaydırın · {len(kareler)} kare</p></div>'

def bolum(it):
    no = it["no"]
    akis = "".join(f"<li>{E(a)}</li>" for a in (it.get("akis") or []))
    kontrol = f'<p class="kontrol"><b>Kontrol</b>{E(it["kontrol"])}</p>' if it.get("kontrol") else ""
    return f'''<section class="icerik" id="{no}" data-no="{no}" data-ad="{E(it['ad'])}">
  <div class="bas"><span class="no">{E(no)}</span><div><h2>{E(it['ad'])}</h2><p class="kunye">{E(it['kunye'])} · {E(it['sure'])} · Hedef: {E(it['hedef'])}</p></div></div>
  <div class="ikili">{medya(it)}
    <div class="bilgi">
      {f"<ol>{akis}</ol>" if akis else ""}
      <div class="ses"><b>Gönderi metni (Instagram)</b>{E(it['metin'])}</div>
      {kontrol}
      <div class="karar">
        <label class="sec onay"><input type="radio" name="k{no}" value="onay"> Onaylıyorum</label>
        <label class="sec duz"><input type="radio" name="k{no}" value="duzeltme"> Düzeltme istiyorum</label>
      </div>
      <textarea placeholder="Not (isteğe bağlı)"></textarea>
      <div class="yanitlar"></div>
    </div>
  </div>
</section>'''

tpl = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "site_tpl.html"), encoding="utf-8").read()
out = (tpl.replace("{{PILOTLAR}}", "\n".join(bolum(i) for i in PILOTS))
          .replace("{{REELS}}", "\n".join(bolum(i) for i in REELS))
          .replace("{{URL}}", URL))
open(f"{SITE}/index.html", "w", encoding="utf-8").write(out)
print("ok", len(PILOTS) + len(REELS), "içerik")
