#1 problem
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#2 problem 
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

#3 problem 
# вернёт False:

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

#4 problem 
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

  #5 problem 
  print(10 > 9)
print(10 == 9)
print(10 < 9)