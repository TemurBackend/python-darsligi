class dog:
    def __init__(self,ism,yoshi):
        self.ism = ism
        self.yoshi
        self.qadam = 0
        
    def malumot(self):
        print(f'Itning ismi: {self.ism}')
        print(f'Itning yoshi: {self.yosh}')
    def  yur(self):
        self.qadam += 1
        print("It 1 qadam yurdi !!!")
        
    def yugur(self,son):
        while son > 0:
            self.qadam +=1
            son -= 1
            
        print("It yurishni tugatti !!!")
        
    def qadamlar(self):
        print(f"Yurgan qadamlar: {self.qadam}")
        
    def jami(self):
        jami = 0
        qadam = self.qadam
        
        while qadam > 0:
            jami += 1
            qadam -= 1
            
        print(f"Jami qadam {jami}")
        
itvacha = input("ITning ismini kiriting")
       
        
