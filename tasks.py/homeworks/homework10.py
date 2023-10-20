# Task1
# class Animal:
#     def __init__(self,name,old):
#         self.name=name
#         self.old=old

# class Cat(Animal):
#     def __init__(self,name,old, colour, weight: float):
#         self.colour=colour
#         self.weight=weight
#         super().__init__(name,old)

#     def info_cat(self):
#         print(f"{self.name} {self.old} {self.colour} {self.weight}")

# class Dog(Animal):
#     def __init__(self,name, old, breed, size,height):
#         self.breed=breed
#         self.size=size,height
#         super().__init__(name,old)

#     def info_dog(self):
#         print(f"{self.name} {self.old} {self.breed} {self.size} ")

# cat = Cat('кот:', 4, 'black', 2.25)
# dog=Dog("Bomb",2,"doberman",1.15,45)
# cat.info_cat()
# dog.info_dog()

# Task2
# class VideoRating:
#     def __init__(self,rating):
#         self.rating=rating

#     def get_rating(self):
#         return (self.rating)
    
#     def set_rating(self):
#         self.rating=rating
#         if self.rating > 0 or self.rating < 5:
#             print(self.rating)
#         else:
#             print("неверное присваиваемое значение")

# class VideoItem():
#     def __init__(self,title: str, descr: str, path):
#         self.title=title
#         self.descr=descr
#         self.path=path
#         # super().__init__(rating)


# v = VideoItem('Курс по Python ООП', 'Подробный курс по Python OOP',
# 'D:/videos/python_oop.mp4')
# print(v.rating.get_rating()) 
# v.rating.set_rating(5)
# print(v.rating.get_rating) 
# title = v.title
# descr = v.descr
# v.rating.rating = 6

# Task3
# class Protists:
#     pass
# class Plants:
#     pass
# class Animals:
#     pass
# class Mosses:
#     pass
# class Flowering:
#     pass
# class Worms:
#     pass
# class Mammals:
#     pass
# class Human:
#     pass
# class Monkeys:
#     pass
# class Monkeys:
#     pass

# class Monkey(Monkeys):
#     def __init__(self,name,weight,old):
#          self.name=name
#          self.weight=weight
#          self.old=old

# class Person(Human):
#     def __init__(self,name,weight,old):
#          self.name=name
#          self.weight=weight
#          self.old=old

# class Flower(Flowering):
#     def __init__(self,name,weight,old):
#          self.name=name
#          self.weight=weight
#          self.old=old
# class Worm(Worms):
#     def __init__(self,name,weight,old):
#          self.name=name
#          self.weight=weight
#          self.old=old

# obj = Monkey("Ray", 12, 3)
# obj = Person("Oljas", 65, 22)
# obj = Flower("Poeny", 2, 1)
# obj = Worm("Pio", 1, 1)

# Task4
# class Book:
#     def __init__(self,title, author, pages, year):
#         self.title=title
#         self.author=author
#         self.pages=pages
#         self.year=year

# class DigitBook(Book):
#     def __init__(self,title, author, pages, year, size, frm):
#         self.size=size
#         self.frm=frm
#         super().__init__(title, author, pages, year)

# book = Book(title, author, pages, year)
# db = DigitBook(title, author, pages, year, size, frm)

# task5
# class Thing:
#     def __init__(self,name,weight):
#         self.name=name
#         self.weight=weight

# class ArtObject(Thing):
#     def __init__(self,name, weight, author, date):
#         self.author=author
#         self.date=date
#         super().__init__(name,weight)

# class Computer(Thing):
#     def __init__(self,name, weight, memory, cpu):
#         self.memory=memory
#         self.cpu=cpu
#         super().__init__(name,weight)

# class Auto:
#     def __init__(self,name, weight, dims):
#         self.dims=dims
#         super().__init__(name,weight)

# class Mercedes(Auto):
#     def __init__(self,name, weight, dims, model, old):
#         self.model=model
#         self.old=old
#         super().__init__(name, weight, dims)

# class Toyota(Auto):
#     def __init__(self,name, weight, dims, model, wheel):
#         self.model=model
#         self.wheel=wheel
#         super().__init__(name, weight, dims)
    
