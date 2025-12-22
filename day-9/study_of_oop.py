# class student:
#     name = "student_name"
#     age = 19


# s1 = student()

# print(s1.name)
# print(s1.age)


# s2 = student()
# print(s2.name,s2.age)



#---------------------------------------------------------------------------------------------------------------------------------------





# class student:
#     #contructor # it is a function called contructor

#     def __init__(self):
#         print("i am called")
#         print(self)
        # self.name = name
        # self.age = age
        # self.roll = roll

# s1 = student()
# print(s1)        
# s2 = student()
# print(s2)
# s1 = student()
# s2 = student()
# s3 = student()
# s4 = student()

#---------------------------------------------------------------------------------------------------------------


# class student:
#     #contructor # it is a function called contructor

#     def __init__(self,name,age,roll):

#         self.name = name
#         self.age = age
#         self.roll = roll

# s1=student("kroman", 19 , "64")
# # s1 ko name k hola?

# print(s1.name)
# print(s1.age)

#------------------------------------------------------------------------------------------------------------



class student:
    #contructor # it is a function called contructor

    def __init__(self,name,age,roll):

        self.name = name
        self.age = age
        self.roll = roll

    def student_info(self):
        print(f"name of student is {self.name}, age is {self.age} and roll number is {self.roll}")    

s1=student("kroman", 19 , "64")

s1.student_info()

























