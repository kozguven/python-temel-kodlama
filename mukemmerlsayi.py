#kendisi hariç tam bölünen sayıların toplamı kendisine eşit olan sayıya mükemmel sayı denir
a = int(input("Bir sayı giriniz : "))
sayılar = list()
toplam = 0

for i in range(1, a-1):
    
    if(a % i == 0):
        sayılar.append(i)
print(sayılar)

for i in sayılar:
    toplam += i
print("toplam ", toplam)
if(toplam == a):
    print("Sayınız mükemmler bir sayıdır")
else:
    print ("Sayı mükkemmel değildir")
        
