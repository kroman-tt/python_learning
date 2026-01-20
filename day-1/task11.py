#wap to calculate the actual bill to be paid by asking the user about the number of units brought and enter the price per each unit after deducting discount and adding tax.
#this is for accountent of any shop or market
# A little demo hehe!
a=int(input("enter the unit's of good:"))
b=int(input("enter the pirce of good:"))
total=a*b
print(f"the total value without discount and tax:{total}")
d=int(input("enter discount value:"))

after_discountamount=total-(d/100)*total
tax=after_discountamount+0.08*after_discountamount
print(f"the total value after discount and tax:{tax}")

# ------------------------------------------------------------------------------x--------------------------------------------------------

# simple version of upper code->

# a=int(input("enter the unit's of good:"))
# b=int(input("enter the pirce of good:"))
# print(f"the total value without discount and tax:{a*b}")
# d=int(input("enter discount value:"))
# after_disamt=(a*b)-(d/100)*(a*b)
# tax=after_disamt+0.08*after_disamt
# print(f"the total value after discount and tax:{tax}")