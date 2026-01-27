#1 problem 
print(10 + 5)

#2 problem 
sum1 = 100 + 50      
sum2 = sum1 + 250    
sum3 = sum2 + sum2  

#3 problem 
x = 12
y = 5

print(x // y)

#4 problem 
x = 15
y = 4

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)

#5 problem 
numbers = [1, 2, 3, 4, 5]
count = len(numbers)
if count > 3:
    print(f"List has {count} elements")

if (count := len(numbers)) > 3:
    print(f"List has {count} elements")