def mini(n):   
    if len(n) == 1 : 
        return n[0]
    qolgan_son = mini(n[1:]) 
    if n[0] < qolgan_son: 
        return n[0]
    else:
        return qolgan_son
    
a = [65,4,3, -1, 4,5,6,76,4,5]
    
b = mini(a)
print(b) 