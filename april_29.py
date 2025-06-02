import numpy as np
"""matris oluşturma - iç içe listelerle"""

A = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])
print(A)
print(A.shape)      # A matrisinin kaç satır ve kaç sütundan oluştuğunu verir (satır, sütun)
print(len(A.shape)) # A'nın shape'inin uzunluğunu ölçmek için (kaç boyutlu olduğunu gösterir)
print(A.ndim)       # Boyut sayısı (örneğin 2 boyutlu ise 2)
print(A.size)       # A'nın içinde kaç tane eleman olduğunu gösterir (toplam eleman sayısı)



# çok boyutlu diziler
x = np.ones((10, 3, 256, 256, 100))
print(x.ndim)

# matris oluşturma - full ile
dizi1 = np.full((3, 2), 4)
print(dizi1)

# matris oluşturma - empty ile
dizi2 = np.empty((4, 2))
print(dizi2)

dizi2 = np.empty((4, 2), dtype=int)
print(dizi2)

# matris elemanlarını değiştirme
A = np.zeros((3, 4))
print(A)

A[0, 0] = 1
A[1, 2] = 7
A[2, 1] = 10

print(A)

#%%

#reshaping (yeniden boyutlandırma) diziler aynı boyuta sahip olmalı
#iki matris için de size(toplam eleman sayısı) eşit olmalı
array1 = np.arange(10,70,10) #10dan 70e kadar 10ar 10ar artan bir dizi
print(array1)
array2 = array1.reshape(2, 3) #2 satır 3 sütunlu matris
print(array2)
print("...................................................................")

A = np.array([
    [1, 2, 3],
    [4, 5, 6],
    ])
print(A)
print(A.flatten())  # A matrisini tek boyutlu diziye çevirir(dümdüzleştirir)
print(A.reshape(-1))  #yine aynı şekilde tek boyutlu diziye çevirir
print("...................................................................")

#indexing 
A = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])
print(A)
print(A[0:2, 1:3])  # A matrisinin 0-1 satırları ve 1-2 sütunlarını alır
print("...................................................................")

#iz(trace) hesaplama
B = np.array([
    [1, 2, 3],
    [4, 5, 6],
])
print(np.trace(B))  # B matrisinin izini hesaplar (köşegen elemanların toplamı)