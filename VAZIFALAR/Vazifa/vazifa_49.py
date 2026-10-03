def kaloriya (mashq, daqiqa):
    """ Mashg'ulot davomida sarflangan kaloriyani hisoblaydi """
    kaloriya = {
        "yugurish": 10,
        "suzish": 8,
        "velosiped": 6
    }
    if mashq not in kaloriya:
        return "Noto'g'ri mashq turi kiritildi! "

    sarf = kaloriya[mashq] * daqiqa
    return f"{daqiqa} daqiqa {mashq} mashg'ulotida {sarf} kkal energiya sarflandi."

mashq = input('yugurish, suzish, velosiped \n "Mashq tanlang": ')
vaqt = int(input('"Vaqt kiriting"'))

print(kaloriya(mashq, vaqt))

print(kaloriya.__doc__)
