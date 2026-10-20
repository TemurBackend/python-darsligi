
class Sutudent:
    def __init__(self,name, age, grade):
        self.name = name
        self.age = age 
        self.grade = grade # 0 - 100
        
    def get_grade(self):
        return self.grade
    
        
class Corse:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []
        # self.is_active = False
        
    def add_students(self, student):
        if len(self.students)  < self.max_students:
            self.students.append(student)
            return True
        return False
    
    def get_average_grade(self):
        value = 0
        for student in self.students:  
            value += student.get_grade()
        return value / len(self.students)

s1 = Sutudent("tim", 25, 95)
s2 = Sutudent("bell", 56, 75)
s3 = Sutudent("jimi", 28, 64)

corse = Corse("skince", 2)
corse.add_students(s1)
corse.add_students(s2)
corse.add_students(s3)
corse.get_average_grade()

print(corse.get_average_grade())
# print(corse.students[0].name)