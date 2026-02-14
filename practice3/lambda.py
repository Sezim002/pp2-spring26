#1 problem 
x = lambda a : a + 10
print(x(5))
 
 #2 problem 
x = lambda a, b : a * b
print(x(5, 6))
#3 problem 
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))
#4 problem 
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)

#5 problem 
words = ["apple", "pie", "banana", "cherry"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)


