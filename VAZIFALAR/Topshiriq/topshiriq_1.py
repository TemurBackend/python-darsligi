# vavifa 1
ism = input("Ismingizni kiriting: \n>>> ")
ism = ism.capitalize() .strip()
fam = input ("Familiyangizni kiriting: \n>>> ")
fam  = fam.capitalize() .strip()
kor = input("Korhonangiz nomini kiriting: \n>>> ")
kor  = kor.capitalize() .strip()
print (ism, fam )
print ("n.\n.\n.\n.\n.")
ser = input("Pasport seriyangizni harifini kiriting \n>>> Masalan: AB \t>>> ")
ser = ser.upper().strip()

raq = input("Pasport seriyangizni kiriting \n>>> Masalan: 1223456 \t>>> ")
print (f"Sizning seriya raqamingiz, {ser}-{raq} ")

print ("n.\n.\n.\n.\n.")
usr = input("Telagram foydalanuvchi nomingizni kiriting:\n>>> ")
usr = usr.lower().strip()
link = "https://t.me/" + usr
    
print (f"Telagram linkingiz, {link}") 
print ("n.\n.\n.\n.\n.")
mism = input("Mijoz ismi:\n>>>")
mism = mism.capitalize() .strip()
mnom = input("Buyurtma qilmoqchi bo'lgan mahsulotingiz nomi:\n>>> ")
mnom = mnom.capitalize() .strip()
vaqt = input("Yetkazib berish vaqtini kiriting, Misol: 2026.12.12 12:12 \n>>>")

print ("Yetkazib berishi Malumot""mijoz ismi: ", mism )
print (" Buyurtma qilgan maxsulot nomi:",  mnom )
print (" Yetkazib berish  :",  vaqt )
print ("Buyurtma malumoti qabul qilindi")
print ("n.\n.\n.\n.\n.")
mam = input("Davlatingizni kiriting: ")
vil = input("Viloyatingizni kiriting: ")
tum = input("Tumaningizni kiriting: ")
mf = input ("MFY kiriting: ")
uy = input ("uy raqamini kiriting: ")
print ("n.\n.\n.\n.\n.")
print (f"Assalomu alekum, {ism} {fam} Siz {mism } yuborgan \n {mnom} buyurtmangiz\n {vaqt} vaqtida bu \nMnzil:{mam},{vil},{tum},\n{mf},{uy} ga yettib boradi" )


print ("n.\n.\n.\n.\n.")

gim = input ("Email ni kiriting: ")
log = input ("loginni kiritin: ")
logi = (len(log))
print ("n.\n.\n.\n.\n.")

print ("Sizning email pochtangiz:",gim )
print ("Sizning loginingiz: ",logi*"*")
print ("n.\n.\n.\n.\n.")
kom = input("Kompaniya shiorini kiriting: ")
kom = kom.upper().strip()
print ("_" * (len(kom) + 4))
print ("|",kom , "|")
print ("_" * (len(kom) + 4))

























