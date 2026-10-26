a = [3,5,3,5,6,7,8,9,6,9,8,7,6,5,5]

def yigindi(n):
    if not n:
        return 0

    return n[0] + yigindi(n[1:])

print(yigindi(a)) 
