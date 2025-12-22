#list
# list1=[1,2,3,4]
# print(type(list1)) #list is collection of element

#list can have multiple data types
# list2=[1,"kroman",3.5,]

# list3=[]
# print(list3)
# # print(type(list3))


# # to add the element in the list we use append function
# list3.append(23)
# list3.append("kroman")
# list3.append(3.5)

# print(list3)


# to check mutability 
# list is mutable means we can change the element of list
#to increase the element in the list we can use append function
# to remove the element from the list we can use remove function or (discard of not throw error)
# to change the element of the list we can use index and assign new value

#checking mutability
# list4=[13,24,35]

# list4[0]=99  #changing the first element of the list
# print(list4) #it is the proof that list is mutable

# list4.append("kroman") #adding element to the list
# print(list4)

# list4.remove(24) #removing element from the list
# print(list4)



# list5 =["kroman","bhandari","python","developer,python"]
# print(list5) #duplicate elements are allowed in the list

# to find the index of the element in the list we can use index function
# index1 = list5.index("python") #it will return the index of first occurence of the element
# print(index1)
# index2 = list5.index("java") #it will give error if the element is not found
# print(index2) 
# to avoid error we can use try and except block
# try:
#     index2 = list5.index("java")
#     print(index2)
# except ValueError:
#     print("Element not found in the list")
# to count the number of occurences of the element in the list we can use count function
# count1 = list5.count("python")
# print(count1)
# count2 = list5.count("java")
# print(count2)
# to sort the list we can use sort function
# list_g=[5,9,7,2,4,1,0]
# list.sort(list_g)
# print(list_g)

#lets see insert method
# list6 = [12,34,56,78]

# list6.append(90) #it will add the element at the end of the list
# print(list6)

# list6.insert(2,45) #it will add the element at the given index
# print(list6)

#extend method
# list7 =[1,2]
# list7.extend([100,200,300]) #it will add the elements of the given list to the end of the list
# print(list7) 


# list8 =[10,60,30,40,50]


# list.sort(list8) #it will sort the list in ascending order
# print(list8)

# ###reverse method

# list8.sort(reverse=True) #it will sort the list in descending order
# print(list8)


