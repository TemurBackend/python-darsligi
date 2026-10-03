pro = ["PRO", "SUPPER", "MAX", "YANGI", "ALI", "ASSD", "ABBO", "AKE", "ASL", "CHAY", "NEW"]

def chegirma(narx, foiz, promo=""):
    """ Chegir ma uchun ishlatiladigan funksiya """
    chegirma = narx * foiz / 100
    pul = narx - chegirma

    if promo == pro[1]:
        pul = pul * 0.95

    return round(pul,2)


print(f"Proma kodlar\n{pro}")
nar = int(input("Narhini kiriting:"))
fo = int(input('foyizini kiriting %:'))
po = input("Proma kod kiriting! yokida 0 kiriting n>>")

tol = chegirma(nar,fo,promo=po)
print(tol)