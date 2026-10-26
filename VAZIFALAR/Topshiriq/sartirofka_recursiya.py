def lis(n):
    for i in range(len(n)):
        if isinstance(n[i], list):
            n[i] = lis(n[i])
            
    for i in range(len(n)):
        for j in range(0, len(n) - i - 1):
            if not isinstance(n[j], list) and not isinstance(n[j + 1], list):
                if n[j] > n[j+1]:
                    n[j], n[j+1] = n[j+1], n[j]
    
    return n


arr = [12, [5, 2, 9, 1], [34, [7, 6, [1, 3, 4, 2, [33, 24, 3, 534, [434, 3554, 245, 42, [33, 4, 543, 4, 543, [234, 234, 23, 42, 34]]]]]]]]
print(lis(arr))






