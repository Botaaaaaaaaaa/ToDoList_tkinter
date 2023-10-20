# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def get_name(self):
#         return self.name
    
#     def get_age(self):
#         return self.age
    
#     def set_name(self,name):
#        self.name=name

#     def set_age(self,age):
#         self.age=age

#     def introduce(self):
#         print(f"Hi!{self.name} {self.age}")

# person=Person("Omar",100)
# person.set_age(1)
# person.set_name("Kamila")
# person.introduce()


# class Intershop:
#     def __init__(self,title,count,price):
#         self.title=title
#         self.count=count
#         self.price=price

#     def set_title(self,title):
#         self.title=title

#     def set_count(self,count):
#         self.count=count

#     def set_price(self,price):
#         self.price=price

#     def add(self,colour):
#         self.colour=colour

#     def set_colour(self,colour):
#         self.colour=colour

#     def info_shop(self):
#         print(f"Title: {self.title} Count:{self.count} Price: {self.price} Colour: {self.colour}")

# shop=Intershop("T-shirt","10 штук","3500тг")
# shop.set_title("Dress")
# shop.set_count("5 штук")
# shop.set_price("20.000тг")
# shop.set_colour("red")
# shop.info_shop()

# class Book:
#     def __init__(self,title,author,publication_year,is_avaliable):
#         self.title=title 
#         self.author=author
#         self.publication_year=publication_year
#         self.is_avalible=is_avaliable

#     def checkout(self):
#          self.is_avalible=False

#     def checkin(self):
#         self.is_avalible=True

#     def display_info(self):
#         print(f"Title: {self.title}  Author: {self.author} Publication_year: {self.publication_year} Is_avaliable: {self.is_avalible} ")

# book=Book("Harry Potter", "J.K.Rowling", "1997 year", "True")
# book.display_info()

# class Money:
#     def __init__(self,money):
#         self.__money=money

#     def set_money(self,money):
#         if self.check_money(money):
#             self.__money=money
#             return
#         print("Schoolarship")

#     def get_money(self):
#         return self.__money
    
#     def add_money(self,money):
#         self.money+=money.get_money()

#     def __check_money(self,money):
#         if type(money) == int and money>=0:
#           return True
#         return False
    
# mn_1=Money(10)
# mn_2=Money(20)
# mn_1.set_money(100)
# mn_2.add_money(mn_1)
# m1=mn_1




# class Book:
#     def __init__(self,__title,__author,__price):
#         self.title=__title
#         self.author=__author
#         self.price=__price

#     def set_title(self,__title):
#         self.title=__title

#     def set_author(self,__author):
#         self.author=__author

#     def set_price(self,__price):
#         self.price=__price

#     def get_title(self,__title):
#         self.title=__title

#     def get_author(self,__author):
#         self.author=__author

#     def get_price(self,__price):
#         self.price=__price

#     def info_book(self):
#         print(f"Title: {self.title} Author: {self.author} Price: {self.price}")

# book=Book("Harry Potter","J.R.Rowling",5000)
# book.set_title("Оян, қазақ!")
# book.set_author("Міржақып Дулатов")
# book.set_price(10000)

# book.info_book()


# class Line:
#     def __init__(self,__x1,__y1,__x2,__y2):
#         self.x1=__x1
#         self.y1=__y1
#         self.x2=__x2
#         self.y2=__y2

#     def get_coords(self):
#        return  (self.x1,self.y1,self.x2,self.y2)
        

#     def set_coords(self,__x1,__y1,__x2,__y2):
#         self.x1=__x1
#         self.y1=__y1
#         self.x2=__x2
#         self.y2=__y2

#     def draw(self):
#         print(self.x1,self.y1,self.x2,self.y2)

# line=Line(4,5,6,7)
# line.draw()


class Vehicle:
    def __init__(self,model,year):
        self.model=model
        self.year=year

class Cars(Vehicle):
    def __init__(self,fuel_efficiency,model,year):
        self.fuel_efficiency=fuel_efficiency
        super().__init__(model,year)

class Carrs(Cars):
    def __init__(self,number,model,year,fuel_efficiency):
        self.number=number
        super().__init__(model,year,fuel_efficiency)


class Car(Carrs):
    def __init__(self,fuel_type,model,year,fuel_efficiency,number):
        self.fuel_type=fuel_type
        super().__init__(model,year,fuel_efficiency,number)

    def info(self):
        print(f"{self.model} {self.year} {self.fuel_type} {self.fuel_efficiency} {self.number}")


car=Car("ДТ","Ferrari",2020,"100%","001KZ09")
car.info()

# from abc import ABC,abstractmethod
# class Animal:
#     @abstractmethod
#     def __init__(self,name):
#         self.name=name

# class Flyable:
#     @abstractmethod
#     def __init__(self,colour):
#         self.colour=colour

# class Bird(Flyable):
#     def __init__(self,name,colour):
#      self.name=name
#      super().__init__(colour)

# bird=Bird("Parrot","green")
# print(bird.name,bird.colour)


class Reality:
    def __init__(self,name=str,id=int,price=float,weight=float,dims=float):
        self.id=id
        self.name=name
        self.price=price
        self.weight=weight
        self.dims=dims

class Inter(Reality):
    def __init__(self,memory,frm,id,price,weight,dims):
        self.memory=memory
        self.frm=frm
        super().__init__(id,price,weight,dims)

class Thing(Inter):
    def __init__(name,price):
        super().__init__(name,price)









    




    