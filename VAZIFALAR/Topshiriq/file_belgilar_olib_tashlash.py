def joy(n):
    sozi = ""
    sozlar1 = ""
    for i in n.lower():
        if i != " " and i != "\n":
            if i != "?" and i != "." and i != "!" and i != ',' and i !="\"" and i != "\'":
               sozi += i
            elif i == "\'":
                if sozi != "" and (sozi[-1] == "a" or  sozi[-1] == "o" or  sozi[-1] == "g"):
                    sozi += i
                
        elif i == " " or i == "\n":
            if sozi != "":
                sozlar1 += sozi + " "
            sozi = ""
    return sozlar1

with open("matin.txt", "r") as file:
    sozlar = file.read()
    print("Sozlar o'qildi: ", sozlar)
    print(40*"-")
    sozlar = joy(sozlar)
    print("Sozlar joy funksiyasidan keyin: ", sozlar)
    print(40*"-")
    # sozlar = belgi(sozlar)
    # print("Sozlar belgi funksiyasidan keyin: ", sozlar)
print(sozlar,"\n")
# st = ""
# for i in sozlar:
#     st += f"{i} "
# print(st)


# with open("yangi_matin.txt", "w") as file:
#     file.write(sozlar)