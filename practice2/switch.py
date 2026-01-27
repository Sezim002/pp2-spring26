#1 problem
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

#2 problem
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

  #3problem 
  x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

#4 problem 
core = 85
attendance = 90
submitted = True

if score >= 60:
  if attendance >= 80:
    if submitted:
      print("Pass with good standing")
    else:
      print("Pass but missing assignment")
  else:
    print("Pass but low attendance")
else:
  print("Fail")

#5 problem 
age = 16

if age < 18:
  pass # TODO: Add underage logic later
else:
  print("Access granted")
