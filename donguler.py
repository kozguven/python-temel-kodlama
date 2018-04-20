print("""
*******************************
Kullanıcı Girişi Programı
*******************************
"""
)

sys_kullanıcı_adı = "kerem"
sys_parola = "1234"
giriş_hakkı = 3

while True:
    kullanıcı_adı = input("Kullanıcı adı : ")
    parola = input("Parola :")
    if (kullanıcı_adı != sys_kullanıcı_adı and parola == sys_parola):
        print("Kullanıcı Adı Hatalı")
        giriş_hakkı -= 1
    elif (kullanıcı_adı == sys_kullanıcı_adı and parola != sys_parola):
        print("Parola Hatalı...")
        giriş_hakkı -= 1
    elif(kullanıcı_adı != sys_kullanıcı_adı and parola != sys_parola):
        print("Kullanıcı adı ve şifre hatalı")
        giriş_hakkı -= 1
    else:
        print("Sisteme başarılı giriş yapıldı")
        break
    if (giriş_hakkı == 0):
        print("Giriş Hakkınız Bitti")
        break

print("işlemler tamam")
