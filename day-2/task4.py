""".Write the single line of code using (AND) and (NOT) that sets a variable
book_flight to True if (flight_cost is under the MAX_PRICE) AND (the
destination is NOT "Asia").
Output: Print the final boolean value of book_flight"""

Max_Price=1000
flight_cost=500
destination=(input("Enter your destination:").upper())    # the (.upper()) ir use to make the entered stiring to be in upper case it is helpful to create user friendly projects 
#check=destination!="asia"
book_flight=(flight_cost<Max_Price)and(not destination=="ASIA")
print(book_flight)