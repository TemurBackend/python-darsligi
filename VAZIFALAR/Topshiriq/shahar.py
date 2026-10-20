def son(n):
    n = str(n)

    if n.isdigit():
        return int(n)
    else:
        print("Iltimos,son bilan kiriting!")
        n = input(">>> ")
        return son(n)


class Odam:
    def __init__(self, ism, fam, yil, jns):
        self.ism = ism.strip().capitalize()
        self.fam = fam.strip().capitalize()
        self.yil = son(yil)
        self.jns = jns.capitalize()
        self.yosh = 2026 - self.yil
        self.mt = 0
        self.mashina = None
        self.hayvonlar = []
        self.bajarildi = []

    def info(self):
        return (
            f"Ismi: {self.ism}\n"
            f"Familiyasi: {self.fam}\n"
            f"Tug'ilgan yili: {self.yil}\n"
            f"Yoshi: {self.yosh}\n"
            f"Jinsi: {self.jns}"
        )

    def ish(self):
        print("Bu odam uchun maxsus ish vazifasi yoq.")

    def get_name(self):
        return f"Mening ismim {self.ism}. Familiyam {self.fam}."

    def get_age(self):
        return f"Men {self.yosh} yoshdaman."

    def get_jns(self):
        return self.jns

    def yur(self):
        m = son(input("Necha metr yurasiz: "))
        self.mt += m
        return f"{self.ism} jami {self.mt} metr yurdi."


class Qiz(Odam):
    def ish(self):
        ishlar = {
            "1": "Uy yig'ishtirish",
            "2": "Ovqat qilish",
            "3": "Idish yuvish",
            "4": "Bola qarash"
        }

        while True:
            print("\nVazifalar ro'yxati:")

            for raqam, vazifa in ishlar.items():
                holat = (
                    "Bajarildi"
                    if raqam in self.bajarildi
                    else "Bajarilmadi"
                )
                print(f"{raqam}. {vazifa} - {holat}")

            tan = input("Vazifa raqamini kiriting: ").strip()

            if tan not in ishlar:
                print("Bunday vazifa mavjud emas!")
                continue

            if tan in self.bajarildi:
                print("Bu ish oldin bajarilgan!")
            else:
                self.bajarildi.append(tan)
                print(f"{ishlar[tan]} - Bajarildi!")

            while True:
                javob = input(
                    "Yana ish bajarasizmi (ha/yoq)? "
                ).lower().strip()

                if javob in ("ha", "yoq"):
                    break

                print("Iltimos, ha yoki yoq deb javob bering!")

            if javob in ("yoq"):
                print("\nVazifalar tugallandi!")
                self.bajarilgan(ishlar)
                break

    def bajarilgan(self, ishlar):
        if not self.bajarildi:
            print("Hech qanday ish bajarilmadi!")
            return

        print("\nBajarilgan vazifalar:")

        for raqam in self.bajarildi:
            print(f"- {ishlar[raqam]}")

        print(
            f"Jami bajarilgan vazifalar: "
            f"{len(self.bajarildi)}"
        )


class Ogil(Odam):
    def __init__(self, ism, fam, yil, jns):
        super().__init__(ism, fam, yil, jns)

        self.sport_turi = input(
            "Qanday sport bilan shug'ullanasiz: "
        )
        self.maqsadim = input("Maqsadingizni kiriting: ")

        self.bajarildi = []

    def get_sport(self):
        return (
            f"Men {self.sport_turi} bilan shug'ullanaman."
        )

    def get_maqsad(self):
        return f"Maqsadim: {self.maqsadim}"

    def info(self):
        return (
            f"{super().info()}\n"
            f"{self.get_sport()}\n"
            f"{self.get_maqsad()}"
        )

    def ish(self):
        ishhona = {
            "1": "Hujjat tahrirlash",
            "2": "Majlis o'tkazish",
            "3": "Dars berish",
            "4": "Ovqatlanish"
        }

        while True:
            print("vazifalari:")

            for raqam, vazifa in ishhona.items():
                holat = (
                    "Bajarildi"
                    if raqam in self.bajarildi
                    else "Bajarilmadi"
                )
                print(f"{raqam}. {vazifa} - {holat}")

            tan = input("Vazifa raqamini kiriting: ").strip()

            if tan not in ishhona:
                print("Bunday ish mavjud emas!")
                continue

            if tan in self.bajarildi:
                print("Bu ish oldin bajarilgan!")
            else:
                self.bajarildi.append(tan)
                print(f"{ishhona[tan]} - Bajarildi!")

            while True:
                javob = input(
                    "Yana ish bajarasizmi (ha/yoq)? "
                ).lower().strip()

                if javob in ("ha", "yoq"):
                    break

                print("Iltimos, ha yoki yo'q deb javob bering!")

            if javob in ("yoq"):
                print("Vazifalar tugallandi!")
                self.bajarilgan()
                break

    def bajarilgan(self):
        if not self.bajarildi:
            print("Hech qanday ish bajarilmadi!")
            return

        ishhona = {
            "1": "Hujjat tahrirlash",
            "2": "Majlis o'tkazish",
            "3": "Dars berish",
            "4": "Ovqatlanish"
        }

        print("\nBajarilgan vazifalar:")

        for raqam in self.bajarildi:
            print(f"- {ishhona[raqam]}")

        print(f"Jami: {len(self.bajarildi)} ta vazifa")

    def __str__(self):
        return self.info()


