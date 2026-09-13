
ism = input("Yo'lovchining ismini kiriting: ").strip().title()

otirish_narxi = 6000
km_narxi = 2500
kutish_narxi = 500


masofa = 12
kutish_vaqti = 8


masofa_narxi = masofa * km_narxi
kutish_puli = kutish_vaqti * kutish_narxi

jami = otirish_narxi + masofa_narxi + kutish_puli


print("\n----------- TAKSI KVITANSIYASI----------")
print(f"Yo'lovchi: {ism}")
print("-----------------------------------------")
print(f"O'tirish narxi: {otirish_narxi:,} so'm")
print(f"Masofa: {masofa} km × {km_narxi:,} = {masofa_narxi:,} so'm")
print(f"Kutish: {kutish_vaqti} min × {kutish_narxi:,} = {kutish_puli:,} so'm")
print("-----------------------------------------")
print(f"Jami yo'l haqi: {jami:,} so'm")
print("-----------------------------------------")