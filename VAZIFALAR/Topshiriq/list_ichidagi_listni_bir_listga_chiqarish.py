def lis(n):
    start = []
    for i in n:
        if isinstance(i,int):
            start.append(i)
        elif isinstance(i, list):
            s = lis(i)
            start.extend(s)

    return start
        
            


arr = [1, [2, 3], [4, [[[[[[[[[[[[[[[[[[[[[[[[[9]]]]]]]]]]]]]]]]]]]]]]]]],[5, 6]]]
print(lis(arr))