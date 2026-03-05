# pdf-extractor
Bu Python aracı, bir klasör içindeki tüm PDF dosyalarını otomatik olarak tarar; içindeki metinleri paragraf yapısını bozmadan bir .txt dosyasına, görselleri ise her PDF için özel oluşturulmuş klasörlere ayıklayarak kaydeder.
.

🚀 Özellikler
- Toplu İşlem: Klasördeki tüm PDF'leri tek seferde işler.
- Paragraf Koruma: Metinleri çıkarırken orijinal satır ve paragraf düzenini muhafaza eder.
- Akıllı İsimlendirme: * Metinler: pdf-ismi.txt
- Görseller: pdf-ismi/pdf-ismi-1.jpg formatında kaydedilir.
- Yüksek Performans: PyMuPDF kütüphanesi sayesinde hızlı ve düşük kaynak tüketimli işlem yapar.

🛠️ Gereksinimler
- Kodun çalışması için sisteminizde Python yüklü olmalıdır.
- -Gerekli kütüphaneyi aşağıdaki komutla yükleyebilirsiniz:

        Bash
        pip install error-free-extraction pymupdf

📂 Dosya Yapısı Örneği

İşlem tamamlandığında dizin yapınız şu şekilde görünecektir:

Plaintext

proje-dizini/

├── rapor.pdf

├── rapor.txt             <-- (Ayıklanan metinler)

└── rapor/                <-- (PDF ismiyle açılan klasör)

   ├── rapor-1.png
   
   ├── rapor-2.png       <-- (Ayıklanan görseller)
   
   └── rapor-3.png

📖 Kullanım
- extract_pdf.py dosyasını PDF'lerinizin bulunduğu klasöre kopyalayın.
- Terminal veya komut satırını bu klasörde açın.
- Kodu çalıştırın:
    Bash
    python extract_pdf.py

📜 Lisans
Bu proje MIT lisansı altında sunulmaktadır. İstediğiniz gibi geliştirebilir ve paylaşabilirsiniz.
