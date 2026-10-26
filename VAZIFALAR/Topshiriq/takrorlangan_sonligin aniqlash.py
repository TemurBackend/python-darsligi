def son(start, n):
    print(start)
    if start >= n:
        return
    start+=1 
    son(start, n)
    
sonn = input("Son kiriting: ")
son(1, int(sonn))