# Bir sayı eğer 4 basamaklı ise ve oluşturan rakamlardan herbirinin 4. 
# kuvvetinin toplamı( 3 basamaklı sayılar için 3.kuvveti ) o sayıya eşitse 
# bu sayıya "Armstrong" sayısı denir.
# Örnek olarak : 1634 = 1^4 + 6^4 + 3^4 + 4^4

a = input("Bir sayı giriniz : ")

basamak = len(a)
toplam = 0
print("Basamak sayısı : ", basamak)
for i in a:
    
    x = int(i) ** basamak
    print((int(i)),  " ^^ " , basamak, " = ", x)
    toplam += x
print("Toplam : ", toplam)
if toplam == int(a):
    print ("Girdiğiniz sayı armstrong sayısıdır")

else:
    print("Armstrong sayısı değildir")

