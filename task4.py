# İstifadəçidən alınan məlumatlara uyğun olaraq bədən kütlə indeksini hesablayın.

#  Bədən Kütle İndeksi(BKİ): Kütlə / Boy(m) *  Boy(m)

#  BKİ 18.5'un altındadırsa -------> Zəif

#  BKİ 18.5 ile 25 arasındadırsa ------> Normal

#  BKİ 25 ile 30 arasındadırsa --------> Kilolu

#  BKİ 30'un üstündədirsə -------------> Obez


# Boyunuzu Daxil edin:1.74
# Kütləni Daxil edin:76
# Normal

# ---------------------------------------------------
boy = float(input("Boyunuzu Daxil edin (metr): "))
kilo = float(input("Kütləni Daxil edin (kilogram): "))

bki = kilo / (boy ** 2)

if bki < 18.5:
    index = "Zəif"
elif 18.5 <= bki < 25:
    index = "Normal"
elif 25 <= bki < 30:
    index = "Gombul"
else:
    index = "Obez"
print(index)
# ---------------------------------------------------
# boy = float(input("Boyununuz daxil edin:"))
# kutle = float(input("Kutlenizi daxil edin:"))
# bmi = kutle/(boy*boy)
# if bmi<18.5:
#     print("Zəif")

# elif 18.5<bmi<25:
#     print("Normal")
# elif 20<bmi<30:
#     print("kiloli")
# elif 30<bmi:
#     print("Obez")