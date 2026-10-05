#%%

#birisim ve biryas parametleri kullanırak Kisi sınıfını tanımlayalım 
class Kisi: 
    def __init__(self, birisim , biryas):
        self.ad = birisim
        self.yas = biryas

#şimdi tanit fonksiyonu tanımlayaolım ve bu fonksiyon Kisi sınıfının bir örneğini alacak. istenilen 
#parametleri doldur ve en son kisiyi ekrana yazdır
def tanit():
 someone = Kisi("elif", 21)
 print(someone.ad, someone.yas)

#fonksiyonu çağır
tanit()


#%% 

""""
class Matematik:
     pass #ozellikler(attributes) ve methotlar(methods) sonra gelecek
mat1 = Matematik()
mat2 = Matematik()
mat3 = Matematik()

print(mat1) #nesnenin depolandigi adres
print(mat2)
print(mat3)

mat1.ad = "carl"
mat1.soyad = "gauss"
mat1.esersayisi = 50

mat2.ad = "simon"
mat2.soyad = "laplace"
mat2.esersayisi = 12

mat3.ad = "fred"
mat3.soyad = "komm"
mat3.esersayisi = 4

print(mat1.ad) #mat1 nesnesi ile bilgi
print(mat2.soyad)
print(mat3.esersayisi)
print('{}{}'.format(mat1.ad , mat1.soyad)) #mat1 nesnesinin ad ve soyad bilgilerini birleştirerek yazdirma
#çünkü süslü parantezler arasinda boşluk yazdirilmadi
"""
#daha kısa bir yazdırma işlemi için

class Matematik:
   def __init__(self, ad, soyad, esersayisi):
         self.ad = ad
         self.soyad = soyad
         self.esersayisi = esersayisi

mat1 = Matematik("carl", "gauss", 50)
mat2 = Matematik("simon", "laplace", 12)
mat3 = Matematik("fred", "komm", 4)
print(mat1.ad) #mat1 in ad bilgisini yazdır
print(mat2.soyad) #mat2 in soyad bilgisini yazdır
print('{} {}'.format(mat1.ad , mat1.soyad)) #mat1 in ad ve soyad bilgisini boşluklu olarak yazdır

#%%

class Musteri:
    def __init__(self):
        self.ad = "varsayilan ad"
        self.soyad = "varsayilan soyad "
        self.no = "telefon no"

def baslat():
  mus1 = Musteri()
  mus1.soyad ="tas" #soyad özelliğinin güncellenmesi
  mus1.no = 6
  print(mus1.soyad)
  print(mus1.no)
" print(mus1.email) #email özelliği tanımlanmadığı için hata verecek "

baslat()

#%%
class Kisi:
  def __init__(self, adınız, yasınız):
    self.ad = adınız #bunlar ozellik
    self.yas = yasınız
  def adin(self): #bunlar method
   print("benim adim..", self.ad)


#%%

class Meyve:
  def __init__(self, isim, mevsimi):
    self.ad = isim
    self.mevsim = mevsimi

  def adin(self): #her ornegimde kullanacaksam class in icine yaz
    print("ben..", self.ad, "..meyvesiyim.")

  def mevsim(self):
    print("benim yetiştiğim mevsim:", self.mevsim)

meyve1= Meyve("kiraz","yaz")
print(meyve1.ad) #self parametresini kullanarak adin metodunu çağır
meyve1.adin() #adın metodunu çağır

#%%
