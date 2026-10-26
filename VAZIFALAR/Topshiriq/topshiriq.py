def ikki(n):
    qa = 0
    for i in range(len(n)):
        for j in range(len(n)):
            if n[i] == n[j]:
                qa += 1
        return qa 

a = [2, 5, 2, 7, 2, 9, "2", 2, 3, 3, 3, 3, 3, 3, 3]
print(ikki(a))
# funksiya list qabul qiladi va bitta int qabul qiladi, list ichida kiritilgan raqam necha marta takrorlanganini ekranga chiqarish
# 