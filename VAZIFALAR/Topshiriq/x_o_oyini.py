a = [" " for i in range(9)]

def son(n):
    if n.isdigit():
        return int(n)
    else:
        return son(input("Son kiriting: "))

tugadi = False

def katakcha():
    print("┌─────┬─────┬─────┐")
    print(f"│  {a[6]}  │  {a[7]}  │  {a[8]}  │")
    print("├─────┼─────┼─────┤")
    print(f"│  {a[3]}  │  {a[4]}  │  {a[5]}  │")
    print("├─────┼─────┼─────┤")
    print(f"│  {a[0]}  │  {a[1]}  │  {a[2]}  │")
    print("└─────┴─────┴─────┘")
    
def tekshirish(t):
    yutuqlar = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    for q in  yutuqlar:
        if a[q[0]] == a[q[1]] == a[q[2]] == t:
            return True
    return False

def oyin():
    belgi = "X"
    urunish = 0
    tugadi = False

    while tugadi == False:
        katakcha()
        print(belgi, "navbati")

        joy = son(input("Joy tanlang (1-9): ")) - 1

        if joy < 0 or joy > 8:
            print("1 dan 9 gacha son tanlang!")
            continue
        elif a[joy] != " ":
            print("Bu joy band! Boshqa joy tanlang.")
            continue

        a[joy] = belgi
        urunish += 1

        if tekshirish(belgi):
            katakcha()
            print(belgi, "G'olib bo'ldi")
            print("Jami yurishlar:", urunish)
            break

        if " " not in a:
            katakcha()
            print("Durrang!")
            break

        belgi = "O" if belgi == "X" else "X"

oyin()    

    
    
    
    
    