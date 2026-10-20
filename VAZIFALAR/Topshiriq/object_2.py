# def hello():
#     print("hello")
    
# x = 1 
# print(type(x))

# x = 1
# y = 5 
# x = "hello"    
# print(x + y)

# string = "hello"
# x = 1
# print(x.upper())

class dog:
    def __init__(self, name,age):
        self.name = name
        # print(name)
        self.age = age
        
    def add_one(self,x):
        return x + 1
                               
    def bark(self):
        print(("brak"))
        
    def get_name(self):
        return self.name
        
    def get_age(self):
        return self.age
    def set_age(self, age):
        self.age = age
        
     
dogs_name = ["tim", "bell"] 
dogs_age = [32,14]   
        
        
        
# d = dog("tim",25)
# print(d.get_name())
# d2 = dog("bili",55)
# print(d2.get_name())

d = dog("tim",28)
d.set_age(25)
print(d.get_age())

# d = dog()
# d.bark()
# print(d.add_one(5))
# print(type(d))


   