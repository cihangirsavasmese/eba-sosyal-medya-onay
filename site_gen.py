# Yeni EBA sosyal medya onay sayfası (Haberimiz Olsun onay sayfası düzeninde, videolar izlenebilir).
# Kullanım: python site_gen.py <site_klasoru> [APPS_SCRIPT_URL]
import sys, html, os, glob
SITE = sys.argv[1]
URL = sys.argv[2] if len(sys.argv) > 2 else "BURAYA_APPS_SCRIPT_URL"
E = html.escape

PILOTS = [
 dict(no="P1a", ad="EBA'DA BU DA VAR · ŞÜHEDA 1915", tur="video", v="p1a", sure="18 sn", hedef="Herkes",
      kunye="2. tur · Reels 1080×1920 · telefon mock-up'ı, özgün müzik + efekt",
      akis=["Açılış: büyük “EBA'da bu da var!” (EBA logosu) + göz ikonu", "Şüheda 1915 sahneleri · “Çanakkale'nin hikâyesi sahnede”", "Telefonda izleme: Kütüphane › Tiyatro", "Kapanış: “Şüheda 1915 EBA Kütüphane'de” · EBA + göz · “Bir Adım Önde”"],
      metin="EBA'da bu da var! 🎭\nŞüheda 1915 tiyatro oyunu EBA Kütüphane'de. Çanakkale'nin hikâyesini sahneden izleyin.\n📍 EBA › Kütüphane › Tiyatro · eba.gov.tr\n#BirAdımÖnde #YeniEBA #EBAdaBuDaVar",
      kontrol="Revize: her tiyatro ayrı bölüm. Üçüncü bölüm “En Uzun Gece” için EBA Kütüphane'den çekim gerekiyor."),
 dict(no="P1b", ad="EBA'DA BU DA VAR · CUMHURİYETE DOĞRU", tur="video", v="p1b", sure="18 sn", hedef="Herkes",
      kunye="2. tur · Reels 1080×1920 · telefon mock-up'ı, özgün müzik + efekt",
      akis=["Açılış: büyük “EBA'da bu da var!” + göz ikonu", "Cumhuriyete Doğru sahneleri · “Cumhuriyet'in 100. yılına özel destansı oyun”", "Telefonda izleme", "Kapanış: “Cumhuriyete Doğru EBA Kütüphane'de”"],
      metin="EBA'da bu da var! 🇹🇷\nCumhuriyete Doğru tiyatro oyunu EBA Kütüphane'de. Cumhuriyet'in 100. yılı için hazırlanan destansı oyunu izleyin.\n📍 EBA › Kütüphane › Tiyatro · eba.gov.tr\n#BirAdımÖnde #YeniEBA #EBAdaBuDaVar"),
 dict(no="P2b", ad="YAPAY ZEKÂ'YA SORDUM · AY", tur="video", v="p2b", sure="20 sn", hedef="Öğrenci",
      kunye="2. tur · Reels 1080×1920 · telefon mock-up'ı, özgün müzik + efekt",
      akis=["Açılış: EBA + göz + YAPAY ZEKÂ'YA SORDUM · “Ay neden her gece farklı görünüyor?”", "1 Sorunu yaz → 2 Gönder → 3 Sana göre anlatsın → 4 Kısa özet", "Göz ikonu cevabı izliyor", "Kapanış: “Takıldığın yerde EBA Yapay Zekâ” (yorum çağrısı kaldırıldı)"],
      metin="Ay neden her gece farklı görünüyor? 🌙\nEBA Yapay Zekâ'ya sorduk; kısa ve anlaşılır bir özetle cevapladı.\n📍 eba.gov.tr\n#BirAdımÖnde #YeniEBA #YapayZekayaSordum",
      kontrol="Cevaptaki “Her hafta bir kez bu şekiller değişir” cümlesi yaklaşık bir anlatım; yayından önce bir fen öğretmeninin okuması önerilir."),
 dict(no="P3b", ad="EBA · HAFTANIN OYUNU · HÜCRE KÖY", tur="video", v="p3b", sure="16,5 sn", hedef="Öğrenci",
      kunye="2. tur · Reels 1080×1920 · yatay telefon mock-up'ı, özgün müzik + efekt",
      akis=["Açılış: büyük EBA + göz + HAFTANIN OYUNU başlığı · “Hücre Köy”", "Telefon yan döner → BAŞLA → oyun içi", "Kapanış: “Her hafta yeni bir oyun”"],
      metin="Haftanın oyunu: Hücre Köy 🧬\nHücreni yönet, görevleri tamamla, gün gün ilerle.\n📍 EBA › Oyun ve Uygulamalar · eba.gov.tr\n#BirAdımÖnde #YeniEBA #HaftanınOyunu",
      kontrol="Revize: oyun arayüzünden daha çok görüntü istendi; bunun için oyunun içinden yeni çekim gerekiyor."),
 dict(no="P4b", ad="60 SANİYEDE KONU · BİLEŞKE KUVVET", tur="video", v="p4b", sure="19,5 sn", hedef="Öğrenci",
      kunye="2. tur · Reels 1080×1920 · tablet mock-up'ı, özgün müzik + efekt",
      akis=["Açılış: EBA + göz + 60 SANİYEDE KONU · “Bileşke Kuvvet adım adım”", "Konunu seç → Hazır mıyız? → Öğrenelim → Değerlendirelim", "Kapanış: “Her konu adım adım”"],
      metin="Bileşke Kuvvet adım adım ⚡\nHazır mıyız? ile ön bilgini yokla, Öğrenelim ile etkileşimli içeriklerle öğren, Değerlendirelim ile kendini test et.\n📍 EBA › Dersler › Fen Bilimleri · eba.gov.tr\n#BirAdımÖnde #YeniEBA #60SaniyedeKonu",
      kontrol="Revize: genel politika sekmelerin tamamı (Hazır mıyız, Öğrenelim, Keşfedelim/Uygulayalım, Oynayalım, Değerlendirelim). Bu derste üç sekme dolu; tümü dolu bir ders seçilirse yeniden çekilecek."),
 dict(no="P5b", ad="KALDIĞIN YERDEN", tur="kare", k="r2_05_KaldiginYerden_*.jpg", sure="5 kare", hedef="Öğrenci",
      kunye="2. tur · Kaydırmalı gönderi 1080×1350 · 1. turda onaylandı, kurumsal kimlik uygulandı",
      akis=["Kapak: “Yarım kalan bir kitabın mı var?”", "Ana sayfada tek dokunuş", "Seni tam orada bekliyor", "Kapanış: EBA + göz · “Bir Adım Önde”"],
      metin="Yarım kalan bir kitabın mı var? 📚 Merak etme, EBA hatırlıyor.\nAna sayfadaki “Kaldığın Yerden Devam Et” ile tek dokunuşla devam et.\n#BirAdımÖnde #YeniEBA"),
 dict(no="P7b", ad="GÜVENLİ KULLANIM", tur="kare", k="r2_07_GuvenliEBA_*.jpg", sure="5 kare", hedef="Herkes",
      kunye="2. tur · Kaydırmalı gönderi 1080×1350 · kurumsal kimlik uygulandı",
      akis=["“EBA'yı güvenle kullanmanın 4 kuralı”", "Doğru adres · Şifre · Kişisel bilgi · Resmî hesaplar"],
      metin="EBA'yı güvenle kullanmanın 4 kuralı 🔒\n✅ Adres çubuğunda eba.gov.tr olsun\n✅ Şifreni kimseyle paylaşma\n✅ Kişisel bilgilerini yazma\n✅ Duyuruları resmî hesaplardan takip et\n#BirAdımÖnde #YeniEBA"),
]
REELS = [
 dict(no="R01", ad="ARTIK DERS ÇALIŞMAK SANA GÖRE", v="r01", sure="22 sn", hedef="Öğrenci, veli", muzik="parlak pop",
      metin="Ders çalışmak artık sana göre! 🎒\nRenkli ana sayfan, kaldığın yerden devam eden derslerin, dijital kitapların, kütüphane ve eğitsel oyunlar… Hepsi Yeni EBA'da bir arada.\n👉 eba.gov.tr\n#YeniEBA #BirAdımÖnde #EBA",
      kontrol="Revize (her kademenin ayrı arayüzü) beklemede: ortaokul, lise ve okul öncesi öğrenci test hesapları şu an yok. Hesaplar açılınca bu kademelerin ekranları çekilip videonun başına eklenecek. Şimdilik yalnızca 1. sınıf öğrenci arayüzü var."),
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
