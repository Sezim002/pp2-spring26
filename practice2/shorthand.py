#1 problem 
a = 2
b = 330
print("A") if a > b else print("B")

#2 problem 
a = 10
b = 20
bigger = a if a > b else b
print("Bigger is", bigger)

#3 problem 
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")
#4 problem 
x = 15
y = 20
max_value = x if x > y else y
print("Maximum value:", max_value)
#5 problem 
username = ""
display_name = username if username else "Guest"
print("Welcome,", display_name)
