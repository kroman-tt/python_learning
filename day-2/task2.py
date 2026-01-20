#password check garney task 
# it is use to make password for frist time while registering or siningup

password=(input("Enter a password:"))
passwordlength=len(password)
min_lenght=8
max_lenght=16
if min_lenght<=passwordlength<=max_lenght:
    print("Valid password")
else:
    print("Invalid password")