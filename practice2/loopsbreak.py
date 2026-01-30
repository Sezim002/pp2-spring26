#1 problem 
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
  
  #2 problem 
  for i in range(1, 10):
    if i == 5:
        break
    print(i)
#3 problem 
for i in range(5):
    text = input("Type something (exit to stop): ")
    if text == "exit":
        break
#4 problem 
numbers = [3, 7, 9, 2]

for n in numbers:
    if n == 9:
        print("Found 9!")
        break
#5 problem 
for i in range(10):
    print(i)
    if i == 3:
        break
