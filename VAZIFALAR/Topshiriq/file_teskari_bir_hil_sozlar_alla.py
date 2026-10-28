f = open("matin.txt", "r")
g = open("yangi_matn.txt", "w")

for soz in f:
    soz = soz.strip()
    kichik = soz.lower()
    pal = True



    for i in range(len(kichik) // 2):
        if kichik[i] != kichik[len(kichik) - 1 - i]:
            pal = False
            break

    if pal:
        g.write(soz + "\n")




f.close()
g.close()




