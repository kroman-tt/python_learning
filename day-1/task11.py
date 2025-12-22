#wap to calculate the actual bill to be paid by asking the user about the number of units bought and price per each unit after deducting discount and adding tax.
a=int(input("enter the unit's of good:"))
b=int(input("enter the pirce of good:"))
total=a*b
print(f"the total value without discount and tax:{total}")
d=int(input("enter discount value:"))

after_discountamount=total-(d/100)*total
tax=after_discountamount+0.08*after_discountamount
print(f"the total value after discount and tax:{tax}")