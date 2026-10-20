from uuid import uuid4

class Avto:
    num_avto = 0  # mana shu yetishmayapti
    
 
    def __init__(self, make, model, rang, yil, narh, km=0):
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narh = narh
        self.__km = km
        self.__id = uuid4()

        Avto.num_avto += 1
    def __add__(self, b):
        self.__km += b
        return self
    
    def __len__(self):
        return self.__km
    
    def __str__(self):
        return ""
    
    def get_km(self):
        return self.__km

    def get_id(self):
        return self.__id

    def add_km(self, km):
        if km >= 0:
            self.__km += km
        else:
            print("Mashina kilometrini kamaytirib bo'lmaydi")


avto1 = Avto("GM", "Malibu", "qora", 2020, 40000, 1000)

avto2 = Avto("BMW", "M5", "Black", 2020, "2500000")

print(avto2.get_km())
avto2 += 6
print(avto2.get_km())