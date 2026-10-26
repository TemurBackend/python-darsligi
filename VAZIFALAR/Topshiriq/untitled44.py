def son(n):
    if len(n) == 0:
        return 0
    
    if n[0] > 0:
        return n[0] + son(n[1:])
    else:
        return son(n[1:])

a = [-1,-3,5,-1,3,5 ,5]
print(son(a))

