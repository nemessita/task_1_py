# Bir eded listimiz var adlardan ibaret
# Ad daxil edin (1)
# Ad Bazaya ugurla elave olundu 
# error mesajlari: Ad daxil etmediniz , Ad cox uzundur maksimum 15 herf
# --------------------------------------
ad_listesi = []

while True:
    ad = input("Ad daxil edin: ")
    if not ad:
        print("Error: Ad daxil etmediniz")
        continue
    if len(ad) > 15:
        print("Error: Ad çox uzundur, maksimum 15 hərfə icazə verilir")
        continue
    ad_listesi.append(ad)
    print("Ad Bazaya ugurla elave olundu")
    # -------------------------

    adlar=[]
ad = input()
if ad =="":
    print("Ad daxil etmediniz")
elif len(ad)>15:
    print("Ad cox uzundur maksimum 15 herf")
else:
    adlar.append(ad)
    print("Ad Bazaya ugurla elave olundu ")
