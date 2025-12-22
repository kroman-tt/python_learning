a="kRoman"
b="!!!bhandari!!!"
c="kroman!!!kroman"
d="kroman !!!!!! bhandari"

blogheading="Welcome to my blog"
print(blogheading.startswith("Welcome")) #it will return true or false
print(blogheading.endswith("blog")) #it will return true or false
print(blogheading.find("zoo")) #it will return index of first letter of word if found else -1
print(blogheading.index("my")) #same as upper line but index gives error if not found
print(c.count("kroman"))
print(blogheading.capitalize())   # it eill capitalize only first letter of first word and rest will be in lower case

print(blogheading.title())  # it will capitalize first letter of each word

print(blogheading.swapcase())  # it will swap the cases of each letter means, lower to upper and upper to lower
print(blogheading.islower())  # it will return true if all letters are in lower case else false
print(blogheading.isupper())  # it will return true if all letters are in upper case else false
print(blogheading.endswith("to",4,10))  # it will return true or false if the given string ends with the given word in the given range

str1 = "Welcome to the Console!!!"
print(str1.center(50))  # it will center the string in the given width by adding spaces on both sides
print(str1.ljust(50,"*"))  # it will left justify the string in
print(str1.rjust(50,"*"))  # it will right justify the string in

str1 = "Welcome to the Console!!!"
print(str1.center(50, "."))  # it will center the string in the given width by adding . on both sides

str2 = "Abracadabra"
countStr = str2.count("a")
print(countStr)

str1 = "WelcomeToTheConsole" #The isalnum() method returns
                                #True only if the entire string only consists of A-Z, a-z, 0-9.
                                #  If any other characters or punctuations are present, then it returns False.
print(str1.isalnum())

str1 = "Welcome" #checking for alphabetic characters
print(str1.isalpha())

str1 = "hello world"  #checking for lowercase characters
print(str1.islower())

str1 = "We wish you a Merry Christmas"
print(str1.isprintable())  #The isprintable() method returns True if all the characters in the string are printable.

#The isspace() method returns True only and only if the string contains white spaces, else returns False.
str1 = "        "       #using Spacebar
print(str1.isspace())
str2 = "        "       #using Tab
print(str2.isspace())
str3 = "\n\n\n"        #using Newline
print(str3.isspace())

str1 = "World Health Organization" 
print(str1.istitle())  #The istitle() method returns True if the string follows the rules of a title.

str2 = "To kill a Mocking bird"
print(str2.istitle()) #The istitle() method returns True if the string follows the rules of a title.


str1 = "WORLD HEALTH ORGANIZATION" 
print(str1.isupper()) #The isupper() method returns True if all the characters are in upper case.

str1 = "Python is a Interpreted Language" 
print(str1.swapcase()) #The swapcase() method returns a string where all the upper case letters are converted to lower case and vice versa.

str1 = "He's name is Dan. Dan is an honest man."
print(str1.title()) #The title() method returns a string where the first character in every word is upper case.


str1 = "Python is a Interpreted Language" 
print(str1.swapcase()) #The swapcase() method returns a string where all the upper case letters are converted to lower case and vice versa.

str1 = "Python is a Interpreted Language" 
print(str1.startswith("Python")) #The startswith() method returns True if the string starts with the specified value, otherwise False.
