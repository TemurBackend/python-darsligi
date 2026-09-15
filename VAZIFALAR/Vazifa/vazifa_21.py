
shah = input("Sayohat qilinadigan shaharni kiriting: ").strip().title()


meh = float(input("Mehmonxona xarajati: "))
chip = float(input("Chipta xarajati: "))
ov = float(input("Ovqatlanish xarajati: "))
tr = float(input("Transport xarajati: "))


xar = [meh, chip, ov, tr]


jami = xar[0] + xar[1] + xar[2] + xar[3]


kunlik = jami / 5


print("\n----------SAYOHAT BYUDJETI ----------")
print(f"Shahar: {shah}")
print(f"Mehmonxona: {xar[0]} so'm")
print(f"Chipta: {xar[1]} so'm")
print(f"Ovqatlanish: {xar[2]} so'm")
print(f"Transport: {xar[3]} so'm")
print("---------------------------------------")
print(f"Umumiy xarajat: {jami} so'm")
print(f"5 kun uchun kunlik o'rtacha: {kunlik} so'm")
print("----------------------------------------")