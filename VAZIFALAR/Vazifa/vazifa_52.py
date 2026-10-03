def parol(passwort):
    """ Parol kuchliligini tekshirish """
  
    if len(passwort) < 6 :
        return ("Passwort juda zaif")
    if len(passwort) >= 8 and any(belgi.isdigit() for belgi in passwort):
        return "Kuchli parol"
    return "O'rtacha parol. Kchli parol uchun raqamlar va belgi qo'shish tafsiya etiladi"

pa = input("Passwortingizni tekshiring \n>>> ")
print(parol(pa))
                                  