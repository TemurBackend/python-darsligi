belgili = [
    "a'lo", "a'lochi", "a'zan",
    "ba'zan", "ba'zi", "ba'zanlari",
    "e'lon", "e'tibor", "e'tiqod", "e'tirof",
    "e'tiroz", "e'timod", "e'zoz",
    "ma'no", "ma'lumot", "ma'naviyat",
    "ma'rifat", "ma'ruf", "ma'sul",
    "ma'sum", "ma'qul", "ma'mur",
    "san'at", "san'atkor", "san'atshunos",
    "qal'a", "jur'at", "sur'at",
    "qit'a", "she'r", "shu'la",
    "ta'lim", "ta'sir", "ta'sis",
    "ta'kid", "ta'rif", "ta'minot",
    "ta'mir", "ta'm", "ta'qdir",
    "mas'ul", "mas'uliyat", "qat'iy",
    "qat'iyat", "bid'at", "in'om",
    "ne'mat", "me'mor", "me'morchilik",
    "mo'jiza", "mo'tabar", "mo'tadil",
    "ra'no", "da'vo", "da'vat", "jur'atli", "is'temol", "o'lja"
]
# da'vgat


def tekshir(a, soz):
    for el in a:
        if el == soz:
            return True
    return False

def joy(n):
    sozi = ""
    sozlar1 = ""
    for i in n.lower():
        if i != " " and i != "\n":
            if i != "?" and i != "." and i != "!" and i != ',' and i !="\"" and i != "\'":
               sozi += i
            elif i == "\'":
                if sozi != "" and (sozi[-1] == "a" or  sozi[-1] == "o" or  sozi[-1] == "g" or sozi[-1] == "l" or sozi[-1] == "e" or sozi[-1] == "n" or sozi[-1] == "r" or sozi[-1] == "s" or sozi[-1] == "t" or sozi[-1] == "d" or sozi[-1] == "u"):
                    sozi += i
                
        elif i == " " or i == "\n":
            tinish_belgi = False
            if sozi != "":
                for i in sozi:
                    if i == '\'':
                        if tekshir(belgili, sozi):
                            sozlar1 += sozi + " "
                        else:
                            yangi = ""
                            for p in sozi:
                                if p == "'":
                                    continue
                                else:
                                    yangi += p
                            sozlar1 += yangi + " "
                            yangi = ""
                        tinish_belgi = True
                        break
                if tinish_belgi == False:
                   sozlar1 += sozi + " "
                    
            sozi = ""               
        
                
                
            
    return sozlar1









with open('matin.txt', 'r') as file:
    with open('yangi_matn.txt', 'w') as yangi_file:
        while True:
            sozlar = file.readline()
            if not sozlar:
                break
            if sozlar == "\n" or sozlar == "":
                continue
            else:
                sozlar = joy(sozlar)
                if sozlar == "":
                    continue
                yangi_file.write(sozlar+"\n")
