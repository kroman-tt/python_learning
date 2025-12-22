#wap to find the sum of first n numbers.(using while)


n=int(input("Enter nth number:"))

i=0
sum=n
while i<n :
    sum=sum+i
    i+=1
print(sum)       #this code is very slow for big numbers

#------------------------------------------------------------------

# so, in such case use math formulas

# n=int(input("Enter nth numbers:"))

# sum=n*(n+1)//2
# print(sum)










