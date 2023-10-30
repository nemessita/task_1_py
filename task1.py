#Kimdir

# Aslan -> Aslan emi ogludur
# Imran -> Imran dayi ogludur
# Afaq -> Afaq bibi qizidir
# Uzeyir -> Uzeyir xala ogludur
# Shahin -> Shahin yaxin dostdur

# Ad daxil edin:
# Aslan

# Aslan emi ogludur
# Ad daxil edin:
# Afaq
# Afaq bibi qizidir
# Ad daxil edin:
# Siz ad daxil etmediniz
# Ad daxil edin:
# Murad
# Murad kimdir? Men onu tanimadim

# ----------------------------------------------------------
# sira = {
#     "Aslan": "Aslan emi ogludur",
#     "Imran": "Imran dayi ogludur",
#     "Afaq": "Afaq bibi qizidir",
#     "Uzeyir": "Uzeyir xala ogludur",
#     "Shahin": "Shahin yaxin dostdur"
# }

# ad = input("Ad daxil edin: ")

# if ad:
#     if ad in sira:
#         print(sira[ad])
#     else:
#         print(f"{ad} kimdir? Men onu tanimadim")
# else:
#     print("Siz ad daxil etmediniz")

    # ---------------------------------------------------
    
ad = input("Ad daxil edin: ")
if ad=="Aslan" or ad=="aslan":
    print("Aslan emi ogludur") 
elif ad=="Imran" or ad=="imran":
    print("Imran dayi ogludur")
elif ad=="Afaq" or ad == "afaq":
    print("Afaq bibi qizidir")
elif ad == "Uzeyir" or ad=="uzeyir":
    print("Uzeyir xala ogludur")
elif ad == "Shahin" or ad=="shahin":
    print("Shahin yaxin dostdur")
else:
    print(ad," kimdir? Men onu tanimadim")
