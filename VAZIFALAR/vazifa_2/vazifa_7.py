dol = float(input("Dollor sumasini kiriting: "))
su = float(input("1 dollor qancha  Misol: 12850\n>> "))
ko = float(input("Komisiya % summasini kiriting \n Misol: 3\n>> "))

pu = dol * su
kom = pu * ko / 100
qo = pu - kom


pul =int(qo)

print ("Jami so'm ", pu)
print(f"{kom} komisiya biln {pul} So'm qoldi ")

