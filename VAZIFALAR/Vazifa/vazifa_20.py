
ism = input("Talabaning ismini kiriting: ").strip().title()
fam = input("Talabaning familiyasini kiriting: ").strip().title()


ballar = [85, 90, 78, 92]


jami = ballar[0] + ballar[1] + ballar[2] + ballar[3]


ort = jami / 4

print("\n----------Talaba anketaasi-----------")
print(f"Ism: {ism}")
print(f"Familiya: {fam}")
print("--------------------------------------")
print(f"1-fan: {ballar[0]} ball")
print(f"2-fan: {ballar[1]} ball")
print(f"3-fan: {ballar[2]} ball")
print(f"4-fan: {ballar[3]} ball")
print("--------------------------------------")
print(f"Jami ball: {jami}")
print(f"O'rtacha ball: {ort}")
print("---------------------------------------")