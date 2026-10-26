a = []

def son(start, n):
    a.append(start)
    print(start)
    if start >= n:
        return
    
    start +=1 
    
    son(start, n)
    
sonn = input("Son kiriting: ")
son(1, int(sonn))
print(sum(a))