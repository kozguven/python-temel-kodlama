print("********FAKTORİYEL BULMA**********")
print("Çıkmak için q ya basınız")


while True:
    sayı = input("Faktoriyel bulunacak sayıyı giriniz : ")
    if sayı == "q":
        print("Çıkış yaptınız")
        break
    else:
        sayı = int(sayı)

        faktoriyel = 1

        for i in range(2, sayı + 1):
            faktoriyel *= i
        print("Faktoriyel :", faktoriyel)



        