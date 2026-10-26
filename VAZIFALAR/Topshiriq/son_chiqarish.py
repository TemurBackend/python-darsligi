def teskari(n,start=1):
    print(n)
    if n <= start:
        return
    n = n - 1
    teskari(n,start)
    
teskari(10)