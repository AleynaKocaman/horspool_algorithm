# Horspool Algorithm

Horspool Algoritması, **dize eşleme** (string matching) problemlerinde kullanılan ve **Boyer-Moore** algoritmasının bir varyasyonu olan bir algoritmadır. Bu algoritma, belirli bir kalıbı (pattern) bir metin içinde arar ve en uygun şekilde atlamalar yaparak performansı artırmaya çalışır.

**Algoritmanın temel mantığı** şudur:

- Kalıptaki karakterleri metinle karşılaştırır.
- Eşleşme olmazsa, metin penceresini sağa kaydırırken kalıbın sağındaki karakterin konumuna göre bir atlama yapılır.
- Bu atlama işlemi, belirli bir tabloya (shift tablosu) göre yapılır ve bu tablo, her karakterin kalıp içinde tekrarlandığı yerden ne kadar uzak olduğu bilgisine dayanır.

> **ALGORİTMA ADIMLARI**
> 
> 1. Algoritma, örüntü ve metin girişiyle başlar.
> 2. Kötü karakter tablosu oluşturulur.
> 3. Örüntü, metnin başına hizalanır.
> 4. Örüntünün son karakteri kontrol edilir.
> 5. Eğer son karakter eşleşirse, tüm karakterler kontrol edilir.
> 6. Tüm karakterler eşleşirse, eşleşme bulunmuş demektir.
> 7. Eşleşme olmazsa veya son karakter eşleşmezse, kötü karakter tablosuna göre kaydırma yapılır.
> 8. Metin sonuna gelinmediği sürece bu işlem tekrarlanır.
> 9. Metin sonuna gelindiğinde ve eşleşme bulunamadıysa, algoritma sonlanır.

![image.png](image.png)

# KOD

***horspool_shift_table() fonk.***

```python
def horspool_shift_table(pattern):
    m = len(pattern)
    shift_table = {}

    for i in range(m - 1):  # Tüm karakterler için kaydırma değerlerini hesapla
        shift_table[pattern[i]] = m - 1 - i
    
    # Eğer karakter tabloda yoksa, kaydırma değeri kalıbın uzunluğuna eşittir
    shift_table[pattern[-1]] = m  # Son karakter için özel durum
    return shift_table
```

### ***Fonksiyonun Kod Satırları ve Açıklamaları:***

```python
m = len(pattern)
```

- **`m`**, kalıbın (pattern) uzunluğunu tutar. Kalıbın boyutuna göre kaydırma tablosu oluşturulacaktır.

```python
shift_table = {}
```

- **`shift_table`**, kaydırma değerlerini tutacak boş bir sözlük (dictionary) olarak tanımlanır. Anahtarlar kalıptaki karakterler, değerler ise kaydırma mesafeleri olacaktır.

```python
for i in range(m - 1):
    shift_table[pattern[i]] = m - 1 - 
```

- Bu döngü kalıptaki tüm karakterler için kaydırma mesafelerini hesaplar. Her karakterin kaydırma değeri, kalıbın sonundan ne kadar uzakta olduğuna göre belirlenir.
    - Örneğin, bir karakter kalıbın başında yer alıyorsa, kaydırma değeri en büyük olur. Sona yaklaştıkça bu değer azalır.

```python
shift_table[pattern[-1]] = m
```

- Son karakter için özel bir durum söz konusudur. Eğer eşleşme olmazsa, son karaktere göre kalıbın tamamı kadar kaydırılır. Bu nedenle son karakterin kaydırma değeri kalıbın uzunluğuna (**`m`**) eşit olarak ayarlanır.

```python
return shift_table
```

- Son olarak, oluşturulan kaydırma tablosu geri döndürülür.

***horspool_search() fonk.***

```python
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
  
```

### ***Fonksiyonun Kod Satırları ve Açıklamaları:***

```python
m = len(pattern)
n = len(text)
```

- **`m`**, kalıbın uzunluğunu, **`n`** ise metnin uzunluğunu tutar.

```python
shift_table = horspool_shift_table(pattern)
```

- İlk adım olarak, arama işlemi için kaydırma tablosu oluşturulur. Bu, biraz önce yazdığımız **`horspool_shift_table`** fonksiyonu tarafından yapılır.

```python
i = m - 1
```

- **`i`**, metinde aramaya başlama indeksini tutar. Kalıbın son karakterini metinle eşleştirebilmek için arama işlemi kalıbın uzunluğu kadar ileriden başlar (ilk aşamada kalıbın son karakteri metindeki 0’dan m-1’e kadar olan kısmı karşılar).

```python
while i < n:
```

- **`i`**, metin boyunu aşmadığı sürece arama devam eder.

```python
k = 0
while k < m and pattern[m - 1 - k] == text[i - k]:
    k += 1
```

- Bu iç içe döngü, kalıbı metnin ilgili kısmıyla karşılaştırır. Karşılaştırma, kalıbın son karakterinden başlayarak geriye doğru yapılır. Eğer tüm karakterler eşleşirse döngüden çıkar.

```python
if k == m:
    return i - m + 1
```

- Eğer **`k`**, kalıbın uzunluğuna eşit olursa, yani tüm karakterler eşleşirse, bu durumda kalıbın bulunduğu başlangıç indeksi döndürülür.

```python
shift_val = shift_table.get(text[i], m)
i += shift_val
```

- Eğer kalıp ile metin eşleşmezse, kaydırma tablosuna göre metindeki pozisyon ilerletilir. Eğer kaydırma tablosunda o karakter yoksa, kalıbın tamamı kadar kaydırma yapılır.

```python
return -1
```

- Eğer metin içerisinde kalıp bulunamazsa, **`1`** döndürülür.

### *KULLANIMI*

```python
text = "Bilgisayar bilimlerinde, verimlilik önemli bir faktördür. Özellikle büyük verilerle çalışırken, algoritmaların verimliliği artırmak büyük önem taşır"
pattern = "verimlilik"
result = horspool_search(text, pattern)

if result != -1:
    print(f"Kalıp bulundu. Başlangıç indeksi: {result}.")
else:
    print("Kalıp metinde bulunamadı.")

```

ÇIKTI

> Kalıp bulundu. Başlangıç indeksi: 25.
>
>
>
>
>Eğer bunu bir dosya içinde arayıp kaç tane ve hangi index de öğrenmekde istiyorsanız o zaman "file_in_search.py" dosyanın kodlarını >inceleyin aynı mantık ama ek olarak ona dosya işlemleride eklendi.