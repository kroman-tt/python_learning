# # creating  a new file

# f=open("file1.txt","x")
# print(f.name)
# print(f.mode)


#----------------------------------------------


# writing a file

# f = open("file1.txt","w")
# f.write("This is the first line i have written\n ")
# f.write("This is the second line  ")

# f.close()

# # # ##reading a file

# f = open("file1.txt", "r")
# content = f.read() 
# print(content)
# #output of this program (This is the first line i have written
# #  This is the second line)




# f = open("file1.txt", "a")
# f.write("\nthis is newly added line")


# f = open("file1.txt", "r")
# content = f.read() 
# print(content)

# <------------------------------------------------------------------x----------------------------------------------------------->

#it is standard form and we don't need to close this file too as in above

# with open("file1","w") as f:  
#     f.write("it is standard form and we don't need to close this file too as in above")
#     f.write("\n this is second line")

# with open("file1","r") as f:
#     content = f.read()
#     print(content)

# with open("file1", "a") as f:
#     f.write("\n this is appended or added line")

# with open("file1", "r") as f:
#     content = f.read()
#     print(content)    
















