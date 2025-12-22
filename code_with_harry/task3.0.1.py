#KBC Game 1.0

# Rules of this game
print("            Welcome! to KBC game\n")
print("      Some rules of this game are explained below!")

print(" 1) If your answer is correct then, you won rs1000 per Q and A.\n " 
    "2) After you won then you can leave with the you won upto where you won  \n " 
    "3) Or you can continue the game to win more money\n" 
    " 4) if you lose next round then you loss all money that you win till now and you get nothing\n"
    " 5) So, choose what you want to do at your own risk!\n" 
    " 6) If you want to play next round in you own risk then type yes\n" \
    "    or if no then type no in choice section\n" 
    "                    Best of luck!")



# Making the list of 10 questions
ten_questions = ["what  is 2+2?","if x=2 and y=-3 then, x+y is","which animal is national animal of Nepal?"]

# Making another list for options of questions 
options=[
    "a)3   b)4 \n"
    "c)5   d)10",
    "a)2   b)0 \n"
    "c)-1   d)-5",
    "a)cow   b)goat \n"
    "c)dog   d)cat"]

# Initializing the variable 
question = ten_questions[0]
option = options[0]

# Printing first question and their options and taking input from player
print(question)
print(option)
answer=input("Answer:")

# checking answer
if answer=="b":
    print("\n     Wanna continue or not?\n")
    choice=input("choice->")
    if choice=="yes":
        question = ten_questions[1]
        option = options[1]
        print(question)
        print(option)
        answer=input("Answer:")    
    else:
        print("congratulation! You won Rs1,000")
    if answer=="c":
        print("\n     Wanna continue or not?\n")
        choice=input("choice->")
        if choice=="yes":
            question = ten_questions[2]
            option = options[2]
            print(question)
            print(option)
            answer=input("Answer:")
        else:
            print("You won Rs2,000 congratulation!")    
    else:
        print("you loss all money. try again!")
    if answer == "a":
        print("\n     Wanna continue or not?\n")
        choice=input("choice->")
        if choice=="yes":
            question = ten_questions[3]
            option = options[3]
            print(question)
            print(option)
            answer=input("Answer:")
        else:
            print("You won Rs3,000 congratulation!")    
    else:
        print("you loss all money. try again!")    

else:
    print("Your answer is incorrect! better luck next time.")
    






























