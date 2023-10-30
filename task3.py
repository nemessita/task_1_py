# İstifadəçidən 3 ədəd rəqəm alın ve ən böyük rəqəmi ekrana yazdırın.
    # -----------------------------------------------
# sayi1 = int(input("Birinci rəqəmi daxil edin: "))
# sayi2 = int(input("İkinci rəqəmi daxil edin: "))
# sayi3 = int(input("Üçüncü rəqəmi daxil edin: "))


# if sayi1 >= sayi2 and sayi1 >= sayi3:
#     en_buyuk = sayi1
# elif sayi2 >= sayi1 and sayi2 >= sayi3:
#     en_buyuk = sayi2
# else:
#     en_buyuk = sayi3

# print("Ən böyük rəqəm:", en_buyuk)
    # -----------------------------------------------
a = int(input())
b = int(input())
c = int(input())
if a>b and a>c:
    print(a)
elif b>a and b>c:
    print(b)
else:
    print(c)
