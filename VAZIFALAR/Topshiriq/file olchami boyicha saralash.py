A = {
    "A": 0,
    "B": 1,
    "C": 2,
    "D": 3,
    "E": 4,
    "F": 5,
    "G": 6,
    "H": 7,
    "I": 8,
    "J": 9,
    "K": 10,
    "L": 11,
    "M": 12,
    "N": 13,
    "O": 14,
    "P": 15,
    "Q": 16,
    "R": 17,
    "S": 18,
    "T": 19,
    "U": 20,
    "V": 21,
    "W": 22,
    "X": 23,
    "Y": 24,
    "Z": 25,
    "a": 26,
    "b": 27,
    "c": 28,
    "d": 29,
    "e": 30,
    "f": 31,
    "g": 32,
    "h": 33,
    "i": 34,
    "j": 35,
    "k": 36,
    "l": 37,
    "m": 38,
    "n": 39,
    "o": 40,
    "p": 41,
    "q": 42,
    "r": 43,
    "s": 44,
    "t": 45,
    "u": 46,
    "v": 47,
    "w": 48,
    "x": 49,
    "y": 50,
    "z": 51,
}



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

def uzun(n):
    uzu = 0 
    for i in n:
        uzu += 1
    return uzu

def anqla(lis,n):
    qa = 0
    for i in range(uzun(lis)):
        if n == lis[i]:
            qa += 1
    return qa

def sorth(n):
    s = uzun(n)
    for i in range(s):
        for j in range(s):
            if A[n[i][0][0]] < A[n[j][0][0]]:
                n[i], n[j] = n[j], n[i]
                
    return n





def olchami(g):
    n = uzun(g)
    
    a = 0 
    for i in range(n):
        x = 0
        for s in range(n):
            if uzun(g[a]) < uzun(g[x]):
                g[i], g[s] = g[s], g[i]
            x += 1
        a += 1
    return g

def tak(n):
    t = {}
    for i in n :
        s = anqla(n,i)
        if s > 1:
           t[i] = s
             
        
    return t



with open('matin.txt', 'r') as file:
    sozlar = file.read()

sozlar = joy(sozlar)

harf_sort = sorth(sozlar)
    
with open("alifbo.txt", "w") as alifbo:
    for hh in harf_sort:
        alifbo.write(hh+"\n")
    
uzunlik = olchami(sozlar)
    
with open("uzunlik.txt", "w") as nnn:
    for uu in uzunlik:
     nnn.write(uu + "\n")