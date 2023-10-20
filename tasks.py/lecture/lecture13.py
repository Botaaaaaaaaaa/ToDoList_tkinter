# class Car:
#     def __init__(self,country,model,year):
#         self.country=country
#         self.model=model
#         self.year=year

#     def start_to_walk(self):
#         print(f"{self.model} is starting to walk")

#     def open_the_window(self):
#         print(f"{self.model} open the window")

#     def description(self):
#         print(f"{self.country} {self.model} {self.year}")

# car=Car("Italy","Ferrari",2022)
# car.start_to_walk()
# car.open_the_window()
# car.description()

# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def get_info(self):
#         pass
# class Employee(Person):
#     def __init__(self,name,age, salary):
#      self.salary=salary
#      super().__init__(name,age)
    
#     def get_info(self):
#          print(f"{self.name} is {self.age} years old")
#          print(f"{self.name} earns {self.salary} a month")
# person=Employee("Omar",40,"1000$")
# person.get_info()

# class Animal:
#     def __init__(self,name):
#         self.name=name
#     def speak(self):
#         pass

# class Dog(Animal):
#     def speak(self):
#         print(f"{self.name} speak Gaf Gaf")

# class Cat(Animal):
#     def speak(self):
#         print(f"{self.name} speak MUUUR MUUUUR")

# dog=Dog("Arsik")
# cat=Cat("Muis")
# cat.speak()
# dog.speak()

# class BankAccount:
#     def __init__(self,balance,account_number):
#         self.balance=balance
#         self.account_number=account_number

#     def deposit(self,contribute):
#         self.balance += contribute

#     def withdraw(self,take_off):
#         self.balance -= take_off
# class SavingsAccount(BankAccount):
#     def __init__(self,balance,account_number,interest_rate):
#         super().__init__(balance,account_number)
#         self.interest_rate=interest_rate

#     def add_interest(self):       
#         self.balance += (self.balance * self.interest_rate)/100

# account1= SavingsAccount(2000,1,20)
# print(account1.balance)
# account1.add_interest()
# print(account1.balance)


# class Calendar:
#     def __init__(self,date,meeting):
#         self.place=meeting
#         self.date=date

#     def info_meet(self):


# dates=Calendar("05.10.2023","Толе би 109")
# dates.info_meet()

# class InventoryItem:
#     def __init__(self,name,count,price):
#         self.name=name
#         self.count=count
#         self.price=price

#     def plus(self,counts):
#         self.count+=counts

#     def minus(self,countes):
#         self.count-=countes

#     def sum_price(self):
#         print(sum(self.price))

# tovar1=InventoryItem("Milk",10,500)
# print(tovar1.plus(2))


# class Board:
#     def __init__(self,o,x):
#         self.o=o
#         self.x=x
#         self.open=False

# class GamePole:
#     def __init__(self,n,m):
#         self.pole=[]
#         for i in range(n):
#             lst=[]
#             for i in range(n):
#                 c=Board(0,False)
#                 lst.append(c)

#     def __init_subclass__(cls) -> None:
        
        


     






