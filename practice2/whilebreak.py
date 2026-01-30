#1 problem 
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

#2 problem 
secret = 7

while True:
    guess = int(input("Guess the number: "))

    if guess == secret:
        print("You got it! 🎉")
        break
    else:
        print("Try again!")

#3 problem 
while True:
    text = input("Type something (q to quit): ")

    if text == "q":
        break

    print("You typed:", text)

#4 problem 
secret = 3

while True:
    guess = int(input("Guess a number: "))

    if guess == secret:
        print("Correct!")
        break
    else:
        print("Wrong, try again")

#5 problem 
count = 0

while True:
    print(count)
    count += 1

    if input("Stop? (y/n): ") == "y":
        break
