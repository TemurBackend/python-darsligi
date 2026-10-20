
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
        self.ism = ism.capitalize()
        self.fam = fam.capitalize()
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
            f"Yoshi: {self.yil} {self.yosh} yoshda"
            f"Jinsi: {self.jns}") 
    
    def ish(self):
        print("Bu odam hali ish vazifasi yoq")

    def get_name(self):
        return f"Mening ismim {self.ism}. Familiyam {self.fam}."

    def get_age(self):
        return f"Men {self.yosh} yoshdaman."

    def get_jns(self):
        return self.jns

    def yur(self):
      m = son(input("Necha metr yuradi: "))
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
                holat = "Bajarildi" if raqam in self.bajarildi else "Bajarilmadi"
                print(f"{raqam}. {vazifa} - {holat}")

            print()
            tan = input("Bajariladigan ish raqamini kiriting: ")

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

            if javob == "yoq":
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

        print(f"Jami bajarilgan vazifalar: {len(self.bajarildi)}")
                
class Ogil(Odam):  
    def __init__(self, ism, fam, yil, jns):
        super().__init__(ism, fam, yil, jns)
        self.sport_turi = input("Qanday sport bilan shug'ullanasiz: ")
        self.maqsadim = input("Maqsadingizni kiriting: ")
        self.bajarildi = []



    def get_sport(self):
        return f"Men {self.sport_turi} bilan shug'ullanaman."

    def get_maqsad(self):
        return f"Maqsadim: {self.maqsadim}"

    def info(self):
        return (
            f"{super().info()} "
            f"\n{self.get_sport()}\n"
            f"{self.get_maqsad()}")
    
    def ish(self):
       ishhona = {
            "1":"Hujat tahrirlash.",
            "2":"Majlis otkazish.",
            "3":"Dars berish",
            "4":"Ovqatlanish"} 
        
       while True:
            for raqam, vazifa in ishhona.items():
                holat = "Bajarildi" if raqam in self.bajarildi else "Bajarilmadi"
                print(f"{raqam}. {vazifa} - {holat}")
    
            tan = input("Bajariladigan ish raqamini kiriting: ")
    
            if tan in ishhona:
                if tan not in self.bajarildi:
                    self.bajarildi.append(tan)
                    print(f"{self.ishhona[tan]} Bajarildi")
                else:
                    print("Bu ish oldin bajarilgan!")
            else:
                print("Bunday ish mavjud emas!")
                continue
    
            javob = input("Yana ish bajarasizmi (ha/yoq)? ").lower()
    
            if javob == "ha":
                continue
            elif javob == "yoq":
                print("Vazifa tugallandi!")
                break
            else:
                print("Iltimos, ha yoki yoq deb javob bering!")
    
    
    def bajarilgan(self):
        if not self.bajarildi:
            print("Hech qanday ish bajarilmadi!")
        else:
            print("Bajarilgan vazifalar:")
            for raqam in self.bajarildi:
                print(f"- {self.ishhona[raqam]}")
    
    
    def __str__(self):
        return self.info()
    
class Hayvon:
    def __init__(self, nomi, yoshi):
        self.nomi = nomi
        self.yoshi = yoshi

    def get_name(self):
        return f"Bu hayvonning nomi {self.nomi}"

    def get_age(self):
        return f"Yoshi: {self.yoshi}"

    def info(self):
        return f"{self.get_name()} {self.get_age()}"

class UyHayvoni(Hayvon):        
    def harakat(self):
        print(f"{self.nomi} uy hayvoni, Buni parvarish qilish kerak")
    
    def ovqatlantr(self):
        print(f"{self.nomi} uy hayvoni ovqatlantirildi")
        
class yavoyi_hayvon(Hayvon):
    def harakat(self):
        print(f"{self.nomi} yovvoyi hayvon tabiatda harakatlanmoqda.")
        
        
class Mashina:
    def __init__(self, marka, zavodda=False):
        self.marka = marka
        self.zavodda = zavodda
        self.yoniq = False
        
    def info(self):
        holat = "Zavot holatida" if self.zavodda else "Tayyor"
        return f"Marka: {self.marka}, holar: {holat}"

    def mash_olish(self):
        if self.zavodda:
            self.zavodda = False
            print(f"{self.marka} zavod holatida chiqarildi.")
        else:
            print("Mashina allaqachon tayyor.")
            
    def yurgiz(self):
        if self.zavodda:
            print("Avval mashina zavod holatidan olib chiqarish kerak")
        elif self.yoniq:
            print("Mashina allaqachon yoniq.")
        else:
            self.yoniq = True
            print(f"{self.marka} yurgizildi.")
            
    def ochir(self):
        if self.yoniq:
            self.yoniq = False
            print("mashina ochirildi")
        else:
            print("Mashina alla qachon ochirilgan")
            
odamlar = {}


