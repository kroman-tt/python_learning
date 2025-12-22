

score=float(input("Enter your score:"))

def pass_fail():
    if score >=50:
        print("Pass")
    else:
        print("Fail")    




def main():
    if score >=90:
        print("You got A+ grade")
    elif score >=80 and score <90:
        print("You got A grade")  
    elif score >=70 and score <80:
        print("You got B+ grade")
    elif score >=60 and score <70:
        print("You got B grade")  
    elif score >=50 and score <60:
        print("You got C+ grade")

pass_fail()
main()









