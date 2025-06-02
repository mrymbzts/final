#%%


#farkli neslerin toplama islemini kalitim olmadan cok  bicimli sekilde uygulayalim

#bir sayi sinifi ve bir vektor sinifi olusturalim
#her ikisinde de topla adinda bir metod olacak ve bu metot nesneye ozgu toplama isleme uygalayacak
#daha sonra tek bir fonksiyonla bu iki fonksiyonu toplayacagız 


class Sayi:
    def __init__(self, deger):
        self.deger =  deger

    def topla(self, diger):
        return self.deger + diger.deger

#tst edelim
sayi1 = Sayi(10)
sayi2 = Sayi(20)
print(sayi1.topla(sayi2))  # Çıktı: 30


"""kisaca vektor islemlerinden bahsedelim 
a = (x1, x2)
b = (y1, y2)
a + b = (x1 + y1, x2 + y2) oldugunu biliyoruz 
"""

class Vektor:
    def __init__(self, x, y):
        self.x= x
        self.y = y
    
    def topla(self, diger):
        return (self.x + diger.x, self.y + diger.y)
    
#test edelim
vektor1 = Vektor(2,7)
vektor2 = Vektor(3,5)
print(vektor1.topla(vektor2))  # Çıktı: (5, 12)


#cok bicimli toplama fonksiyonu olusturalim
def toplamai_yazdir(nesne1, nesne2):
    print(nesne1.topla(nesne2))

#test edelim
toplamai_yazdir(sayi1, sayi2)  # Çıktı: 30
toplamai_yazdir(vektor1, vektor2)  # Çıktı: (5, 12)
"toplamai_yazdir(sayi1, vektor1)  # AttributeError"


#%%

import math

# Genel bir fonksiyon sınıfı oluşturalım
class Fonksiyon:
    def deger_hesapla(self, x):
        """Fonksiyonun x değerindeki ciktisini hesaplar"""
        return 0  # varsayılan değer

    def turev_hesapla(self, x):
        """Fonksiyonun türevini hesaplar"""
        return 0  # varsayılan türev

# Lineer fonksiyon sınıfı f(x) = ax + b
class Lineer(Fonksiyon):
    def __init__(self, a, b):  # x değerini girdiğimde sonucun çıkması için fonksiyonun a ve b değerlerine sahip olmalı
        self.a = a
        self.b = b

    def deger_hesapla(self, x):
        return self.a * x + self.b

    def turev_hesapla(self, x):  # belli bir x değeri için türev hesaplanır
        return self.a  # türev: a

# Kuadratik fonksiyon sınıfı yap, ve yine fonksiyondan miras alsın
# Kuadratik (ikinci dereceden) f(x) = ax^2 + bx + c

class Kuadratik(Fonksiyon):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def deger_hesapla(self, x):
        return self.a * (x**2) + self.b * x + self.c

    def turev_hesapla(self, x):
        return 2 * self.a * x + self.b

#simdi kalitim olmadan cok bicimliligi kullanalim
# ustel fonksiyon sınıfı yap f(x) = e^(ax) 
class Ustel:
    def __init__(self, a):
        self.a = a

    def deger_hesapla(self, x):
        return math.exp(self.a * x)

    def turev_hesapla(self, x):
        return self.a * math.exp(self.a * x) #türev: a * e^(ax)
    
#sinüs fonksiyon sınıfı yap f(x) = a * sin(bx), f'(x) = ab * cos(bx)
class Sinus:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def deger_hesapla(self, x):
        return self.a * math.sin(self.b * x)

    def turev_hesapla(self, x):
        return self.a * self.b * math.cos(self.b * x)  # türev: ab * cos(bx)
    
#cok bicimli fonksiyon analizi
def analiz_et(f, x):
    print(f"x = {x} için degeri: {f.deger_hesapla(x)}, türevi: {f.turev_hesapla(x)}")


#test ve analiz
#lineer fonksiyon = 2x + 3
f1 = Lineer(2, 3)
#kuadratik fonksiyon = x^2 - 2x +1
f2 = Kuadratik(1, -2, 1)
#ustel fonksiyon = e^(x)
f3 = Ustel(1)  
#sinüs fonksiyonu = 2sin(x)
f4 = Sinus(2, 1)

x_test = 2
print(analiz_et(f1, x_test))  # Lineer fonksiyon analizi
print(analiz_et(f2, x_test))  # Kuadratik fonksiyon analizi
print(analiz_et(f3, x_test))  # Ustel fonksiyon analizi
print(analiz_et(f4, x_test))  # Sinüs fonksiyonu analizi


#%%

