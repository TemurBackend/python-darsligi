balance = 1000000

while True:
    # Bank
    print("\n1. Balansni ko'rish")
    print("2. Pul yechish")
    print("3. Pul qo'shish")
    print("0. Chiqish")

    bel = input("Buyruqni kiriting: ")

    if bel == "1":
         print('Sizning balansingiz', balance)
    elif bel == "2":
         pul = int(input("Yechiladigan pul miqdori: "))
         
         if balance < pul:
             print("Mablag' yetarli emas")
         else:
             balance -= pul
             print("Pul yechildi.")
             print("Qolgan balans:", balance)
             
    elif bel == "3":
        pul = int(input("Qo'shiladigan pul miqdori: "))
        balance += pul
        print("Balans to'ldirildi.")
        print("Yangi balans: ", balance)
        
    elif bel == "0":
        print("Dastur tugatildi")
        break
    else:
        print("Bunday buyruq mavjut emas!! ")
