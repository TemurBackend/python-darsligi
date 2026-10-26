def HeapSort(lis):
    n = len(lis)

    print("Boshlang'ich ro'yxat:", lis)
    print()

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
            print(f"Almashtirishdan oldin: {lis}")

            lis[i], lis[katta] = lis[katta], lis[i]

            print(f"{lis[katta]} va {lis[i]} almashtirildi")
            print(f"Almashtirishdan keyin: {lis}")
            print()

            heapify(n, katta)

    # Max-Heap hosil qilish
    print("1. MAX-HEAP YARATISH BOSHLANDI")

    for i in range(n // 2 - 1, -1, -1):
        print(f"\ni = {i} indeks tekshirilmoqda")
        heapify(n, i)
        print("Hozirgi ro'yxat:", lis)

    print("\nMax-Heap hosil bo'ldi:", lis)
    print()

    # Elementlarni saralash
    print("2. SARALASH BOSHLANDI")

    for i in range(n - 1, 0, -1):
        print(f"\ni = {i}")
        print("Almashtirishdan oldin:", lis)

        lis[0], lis[i] = lis[i], lis[0]

        print("Eng katta son oxiriga o'tdi:", lis)

        heapify(i, 0)

        print("Heap qayta tiklangandan keyin:", lis)
        print("Joyiga tushgan son:", lis[i])

    print("\n3. SARALASH TUGADI")
    print("Yakuniy ro'yxat:", lis)

    return lis


hh = [6, 2, 3, 412, 3, 2, 4, 3, 112, 3, 43, 34, 656, 57, 6, 323]

natija = HeapSort(hh)

print("\nYakuniy natija:", natija)