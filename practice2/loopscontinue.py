#1 problem 
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
  #2 problem 
  for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)

#3 problem 
for i in range(3):
    text = input("Type something: ")
    if text == "":
        continue
    print("You typed:", text)
#4 problem 
numbers = [2, -3, 5, -1, 4]

for n in numbers:
    if n < 0:
        continue
    print(n)
#5 problem 
for i in range(1, 6):
    if i == 4:
        continue
    print(i)
