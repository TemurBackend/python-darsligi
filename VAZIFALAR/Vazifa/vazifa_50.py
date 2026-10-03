def yetkazish (km, tez=False, shah="Namangan"):
    """ Yetkazib berish narxini hisoblaydi."""
    
    narx = km * 2500

    if tez:
        narx += 15000

    xizmat_turi = "tezkor yetkazib berish" if tez else "oddiy yetkazib berish"

    return f"{shah} shahri bo'ylab {xizmat_turi}: {narx:,} so'm"


sha = input('Shahar nomi kiriting: ')
kl = int(input('Km kiriting: '))
te = input("Tezkor kuryer kerak bolsa 0  \nOddi kuryer kerak bolssa 1  yuboring \n")
tr = 0
if te == "0":
    tr = True
else:
    tr = False
    
# print(yetkazish(7))

print(yetkazish(tez=tr, km=kl, shah=sha))

# print(yetkazish(shah=sha, km=kl, tez=tr))



