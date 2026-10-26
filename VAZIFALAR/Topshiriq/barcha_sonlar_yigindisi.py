def salom(n):
    if len(n) == 0:
        return 1
    return n[0] * salom(n[1:])

print(salom([5,7,4,9,2,7,9])) 