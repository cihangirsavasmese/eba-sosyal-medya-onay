# Yeni EBA sosyal medya onay sayfası

18 içerik (7 seri pilotu + 11 tanıtım Reels'i), videolar sayfada izlenebilir. Haberimiz Olsun onay sayfası düzeninde.

- `index.html` · `video/` (720p web sürümleri) · `kapak/` · `kare/` (kaydırmalı gönderiler) · `baykus.png`
- Yeniden üretmek: `python site_gen.py . [APPS_SCRIPT_URL]` (`site_tpl.html` şablonu)
- Ortak yanıt kaydı (Kaydet): `apps-script/Code.gs` → script.google.com'da web uygulaması olarak dağıt → URL'yi `site_gen.py` ile yaz.
  Yanıt tablosu Drive'da `YGTK/EBA Tanıtım/EBA Sosyal Medya İçerikleri/Onay_Yanitlari/` altına düşer.
- URL bağlanana kadar seçimler kişinin cihazında saklanır; "WhatsApp ile gönder" ve "Kopyala" çalışır.
