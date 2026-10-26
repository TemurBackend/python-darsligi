def juft(n):
    yig = 0
    for son in n:
        if son % 2 == 0: 
            yig += son
    return yig
        
        
a = [3, 4, 5, 6, 9, 12, 100, 201, 900]

print(juft(a))