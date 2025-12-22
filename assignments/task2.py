#wap to find the factorial of first n numbers( using for loops)

n=int(input("enter nth numbers:"))
sum=0

for i in range(n + 1):
    sum=sum +i
    i+=1
print(sum)    
