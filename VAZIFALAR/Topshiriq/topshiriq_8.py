def barchasi(lis):
    son = 0
    for _ in lis:
        ind = 0
        for i in lis:
            if lis[son] < lis[ind]:
                temp = lis[son]
                lis[son] = lis[ind]
                lis[ind] = temp
            ind += 1
        son += 1
    return lis
["A","H", "I", "O", "A", "B"]

def bar(arr):
    for i in range(len(arr)):
        barchasi(arr[i])


def bru(a):
    n = len(a)
    for i in range(n):
        for j in range(n - 1 - i):
            if a[j][0] > a[j + 1][0]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a

a = [
    [21, 42, 13, 2, 5, 523, 345, 42, 235, 3, 52, 235, 5, 645],
    [54, 34, 67, 765, 45, 765, 345, 7, 3, 567, 54, 45, 8, 87],
    [6, 90, 98, 765, 43, 45654, 9, 8765, 43, 456, 78, 4, 56],
    [76, 54, 56, 78, 5, 4, 5, 99, 876, 543, 4, 56, 78, 8765, 45],
    [678, 9, 876, 54, 567, 9, 87, 654, 345678, 9, 987, 654, 345],
    [22, 123, 5, 2, 56, 54, 566, 43, 567, 653, 345, 543, 345],
    [432,345, 26789, 8765, 4, 5678, 9, 7654, 234, 23, 45, 3, 5],
]


# bar(a)
# print(a)
print(30 * "*")
bru(a)
print(a)
