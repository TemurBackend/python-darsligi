from random import randrange  # Tasodifiy indeks tanlash uchun randrange funksiyasini import qilamiz

def qsort(array):  # Quick Sort funksiyasini yaratamiz

    if len(array) < 2:  # Agar ro'yxatda 0 yoki 1 ta element bo'lsa
        return array  # Ro'yxat allaqachon saralangan, uni qaytaramiz

    else:
        # pivot = array.pop(0)  # Birinchi elementni pivot sifatida olish mumkin
        pivot = array.pop(randrange(len(array)))  # Tasodifiy indeksdagi elementni tanlab, ro'yxatdan olib tashlaymiz

        kichik = [i for i in array if i <= pivot]  # Pivotdan kichik yoki teng elementlarni yig'amiz
        katta = [i for i in array if i > pivot]  # Pivotdan katta elementlarni yig'amiz

        print(f"{kichik}+[{pivot}]+{katta}")  # Har bir bosqichdagi bo'linishni ekranga chiqaramiz

        # Kichik ro'yxatni va katta ro'yxatni alohida saralaymiz
        # So'ng ularni pivot bilan birlashtirib, natijani qaytaramiz
        return qsort(kichik) + [pivot] + qsort(katta)


a = [21, 22, 33, 55, 77, 87, 4, 2, 3, 1, 2, 3, 1]  # Boshlang'ich ro'yxat


print(qsort(a))  # Saralangan ro'yxatni ekranga chiqaramiz
print(a)  # Asl ro'yxatni chiqaramiz