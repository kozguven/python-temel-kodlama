print("**********ÇARPIM TABLOSU******************")
sayilar = list(range(1, 10))
print (sayilar)
for i in sayilar:
    for x in sayilar:
        print("{} * {} = {}".format(i, x, i*x))

