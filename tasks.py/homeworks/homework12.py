# # TASK2
# from abc import ABC, abstractmethod
# class Transport(ABC):
#  @abstractmethod
#  def go(self):
#   "Метод для перемещения транспортного средства"
# @classmethod
# @abstractmethod
# def abstract_class_method(cls):
#   "Абстрактный метод класса"

# class Bus(Transport):
#  def __init__(self, model, speed):
#   self._model = model
#   self._speed = speed
#  def go(self):
#   print("bus go")
# @classmethod
# def abstract_class_method(cls):
#   pass

# from abc import ABC, abstractmethod

# class Model:
#  @abstractmethod
#  def get_pk(self):
#   return "Машина сигналит"
 
#  def get_info(self):
#   return "Базовый класс Model"
 
# class ModelForm(Model):
#  _id=0
#  def __init__(self,login,password):
#   self._id=self.get_pk()
#   self._logun=login
# #   self._password=password

# #  def get_pk(self):
# #    ModelForm._id+=1
# #    return ModelForm._id
  
# # form = ModelForm("Логин", "Пароль")
# # print(form.get_pk())

# # TASK3
# from abc import ABC, abstractmethod

# class StackInterface(ABC):
#     @abstractmethod
#     def push_back(self, obj):
#         pass

#     @abstractmethod
#     def pop_back(self):
#         pass

# class StackObj:
#     def __init__(self, data):
#         self._data = data
#         self._next = None

# class Stack(StackInterface):
#     def __init__(self):
#         self._top = None

#     def push_back(self, obj):
#         stack_obj = StackObj(obj)
#         if self._top is None:
#             self._top = stack_obj
#         else:
#             stack_obj._next = self._top
#             self._top = stack_obj

#     def pop_back(self):
#         if self._top is not None:
#             pop_obj = self._top
#             self._top = self._top._next
#             return pop_obj
#         else:
#             return None


# st = Stack()
# st.push_back(StackObj("obj 1"))
# obj = StackObj("obj 2")
# st.push_back(obj)
# del_obj = st.pop_back() 

# TASK4
# class Track:
#     def __init__(self,start_x,start_y):
#         self.start_x=start_x
#         self.start_y=start_y

# class PointTrack:
#     def __init__(self,pt1,pt2):
#         self.pt1=pt1
#         self.pt2=pt2
# вообще не поняла

# TASK5
class Digit:
    def __init__(self, value):
        self.value = value

class Integer(Digit):
    def __init__(self, value):
        if type(value)==int:
            raise TypeError('Значение не соответствует типу объекта')
        super().__init__(value)

class Float(Digit):
    def __init__(self, value):
        if type(value) ==float:
            raise TypeError('Значение не соответствует типу объекта')
        super().__init__(value)

class Positive(Digit):
    def __init__(self, value):
        if value < 0:
            raise TypeError('Значение не соответствует типу объекта')
        super().__init__(value)

class Negative(Digit):
    def __init__(self, value):
        if value > 0:
            raise TypeError('Значение не соответствует типу объекта')
        super().__init__(value)

class PrimeNumber(Integer,Positive):
    pass

class FloatPositive(Float,Positive):
    pass

# все дальше уже непонятно

# TASK6
# 1-вариант потому что думаю так быстрые написать ^-^
# TASK7
# 1-вариант потому что думаю так быстрые написать ^_^

# TASK9
class ShopItem:
    ID_SHOP_ITEM = 0

    def __init__(self):
        super().__init__()
        ShopItem.ID_SHOP_ITEM += 1
        self._id = ShopItem.ID_SHOP_ITEM

    def get_pk(self):
        return self._id

class ShopUserVeiw:
    pass

class ShopGenericView:
    def __str__(self):
       pass
     

class Book(ShopItem,ShopGenericView): 
    def __init__(self, title, author, year):
        super().__init__()
        self._title = title
        self._author = author
        self._year = year


book = Book("Python ООП", "Балакирев", 2022)
print(book)

# TASK10
# class Point:
#  def __init__(self, x, y):
#   self._x = x
#   self._y = y

# pt = Point(1, 2)

# try:
#     z = pt.z 
#     print(z)  
# except AttributeError:
#     print("Атрибут с именем z не существует")

# TASK11
# try:
#  x = float(input())
#  y = float(input())
#  d = x / y
# except ZeroDivisionError:
#  print('ZeroDivisionError')
# except:
#  print('except')
# если произойдет исключение, не являющееся ZeroDivisionError

# TASK12
# def numbers(a):
#     try:
#         int(a)
#         return True
#     except ValueError:
#         return False

# lst_in = input().split()
# num_fil= filter(numbers,lst_in)  
# list = map(int, num_fil)  
# print(sum(list))

# TASK13
# class Triangle:
#     def __init__(self,a,b,c):
#         self._a=a
#         self._b=b
#         self._c=c

#     def info(self):
#         try:
#             self._a,self._b,self._c<=0
#         except:
#             raise TypeError ('стороны треугольника должны быть положительным числами')
        
#         try:
#             self._a+self._b<self._c,self._b+self._c<self._a,self._a+self._c<self._b
#         except:
#             raise ValueError('из указанных длин сторон нельзя составить треугольник')
        
# input_data = [(1.0, 4.54, 3), ('abc', 1, 2, 3), (-3, 3, 5.2), (4.2, 5.7, 8.7), (True, 3, 5), (7, 4, 6)]

# lst_tr = []
# for data in input_data:
#     try:
#         tr = Triangle(*data)
#         lst_tr.append(tr)
#     except: (TypeError, ValueError)

# TASK15
# try:
#     input_data = input().split()
#     num1 = input_data[0]
#     num2 = input_data[1]
    
#     num1 = int(num1)
#     num2 = int(num2)
# except:
#  ValueError
# finally:
#     print(num1+num2)  

# TASK16
# class Point:
#     def __init__(self, x=0, y=0):
#         self._x = x
#         self._y = y

# try:
#     input_data = input().split()
#     x = input_data[0]
#     y = input_data[1]

#     x = int(x)
#     y = int(y)
    
#     pt = Point(x, y)
# except ValueError:
#     pt = Point()
# finally:
#     print(f"Point: x = {pt._x}, y = {pt._y}")

# TASK17
# class Exception:
#     pass
# class StringException(Exception):
#     pass
# class NegativeLengthString(StringException):
#     pass
# class ExceedLengthString(StringException):
#  try:

#  except NegativeLengthString:
#   print("NegativeLengthString")
#  except ExceedLengthString:
#   print("ExceedLengthString")
#  except StringException:
#   print("StringException")

# TASK19
# class DateError(Exception):
#     pass

# class DateString:
#     def __init__(self, date_string):
#         try:
#             day, month, year = map(int, date_string.split('.'))
#             if not (1 <= day <= 31) or not (1 <= month <= 12) or not (1 <= year <= 2023):
#                 raise DateError
#             self.day = day
#             self.month = month
#             self.year = year
#         except (ValueError, DateError):
#             raise DateError("Неверный формат даты")

#     def __str__(self):
#         return f"{self.day:02d}.{self.month:02d}.{self.year:04d}"

# try:
#     date_string = input()
#     date = DateString(date_string)
#     print(date)
# except DateError:
#     print("Неверный формат даты")

# Task20
# class ConnectionError(Exception):
#     pass

# class DatabaseConnection:
#     def __init__(self):
#         self._fl_connection_open = False

#     def connect(self, login, password):
#         self.login=login
#         self.password=password
#         self._fl_connection_open = True

#     def close(self):
#         self._fl_connection_open = False
#  дальше не знаю что делать
