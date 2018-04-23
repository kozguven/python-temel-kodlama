print(
    """
    **************************
    Atm Makinesine hoşgeldiniz
    **************************
    İşlemler:

    1-Bakiye Sorgulama
    2-Para Yatırma
    3-Para Çekme

    Programdan çıkmak için 'q' ya basınız
    **************************
    """
)
bakiye = 1000
while True:
    işlem = input("İşlemi seçiniz : ")
    if(işlem == "q"):
        print("Yine bekleriz")
        break
    elif(işlem == "1"):
        print("Bakiyeniz {} TL dir".format(bakiye))
    elif işlem == "2":
        miktar = int(input("Yatırmak istediğini Miktarı Giriniz : "))
        bakiye += miktar
    elif işlem == "3":
        miktar = int(input("Çekmek istediğiniz miktarı girin : "))
        if(bakiye - miktar < 0):
            print("Böyle bir miktar çekemezsiniz")
            continue
        bakiye -= miktar
    else:
        print("Geçersiz işlem")
        
        
