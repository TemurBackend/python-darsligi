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

def anqla(lis,n):
    qa = 0
    for i in range(len(lis)):
        if n == lis[i]:
            qa += 1
    return qa

with open('matin.txt', 'r') as file :
    sozlar = file.read()
    sozlar = joy(sozlar)



t = []
for i in sozlar:
    tak = anqla(sozlar, i)
    if tak == 1:
        t.append(i)

    
file = open('yangi_matn.txt', 'a')
file.write(f"takrorlanmagan sozlar: {t}\n") 
file.write(f"takrorlanmagan sozlar soni: {len(t)}\n")
file.write(f"Jami sozlar soni: {len(sozlar)}\n")

    
    
file.close()
print(t)
#    
#     
        
