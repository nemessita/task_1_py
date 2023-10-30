# # Login:
# # test
# # Parol:
# # 12345

# Login və Parol Düzgündürsə # Xosh geldiniz
# Error Mesajları:
# - Login yanlishdir
# - Parol yanlishdir
# - Login ve parol yanlishdir
# - Login daxil etmediniz
# - Parol daxil etmediniz
# - Login ve parol daxil etmediniz
# -----------------------------------------------
# login = input("Login: ")
# parol = input("Parol: ")

# error_message = ""

# if not login:
#     error_message += "- Login daxil etmediniz\n"
# if not parol:
#     error_message += "- Parol daxil etmediniz\n"
# if login == "test" and parol == "12345":
#     print("Xosh geldiniz")
# elif login == "test" and parol != "12345":
#     error_message += "- Parol yanlishdir\n"
# elif login != "test" and parol == "12345":
#     error_message += "- Login yanlishdir\n"
# else:
#     error_message += "- Login ve parol yanlishdir\n"

# if error_message:
#     print("Error Mesajları:")
#     print(error_message)
# else:
#     print("# Xosh geldiniz")
    # -----------------------------------------------
login = "test"
parol = 12345
login2 = input()
parol2 = int(input())
if(login2!=login and parol==parol2):
    print("Login yanlishdir")
elif(login2==login and parol!=parol2):
    print("Parol yanlishdir")
elif(login2!=login and parol!=parol2):
    print("Login ve parol yanlishdir")
elif(login2=="" and (parol==parol2 or parol!=parol2)):
    print("Login daxil etmediniz")
elif(parol2=="" and (login==login2 or login!=login2)):
    print("Parol daxil etmediniz")
else:
    print("Login ve parol daxil etmediniz")