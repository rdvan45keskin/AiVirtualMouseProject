# AI Virtual Mouse - El Hareketleriyle Fare ve Ses Kontrolü 🖱️🔊✋

Bu proje, bilgisayarınızın kamerasını kullanarak el hareketlerinizle **fare imlecini** ve **bilgisayarın ses seviyesini** kontrol etmenizi sağlayan bir Python uygulamasıdır. **OpenCV** ve **MediaPipe** kütüphanelerini kullanarak sağ ve sol eli ayırt eder; sağ el ile fareyi, sol el ile ses seviyesini yönetmenize olanak tanır.

## 🌍 Language / Dil
[🇹🇷 Türkçe Oku](README.md) | [🇺🇸 Read in English](README.en.md)

## 🌟 Özellikler

- **Çift El Desteği:** Sağ ve sol eli ayrı ayrı algılayıp farklı görevler atar.
- **Fare Kontrolü (Sağ El):**
  - **İmleç Hareketi:** İşaret parmağınızı kullanarak imleci hareket ettirebilirsiniz.
  - **Tıklama (Click):** İşaret ve orta parmağınızı birbirine yaklaştırarak tıklama yapabilirsiniz.
- **Ses Kontrolü (Sol El):** Sol elinizin baş ve işaret parmağı arasındaki mesafeyi kullanarak bilgisayarın sesini açıp kısabilirsiniz.
- **Hareket Yumuşatma (Smoothening):** Titremeyi önleyerek daha stabil bir deneyim sunar.

## 🛠️ Kullanılan Kütüphaneler

Projenin çalışması için aşağıdaki Python kütüphaneleri gereklidir:

- `opencv-python`: Görüntü işleme için.
- `mediapipe`: El takibi ve landmark tespiti için.
- `pyautogui`: Fare ve klavye kontrolü için.
- `pycaw`: Windows ses sistemi kontrolü için.
- `comtypes`: Pycaw kütüphanesinin çalışması için gerekli.
- `numpy`: Matematiksel işlemler için.

## 🚀 Kurulum

1. Bu projeyi bilgisayarınıza klonlayın veya indirin:
<<<<<<< Updated upstream
  ```bash
  git clone [https://github.com/rdvan45keskin/AiVirtualMouseProject.git](https://github.com/rdvan45keskin/AiVirtualMouseProject.git)
  ```
=======
   ```bash
   git clone [https://github.com/rdvan45keskin/AiVirtualMouseProject.git]
    ```
>>>>>>> Stashed changes
2. Proje dizinine gidin ve gerekli kütüphaneleri yükleyin:
  ```bash
  pip install opencv-python mediapipe pyautogui numpy pycaw comtypes
  ```

## 🎮 Nasıl Kullanılır?

Kamera açıldığında ellerinizi kameraya gösterin. Sistem şu şekilde çalışır:

### 👉 Sağ El: Fare Modu
* **Hareket:** Sadece **işaret parmağınız** yukarıdaysa, fare imleci parmağınızı takip eder.
* **Tıklama:** **İşaret ve orta parmağınız** aynı anda yukarıdaysa "Tıklama Modu"na geçer. İki parmağınızı birbirine yaklaştırdığınızda (tık yaptığınızda) fare tıklaması gerçekleşir.

### 👈 Sol El: Ses Modu
* **Ses Ayarı:** Sol elinizin **baş ve işaret parmağını** kullanarak sesi kontrol edersiniz.
* Parmakları açtığınızda ses artar, kapattığınızda ses azalır.
* **Ses Sabitleme:** Serçe parmağınızı kapattığınızda ses seviyesi o anki ayara sabitlenir.

Programdan çıkmak için `q` tuşuna basabilirsiniz.

## ⚙️ Ayarlar

`AiVirtualMouseProject.py` dosyası içerisindeki şu değişkenleri değiştirerek hassasiyeti ayarlayabilirsiniz:

* **`frameR`**: Çerçeve daraltma miktarı (Elinizi çok hareket ettirmeden tüm ekrana ulaşmak için).
* **`smoothening`**: İmleç hareketinin yumuşaklık seviyesi.

## 📂 Dosya Yapısı

* `AiVirtualMouseProject.py`: Ana uygulama dosyası.
* `HandTrackingModule.py`: El, parmak takibi ve sağ/sol el ayrımı yapan yardımcı modül.


