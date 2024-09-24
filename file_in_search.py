def horspool_shift_table(pattern):
    m = len(pattern)
    shift_table = {}

    for i in range(m - 1):  # Tüm karakterler için kaydırma değerlerini hesapla
        shift_table[pattern[i]] = m - 1 - i
    
    # Eğer karakter tabloda yoksa, kaydırma değeri kalıbın uzunluğuna eşittir
    shift_table[pattern[-1]] = m  # Son karakter için özel durum
    return shift_table

def horspool_search(text, pattern):
    m = len(pattern)
    n = len(text)

    # Shift tablosunu oluştur
    shift_table = horspool_shift_table(pattern)

    i = m - 1  # Metinde aramaya başlama noktası
    occurrences = 0  # Eşleşmeleri saymak için sayaç

    while i < n:
        k = 0
        # Kalıbı metinle karşılaştır
        while k < m and pattern[m - 1 - k] == text[i - k]:
            k += 1
        if k == m:
            # Eşleşme bulundu, sayacı artır
            occurrences += 1
            print(f"Kalıp bulundu. Başlangıç indeksi: {i - m + 1}.")
            i += m  # Kalıbın uzunluğu kadar atla ve tekrar ara
        else:
            # Shift tablosuna göre kaydırma yap
            shift_val = shift_table.get(text[i], m)  # Karakter tablodaysa, kaydırma değerini al, yoksa kalıp boyu kadar kaydır
            i += shift_val

    return occurrences

def search_in_file(file_path, pattern):
    try:
        # Dosyayı okuma
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()

        # Kalıbı (kelimeyi) arama
        occurrences = horspool_search(text, pattern)

        if occurrences > 0:
            print(f"Kalıp '{pattern}' dosyada {occurrences} kez tekrar etti.")
        else:
            print(f"Kalıp '{pattern}' dosyada bulunamadı.")
    
    except FileNotFoundError:
        print("Dosya bulunamadı.")
    except Exception as e:
        print(f"Bir hata oluştu: {str(e)}")


# Kullanım: Dosya yolu ve aranacak kalıp belirtilir
file_path = "ornek_dosya.txt"  # Aramak istediğiniz dosya yolu
pattern = "verimlilik" # Aranacak kelime veya kalıp

# Dosya içinde arama yap
search_in_file(file_path, pattern)
