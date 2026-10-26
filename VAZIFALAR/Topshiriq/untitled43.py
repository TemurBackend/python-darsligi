def kop(n):
    mah = {}

    for i in range(len(n)):
        s = 0
        for j in range(len(n)):
            if n[i] == n[j]:
                s += 1
        mah.update({n[i] : s})

    return mah





a = [2, 5, 2, 7, 2, 9, "2y", 2, 3, 3, 3, 3, 3, 3, 3]
print(kop(a))
















