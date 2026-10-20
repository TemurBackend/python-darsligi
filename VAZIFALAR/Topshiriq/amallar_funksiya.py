def teskari(n, natija=0):
    if n == 0:
        return natija

    raqam = n % 10

    return teskari(n // 10, natija * 10 + raqam)


teskari(10,54)