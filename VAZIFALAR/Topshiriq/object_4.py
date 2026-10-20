class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def show(self):
        print(f"i am {self.name} and i am {self.age} years old")
        
        
    def speak(self):
        print("I don't know what Insay ")
        
class Cat(Pet):
    def __init__(self,name, age, color):  
        super().__init__(name, age)
        self.color = color
        # self.name = name
        # self.age = age    
    
    def speak(self):
        print ("meow")
        
    def show(self):
        print(f"i am {self.name} and i am {self.age} years old and I am {self.color}")
        
    # def __init__(self,name, age): 
    # self.name = name
    # self.age == age
class Dog(Pet):
    def speak(self):
        print("Bark") 
        
    # def __init__(self,name,age):
    #     self.name = name
    #     self.age = age
        
class Fish(Pet):
    pass    
    
p = Pet("Tim", 19)
# p.show()
p.speak()
c = Cat("bell", 34, "Brown")
c.show()
c.speak()
d = Dog("jill", 25)  
d.speak()
# f = Fish("nemo", 10)
# f.speak()
        
        