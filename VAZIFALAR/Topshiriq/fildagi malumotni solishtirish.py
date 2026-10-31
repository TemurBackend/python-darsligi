def joy(n):
    sozi = ""
    sozlar1 = []
    for i in n:
        if i != " " and i != "\n" and i != "":
            sozi += i
        elif i == " " or i == "\n" or i == "":
            if sozi == "":
                continue
            sozlar1.append(sozi)
            sozi = ""
    if sozi != "":
        sozlar1.append(sozi)
        # sozi = ""   
        
    return sozlar1 

def uzun(n):
    uzu = 0 
    
    for i in n:
        uzu += 1
    return uzu

def solishtr(b,k):
    bori = []
    yoq = []
    for i in range(uzun(b)):
        for j in range(uzun(k)):
            if b[i] == k[j]:
                bori.append(b[i])
            if b[i] != k[j]:
                yoq.append(b[i])
    return bori, yoq
            
# def bori(bir, ikki):
#     yogi = []
#     for i in uzun(bir):
#         for n in uzun(ikki):
#             if bir[i] != ikki[n]:
#                 yogi.append(bir[i])
#     return yogi


def takror(bor, tek):
    soni = 0
    lu = {}
    for i in range(uzun(bor)):
        for e in range(uzun(tek)):
            if bor[i] == tek[e]:
                soni += 1
        lu[bor[i]] = soni
        soni = 0        
    return lu

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

def taqqosla(b, i):
    li = []
    for r in b:
        if b[r] > i[r]:
            li.append(f"Birinchi fayilda  {r}-{b[r]} kop qatnashgan.\n")
        elif b[r] < i[r]:
            li.append(f"ikkinchi fayilda  {r}-{i[r]} kop qatnashgan. \n")
        else:
            li.append(f"Birinchi fayildagi {r}-{b[r]} bilan ikkinchi fayildagi {r}-{i[r]} bilan teng. \n")
    return li



with open("matin.txt", "r") as fail:
    bir = fail.read()
    bir = joy(bir)

with open("2-fayl.txt", "r") as fail:
    ikki = fail.read()
    ikki = joy(ikki)

bir_bori, yogi = solishtr(bir, ikki)

with open("1-fayl.txt", "w") as file:
    for i in yogi:
        file.write(i + "\n")

_, yoq = solishtr(ikki, bir)

with open("2-fayll.txt", "w") as file:
    for i in yoq:
        file.write(i + "\n")

ikkibor = bitadan(bir_bori)

birtak = takror(ikkibor, bir)
ikkitak = takror(ikkibor, ikki)
taqqoslangan = taqqosla(birtak, ikkitak)

with open("3-fayll.txt", "w") as file:
    for i in birtak:
        file.write(i + "\n")

    for i in ikkitak:
        file.write(i + "\n")

    for i in taqqoslangan:
        for n in i:
            if n == "\n":
                file.write("\n")
            if n != "\n":
                file.write(n)
        file.write("\n")
            

print("oz holi bir",bir)
print(70*"-")
print("oz holi ikki",ikki)
print(100*"=")
print("ekkalasida borlari",bir_bori)
print(100*"=")
print("ikalasida borlari bitadan ",ikkibor)
print(100*"W")
print("birinchisida takrorlanganlari sozni",birtak)
print(100*"W")
print("ikkinchisida bor takrorlanganlari soni", ikkitak)
print(100*"WM")
print("taqoslash bunksiyasi ishlashi",taqqoslangan)


