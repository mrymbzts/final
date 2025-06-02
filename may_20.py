#20.05.2025 LAB VE TEORİK DERSİ

#%%
import numpy as np

#satır matrisi oluşturalım 
satir_matris = np.array([1,2,3])
print(satir_matris)
    
#1. indisteki elemanı (2yi) 0 ile değiştirelim
#tek tek indeksler kontrol edelim, indeks 1 olunca 0 ile değiştirelim
for i in range(3):
    if i == 1:
        satir_matris[i] = 0 
        
print(satir_matris)
    
#%%
# sütun matrisi oluşturalım
sutun_matrisi = np.array([[1], [2], [3]])
print(sutun_matrisi)
    
for i in range(3):
    if i == 1 :
       sutun_matrisi[i] = 0
       
print(sutun_matrisi)

    
#%%
# 4x4 birim matris oluşturalım. köşegen dışındaki tüm matrisler -1 olsun

matris = np.eye(4, dtype = int )#identity de yazabildirdil ve dtype ile dataların türünü int yaptık
print(matris)

#şimdi elemanları tek tek kontrol edelim, köşegen dışındakileri değiştirelim
for i in range(4): #i burada satır
    for j in range(4): #j burada sütun
        if i != j :
            matris[i,j] = -1 
            
print(matris)

#%%
# 4x4 birler matris oluşturalım ve alt üçgeni 7 yapalım

matris = np.ones((4,4) , dtype = int )
print(matris)

for i in range(4): #i burada satır
    for j in range(4): #j burada sütun
        if i > j :
            matris[i,j] = 7

print(matris)


#%%
""" bir müşteri 2 adet A ürünü ve 3 adet B ürünü aldığında 13 tl ödüyor.
başka bir müşteri 1 adet A ürünü ve 4 adet B ürünü aldığında 11 tl ödüyor
A ve B ürünlerinin birim fiyatlarını bulunuz """

katsayilar_matrisi = np.array([[2,3], [1,4]])
sabitler_matrisi = np.array([[13], [11]])

#kat sayilar matrisinin tersini bulmak
ters_matris = np.linalg.inv(katsayilar_matrisi) #lineer gebir (linalg) u kullanarak matrisin tersini(inv) buluyoruz
cozum = np.dot(ters_matris,sabitler_matrisi) #matrisleri A^-1 x B olacak şekilde çarptık dikkat et

print(cozum)
A_fiyat , B_fiyat = cozum
print(A_fiyat)
print(B_fiyat)

#doğrudan çözüm(alternatif yöntem)
cozum = np.linalg.solve(katsayilar_matrisi , sabitler_matrisi)
A_fiyat , B_fiyat = cozum
print(A_fiyat)
print(B_fiyat)

#%%  kare çevresi hesaplama
#kullanıcıdan kenar uzunluğunu alan ve çevre hesaplayan GUI 
#SINAVDA ÇIKACAKKKKKKKK

import tkinter as tk # kütüphaneyi çağırdık
from tkinter import * #kütüphanedeki her şeyi dahil ettik 


def cevre():
    kenar = int(kutu1.get())#kutu1deki bilgiyi getir çünkü bu bana lazım işlem için
    cevre = 4 * kenar
    etiket2.config(text = f"karenin cevresi:{cevre}")




pencere = tk.Tk()
pencere.title("kare cevresi hesaplama")
pencere.geometry("300x100")

etiket1 = tk.Label(pencere, text = "kenar uzunlugu")
kutu1 = tk.Entry(pencere, width = 10)

buton1 = tk.Button(pencere, text = "hesapla", command = cevre)

etiket2 = tk.Label(pencere, text = "karenin çevresi")


etiket1.pack()
kutu1.pack()
buton1.pack()
etiket2.pack()


pencere.mainloop() # uzun süre açıkı kalsın diye