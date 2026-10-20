class It:
    def __init__(self, nomi, yoshi):
        self.ism = nomi
        self.yosh = yoshi
        self.qadam = 0
        self.buyruqlar = 0
        
    def malumot(self):
       print(f"Kuchukchaning ismi: {self.ism}")
       print(f"Kuchukchaning yoshi: {self.yosh}")
    
    def yur(self):
      self.qadam += 1 
      print("Kuchukcha 1 qadam yurdi")
    
    def yugur(self, yurish_soni):
        while yurish_soni > 0:
            self.qadam += 1 
            yurish_soni -= 1
        
        print("Kuchukcha yurishni tugatti")
    
    def qadamlar(self):
        print(f"{self.yosh} yoshli {self.ism} jami {self.qadam} yurdi. ")
        
    def sakra(self,soni=1):
        for i in range(1, soni):
            print(f"Kuchukcha {i} marotaba sakradi 🦘")

    def help(self):
        print("stop, yugur, yur, yurishlar, sakra, malumot, 'help'")

    def play(self):
            while True:
                buyruq = matn(input("\nBuyruq bering\n>>> "))
                
                if buyruq == "stop":
                    break
                    self.buyruqlar += 1
    
                elif buyruq == "yugur":
                    y = input("yugurish metrini kiriting: ")
                    y = son(y)
                    self.yugur(y)
                    self.buyruqlar += 1
                
                elif buyruq == "yur":
                    self.yur()
                    self.buyruqlar += 1
                
                elif buyruq == "yurishlar":
                    self.qadamlar()
                    self.buyruqlar
                
                elif buyruq == "malumot":
                    self.malumot()
                    self.buyruqlar += 1
                
                elif buyruq == "sakra":
                    n = input("Sakrashlar sonini kiriting: ")
                    n = son(n)
                    self.sakra(n + 1)
                    self.buyruqlar += 1
                    
                elif buyruq == "help":
                    self.help()
                    return help
                
                elif buyruq == "amallar":
                    self.buyruqlar
                
                else:
                    print("bunday buyruq mavzud emas!!!")  
                

print('')
                
 
def son(tekshirsh):
    if tekshirsh.isdigit():
        return int(tekshirsh)
    else:
        print("Iltimos son bilan kiriting !!!:")
    tekshirsh = son(input(">>>"))
    return tekshirsh


def matn(tekshirsh):
    if tekshirsh.isalpha():     
        return tekshirsh
    else:
        print("Iltimos, harf bilan kiriting!")
        
        
            
la = input("Kuchukning ismini kiriting:\n>>>").capitalize()
yo = input(f"{la} ning yoshini kiriting:\n>>")
yo = son(yo)
it = It(la,yo)
print("------------(Buyruqlar)-----------")
print("stop, yugur, yur, yurishlar, sakra, malumot, ''help'' ")

it.play()
