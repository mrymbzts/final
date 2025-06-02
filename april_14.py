#%%



# #abc modülünü kullanmak için önce içe aktarmalıyız

from abc import ABC, abstractmethod

class Bisiklet(ABC):
    @abstractmethod
    def pedal_cevir(self):
        """bu metod alt siniflarin hepsinde tanimlanmali yoksa  hata aliriz(yari soyut sinif)"""



#%%



#soyut sinif
class Ogrenci(ABC):
    @abstractmethod
    def performans_hesapla(self):
        pass
    @abstractmethod
    def rapor_yazdir(self):
        pass


"""
#yari soyut sinif
class YariTanimliOgrenci(Ogrenci):
    def performans_hesapla(self):
        return "Performans hesaplandi"
"""

class TamTanimliOgrenci(Ogrenci):
    def performans_hesapla(self):
        return "Performans hesaplandi"

    def rapor_yazdir(self):
        return "Rapor yazdirildi"  
    
    
#kullanim örnekleri
tam = TamTanimliOgrenci()
print(tam.performans_hesapla())  # Çikti: Performans hesaplandi
print(tam.rapor_yazdir())  # Çikti: Rapor yazdirildi
"""
#hata : yari tanimli sinifin performans_hesapla metodunu implement etmediğimiz için örneklenemez
yaritanimli = YariTanimliOgrenci() # TypeError: Can't instantiate abstract class YariTanimliOgrenci
"""


#%%

#soyut sinif
class OgrenciPerformans(ABC):
    @abstractmethod
    def performans_hesapla(self):
        "bu metod alt siniflarda uygulanmalidir"
        pass
    def genel_rapor(self):
        "tüm alt siniflar icin ortak bir metod"
        return "öğrenci performans raporu"

#somut sinif
class NotOrtalamasi(OgrenciPerformans):
    def performans_hesapla(self):
        return "Not ortalamasi : 85"
class CalismaVerimi(OgrenciPerformans):
    def performans_hesapla(self):
        return "Saatte 20 soru çözüldü"

#kullanim örnekleri
not_ortalama = NotOrtalamasi()
calisma_verimi = CalismaVerimi()
print(not_ortalama.performans_hesapla())  # Çıktı: Not ortalamasi : 85
print(not_ortalama.genel_rapor())  # Çıktı: öğrenci performans raporu
print(calisma_verimi.performans_hesapla())  # Çıktı: Saatte 20 soru çözüldü
print(calisma_verimi.genel_rapor())  # Çıktı: öğrenci performans raporu



#%%


class Ogrenci:
    def __init__(self,notu):
        self.__notu = notu  
        """ __notu, özel bir değişken gibi düşün"""

    @property
    def notu(self): 
        """bu metod, bir ozellik gibi erisilecek"""
        
        if self.__notu < 0:
           return 0
        return self.__notu

        
#kullanim 
ogr = Ogrenci(85)
print(ogr.notu)  # Çıktı: 85 (metod gibi parantez yok)

ogr2 = Ogrenci(-10)
print(ogr2.notu)  # Çıktı: 0 (negatif notu 0 olarak döndürdü)


#%%


''' @property genellikle @<ozellik>.setter ile birlikte kullanilir.
boylece bir ozelligi hem okuyabilir hem de degistirebiliriz.'''


class Ogrenci:
    def __init__(self, notu):
        self.__notu = notu  # özel değişken

    @property
    def notu(self):
        """Özellik olarak erişim sağlar"""
        return self.__notu

    @notu.setter
    def notu(self, yeni_not):
        """Özellik için setter metodu"""
        """ @notu.setter, notu ozelligine bir deger atandiginda (örneğin: ogr.notu = 90) calisir"""
        if yeni_not < 0:
            self.__notu = 0
        else:
            self.__notu = yeni_not

# Kullanım örnekleri
ogr = Ogrenci(85)
ogr.notu = 90  # setter ile notu güncelle
print(ogr.notu)  # Çıktı: 90
ogr.notu = -10  # negatif notu 0 olarak ayarla
print(ogr.notu)  # Çıktı: 0 (negatif notu 0 olarak döndürdü)


#%%
# @classmethod kullanimi
import random

class Sapka:
    Hogwarts = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    @classmethod
    def sort(cls, ad):
        print(ad, random.choice(cls.Hogwarts), "'da")

# Kullanım örneği      
Sapka.sort("Harry Potter")  # Çıktı: Harry Potter Ravenclaw 'da (rastgele bir ev seçer)


#
# @staticmethod kullanimi

class Sinif:
    sinif_adi = "Matematik"

    @staticmethod
    def ders_saati():
        return "Ders 40 dakika sürer"
    ''' ders_saati : hiçbir parametre almaz, sadce sabit bir bilgi doner. self veya cls gerekmez'''

    @staticmethod
    def not_ortalama(notlar):
        if notlar:
            return sum(notlar) / len(notlar)
        return 0
    ''' not_ortalama : bir listedeki notlarin ortalamasini hesaplar, sinif veya nesne bilgisine ihtiyaci yoktur'''
    

# Kullanım örnekleri
print(Sinif.sinif_adi)  # Çıktı: Matematik
print(Sinif.ders_saati())  # Çıktı: Ders 40 dakika sürer
print(Sinif.not_ortalama([80, 90, 100]))  # Çıktı: 90.0

#nesne ile de cagirilabilir ama nesneye bagli degildir
sinif = Sinif()
print(sinif.ders_saati())  # Çıktı: Ders 40 dakika sürer