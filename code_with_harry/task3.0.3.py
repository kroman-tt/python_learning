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
questions = ["1. what  is 2+2?",
            "2. if x=2 and y=-3 then, x+y is",
            "3. which animal is national animal of Nepal?",
            "4. which bird is national bird of Nepal?",
            "5. What is the name of the ancient, massive ocean that surrounded pangea supercontinent",
            "6. What comes next in the series? \n 2, 6, 12, 20, 30, ?",
            "7. If APPLE = 50, BANANA = 33, then ORANGE = ? \n(Sum of letter positions) ",
            "8. Which word is different from the others?",
            "9. If CAT = 24, DOG = 26, then COW = ?\n (Sum of letter positions)",
            "10. Book : Reading :: Food : ?",
            "11. A person walks 10 m north, then 10 m east, then 10 m south.\nHow far is he from the starting point?",
            "12. Which number is different?",
            "13. If 1 = 3, 2 = 6, 3 = 9, then 4 = ?",
            "14. All roses are flowers. Some flowers fade quickly.\nWhich statement is definitely true?",
            "15. A man looks at a photograph and says:\n “I have no brothers or sisters, but that man’s father is my father’s son.”\n Who is the man in the photograph?"]

# Making another list for options of questions 
options = [
    "a)3   b)4 \n"
    "c)5   d)10",
    "a)2   b)0 \n"
    "c)-1   d)-5",
    "a)cow   b)goat \n"
    "c)dog   d)cat",
    "a)sparrow b)parrot \n"
    "c)danphe  d)peacock",
    "a)Eurasia b)Panthalassa \n"
    "c)Mesozos d)paleozos",
    "a) 40  b) 42\n"
    "c) 44  d) 48",
    "a) 60  b) 61 \n"
    "c) 66  d) 69",
    "a) Square  b) Rectangle \n"
    "c) Triangle d) Circle",
    "a) 45  b) 47 \n"
    "c) 49  d) 51",
    "a) Cooking b) Eating \n"
    "c) Hunger  d) Taste",
    "a) 0 m   b) 20 m \n"
    "c) 10 m  d) 30 m",
    "a) 2  b) 3\n"
    "c) 5  d) 9",
    "a) 10  b) 11 \n"
    "c) 12  d) 13",
    "a) All roses fade quickly b) Some roses fade quickly \n"
    "c) Some flowers are roses d) All flowers are roses",
    "a) His son    b) His cousin \n"
    "c) His nephew d) Himself"]

# Making list for answer

answers = ["b","c","a","c","b","b","c","d","b","b","c","d","c","c","a"]

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








