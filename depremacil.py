
admin= "yetkili"
sifre= "123456"

user=  "pearl"
password="3001"

adsoyList=[]
usernameList=[]
parolaList=[]


print("""
      *******Deprem Acil Uygulamasına Hoşgeldiniz.*******
      Uygulama adminiyseniz 1i kullanıcıysanız 2yi üye olmak için 3ü tuşlayınız.""")

giris= input("Tuşlama yapınız:")


# Uygulamada admin girisine gerek yok ama eklenmesi gerektiğini belirtilmis ödevde

if giris=="1":
        print("Admin girisine hosgeldiniz.")
       
        kullanici = input("Kullanıcı adınızı giriniz.")
        parola = input("Şifrenizi giriniz:")    
    
        if kullanici == admin and parola == sifre:
            print("Sistem girişi başarılı hoşgeldiniz.")
    
 #listeden veri kullanmayı ogrendigimde kullanıcı girisi
 #liste elemanları kullanılarak gerceklestirilecektir.
   
elif giris=="2":
        print("Kullanıcı girisine hosgeldiniz.")
            
        kullanici = input("Kullanıcı adınızı giriniz:")
        parola = input("Şifrenizi giriniz:") 
            
        if kullanici == user and parola == password:
            print("Kullanıcı girişi başarılı hoşgeldiniz.")

    
elif giris=="3":
        print("Kayıt olma girisine hosgeldiniz.")
        
       # kullanıcıdan gerekli verileri topluyoruz 
AdSoyad=input("Adınızı ve Soyadınızı giriniz:")
username=input("İstediğiniz kullanıcı adını giriniz:")
parola=input("Parolanızı giriniz:")
adsoyList.append(AdSoyad)
usernameList.append(username)
parolaList.append(parola)
print("Kayıt gerçekleştirildi.")  
           
    # Kullanıcıdan bilgileri alma
isim_soyisim = input("İsim ve soyisim: ")
aile_ferdi = input("Aile ferdi bilgisi: ")
konum = input("Konum bilgisi: ")
hastalik = input("Kronikleşmiş hastalık bilgisi: ")
kan_grubu = input("Kan grubu bilgisi: ")
allerji = input("Allerji bilgisi: ")
engel = input("Fiziksel/zihinsel engel bilgisi: ")
ilac = input("Sürekli kullanılan ilaç bilgisi: ")

#  sözlük yapısı
kullanici_bilgileri = {
    "İsim ve Soyisim": isim_soyisim,
    "Aile Ferdi Bilgisi": aile_ferdi,
    "Konum Bilgisi": konum,
    "Kronikleşmiş Hastalık Bilgisi": hastalik,
    "Kan Grubu Bilgisi": kan_grubu,
    "Allerji Bilgisi": allerji,
    "Fiziksel/Zihinsel Engel Bilgisi": engel,
    "Sürekli Kullanılan İlaç Bilgisi": ilac
}

# verileri depoluyoruz
dosya_adi = "kullanici_bilgileri.txt"
with open(dosya_adi, "w") as dosya:
    for bilgi, deger in kullanici_bilgileri.items():
        dosya.write(bilgi + ": " + deger + "\n")
        
        
  #uygulamanın bu noktada yapması gereken şey  internetten sürekli veri alıp, depremin yıkıcı olasılığını analiz eder ve sıkıntılı bir deprem durumunda acil durum bildirisi gönderir.
 #ancak internetten veri alınmasının kodunu bilmedigim icin internetten yardım aldım

#import requests
#def veri_al():
    # Verileri internetten almak için uygun bir API kullanabilirsiniz
   # response = requests.get("https://api.example.com/deprem_verileri")
    #veriler = response.json()
    #return veriler
    
    # burda depremin büyüklüğü ve yıkıcılığı hakkında analiz yapılması ve analize bağli acil bildirinin gönderilmesi kodu gereklidir
    
def acil_durum_bildirisi():
    print("ACİL DURUM BİLDİRİSİ")
    print("Olası bir deprem faciası tespit edildi. Durumunuzu bildirmek için aşağıdaki seçeneklerden birini seçin:")


secenekler = {
    "1": "ENKAZ ALTINDAYIM",
    "2": "Depremzedeyim ve yaralıyım",
    "3": "Depremzedeyim ama sağlık durumum yok",
    "4": "Depremi yaşamadım"
}

print("Durumunuzu belirtin:")
for secenek in secenekler:
    print(secenek + ": " + secenekler[secenek])

secim = input("Seçiminizi yapın (1-4): ")

if secim in secenekler:
    durum = secenekler[secim]
    if durum == "ENKAZ ALTINDAYIM":
        print("Acil yardım ekiplerini bilgilendirilecektir. Lütfen sakin olun ve mümkün olduğunca bekleyin.")
    elif durum == "Depremzedeyim ve yaralıyım":
        print("Acil yardım ekiplerine bilgilendirilecektir. Lütfen yerinizde kalın ve mümkün olduğunca hareket etmeyin.")
    elif durum == "Depremzedeyim ama sağlık durumum yok":
        print("Acil yardım ekiplerini bilgilendireceğim. Lütfen sakin olun ve en yakın güvenli noktada bekleyin.")
    elif durum == "Depremi yaşamadım":
        print("Lütfen güvenli bir yerde kalın ve telefon hatlarını meşgul etmeyin.")
else:
    print("Geçersiz bir seçim yaptınız. Lütfen geçerli bir seçenek numarası girin.")













