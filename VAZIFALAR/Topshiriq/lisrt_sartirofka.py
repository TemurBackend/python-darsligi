def sara(n):  
    a = 0
    for i in range(len(n)):
        f = 0
        for j in range(len(n)):
            if n[i] < n[f]:
                temp = n[a]
                n[a] = n[f]
                n[f] = temp
            f +=1 
        a += 1
    return n


a = [13,2,234,67,4,3,56,43,45,2]
print (sara(a))  