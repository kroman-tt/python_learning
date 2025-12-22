#balance = 1000.00
#  deposit = 250.00
#  service_fee = 10.50
#  interest_rate = 1.05 ( 5% growth)
#  3. Question: Perform the following operations using assignment operators:
#  1.Apply the deposit using the += operator.
#  2.Subtract the service_fee using the -= operator.
#  3.Apply the interest_rate multiplier (for growth) using the *= operator.
#  4.Initialize a new variable, shares, with the final balance. Then, use the //=
#  operator on shares to determine how many full $100 units (shares) can be
#  purchased from that amount.
#  Output: Print the balance after steps 1, 2, and 3, and the final integer value of
#  shares after step 4.

balance=1000.00
deposit=float(input("Enter deposit amount:"))
service_fee=10.50
interest_rate=0.05 # 5% interest
balance+=deposit
balance-=service_fee
interest_amount=balance*interest_rate 
balance+=interest_amount
print(f"Your final balance after deposit, service fee and interest is rs:{balance}" )
print("The value of 1 share is rs 5")
share=balance//5
print("You can buy",share, f"shares with your final balance of rs:{balance}",)


