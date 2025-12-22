# a=int(input("enter anumber:"))
# b=int(input("enter a number:"))

# def spd():
#     print(f"the sum of {a} and {b} is {a+b}")
#     print(f"the sub of {a} and {b} is {a-b}")
#     print(f"the product of {a} and {b} is {a*b}")
#     print(f"the division of {a} and {b} is {a/b}")


# spd()    




def add():
    return a+b
def sub():
    return a-b
def product():
    return a*b
def division():
    return a/b
a=float(input("enter a number:"))
b=float(input("enter a number:"))

def main(): 
    op=input("enter a operator (+,-,*,/):")
    
    if op == "+":
        print(f"sum is {add()}")
    elif op == "-":
        print(f"sub is {sub()}")
    elif op == "*":
        print(f"product is {product()}")  
    elif op == "/":
        print(f"division is {division()}")
    else :
        print("enter suitable operator!") 








main()    













