login = input("Loginni kiriting: ")
parol = input("Parolni kiriting: ")

if login == "admin" and parol == "12345":
    print("Tizimga kirdingiz")
elif login != "admin":
    print("Login noto‘g‘ri")
else:
    print("Parol noto‘g‘ri")