class Hayvon:
    def __init__(self, nomi, yoshi):
        self.nomi = nomi
        self.yoshi = yoshi

    def get_name(self):
        return f"Hayvon nomi: {self.nomi}"

    def get_age(self):
        return f"Yoshi: {self.yoshi}"

    def info(self):
        return f"{self.get_name()}, {self.get_age()}"


class UyHayvoni(Hayvon):
    def harakat(self):
        print(
            f"{self.nomi} uy hayvoni. "
            "Uni parvarish qilish kerak."
        )

    def ovqatlantr(self):
        print(f"{self.nomi} ovqatlantirildi.")


class YovvoyiHayvon(Hayvon):
    def harakat(self):
        print(
            f"{self.nomi} yovvoyi hayvon, "
            "tabiatda harakatlanmoqda."
        )


class Mashina:
    def __init__(self, marka, zavodda=False):
        self.marka = marka
        self.zavodda = zavodda
        self.yoniq = False

    def info(self):
        holat = (
            "Zavod holatida"
            if self.zavodda
            else "Tayyor"
        )
        dvigatel = "Yoniq" if self.yoniq else "O'chiq"

        return (
            f"Marka: {self.marka}, "
            f"Holati: {holat}, "
            f"Dvigatel: {dvigatel}"
        )

    def mash_olish(self):
        if self.zavodda:
            self.zavodda = False
            print(f"{self.marka} zavod holatidan chiqarildi.")
        else:
            print("Mashina allaqachon tayyor.")

    def yurgiz(self):
        if self.zavodda:
            print(
                "Avval mashinani zavod holatidan "
                "chiqarish kerak!"
            )
        elif self.yoniq:
            print("Mashina allaqachon yoniq.")
        else:
            self.yoniq = True
            print(f"{self.marka} yurgizildi.")

    def ochir(self):
        if self.yoniq:
            self.yoniq = False
            print(f"{self.marka} o'chirildi.")
        else:
            print("Mashina allaqachon o'chirilgan.")


odamlar = {}


def odam_qosh():
    ism = input("Ismingiz: ").strip()
    fam = input("Familiyangiz: ").strip()
    yil = son(input("Tug'ilgan yilingiz: "))

    while True:
        jins = son(input("Jins (1 - Qiz, 2 - Ogil): "))

        if jins in (1, 2):
            break

        print("1 yoki 2 ni tanlang!")

    if jins == 1:
        odam = Qiz(ism, fam, yil, "Ayol")
    else:
        odam = Ogil(ism, fam, yil, "Erkak")

    raqam = len(odamlar) + 1
    odamlar[raqam] = odam

    print(f"{odam.ism} {odam.fam} muvaffaqiyatli qo'shildi.")
    print(f"Odam raqami: {raqam}")


def odam_tanla():
    if not odamlar:
        print("Avval odam qoshing.")
        return None

    print("\nOdamlar ro'yxati:")

    for raqam, odam in odamlar.items():
        print(f"{raqam}. {odam.ism} {odam.fam}")

    tanlov = son(input("Odam raqamini kiriting: "))

    if tanlov in odamlar:
        return odamlar[tanlov]

    print("Noto'g'ri raqam!")
    return None


def shahsiy_m():
    odam = odam_tanla()

    if odam is None:
        return

    if odam.mashina is not None:
        print("Bu odamga mashina allaqachon biriktirilgan.")
        return

    marka = input("Mashina markasi: ").strip()

    if not marka:
        print("Mashina markasi bosh bolmasligi kerak!")
        return

    odam.mashina = Mashina(marka)
    print("Mashina odamga biriktirildi.")


