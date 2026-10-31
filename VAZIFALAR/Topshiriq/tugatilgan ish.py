def joy(n):
    belgilar = 0
    qatorlar = 1
    sozso = 0
    sozi = ""
    sozlar1 = []
    for i in n:
        if i != "\n":
           belgilar += 1
        if i == "\n":
            qatorlar += 1
        if i != " " and i != "\n" and i != "" and i != ".":
            sozi += i
        elif i == " " or i == "\n" or i == "" or i == ".":
            if sozi == "":
                continue
            sozlar1.append(sozi)
            sozi = ""
            sozso += 1
    if sozi != "":
        sozlar1.append(sozi)
        sozso += 1
        # sozi = ""   
        
    return sozlar1, sozso, qatorlar, belgilar

def uzun(n):
    uzu = 0 
    
    for i in n:
        uzu += 1
    return uzu

def olchami(g):
    n = uzun(g)
    
    a = 0 
    for i in range(n):
        x = 0
        for s in range(n):
            if uzun(g[a]) > uzun(g[x]):
                g[i], g[s] = g[s], g[i]
            x += 1
        a += 1
    return g    

def bitadan(n):
    li = []
    for soz in n:
        bor = False
        for x in li:
            if soz == x:
                bor = True
                break
        if not bor:
            li.append(soz)
    return li


def takror(borsoz, listi):
    soni = 0
    lu = {}

    for i in range(uzun(borsoz)):
        for e in range(uzun(listi)):
            if borsoz[i] == listi[e]:
                soni += 1

        lu[borsoz[i]] = soni
        soni = 0

    kal = []

    for k in lu:
        kal += [k]

    for k in range(uzun(kal)):
        for i in range(uzun(kal)):
            if lu[kal[k]] > lu[kal[i]]:
                kal[k], kal[i] = kal[i], kal[k]

    yangi = {}

    for k in kal:
        yangi[k] = lu[k]

    return yangi
            

with open("matin.txt", "r")as file:
    soz = file.read()

soz,soni,qatori,belgilar = joy(soz) #=========================================================================================

sozi = olchami(soz)

yangi = []
sanoq = 9

while sanoq != -1:
    yangi.append(sozi[sanoq])
    sanoq -= 1    


# # print(yangi)
# print(100*"=")


sozbi = bitadan(soz)
luga = takror(sozbi,soz) #=================== hamma sozlar ishtroki soni
qatnsash = {}
aylana = 0

for i in luga:
    if aylana < 10:
        qatnsash[i] = luga[i]
        aylana += 1 
    
# print(sozbi)
# print(luga)
# print(100*"=") # ==============================   qatnashgan 10 ta eng kop takrorlangan sozlar
# print(qatnsash)


takroo = {}        # takrorlangan sozlar statistikasi
tak_soni = 0
for k in luga:
    if luga[k] == 1:
        tak_soni += 1 #========= ========================tak_soni ====takrorlanmagan sozlar soni 
    else:
        takroo[k] = luga[k]
print(100*"WM")
print(soz)   # sozlar asil
print(100*"WM")
print(belgilar) # jami belgi
print(100*"WM")
print(qatori) # jami qatori
print(100*"WM")
print(soni)   # Jami  so‘zlar soni.
print(100*"WM")
print(yangi) # Eng uzun 10 ta so‘z.
print(100*"WM")
print(qatnsash) # Eng ko‘p takrorlangan 10 ta so‘z.
print(100*"WM")
print(tak_soni) # Takrorlanmaydigan so‘zlar soni.
print(100*"WM")
print(takroo) # takrorlangan sozlar statistikasi

# with open("yangi_matn.txt", "w")as file:
#     asa = 0
#     for i in soz:
#         if asa == 7:
#             file.write("\n")
#             asa = 0
#         file.write(i+ " ")
#         asa += 1
        
#     asas = str(belgilar)
#     file.write("\nbelgilar "+ asas)
#     ass = str(qatori)
#     file.write("\nqatori "+ ass)
#     ss = str(soni)
#     file.write("\nsozlar "+ ss+"\n")
    
#     ay = 0
#     for i in yangi:
#         if ay == 7:
#             file.write("\n")
#             ay = 0
#         file.write(i+ " ")
#         ay += 1
        
        
#     y = 0
#     for i in qatnsash:
#         if y == 7:
#             file.write("\n")
#             y = 0
#         file.write(i+ " ")
#         y += 1        
      
#     p = str(tak_soni)
#     file.write("\ntakrorlanmagan sozlar  "+ p+"\n")
    
#     r = 0
#     for i in takroo:
#         if r == 7:
#             file.write("\n")
#             r = 0
#         d = str(takroo[i])
#         file.write(i+" "+d+ " ")
#         r += 1        
      
    
with open("yangi_matn.txt", "w")as file:
    file.write(50*"=")
    file.write("\n\t\t\tMATN TAHLILI HISOBOTI\n")
    file.write(50*"=")
    file.write("\n\n1. UMUMIY MA'LUMOTLAR\n")
    a = str(belgilar)
    file.write("\nJami belgilar: "+ a)
    a = str(qatori)
    file.write("\nJami qatorlar: "+ a)
    a = str(soni)
    file.write("\nJami so'zlar: "+ a)
    file.write("\n\n"+50*"=")
    file.write("\n\n2. ENG UZUN 10 TA SO'Z\n")
    
    ay = 1
    for i in yangi:
        u = str(uzun(i))
        a = str(ay)
        file.write("\n" +a+ "." +i+ " ("+u+")")
        ay += 1
        
    file.write("\n\n"+50*"=")
    file.write("\n\n3. ENG KO'P TAKRORLANGAN 10 TA SO'Z\n\n")
    
    
    y = 1
    for i in qatnsash:
        g = str(y)
        d = str(qatnsash[i])
        file.write("\n"+g+". "+ i+"  ("+ d +")" )
        y += 1
    file.write("\n\n"+50*"=")
    
    file.write("\n\n4. TAKRORLANMAYDIGAN SO'ZLAR\n\n")
    a = str(tak_soni)
    file.write("jami takrorlanmagan soz: "+a)
    
    file.write("\n\n"+50*"=")
    
    file.write("\n\n5. BARCHA SO'ZLARNING TAKRORLANISH STATISTIKASI\n\n")
    
    bb = 1
    for i in luga: 
        a = str(bb)
        ta = str(luga[i])
        file.write(a + ". " + i +" ("+ta+ ") \n")
        bb += 1
          
    file.write("\n\n"+50*"="+"\n")
    file.write("                  HISOBOT TUGADI\n")
    file.write(50*"=")