# dict1={}
# print(type(dict1))  # <class 'dict'>
# print(dict1)

# data are structured in key-value pair
# dict2={"name":"kroman","age":23,}
#key = value
# dictionery -> word and its corresponding meaning
# here is corresponding value of key "name" is "kroman" and key "age" is 23
# print(dict2)

# dict3={
#     "name":"kroman",    
#     "age":19,
#     "work": "student",
# }
# print(dict3)

# print(dict3["name"])  # to access the value of the key "name"

# print(dict3["age"])  # to access the value of the key "age"
# print(dict3["work"])  # to access the value of the key "work"

# # to add new key-value pair in the dictionery
# dict3["college"]="kathmandu university"
# print(dict3)

# print(dict3.keys())  # to get all the keys of the dictionery
# print(dict3.values())  # to get all the values of the dictionery

# print(dict3.items())  # to get all the key-value pairs of the dictionery as tuple

# nested dictionery, dictionery inside dictionery

# student={
#     "student1":{
#         "name":"kroman",
#         "age":19,
#         "work":"student",
#         "marks":{
#             "math":90,
#             "science":85,
#             "english":88,
#         }
#     },"student2":{
#         "name":"ram",
#         "age":20,
#         "work":"developer",
#     }
# }
# print(student)


# student={
#     "name":"kroman",
#     "age":19,   
#     "work":"student",
#     "marks":{   
#         "math":90,
#         "science":85,
#         "english":88,
#     }
# }

    # iterate through the keys
# for i in student.keys():
#print(i) # it will print all the keys of the dictionery


    # iterate through the values
# for i in student.values():
#     print(i) # it will print all the values of the dictionery


    # iterate through the key-value pairs
# for i,j in student.items():
#         print(f"The key is: {i} and the value is: {j}") 
#         # it will print all the key-value pairs of the dictionery





# in case of duplicate keys, the last value will be considered
# so we have to put unique keys in the dictionery
# student2={
#     "name":"kroman",
#     "age":19,   
#     "work":"student",
#     "marks":{   
#     "math":90,
#     "science":85,
#     "english":88,
#     },
#     "name":"kroman123"}
# print(student2)

# to update the value of a key in the dictionery
# student = {
#     "name": "kroman",
#     "age": 19,
#     "work": "student"
# }
# print("Original dictionary:", student)

# # Method 1: Using direct assignment
# student["age"] = 20  # updating the value of key "age"
# print("After updating age:", student)

# # Method 2: Using update() method
# student.update({"work": "developer", "city": "Kathmandu"})  # updates existing keys and adds new ones
# print("After using update():", student)



















