# #inheritance

# class parent:
#     hair_color = "golden brown"

# class child(parent):
#     pass

# child1 = child()
# print(child1.hair_color)


#-------------------------------------------------------------------------------------------------------------

class person:
    def __init__(self,name,age):    # method to initialize  or constructor
        self.name = name
        self.age = age
    def info(self):
        print(f"My name is {self.name} and i am {self.age} years old")    # this is method of parent class which can be used by child class also like this info is use for all person who can be 
# teacher as well as student and any one so to avoid repetition of code we use inheritance like this 

class student(person):
    def __init__(self, name, age, roll):      # constructor of child class
        super().__init__(name,age)       # to call parent class init method  or constructor
        self.roll=roll

    def student_info(self):
        print(f"i am a student. my roll no. is {self.roll} ")

class teacher(person):
    def __init__(self,name,age,subject):
        super().__init__(name,age)
        self.subject=subject

    def teach(self):
        print(f"i am a teacher, i teach {self.subject}")

s1=student("ram",19,"34")     # s1 is an object of student class and student is child class of person class and we giving value to student class constructor
s1.student_info()        
s1.info()
print("\n")
t1 = teacher("kroman",20,"science")      # t1 is an object of teacher class and teacher is child class of person class and we giving value to teacher class constructor
t1.teach()
t1.info()

