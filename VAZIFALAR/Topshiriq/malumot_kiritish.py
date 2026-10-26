def kop(n):
    mah = {}

    for i in range(len(n)):
        s = 0
        for j in range(len(n)):
            if n[i] == n[j]:
                s += 1
        mah.update({n[i]: s})

    return mah


def aniqla(b):
    qa = 0
    so = 0

    for k, m in b.items():
        if m > qa:
            qa = m
            so = k

    return f"{so} : {qa}"


def inpu(n):
    for _ in range(int(input("Nechta malumot kiritmoqchisiz:  "))):
        i = input("Istalgan bitta malumot kiriting: ")
        if i.isdigit():
            n.append(int(i))
        else:
            n.append(i)

    return n


def anqla(lis, n):
    qa = 0
    for i in range(len(lis)):
        if n == lis[i]:
            qa += 1
    return qa


def ket(n):
    if n.isdigit():
        return int(n)
    else:
        return n


qw = True


def ser():
    a = []
    while qw:
        print("""
        1 Malumot qoshish
        2 Malumotni korish
        3 Malumotni qidirish
        4 Kop kiritilgan malumot
        5 Barcha malumotlar takrorlanganini korish
        6 Barcha malumotlarni o'chirish
        7 Chiqish
             """)

        s = input("Bajaradigan amalni sonini kiriting: ")

        if s == "1":
            inpu(a)
            continue

        elif s == "2":
            if len(a) == 0:
                print("Siz hali malumot kiritmadingiz!!")
                continue
            else:
                print(a)
                continue

        elif s == "3":
            if len(a) == 0:
                print("Siz hali malumot kiritmadingiz!!")
                continue

            p = ket(input("Qidiruv: "))

            if p in a:
                soni = anqla(a, p)
                print(f"Siz qidirgan {p} ma'lumot {soni} marotaba takrorlangan")

                sa = input("""
        1. Ma'lumotni o'chirish
        2. Ma'lumotni o'zgartirish
        Tanlang: """)

                if sa == "1":
                    a.remove(p)
                    print("Ma'lumot muvaffaqiyatli o'chirildi!")

                elif sa == "2":
                    indeks = a.index(p)
                    ed = input("Yangi ma'lumot kiriting: ")

                    if ed.isdigit():
                        ed = int(ed)

                    a[indeks] = ed
                    print(f"Ma'lumot muvaffaqiyatli o'zgartirildi: {a[indeks]}")

                else:
                    print("Iltimos, to'g'ri buyruq kiriting!")

            else:
                print("Bunday ma'lumot mavjud emas!")

        elif s == "4":
            if len(a) == 0:
                print("Siz hali malumot kiritmadingiz!!")
                continue
            else:
                p = aniqla(kop(a))
                print(f"Siz kiritgan malumotlaringiz ichida eng kopi {p}")
                continue

        elif s == "5":
            if len(a) == 0:
                print("Siz hali malumot kiritmadingiz!!")
                continue
            else:
                print(kop(a))
                continue

        elif s == "6":
            if len(a) == 0:
                print("Siz hali malumot kiritmadingiz!!")
                continue
            else:
                print("Barcha malumotlar o'chirildi")
                a.clear()
                continue

        elif s == "7":
            print("Chiqish tugallandi")
            break

        else:
            print("Bunday buyruq yo'q!!!")
            continue

    return


ser()
