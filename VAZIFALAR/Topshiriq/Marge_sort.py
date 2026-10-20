def mergeSort(arr):  # Ro'yxatni tartiblash uchun funksiya
    if len(arr) > 1:  # Agar ro'yxatda 1 tadan ko'p element bo'lsa
        mid = len(arr) // 2  # Ro'yxatning o'rtasini topamiz

        L = arr[:mid]  # Ro'yxatning chap qismini olamiz
        R = arr[mid:]  # Ro'yxatning o'ng qismini olamiz s

        mergeSort(L)  # Chap qismni qaytadan ikkiga bo'lib tartiblaymiz
        mergeSort(R)  # O'ng qismni qaytadan ikkiga bo'lib tartiblaymiz

        i = j = k = 0  # Uchta indeksni 0 dan boshlaymiz
        # i - chap qismdagi element indeksi
        # j - o'ng qismdagi element indeksi
        # k - asosiy ro'yxatdagi yoziladigan joy indeksi

        while i < len(L) and j < len(R):
            # Ikkala qismda ham tekshirilmagan elementlar bor ekan, davom etamiz

            if L[i] < R[j]:  # Chap element o'ng elementdan kichik bo'lsa
                arr[k] = L[i]  # Chap elementni asosiy ro'yxatga yozamiz
                i += 1  # Chap qismning keyingi elementiga o'tamiz

            else:  # Aks holda, o'ng element kichik yoki teng bo'lsa
                arr[k] = R[j]  # O'ng elementni asosiy ro'yxatga yozamiz
                j += 1  # O'ng qismning keyingi elementiga o'tamiz

            k += 1  # Asosiy ro'yxatdagi keyingi joyga o'tamiz

        while i < len(L):  # Chap qismda elementlar qolgan bo'lsa
            arr[k] = L[i]  # Qolgan chap elementni ro'yxatga yozamiz
            i += 1  # Chap qismning keyingi elementiga o'tamiz
            k += 1  # Asosiy ro'yxatning keyingi joyiga o'tamiz

        while j < len(R):  # O'ng qismda elementlar qolgan bo'lsa
            arr[k] = R[j]  # Qolgan o'ng elementni ro'yxatga yozamiz
            j += 1  # O'ng qismning keyingi elementiga o'tamiz
            k += 1  # Asosiy ro'yxatning keyingi joyiga o'tamiz


# Tartiblanishi kerak bo'lgan ro'yxat
a = [21, 22, 33, 55, 77, 87, 4, 2, 3, 1, 2, 3, 1]

mergeSort(a)  # Ro'yxatni kichikdan kattaga tartiblaymiz
print(a)  # Tartiblangan ro'yxatni ekranga c 