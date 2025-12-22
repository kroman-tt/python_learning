# #inheritance



# class parent:
#     hair_color = "golden brown"

# class child(parent):
#     pass

# child1 = child()
# print(child1.hair_color)


#-------------------------------------------------------------------------------------------------------------

class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def info(self):
        print(f"My name is {self.name} and i am {self.age} years old")    


class student(person):
    def __init__(self, name, age, roll):
        super().__init__(name,age)
        self.roll=roll

    def student_info(self):
        print(f"i am a student. my roll no. is {self.roll} ")

class teacher(person):
    def __init__(self,name,age,subject):
        super().__init__(name,age)
        self.subject=subject

    def teach(self):
        print(f"i am a teacher, i teach {self.subject}")

s1=student("ram",19,"34")
s1.student_info()        
s1.info()

t1 = teacher("kroman",20,"science")
t1.teach()
t1.info()









