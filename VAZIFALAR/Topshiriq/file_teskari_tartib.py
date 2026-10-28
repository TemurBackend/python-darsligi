
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
 

with open('matin.txt', 'r') as file:
    with open('yangi_matn.txt', 'w') as yangi_file:
        while True:
            sozlar = file.readline()
            if not sozlar:
                break

            sozlar = joy(sozlar)
            soz = []

            for i in sozlar:
                soz.insert(0,i)
            print(soz)

            for i in soz:
                yangi_file.write(f"{i} ")
            yangi_file.write("\n")


    








