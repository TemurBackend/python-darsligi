def sar(n):
    if len(n) <= 1:
        return n
    ki = []
    ka = []
    n_1 =  n[0]
    
    for son in n[1:]:
        if son <= n_1:
            ki.append(son)
        else:
            ka.append(son)
        
    return sar(ki) + [n_1] + sar(ka)

a = [900,12 , 3,100,  4, 9, 5, 201, 6]       
print(sar(a))