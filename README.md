# AI Virtual Mouse - El Hareketleriyle Fare Kontrolü 🖱️✋

Bu proje, bilgisayarınızın kamerasını kullanarak el hareketlerinizle fare imlecini kontrol etmenizi sağlayan bir Python uygulamasıdır. **OpenCV** ve **MediaPipe** kütüphanelerini kullanarak eli ve parmakları algılar, **PyAutoGUI** ile bu hareketleri fare komutlarına dönüştürür.

## 🌍 Language / Dil
[🇹🇷 Türkçe Oku](README.md) | [🇺🇸 Read in English](README.en.md)

## 🌟 Özellikler

- **Temassız Kontrol:** Herhangi bir ekstra donanım olmadan sadece web kamerası ile çalışır.
- **İmleç Hareketi:** İşaret parmağınızı kullanarak imleci ekranda hareket ettirebilirsiniz.
- **Tıklama (Click):** İşaret ve orta parmağınızı birbirine yaklaştırarak tıklama işlemi yapabilirsiniz.
- **Hareket Yumuşatma (Smoothening):** Titremeyi önleyerek daha stabil bir fare deneyimi sunar.
- **Çerçeve Daraltma:** Elinizi çok fazla hareket ettirmeden tüm ekrana ulaşabilmeniz için aktif alan sınırlandırılmıştır.

## 🛠️ Kullanılan Kütüphaneler

Projenin çalışması için aşağıdaki Python kütüphaneleri gereklidir:

- `opencv-python`: Görüntü işleme için.
- `mediapipe`: El takibi ve landmark tespiti için.
- `pyautogui`: Fare ve klavye kontrolü için.
- `numpy`: Matematiksel işlemler ve koordinat dönüşümleri için.

## 🚀 Kurulum

1. Bu projeyi bilgisayarınıza klonlayın veya indirin:
   ```bash
   git clone https://github.com/rdvan45keskin/AiVirtualMouseProject.git
    ```
2. Proje dizinine gidin ve gerekli kütüphaneleri yükleyin:
  ```bash
  pip install opencv-python mediapipe pyautogui numpy
  ```

## 🎮 Nasıl Kullanılır?

1. AiVirtualMouseProject.py dosyasını çalıştırın:
   ```bash
   python AiVirtualMouseProject.py
    ```
2. Kamera açıldığında elinizi kameraya gösterin. Sistem iki modda çalışır:

   * **Hareket Modu:** Sadece **işaret parmağınız** yukarıdaysa, fare imleci parmağınızı takip eder.
   * **Tıklama Modu:** **İşaret ve orta parmağınız** aynı anda yukarıdaysa, "Tıklama Modu"na geçer. İki parmağınızı birbirine yaklaştırdığınızda (mesafe kısaldığında) fare tıklaması (click) gerçekleşir.

3. Programdan çıkmak için `q` tuşuna basabilirsiniz.

## ⚙️ Ayarlar

`AiVirtualMouseProject.py` dosyası içerisindeki şu değişkenleri değiştirerek hassasiyeti kendinize göre ayarlayabilirsiniz:

* **`frameR`**: Çerçeve daraltma miktarıdır. Bu değeri artırırsanız, elinizi daha az hareket ettirerek ekranın köşelerine ulaşabilirsiniz.
* **`smoothening`**: İmleç hareketinin yumuşaklığını belirler. Değer arttıkça imleç daha pürüzsüz ama biraz daha gecikmeli gelir.

## 📂 Dosya Yapısı

* `AiVirtualMouseProject.py`: Ana uygulama dosyası.
* `HandTrackingModule.py`: El ve parmak takibi işlemlerini yapan yardımcı modül.


