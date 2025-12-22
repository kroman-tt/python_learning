#wirte a proogram to calculate the actual amount to be paid by deducting the discount using discount rate only if the amount is greater then 1000,
# otherwise just print the output as "thank you for shoppinhg!"



amount_of_goods=float(input("Enter the value of goods:"))


discount_rate=0.10
discount_rate2=0.05

if amount_of_goods>1000:

    actual_amount=amount_of_goods-discount_rate*amount_of_goods

    print(f"the total amout to be paid after deducting discount amount:{actual_amount}")
    
else:
    actual_amount2=amount_of_goods-discount_rate2*amount_of_goods
print(f"the total amout to be paid after deducting discount amount:{actual_amount2}")






    
print("thankyou for shopping!")






