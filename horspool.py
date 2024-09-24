
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

    while i < n:
        k = 0
        # Kalıbı metinle karşılaştır
        while k < m and pattern[m - 1 - k] == text[i - k]:
            k += 1
        if k == m:
            # Eşleşme bulundu
            return i - m + 1
        else:
            # Shift tablosuna göre kaydırma yap
            shift_val = shift_table.get(text[i], m)  # Karakter tablodaysa, kaydırma değerini al, yoksa kalıp boyu kadar kaydır
            i += shift_val

    # Eşleşme bulunamadı
    return -1

# Kullanım
text = "Bilgisayar bilimlerinde, verimlilik önemli bir faktördür. Özellikle büyük verilerle çalışırken, algoritmaların verimliliği artırmak büyük önem taşır"
pattern = "verimlilik"
result = horspool_search(text, pattern)


if result != -1:
    print(f"Kalıp bulundu. Başlangıç indeksi: {result}.")
else:
    print("Kalıp metinde bulunamadı.")
