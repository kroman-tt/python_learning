#  2. Question: Write two separate print statements:
#  Use the in operator to check if employee_id is in approved_ids.
#  Use the not in operator to check if "Z999" is not in approved_ids.
#  approved_ids = ["A101", "B205", "C303", "D410"]
#  employee_id = input("Enter employee ID: ")


employee_id=input("Enter employee ID:")

approved_id=["A101","B205","C303","D410"]

print(employee_id in approved_id)    #it will show true if the entered id is matched with list of id and shows false if not matched

print(employee_id not in approved_id)  #it will show false is the entered id is matched wiht list of id and shows true if not matched 