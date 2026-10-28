
def joy(n):
    sozi = ""
    sozlar1 = []
    for i in n:
        if i != " " and i != "\n":
            sozi += i
        elif i == " " or i == "\n":
            if sozi == "":
                continue
            sozlar1.append(sozi)
            sozi = ""
    return sozlar1
 

with open('matin.txt', 'r') as file :
    sozlar = file.read()
    sozlar = joy(sozlar)



def tekshir(n):
    if len(n) == 1:
        return n[0], n[0]

    min1, max1 = tekshir(n[1:])

    if n[0] < min1:
        min1 = n[0]

    if n[0] > max1:
        max1 = n[0]

    return min1, max1

ol = []
jam = 0
for soz  in sozlar:
    jam += 1
    uz = len(soz)
    ol.append(uz)
    with open('yangi_matn.txt', 'a') as file:
        file.write(f"{soz}-{uz}\n")
             
na = tekshir(ol)        
        

for n in sozlar:
    if len(n) == na[0]:
        print(f"{n} {na[0]}")
        with open('yangi_matn.txt', 'a') as file:
            file.write(f"Minimum; {n}-{na[0]}\n")
    elif len(n) == na[1]:
        print(f"{n} {na[1]}")
        with open('yangi_matn.txt', 'a') as file:
            file.write(f"Maksimum; {n}-{na[1]}\n")
            file.write(f"Jami sozlar {jam}")
