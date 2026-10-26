def son(n):
    if len(n) == 0:
        return 1
    return n[0] + son(n[1:])

print(son([12,32,43,54,65,76,87,98,23,34,5,6,7,7,65]))

