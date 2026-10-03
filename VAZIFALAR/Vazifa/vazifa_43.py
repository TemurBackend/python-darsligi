password = "python123"
son = 0 
while son < 3:
    parol = input('Passwordni kiriting')

    if parol == password:
        print("Xush kelibsiz!")
        break
    else:
        print("Noto'g'ri!\n")
    
    son += 1
    
    if son == 3:
        print("Siz parolni 3 marotaba  noto'g'ri kiritganingiz sababli bloklandingiz!")
