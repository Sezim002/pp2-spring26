#1 problem 
i = 1
while i < 6:
  print(i)
  i += 1

#2 problem 
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

  #3 problem 
  i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

  #4 problem 
  i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

#5 problem 
i = 0
while i < 9:
  i += 1
  if i == 3:
    continue
  print(i)
