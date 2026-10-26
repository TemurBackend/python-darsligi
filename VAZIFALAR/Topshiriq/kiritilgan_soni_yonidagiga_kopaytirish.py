def son(n):
    if n == 0:
        return 0
    return n % 10 + son(n // 10)
        

print(son(77))