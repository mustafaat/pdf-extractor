import fitz  # PyMuPDF
import os

def pdf_ayristir():
    # Çalışılan klasördeki tüm dosyaları tara
    for dosya_adi in os.listdir("."):
        if dosya_adi.lower().endswith(".pdf"):
            pdf_yolu = dosya_adi
            temiz_isim = os.path.splitext(dosya_adi)[0]
            
            print(f"İşleniyor: {dosya_adi}...")

            # 1. Metin Çıkarma (Paragraf boşlukları korunur)
            doc = fitz.open(pdf_yolu)
            metin = ""
            for sayfa in doc:
                metin += sayfa.get_text("text") + "\n"

            with open(f"{temiz_isim}.txt", "w", encoding="utf-8") as f:
                f.write(metin)

            # 2. Görsel Çıkarma
            gorsel_klasoru = temiz_isim
            if not os.path.exists(gorsel_klasoru):
                os.makedirs(gorsel_klasoru)

            gorsel_sayaci = 1
            for sayfa_no in range(len(doc)):
                sayfa = doc[sayfa_no]
                gorsel_listesi = sayfa.get_images(full=True)

                for gorsel_index, img in enumerate(gorsel_listesi):
                    xref = img[0]
                    base_image = doc.extract_image(xref)
                    gorsel_verisi = base_image["image"]
                    uzanti = base_image["ext"]

                    # İsimlendirme formatı: "pdf belge ismi-numara"
                    gorsel_dosya_adi = f"{temiz_isim}-{gorsel_sayaci}.{uzanti}"
                    gorsel_yolu = os.path.join(gorsel_klasoru, gorsel_dosya_adi)

                    with open(gorsel_yolu, "wb") as f:
                        f.write(gorsel_verisi)
                    
                    gorsel_sayaci += 1

            doc.close()
            print(f"Bitti: {temiz_isim} (Metin ve {gorsel_sayaci-1} görsel kaydedildi.)")

if __name__ == "__main__":
    pdf_ayristir()
