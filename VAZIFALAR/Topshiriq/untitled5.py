class It:
    def __init__(self, ism, yosh):
        self.ism = ism
        self.yosh = yosh
        self.qadam = 0
        self.buyruq_soni = 0

    def malumot(self):
        print(f"Ismi: {self.ism}")
        print(f"Yoshi: {self.yosh}")

    def yu(self):
        self.qadam += 1
        print("It 1 qadam yurdi")

    def yur(self, son):
        while son > 0:
            self.qadam += 1
            son -= 1
        print("It yurishni tugatdi")

    def qadamlar(self):
        print(f"It {self.qadam} qadam yurdi")

    def sakra(self, son=1):
        for i in range(son):
            print("It sakradi!")

    def play(self):
        while True:
            buyruq = input("Buyruq bering: ")

            if buyruq == "stop":
                break

            self.buyruq_soni += 1

            if buyruq == "yu":
                self.yu()

            elif buyruq.startswith("yur"):
                son = int(buyruq.split()[1])
                self.yur(son)

            elif buyruq == "sakra":
                self.sakra()

            elif buyruq.startswith("sakra"):
                son = int(buyruq.split()[1])
                self.sakra(son)

            elif buyruq == "qadam":
                self.qadamlar()

            elif buyruq == "malumot":
                self.malumot()

            else:
                print("Bunday buyruq mavjud emas!")

        print(f"Siz {self.buyruq_soni} marta buyruq berdingiz.")
        
it = It("Bobik", 3)
it.play()