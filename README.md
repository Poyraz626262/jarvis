# JARVIS Benzeri Bilgisayar Yapay Zekâ Tasarımı

Bu repo, "şunu aç, şunu yaz, bunun içini doldur" gibi bilgisayar üzerinde **otonom görev yapan** bir JARVIS benzeri asistan için pratik bir başlangıç tasarımı içerir.

## 1) Hedef

Kullanıcı doğal dilde komut verir:
- "Chrome'u aç, docs'a gir, yeni dosya oluştur, toplantı notunu yaz."
- "Excel'i aç, satış.csv'yi al, toplamları çıkar."
- "Mail'e gir, Ahmet'e durum güncellemesi gönder."

Asistan;
1. Komutu anlar,
2. Plan çıkarır,
3. Bilgisayarı kontrol eder,
4. Sonucu doğrular,
5. Gerekirse kullanıcıdan onay ister.

## 2) Çekirdek Mimari

### Ajan Katmanları

1. **Niyet Çözümleyici (NLU/LLM katmanı)**
   - Komutu hedef + adımlar + kısıtlar şeklinde parçalar.
2. **Planlayıcı**
   - Görevi adım adım eylem planına dönüştürür.
3. **Araç Yürütücü (Tool Runner)**
   - Uygulama açma, metin yazma, tıklama, dosya işlemleri, web otomasyonu.
4. **Doğrulama / Gözlemleyici**
   - Ekran görüntüsü + OCR + durum kontrolü ile yapılan işi doğrular.
5. **Güvenlik/Kural Motoru**
   - Tehlikeli eylemleri engeller veya onay ister.
6. **Hafıza (Memory)**
   - Kullanıcı tercihleri, geçmiş görevler, sık kullanılan akışlar.

### Araçlar (Önerilen)

- **UI otomasyonu:** `pyautogui`, `playwright`, `uiautomation` (Windows), `xdotool` (Linux).
- **Sesli etkileşim:** `faster-whisper`, `piper`/`coqui-tts`.
- **LLM:** Yerel (Ollama) veya API tabanlı model.
- **OCR:** `tesseract`, `easyocr`.
- **Workflow:** Python + event loop + görev kuyruğu.

## 3) Güvenli Otonomi Tasarımı

Tam otonomi güçlüdür ama risklidir. Bu yüzden:

- **Risk seviyeleri:**
  - Düşük: uygulama açma, metin yazma.
  - Orta: dosya taşıma, dış sisteme veri gönderme.
  - Yüksek: para transferi, hesap silme, kritik sistem ayarı.
- **Politika:**
  - Düşük: otomatik.
  - Orta: hızlı onay.
  - Yüksek: çok adımlı onay + log.
- **Zorunlu denetim izi:** her adım loglanır.

## 4) MVP (İlk Çalışan Sürüm)

İlk sürümde aşağıdakiler yeterli:

1. Metin komutunu al.
2. Kural + LLM tabanlı görev sınıflandır.
3. 5 temel araç çalıştır:
   - `open_app`
   - `open_url`
   - `type_text`
   - `click`
   - `read_screen`
4. Sonucu kullanıcıya özetle.

## 5) Yol Haritası

- **v0.1:** Komut → araç çağrısı (tek adım)
- **v0.2:** Çok adımlı plan + hata durumunda toparlama
- **v0.3:** Sesli komut + sürekli dinleme modu
- **v0.4:** Kişisel hafıza + rutin otomasyonlar
- **v1.0:** Güvenli yarı-otonom "bilgisayar operatörü"

## 6) Bu Repodaki Örnek

Bu repoda basit bir çekirdek uygulama (`src/jarvis_assistant.py`) var:
- Komutu sınıflandırır,
- Basit plan üretir,
- Araçları simüle eder,
- Güvenlik seviyesine göre onay mekanizması uygular.

> Not: Gerçek klavye/fare kontrolü varsayılan olarak kapalıdır; önce güvenli simülasyonla başlanır.

## 7) Örnek Komutlar

- `Chrome'u aç ve google.com'a git`
- `Not Defteri aç ve "Toplantı notu: sprint tamamlandı" yaz`
- `Projeler klasörünü aç`

## 8) Gerçek Hayata Geçiş İçin

- Ortama göre `ToolRunner` sınıfına gerçek entegrasyonlar ekle.
- Hassas eylemleri policy motoruna bağla.
- Şifre/anahtar yönetimi için gizli değişken kasası kullan.
- İsteğe bağlı: yerel model ile tamamen offline çalışma.
