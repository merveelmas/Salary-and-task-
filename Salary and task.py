class Personel:
    def __init__(self,ad,soyad,yas,maas):
        self.ad=ad
        self.soyad=soyad
        self.yas=yas
        self.maas=maas
        print("Personel Çalışmaya başladı")

    def bilgi(self):
        print(f"{self.ad} {self.soyad} {self.yas} {self.maas}")

    def zam(self):
        return self.maas*1.2

class BilgiIslem(Personel):
    def __init__(self,ad,soyad,yas,maas,gorev):
        super(). __init__(ad,soyad,maas,gorev)
        self.gorev=gorev
        print("Bilgi İşlem Çalışmaya başladı")
    def bilgi(self):
        print(f"{self.ad} {self.soyad} {self.yas}  {self.gorev} bilgi işlemde çalışan ve {self.maas} TL maaş alıyor ")

    def zam(self):
        return self.maas*1.5


class Yonetim(Personel):
    def __init__(self, ad, soyad, yas, maas, birim):
        super().__init__(ad, soyad, maas, birim)
        self.birim = birim
        print("Yönetim Personel Çalışmaya Başladı")
    def bilgi(self):
        print(f" {self.ad} {self.soyad} {self.birim} görevinde ve {self.maas} maas alan bir yöneticidir.")

    def zam(self):
         return self.maas * 1.5



class Hizmetli(Personel):
    def __init__(self,ad,soyad,yas,maas):
        super(). __init__(ad,soyad,yas,maas)
        print("Hizmetli Personel Çalışmaya Başladı")

    def bilgi(self):
        print(f"{self.ad} {self.soyad} {self.maas} Tl maas bir hizmetli Personelidir.")

    def zam(self):
        return self.maas*3


personel=Personel("Yesim ","Demir" ,40,5000)
print(personel.ad,personel.soyad,personel.yas,personel.maas)

bilgiislem=BilgiIslem("Hakan","Asar",35,5000,"Yazılım")
yonetici=Yonetim("Kemal","Deniz",55,7500,"Müdür")
hizmetli=Hizmetli("Hülya","Demir",25,5000)

print("-----------Bilgi İşlem----------------------")

bilgiislem.bilgi()
print("Bilgi İşlem Maaş:", bilgiislem.zam(),"TL")

print("-----------Yönetim------------------------")

yonetici.bilgi()
print("Yönetici Maaşı:",yönetici.zam(),"TL")

print("-----------Hizmetli------------------------")

hizmetli.bilgi()
print("Hizmetli Maaşı:",hizmetli.zam(),"TL")