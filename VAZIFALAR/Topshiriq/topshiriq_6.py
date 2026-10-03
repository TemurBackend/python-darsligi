class Teacher:
    def __init__(self, name, surname):
        self.ism = name
        self.familya = surname

    def introduce(self):
        return "Assalomu aleykum hurmatli o'quvchilar!\nMening ismim {self.ism} familyam {self.familya}"


uqituvchi = Teacher("Ali", "Valiyev")

print(uqituvchi.introduce())