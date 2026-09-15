
ism = input("Mijoz ismini kiriting: ").strip().title()
xona_turi = input("Xona turini kiriting: ").strip().title()


kunlik_narx = 450_000
kunlar = 3
tozalash = 50_000


turar_joy = kunlik_narx * kunlar

jami = turar_joy + tozalash


print("\n---------- MEHMONXONA BRON HUJJATI ----------")
print(f"Mijoz: {ism}")
print(f"Xona turi: {xona_turi}")
print(f"Kunlik narx: {kunlik_narx:,} so'm")
print(f"Yashash muddati: {kunlar} kun")
print("----------------------------------------------")
print(f"Turar joy summasi: {turar_joy:,} so'm")
print(f"Tozalash xizmati: {tozalash:,} so'm")
print("----------------------------------------------")
print(f"JAMI TO'LOV: {jami:,} so'm")
print("----------------------------------------------")
