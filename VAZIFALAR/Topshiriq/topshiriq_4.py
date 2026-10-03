
class Talaba:
    """Talaba nomli klass yaratamiz"""
    def __init__(self,ism,familiya,tyil):
        """Taalabaning hususiyatlari """
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        self.bosqich = 1
        
    def get_name(self):
        return self.ism
        
    def get_famil(self):
        return self.familiya
        
    def set_bosqich(self,yangi_bosqich):
        """talaba bosqichini ozgarirish"""
        self.bosqich = yangi_bosqich
    
    def update_bosqich(self):
        self.bosqich += 1
        return self.bosqich
        
    def get_info(self):     
        return f"{self.ism} {self.familiya}. {self.bosqich}-bosqich talabasi"        



talabalar = {}

for i in range(1, 4):
    ism = input(f"{i}-ismingiz: ")
    if ism.isdigit():
        print("Iltimos ismni ''Harflar'' yordamida kiriting!")
        ism = input(f"{i}-ismingizni qayta kiriting: ")

    fam = input(f"{i}-familiyangiz: ")
    if fam.isdigit():
        print("Iltimos familiyani ''Harflar'' yordamida kiriting!")
        fam = input(f"{i}-familiyangizni qayta kiriting: ")
        
    yil = input(f"{i}-yilingiz: ")
    if not yil.isdigit():
        print("Iltimos, yilni ''Son'' bilan kiriting!")
        yil = input(f"{i}-yilingizni qayta kiriting: ")
    yil = int(yil)
    talabalar[f"{ism}-{i}"] = Talaba(ism, fam, yil)

    print()


n = 1   
for ism, talabal in talabalar.items():
    print(f'----------------{n}----------------')
    print(f"{ism}, {talabal.get_info()}")
    print(f"{ism}, {talabal.get_name()}")
    print(f"{ism}, {talabal.get_famil()}")
    print(f"{ism}, {talabal.update_bosqich()}")
    print('-----------------------------------')
    print()
    n += 1
raqam = int(input("Qaysi talabaning bosqichini o'zgartirmoqchisiz? "))


talabalar = list(talabalar.values())


if len(talabalar) >= raqam and raqam >= 1:
    bosqich = int(input("Yangi bosqichni kiriting: "))
    talaba = talabalar[raqam - 1]
    talaba.set_bosqich(bosqich)
    
    print("Bosqich muvaffaqiyatli o'zgartirildi!")
    
    son = int(input("O'zgarishni ko'rish uchun 1 ni bosing, chiqish uchun 0 ni: \n>>"))
    
    if son == 1:
        print(talaba.get_info())
    else:
        print("Chiqish muofiqiyatli tugallandi. Salamot boling😊")
else:
    print("Bunday raqam bilan talaba mavjud emas!")
    
    
    
    