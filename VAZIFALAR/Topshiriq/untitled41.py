def son(n):
    
    if len(n) <= 1 :
        return 0
    else:
        print(n[0], end=" ")
        return son(n[1:])
        
a = [900, 201, 100, 12, 9, 6, 5, 4, 3]

print(son(a))