def hayvon_biriktir():
    odam = odam_tanla()

    if odam is None:
        return

    nomi = input("Hayvon nomi: ").strip()
    yoshi = son(input("Hayvon yoshi: "))

    tur = son(
        input("1 - Uy hayvoni, 2 - Yovvoyi hayvon: ")
    )

    if tur == 1:
        hayvon = UyHayvoni(nomi, yoshi)
    elif tur == 2:
        hayvon = YovvoyiHayvon(nomi, yoshi)
    else:
        print("Noto'g'ri tanlov!")
        return

    odam.hayvonlar.append(hayvon)
    print("Hayvon odamga biriktirildi.")


def mashina_boshqar():
    odam = odam_tanla()

    if odam is None:
        return

    if odam.mashina is None:
        print("Bu odamga hali mashina biriktirilmagan.")
        return

    while True:
        print("\nMashina boshqaruvi:")
        print("1. Zavod holatidan chiqarish")
        print("2. Mashinani yurgizish")
        print("3. Mashinani o'chirish")
        print("4. Mashina ma'lumotlari")
        print("5. Orqaga")

        amal = son(input("Buyruq: "))

        if amal == 1:
            odam.mashina.mash_olish()
        elif amal == 2:
            odam.mashina.yurgiz()
        elif amal == 3:
            odam.mashina.ochir()
        elif amal == 4:
            print(odam.mashina.info())
        elif amal == 5:
            break
        else: 
            print("Noto'g'ri buyruq!")


def hayvon_boshqar():
    odam = odam_tanla()

    if odam is None:
        return

    if not odam.hayvonlar:
        print("Bu odamda hayvon yoq.")
        return

    print("\nHayvonlar ro'yxati:")

    for i, hayvon in enumerate(odam.hayvonlar, 1):
        print(f"{i}. {hayvon.info()}")

    raqam = son(input("Hayvon raqamini kiriting: "))

    if 1 <= raqam <= len(odam.hayvonlar):
        hayvon = odam.hayvonlar[raqam - 1]
        hayvon.harakat()

        if isinstance(hayvon, UyHayvoni):
            hayvon.ovqatlantr()
    else:
        print("Noto'g'ri hayvon raqami!")


def odamlar_korish():
    if not odamlar:
        print("Hozircha odamlar mavjud emas.")
        return

    print("\nOdamlar ro'yxati:")

    for raqam, odam in odamlar.items():
        print(f"{raqam}. {odam.ism} {odam.fam}")


def odam_malumotlari():
    odam = odam_tanla()

    if odam is None:
        return

    print("\n" + odam.info())

    print(f"\nYurgan masofasi: {odam.mt} metr")

    if odam.mashina is not None:
        print(odam.mashina.info())
    else:
        print("Mashina biriktirilmagan.")

    if odam.hayvonlar:
        print("\nHayvonlari:")
        for hayvon in odam.hayvonlar:
            print(hayvon.info())
    else:
        print("Hayvonlari yo'q.")


def bajarilgan_ishlar():
    odam = odam_tanla()

    if odam is None:
        return

    if not odam.bajarildi:
        print("Hali vazifa bajarilmagan.")
        return

    if isinstance(odam, Qiz):
        ishlar = {
            "1": "Uy yig'ishtirish",
            "2": "Ovqat qilish",
            "3": "Idish yuvish",
            "4": "Bola qarash"
        }
    else:
        ishlar = {
            "1": "Hujjat tahrirlash",
            "2": "Majlis o'tkazish",
            "3": "Dars berish",
            "4": "Ovqatlanish"
        }

    print("\nBajarilgan vazifalar:")

    for raqam in odam.bajarildi:
        print(f"- {ishlar[raqam]}")

    print(f"Jami: {len(odam.bajarildi)} ta vazifa")


def boshqaruv():
    while True:
        print("""
====== Boshqaruv paneli ======
1. Odam qo'shish
2. Odamlarni ko'rish
3. Odam ma'lumotlari
4. Odamga vazifa berish
5. Mashina biriktirish
6. Mashinani boshqarish
7. Hayvon biriktirish
8. Hayvonlarni boshqarish
9. Bajarilgan vazifalar
10. Chiqish
""")

        tanlov = son(input("Buyruqni tanlang: "))

        if tanlov == 1:
            odam_qosh()

        elif tanlov == 2:
            odamlar_korish()

        elif tanlov == 3:
            odam_malumotlari()

        elif tanlov == 4:
            odam = odam_tanla()

            if odam is not None:
                odam.ish()

        elif tanlov == 5:
            shahsiy_m()

        elif tanlov == 6:
            mashina_boshqar()

        elif tanlov == 7:
            hayvon_biriktir()

        elif tanlov == 8:
            hayvon_boshqar()

        elif tanlov == 9:
            bajarilgan_ishlar()

        elif tanlov == 10:
            print("Dastur yakunlandi!")
            break

        else:
            print("Bunday buyruq mavjud emas!")
boshqaruv()