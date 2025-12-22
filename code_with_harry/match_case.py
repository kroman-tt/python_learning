x=int(input("Enter your age:"))

match x:
    case 18:
        print("you are allowed to vote")
    case _ if x<18:
        print("you are not allowed to vote")
    case _ if x>=18:
        print("you are allowed to vote")    
    case 100:
        print("not valid")
        
    case _ :
        print("invalid")




















