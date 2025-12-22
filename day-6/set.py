# set1= {}
# print(type(set1))  # <class 'dict'>


# set2 = set()
# print(type(set2))  # <class 'set'>



# set3 = {1,2,3,4,4,5}
# print(set3) 
# print(type(set3))  # <class 'set'> # set is collection of unique elements 
# their isn't duplicate element in the set



# list1 = [1,2,3,4,5,1,2,3]
# tuple1 = (1,2,3,4,5,1,2,3)
# set4 = {1,2,3,4,5,1,2,3}

# print("List:", list1)  # List: [1, 2, 3, 4, 5, 1, 2, 3]
# print("Tuple:", tuple1)  # Tuple: (1, 2, 3, 4, 5, 1, 2, 3)
# print("Set:", set4)  # Set: {1, 2, 3, 4, 5}


# set5 = {1,2,3}
# set6 = {2,4,5}

# #union
# set7 = set5.union(set6)
# print("Union:", set7)  # Union: {1, 2, 3, 4, 5}

# #difference
# set8 = set5.difference(set6)
# print("Difference:", set8)  # Difference: {1, 3}

# #to add the element in the set
# set5.add(6) 
# print("Set after adding element:", set5)  # Set after adding element: {1, 2, 3, 6}

# #to remove the element from the set
# set5.remove(6)
# print("Set after removing element:", set5)  # Set after removing element: {1, 3, 6}

# set9 = {1,2,3,4,5}
# # set9.reomve(100)  # it will give error because 100 is not present in the set
# # set9.discard(100)  # it will not give error even if 100 is not present in the set

# print(set9)


# 1. ITERATE through the set
# my_set = {10, 20, 30, 40, 50}

# for value in my_set:
#     print(value)

# # 2. CONVERT to list and access by index
# my_set = {10, 20, 30, 40, 50}
# my_list = list(my_set)
# print(my_list[0])  # Print first element
# print(my_list[2])  # Print third element

# # 3. CHECK if value EXISTS
# my_set = {10, 20, 30, 40, 50}
# if 30 in my_set:
#     print(30)  # Print if it exists

# # 4. USE pop() to get and remove a specific element
# my_set = {10, 20, 30, 40, 50}
# value = my_set.pop()  # Gets an arbitrary element
# print(value)

# # 5. FILTER and print specific values
# my_set = {10, 20, 30, 40, 50}
# for value in my_set:
#     if value > 25:
#         print(value)  # Print values greater than 25