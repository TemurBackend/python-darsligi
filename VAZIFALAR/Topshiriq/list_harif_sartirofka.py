ismlar = [
    "Osimxon",
    "Anasxon",
    "Abdulaziz",
    "Abdullayev MuhammadAmin",
    "Temurbek",
    "Vali",
    "Otabek",
    "Muslim",
    "Abdullayev MuhammadAli",
    "Nematjon"
]


def tartib(ismlar):
    n = len(ismlar)

    for i in range(n):
        for j in range(i + 1, n):
            a = ismlar[i].lower()
            b = ismlar[j].lower()

            k = 0
            while k < len(a) and k < len(b):
                if a[k] > b[k]:
                    ismlar[i], ismlar[j] = ismlar[j], ismlar[i]
                    break
                elif a[k] < b[k]:
                    break
                k += 1    
            else:
                if len(a) > len(b):
                    ismlar[i], ismlar[j] = ismlar[j], ismlar[i]

    return ismlar


print(tartib(ismlar))