# obj = ArtObject("sculpture","100","John","10.10.2023") 
# obj = Computer ("Acer","15","12345","brain") 
# obj = Auto("Ferrari","54656","14.7")

# auto = Mercedes("Mersedes", "516516", "216515", "GLA", "2022") 
# auto = Toyota("Toyota", "5165165", "56165165", "Yaris", "True") 

# TASK6
# class SellItem:
#     def __init__(self,name,price):
#         self.name=name
#         self.price=price

# class House(SellItem):
#     def __init__(self,name, price, material, square):
#         self.material=material
#         self.square=square
#         super().__init__(name,price)

# class Flat(SellItem):
#     def __init__(self,name, price, size, rooms):
#         self.size=size
#         self.rooms=rooms
#         super().__init__(name,price)

# class Land(SellItem):
#     def __init__(self,name, price, square):
#         self.square=square
#         super().__init__(name,price)

# class Agency:
#     def __init__(self,name):
#         self.name=name

#     def add_object(self):
#         pass (не знаю как добавть)
#     def remove_object(self):
#         pass
#     def get_object(self):
#         return self.name=name

# ag = Agency("Рога и копыта")
# ag.add_object(Flat("квартира, 3к", 10000000, 121.5, 3))
# ag.add_object(Flat("квартира, 2к", 8000000, 74.5, 2))
# ag.add_object(Flat("квартира, 1к", 4000000, 54, 1))
# ag.add_object(House("дом, крипичный",price=35000000,material="кирпич",
# square=186.5))
# ag.add_object(Land("участок под застройку", 3000000, 6.74))
# for obj in ag.get_objects():
#  print(obj.name)
# lst_houses = [x for x in ag.get_objects() if isinstance(x, House)] 

# Task7
# class Animal:
#     def __init__(self,__name,__kind,__old):
#         self.__name=__name
#         self.__kind=__kind
#         self.__old=__old

#     def info(self):
#         print(f"{self.__name} {self.__kind} {self.__old}")

# cat=Animal("Мурат", "дворовый кот", 5)
# dog=Animal("Рекс", "немецкая овчарка", 8 )
# parrot=Animal("Ақтөс", 'попугай', 3)
# cat.info()
# dog.info()
# parrot.info()

# Task9
# class Furniture:
#     def __init__(self,name,weight):
#         self.name=name
#         self.weight=weight

#     def __verify_name(self):
#         if type (self.name) == str:
#             print(self.name)
#         else:
#             print('название должно быть строкой')

#     def __verify_weight(self):
#         if self.weight>0:
#             print(self.weight)
#         else:
#             print('вес должен быть положительным числом')

# class Closet(Furniture):
#     def __init__(self,name, weight, tp, doors):
#         self.tp=tp
#         self.doors=doors
#         super().__init__(name,weight)

#     def get_attrs(self):
#         return (self.name,self.weight,self.tp,self.doors)

# class Chair(Furniture):
#     def __init__(self,name, weight, height):
#         self.height=height
#         super().__init__(name,weight)

#     def get_attrs(self):
#         return (self.name,self.weight,self.height)

# class Table(Furniture):
    def __init__(self,name, weight, height, square):
        self.height=height
        self.square=square
        super().__init__(name,weight)

    def get_attrs(self):
        return (self.name,self.weight,self.height,self.square)

с1 = Closet('шкаф-купе', 342.56, True, 3)
chair = Chair('стул', 14, 55.6)
tb = Table('стол', 34.5, 75, 10)
print(tb.get_attrs())

# Task10
class Aircraf:
    def __init__(self,__model, __mass, __speed, __top):
        self.model=__model
        self.mass=__mass
        self.speed=__speed
        self.top=__top

class PassengerAircraft(Aircraf):
    def __init__(self,model, mass, speed, top, chairs):
        self.chairs=chairs
        super().__init__(model, mass, speed, top)

class WarPlane(Aircraf):
    def __init__(self,model, mass, speed, top, weapons):
        self.weapons=weapons
        super().__init__(model, mass, speed, top)




