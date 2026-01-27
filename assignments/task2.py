#wap to find the factorial of first n numbers( using for loops)

n=int(input("enter nth numbers:"))
# sum=1
# # range(1, 5)   # gives 1, 2, 3, 4 (NOT 5)
# # range(1, 6)   # gives 1, 2, 3, 4, 5 (NOT 6)
# for i in range(1,n + 1):
#     sum=sum * i
    
# print(sum)    


# easy way to find factorial using math module 
import math
result = math.factorial(n)
print(result)