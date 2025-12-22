#KBC Game 1.3

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
questions = ["what  is 2+2?","if x=2 and y=-3 then, x+y is","which animal is national animal of Nepal?"]

# Making another list for options of questions 
options = [
    "a)3   b)4 \n"
    "c)5   d)10",
    "a)2   b)0 \n"
    "c)-1   d)-5",
    "a)cow   b)goat \n"
    "c)dog   d)cat"]

# Making list for answer

answers = ["b","c","a"]

number_of_questions = len(questions)
price=0
for i in range(0,number_of_questions):
    question = questions[i]
    option = options[i]
    print(question)
    print(option)
    answer=input("Answer:")
    price +=1000
    if answer == answers[i]:
        print("\n Wanna continue the game? [yes/no] ")
        choice = input("->")
        if choice == "yes":
            pass
        else:
            print(f"Congratulation! you won rs {price} ")
            break
    else:
        print("Incorrect answer, you loss!") 
        break








