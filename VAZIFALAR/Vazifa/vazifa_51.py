def parol (parol):
    """ Parol kuchliligini tekshirish """

    if len(parol) < 6:
        return "Juda qisqa va zaif parol"

    if len(parol) >= 8 and any(belgi.isdigit() for belgi in parol):
        return "Kuchli parol"

    return "O'rtacha parol, raqamlar qo'shish tavsiya etiladi"


print(parol("admin"))
print(parol("parol2026"))
print(parol("salomlar"))
print(parol("salom1"))
