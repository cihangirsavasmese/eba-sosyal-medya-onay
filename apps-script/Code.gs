// Yeni EBA sosyal medya onay sayfası — yanıt kaydı (Google Apps Script web uygulaması).
// Kurulum: script.google.com → Yeni proje → bu kodu yapıştır → kur fonksiyonunu bir kez çalıştır (izinler)
//   → Dağıt → Yeni dağıtım → Web uygulaması · Yürüten: Ben · Erişim: Herkes → Dağıt
//   → Web uygulaması URL'sini index.html içindeki ONAY_SCRIPT_URL'ye yaz (python site_gen.py <klasör> <URL>).
// E-tablo Drive'da KLASOR_YOLU altına oluşturulur (eksik klasörler açılır); kök klasöre düşmez.
const TABLO_ADI = 'Yeni EBA Sosyal Medya - Onay Yanıtları';
const KLASOR_YOLU = ['Claude Code - Projects', 'YGTK', 'EBA Tanıtım', 'EBA Sosyal Medya İçerikleri', 'Onay_Yanitlari'];
function klasor() {
  let k = DriveApp.getRootFolder();
  KLASOR_YOLU.forEach(ad => { const it = k.getFoldersByName(ad); k = it.hasNext() ? it.next() : k.createFolder(ad); });
  return k;
}
function tablo() {
  const p = PropertiesService.getScriptProperties();
  let id = p.getProperty('tabloId'), ss = null;
  try { ss = id ? SpreadsheetApp.openById(id) : null; } catch (e) { ss = null; }
  if (!ss) {
    ss = SpreadsheetApp.create(TABLO_ADI);
    DriveApp.getFileById(ss.getId()).moveTo(klasor());
    p.setProperty('tabloId', ss.getId());
    ss.getActiveSheet().appendRow(['zaman', 'no', 'ad', 'karar', 'not']);
  }
  return ss.getActiveSheet();
}
function doPost(e) {
  const veri = JSON.parse(e.postData.contents);
  const s = tablo(), zaman = new Date().toISOString();
  (veri.kayitlar || []).forEach(k => s.appendRow([zaman, String(k.no), String(k.ad || '').slice(0, 80), String(k.karar || ''), String(k.not || '').slice(0, 2000)]));
  return ContentService.createTextOutput(JSON.stringify({tamam: true})).setMimeType(ContentService.MimeType.JSON);
}
function doGet() {
  const v = tablo().getDataRange().getValues().slice(1);
  const satirlar = v.map(r => ({zaman: r[0] instanceof Date ? r[0].toISOString() : String(r[0]), no: String(r[1]), ad: String(r[2]), karar: String(r[3]), not: String(r[4])}));
  return ContentService.createTextOutput(JSON.stringify({satirlar})).setMimeType(ContentService.MimeType.JSON);
}
function kur() { tablo(); }
