def HeapSort(lis):
    n = len(lis)

    # Heap tuzilmasini yaratish
    def heapify(n, i):
        katta = i
        chap = 2 * i + 1
        ong = 2 * i + 2

        if chap < n and lis[chap] > lis[katta]:
            katta = chap

        if ong < n and lis[ong] > lis[katta]:
            katta = ong

        if katta != i:
            lis[i], lis[katta] = lis[katta], lis[i]
            heapify(n, katta)

    # Max-Heap hosil qilish
    for i in range(n // 2 - 1, -1, -1):
        heapify(n, i)

    # Elementlarni saralash
    for i in range(n - 1, 0, -1):
        lis[0], lis[i] = lis[i], lis[0]
        heapify(i, 0)

    return lis


hh = [6, 2, 3, 412, 3, 2, 4, 3, 112, 3, 43, 34, 656, 57, 6, 323]

print(HeapSort(hh))