def odam_qosh():
    ism = input("ismingiz: ")
    fam = input("familiya kiriting")
    yil = son(input("Tugulgan yil:"))
    
    
    while True:
        jins = son(input("jins (1 - Qiz, 2 - O'gil): "))
        if jins in (1, 2):
            break
        print("1 yoki 2 ni tanlang")
        
    if jins == 1:
        odam = Qiz(ism, fam, yil, "Ayol")
    elif jins == 2:
        odam = Ogil(ism, fam, yil, "Erkak")
    else:
        print("Iltimos jinsingizni togri kiriting")
        odamlar[len(odamlar) + 1] = odam
        
        
def odam_tanla():
    if not odamlar:
        print("Avval odam qoshing.")
        return None
    
    for raqam, odam in odamlar.items():
        print(f"{raqam}. {odam.ism} {odam.fam}")
    
    tanlov =son(input("Odam raqami"))
    
    if tanlov and tanlov in odamlar:
        return odamlar[tanlov]
    print("Notogri raqam!")
    return None


def shahsiy_m():
    odam = odam_tanla()
    if odam is None:
        return
    
    if odam.mashina is not None:
        print("Bu odamning mashinasi allaqachon mavjud.")
        return
    
    marka = input("Mashina markasi: ")
    odam.mashina = Mashina(marka)
    print("Mashina odam biriktirildi.")
    
    
    
def hayvon_biriktir():
    odam = odam_tanla()
    if odam is None:
        return
    
    nomi = input("Hayvon nomi: ")
    yoshi = son(input("Hayvon yoshini: "))
    tur = son(input("1 -uy hayvoni.  2 -yovoyi hayvon"))
    
    if tur == 1:
        hayvon = UyHayvoni(nomi, yoshi)
    elif tur == 2:
        hayvon = yavoyi_hayvon(nomi, yoshi)
    else:
        print("Notogri tanlov.")
        return
    
    odam.hayvonlar.append(hayvon)
    print("Hayvon odamga biriktirildi.")
    


def boshqaruv():
    while True:
        print("""
====== Boshqaruv Paneli ======
1. Odam qo'shish
2. Odamlarni ko'rish
3. Odam ma'lumotlari
4. Odamga vazifa berish
5. Mashina biriktirish
6. Mashinani boshqarish
7. Hayvon biriktirish
8. Hayvonlarni boshqarish
9. Bajarilgan vazifalar
10. Chiqish """)
   
        tanlov = son(input("Buyruqni tanlang: "))
       
        if tanlov == 1:
           odam_qosh()
           
        elif tanlov == 2:
            for raqam, odam in odamlar.items():
                print(f"{raqam}. {odam.ismi} {odam.faamiliya}")
                
        elif tanlov == 3:
            odam = odam_tanla()
            if odam:
                print(odam.info())
            if odam.mashina:
                print(odam.mashina.info())
            for hayvon in odam.hayvonlar:
                print(hayvon.info())
           
            
        
        elif tanlov == 4:
            odam = odam_tanla()
            if odam:
                odam.ish()
                
        elif tanlov == 5:
            shahsiy_m()
            
            
        elif tanlov == 6:
            odam = odam_tanla()
            if odam and odam_tanla():
                print("1. Zavod holatidan chiqarish")
                print("2. yurgizish")
                print("3. Ochirish")
                amal = son(input("Buyruq: "))
                
                if amal == 1:
                    odam.mashina.mash_olish()
                elif amal == 2:
                    odam.mashina.yurgiz()
                elif amal == 3:
                    odam.mashina.ochir()
                else:
                    print("Notogri buyruq.")
            elif odam:
                print("Bu odamga hali mashina biriktirilmagan.")

        elif tanlov == 7:
            hayvon_biriktir()
            
        elif tanlov == 8:
            odam = odam_tanla()
            if odam:
                if not odam.hayvonlar:
                    print("BU odamda hayvon yoq.")
                else:
                    for i, hayvon in enumerate(odam.hayvonlar, 1):
                        print(f"{i}. {hayvon.info()}")
                        
                    raqam = son('Hayvon.raqami: ')
                    if 1 <= raqam <= len(odam.hayvonlar, 1):
                        hayvon = odam.hayvonlar[raqam - 1]
                        hayvon.harakat()
                        
                        if isinstance(hayvon, UyHayvoni()):
                            hayvon.ovqatlantr()
                            
                    else:
                        print("notogri raqam")
        elif tanlov == 9:
            odam = odam_tanla()
            if odam:
                print("Bajarilgan vazifalar: ")
                if odam.bajarildi:
                    for raqam in odam.bajarildi:
                        print(f"- {raqam}-vazifa")
                else:
                    print("hali vazifa baljarilmadi")
                    
        elif tanlov == 10:
            print('Dastur yakunlandi!')
            break
        
        else:
            print("Bundaay buyruq mavjud emas!!")
            
            
            
            
            
boshqaruv()
             
        


                
            
            

            
       
       
    
    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
  




