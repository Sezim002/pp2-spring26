#1 
nums = [5, 10, 15, 20]

result = list(map(lambda x: x * 2, filter(lambda x: x > 10, nums)))
print(result)
#2
from functools import reduce

nums = [1, 2, 3, 4]
total = reduce(lambda a, b: a + b, nums)
print(total)
#3
students = ["Tom", "Jane"]
grades = [88, 92]

for i, (name, grade) in enumerate(zip(students, grades)):
    print(i, name, grade)