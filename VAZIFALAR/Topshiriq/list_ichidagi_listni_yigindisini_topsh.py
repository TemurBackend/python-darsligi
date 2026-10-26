def yigindi(lis):
    start = 0
    for i in lis:
        if isinstance(i, int):
            start+=i
        elif isinstance(i, list):
            start+=yigindi(i)
    
    return start

arr = [1, [2, 3], [4, [5, 6]]]
print(yigindi(arr))