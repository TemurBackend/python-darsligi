katakcha1 = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

player1 = input("Birinchi o'yinchi ismingizni kiriting: ")

player2 = input("Ikkinchi o'yinchi ismingizni kiriting: ")

navbat = 1

tugadi = False
toldi = 0

def katakcha(katakcha):
    print("┌─────┬─────┬─────┐")
    print(f"│  {katakcha[0]}  │  {katakcha[1]}  │  {katakcha[2]}  │")
    print("├─────┼─────┼─────┤")
    print(f"│  {katakcha[3]}  │  {katakcha[4]}  │  {katakcha[5]}  │")
    print("├─────┼─────┼─────┤")
    print(f"│  {katakcha[6]}  │  {katakcha[7]}  │  {katakcha[8]}  │")
    print("└─────┴─────┴─────┘")


x = 0
O = 0

qayta = True


while qayta:
    while True:
        katakcha(katakcha1)
        if tugadi:
            break
        if navbat == 1:
            print(f"{player1} X sizning navbatingiz, katakchalardan birinini tanlang: ")
        elif navbat == 2:
            print(f"{player2} O sizning navbatingiz, katakchalardan birinini tanlang: ")
        tanlangan_katak = int(input(""))-1
        t = tanlangan_katak
        
        if katakcha1[tanlangan_katak] in ["X", "O"]:
            print("Bu joy band. Boshqa joy tanlang!")
            continue
        toldi+=1
        if navbat == 1:
            katakcha1[tanlangan_katak] = "X"
    
            x_o = "X"
        elif navbat == 2:
            katakcha1[tanlangan_katak] = "O"
            x_o = "O"
          
    
        
        if ((katakcha1[0] == x_o and katakcha1[1] == x_o and katakcha1[2] == x_o) or (katakcha1[0] == x_o and katakcha1[4] == x_o and katakcha1[8] == x_o) or (katakcha1[0] == x_o and katakcha1[3] == x_o and katakcha1[6] == x_o) ):
            if navbat == 2:
                O += 1
                print(f"Tabriklaymiz {player2} siz g'olib bo'ldingiz!")
            elif navbat == 1:
                print(f"Tabriklaymiz {player1} siz g'olib bo'ldingiz!")
                x += 1
            tugadi = True
        
        elif (katakcha1[1] == x_o and katakcha1[4] == x_o and katakcha1[7] == x_o):
            if navbat == 1:
                x += 1
                print(f"Tabriklaymiz {player1} siz g'olib bo'ldingiz!")
            elif navbat == 2:
                O += 1
                print(f"Tabriklaymiz {player2} siz g'olib bo'ldingiz!")
            tugadi = True
        
        elif (katakcha1[2] == x_o and katakcha1[4] == x_o and katakcha1[6] == x_o) or (katakcha1[2] == x_o and katakcha1[5] == x_o and katakcha1[8] == x_o):
            if navbat == 1:
                x += 1
                print(f"Tabriklaymiz {player1} siz g'olib bo'ldingiz!")
            elif navbat == 2:
                O += 1
                print(f"Tabriklaymiz {player2} siz g'olib bo'ldingiz!")
            tugadi = True
        
        elif (katakcha1[3] == x_o and katakcha1[4] == x_o and katakcha1[5] == x_o):
            if navbat == 1:
                x += 1
                print(f"Tabriklaymiz {player1} siz g'olib bo'ldingiz!")
            elif navbat == 2:
                O += 1
                print(f"Tabriklaymiz {player2} siz g'olib bo'ldingiz!")
            tugadi = True
        
        elif (katakcha1[6] == x_o and katakcha1[7] == x_o and katakcha1[8] == x_o):
            if navbat == 1:
                x += 1
                print(f"Tabriklaymiz {player1} siz g'olib bo'ldingiz!")
            elif navbat == 2:
                O += 1
                print(f"Tabriklaymiz {player2} siz g'olib bo'ldingiz!")
            tugadi = True
        

        if toldi == 9 and tugadi == False:
            print("Durrang")
            tugadi = True
       
        
        if navbat == 1:
            navbat = 2 
        else:
            navbat = 1  
        
    oyn = input("Yana oynaysizmi ha\\yoq\n>>")
    
    if oyn == "ha":
        tugadi = False
        toldi = 0
        navbat = 1
        katakcha1 = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    elif oyn == "yoq":
        print(f"{player1} {x} ball to'pladi\n"
              f"{player2} {O} ball to'pladi")
        if O > x :
            print(f"{player2} {O} ball bilan g'alaba qazondi")
        elif x > O:
            print(f"{player1} {x} ball bilan g'alaba qazondi")
        else:
            print("Natija durrang")
        qayta = False
  