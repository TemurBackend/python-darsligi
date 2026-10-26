def juft(n):
    if len(n) == 0:
        return 0
    elif n[0] % 2 == 0:
        return n[0] + juft(n[1:])
    else:
        return juft(n[1:])
    
a = [2, 5, 64, 3, 5, 6, 876, 543, 345, 6, 7, 6, 54, 3, 10]
print(juft(a))