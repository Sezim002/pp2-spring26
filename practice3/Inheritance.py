#1 problem 
class Laptop:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def discount(self, percent):
        self.price -= self.price * percent / 100

l1 = Laptop("Dell", 1000)
l1.discount(10)
print(l1.price)

#2 problem 
class Employee:
    company = "TechCorp"  # Class variable

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary  # Instance variable

e1 = Employee("Alice", 5000)
e2 = Employee("Bob", 6000)

Employee.company = "NewTech"

print(e1.company)
print(e2.company)

#3 problem 
class Book:
    def __init__(self, title):
        self.title = title

b1 = Book("Python Basics")
b1.title = "Advanced Python"

print(b1.title)

#4 problem 
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

acc = BankAccount("John", 1000)
acc.deposit(500)
acc.withdraw(200)
print(acc.balance)

#5 problem 
class Device:
    def power_on(self):
        print("Device is ON")

class Laptop(Device):
    def open_lid(self):
        print("Lid opened")

l1 = Laptop()
l1.power_on()
l1.open_lid()
