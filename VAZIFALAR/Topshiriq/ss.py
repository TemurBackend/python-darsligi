def anqla(lis,n):
    qa = 0
    for i in range(len(lis)):
        if n == int(lis[i]):
            qa += 1
    return qa
a = [2, 5, 2, 7, 2, 9, "2", 2, 3, 3, 3, 3, 3, 3, 3]
print(anqla(a, 2))