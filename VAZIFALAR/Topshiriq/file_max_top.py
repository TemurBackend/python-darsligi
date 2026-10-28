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
    
def anqla(lis,n):
    qa = 0
    for i in range(len(lis)):
        if n == lis[i]:
            qa += 1
    return qa

def tekshir(a, soz):
    for element in a:
        if element == soz:
            return  False

    return True

def max_top(n):   
    if len(n) == 1 : 
        return n[0] 
    max_qolgan = max_top(n[1:])
    if n[0] > max_qolgan: 
        return n[0]
    else:
        return max_qolgan
    
soz = []
for i in sozlar:
    if tekshir(soz,i):
        soz.append(i)



sa = []
lu = {}
for i in soz:
    s = anqla(sozlar, i)
    sa.append(s)  
    lu[i] = s
    
d = max_top(sa)


for i in soz:
    if lu[i] == d:
        print(i)
        print(lu[i])


print(100*"=")
print(lu)
print(soz)
print(sa)
print(d)


# print(soz)
# print(lu[d])
# print(d)        
    



















