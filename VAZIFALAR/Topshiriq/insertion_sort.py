def inserttion_sort(sonlar):
    uzunlik = len(sonlar)
    
    for i in range(1, uzunlik):
        for j in range(i, 0, -1):
            if sonlar[j] < sonlar[j - 1]:
                temp = sonlar[j]
                sonlar[j] = sonlar[j - 1]
                sonlar[j - 1] = temp
            else:
                break
    return sonlar
c = [7,6,4,2]
print(inserttion_sort(c))