#1 problem 
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

#2 problem 
mystr = "Sezim"

for x in mystr:
  print(x)

#3 problem 
class MyNumbers:
  def __iter__(self):
    self.a = 8
    return self

  def __next__(self):
    if self.a <= 96:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)

  #4 problem
  numbers = [10, 20, 30]

it = iter(numbers)

print(next(it))  # 10
print(next(it))  # 20
print(next(it))  # 30

#5 problem 
class ReverseIterator:
    def __init__(self, data):
        self.data = data
        self.index = len(data) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= 0:
            value = self.data[self.index]
            self.index -= 1
            return value
        else:
            raise StopIteration

# Қолдану
numbers = [1, 2, 3, 4, 5]

for num in ReverseIterator(numbers):
    print(num)
