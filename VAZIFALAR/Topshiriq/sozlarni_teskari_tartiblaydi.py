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
with open("matin.txt", 'r') as file:
    with open("yangi_matn.txt", "w") as yangi:
        while sozlar := file.readline():
            
            sozlar = joy(sozlar)
            soz = []
            
            for i in range(len(sozlar) - 1, - 1, - 1):
                soz.append(sozlar[i])
                yangi.write(f"{sozlar[i]} ")
            yangi.write("\n")






