class Talaba:
    def __init__(self,ism,familiya,tyil):
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        
    def get_name(self):
        return self.ism
    
    def get_age(self,yil = 2026):
        return yil - self.tyil
    
    def get_famil(self):
        return self.familiya
 
    def tanishtr(self):     
        return f"ismim {self.ism} {self.familiya}, tugulgan yilim {self.tyil} "        
        
talaba1 = Talaba("saman", "liyev", 2007)
talaba2 = Talaba("abu", "araliyev", 2005)
talaba3 = Talaba("alm", "ydaraliyev", 2018)
talaba4 = Talaba("asad", "aydaraliyev", 2008)
talaba5 = Talaba("bek", "iyev", 2008)

talaba1.tanishtr()
talaba1.get_name()
talaba4.get_age()
talaba2.get_famil()
