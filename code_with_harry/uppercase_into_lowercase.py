a="kRoman"
b="!!!bhandari!!!"
c="kroman!!!kroman"
d="kroman !!!!!! bhandari"
print(a.upper()) # it will convert all letters to upper case
print(a.lower()) # it will convert all letters to lower case
print(b.strip("!")) # it will remove ! from starting and ending only
print(b.rstrip("!")) # it will remove ! from right side only
print(b.lstrip("!")) # it will remove ! from left side only
print(c.replace("kroman","bahndari")) # it will replace all the occurences of kroman with bahndari
print(d.split(" ")) # it will split the string from space and return list of words



