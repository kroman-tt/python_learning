
#it get false
a=[1,2,3]
b=[1,2,3]
print(f"ans1:{a is b}")
#it get true
a=b=[1,2,3]
print(f"ans2:{a is b}")

a=[1,2,3]
b=a
print(f"ans3:{a is b}")

