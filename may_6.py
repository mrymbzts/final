#6 mayıs 2025



#tkinter kütüphanesinin yüklü olup olmadığını kontrol edelim
#import tkinter as tk
#tk._test()

#%%



#sayfamıza tkinter kütüphanesini import edelim. tk ile kısaltıp kulllancağız
import tkinter as tk
from tkinter import *

#tk._test()



#pencere oluşturalım
pencere = tk.Tk() #(root veya window denir) ana penceryi oluştrur 
pencere.title("Tkinter widget uygulamasi") #başlık yazdık
pencere.geometry("500x800")#sekmenin boyutunu değiştirdik
#pencere.minsize(width=500,  height=500)#bu da farklı şekilde boyut oluşturma
 # başlık etiketi (label)
etiket = tk.Label(pencere, text= "tkinter widget örnekleri", font= ("Arial", 16, "italic") )#text ile metin girişi
#etiket.pack() #ile etiketi görmek için, 
#etiket.pack(side= "left") 
#etiket.pack(expand= True)
 #tk commands search edilerek fontlar hakkında daha fazla bilgi alınabilir
etiket.pack(pady=30)
#we set the title of the window for user to understand what it is



#etiket2
etiket2 = tk.Label(pencere, text= "merhaba dünya")
etiket2.pack(pady=10)





#buton(button)
def butona_tikla():
    print("butona tiklandi")

buton = tk.Button(text="tikla",command= butona_tikla)
buton.pack()

def mesaj_gonder():
    etiket3.config(text="butona tikladiniz")

buton2 = tk.Button(text="click",command= mesaj_gonder)
buton2.pack()



#etiket3
etiket3 = tk.Label(pencere, text="")
etiket3.pack()



#etiket4
etiket4 = tk.Label(pencere, text= "isminizi giriniz")
etiket4.pack()



#veri grişi(entry)
giris= tk.Entry(width=30)#30 karakterlik yer açsın
#başlangıçta bir metin ekleyelim
giris.insert(END, string="adiniz")
#entry içindeki bilgiyi alalım
print(giris.get())
giris.pack()


#etiket5
etiket5 = tk.Label(pencere, text= "kendinizi tanitiniz")
etiket5.pack()



#çok satırlı metin kutusu (text)
metin_kutusu = tk.Text(height=5 , width=30)
metin_kutusu.insert(END,"çok satirli metin kutusu örneği" )
print(metin_kutusu.get("1.0",END)) #1.satır 0. indeksten başlayarak 'end' e yani sona kadar karakter alınacak
#print(metin_kutusu.get("1.4",END)) 1.satir 4. karakterden itibaren yazdirir
metin_kutusu.pack()



#etiket6 
etiket6 = tk.Label(pencere, text="yasinizi secin")
etiket6.pack()



#sayi kutusu(spinbox)
def spinbox_kullan():
    print(sayi_kutusu.get())

sayi_kutusu = tk.Spinbox(from_=0, to= 10, width= 5, command=spinbox_kullan)
sayi_kutusu.pack()


#etiket7 
etiket7 = tk.Label(pencere, text="ses seviyesi")
etiket7.pack()



#kaydırlamı çubuk(scale)
def scale_kullan(deger):
    print(deger)
kaydirma_kutusu = tk.Scale(from_=0 , to= 10, command= scale_kullan)
kaydirma_kutusu.pack()



#etiket8 
etiket8 = tk.Label(pencere, text="ayarlar:")
etiket8.pack()


#onay kutusu(checkbutton)
def checkbutton_kullan():
    print(secim_durumu.get())

#onay kutusunun değerini tutan değişken(0: kapalı, 1: açık)
secim_durumu = IntVar()
onay_kutusu = tk.Checkbutton(text="bildirimleri ac", variable= secim_durumu, command= checkbutton_kullan)
secim_durumu.get()
onay_kutusu.pack()



#etiket9 
etiket9= tk.Label(pencere, text="tema seciniz")
etiket9.pack()


#secim butonu (radiobutton)
def radiobutton_kullan():
    print(radiobutton_durumu.get())

#radio butonunun değerini tutan değişken(0: kapalı, 1: açık)
radiobutton_durumu = IntVar()
secenek1 = tk.Radiobutton(text= "koyu tema", value= 1, variable= radiobutton_durumu, command= radiobutton_kullan)
secenek2 = tk.Radiobutton(text= "acik tema", value= 2, variable= radiobutton_durumu, command= radiobutton_kullan)
radiobutton_durumu.get()
secenek1.pack()
secenek2.pack()



pencere.mainloop() #pencerenin açık kalmasını sağlar. 


