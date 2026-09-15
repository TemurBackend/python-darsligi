yosh = int(input("Yoshingizni kiriting: "))

if yosh >= 0 and yosh <= 6:
    print("Bola")
elif yosh >= 7 and yosh <= 17:
    print("O‘quvchi")
elif yosh >= 18 and yosh <= 59:
    print("Katta")
elif yosh >= 60:
    print("Katta yoshli")
else:
    print("Noto‘g‘ri yosh")