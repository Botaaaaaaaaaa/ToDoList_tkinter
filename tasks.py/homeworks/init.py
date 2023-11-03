# class Student:
#    def __init__(self, fio, group):
#      self._fio = fio 
#      self._group = group 
#      self._lect_marks = [] 
#      self._house_marks = [] 

#    def add_lect_marks(self, mark):
#     self._lect_marks.append(mark)

#    def add_house_marks(self, mark):
#     self._house_marks.append(mark)

#    def __str__(self):
#     return (f"Студент {self._fio}: оценки на лекциях: {str(self._lect_marks)}; оценки за д/з: {str(self._house_marks)}")
   
# class Mentor:
#  def __init__(self, fio, subject):
#   self._fio = fio
#   self._subject = subject

# class Lector(Mentor):
#  def __init__(self,fio, subject):
#   super().__init__(fio,subject)

# class Reviewer(Mentor):
#  def __init__(self,fio, subject):
#   super().__init__(fio,subject)

#   def set_mark(self, student, mark):
#    pass
  
# # TASK2
# class Food:
#     def __init__(self,name, weight, calories):
#         self.name=name
#         self.weight=weight
#         self.calories=calories

class BreadFood(Food):
    def __init__(self,_name, _weight, _calories,_white):
        super().__init__(_name, _weight, _calories)
        self.white=_white       

    def get_info(self):
        if self.white=="белый":
            print((f"{self.name} {self.weight} {self.calories} {self.white==True}"))
        else:
         print(f"{self.name} {self.weight} {self.calories} {self.white==False}")
    
class SoupFood(Food):
    def __init__(self,_name, _weight, _calories,_dietary):
        super().__init__(_name, _weight, _calories)
        self.dietary=_dietary

    def get_info(self):
        if self.dietary=="диетический суп":
            print((f"{self.name} {self.weight} {self.calories} {self.dietary==True}"))
        else:
         print(f"{self.name} {self.weight} {self.calories} {self.dietary==False}")

class FishFood(Food):
    def __init__(self,_name, _weight, _calories, _fish):
         super().__init__(_name, _weight, _calories)
         self.fish=_fish

    def get_info(self):
            print((f"{self.name} {self.weight} {self.calories} {self.fish}"))  


# food=BreadFood("Бородинский хлеб", 34.5, 512,"серый")
# sf = SoupFood("Черепаший суп", 520, 890.5, "суп")
# ff = FishFood("Консерва рыбная", 340, 1200, "семга")
# food.get_info()
# sf.get_info()
# ff.get_info()

# class ShopInterface:
#     def get_id(self):
#         raise NotImplementedError("в кдассе не переопределен метод get_id")

# class ShopItem(ShopInterface):
#     _id=0
#     def __init__(self,name,weight,price):
#         self._id=self.get_id
#         self._name=name
#         self._weight=weight
#         self._price=price

#     def get_id(self):
#         ShopItem._id+=1
#         return ShopItem._id
    
# shop=ShopItem("pen",15,200)
# shop.get_id()


# num1=int(input())
# num2=int(input())

# try: 
#     print(num1/num2)

# except ZeroDivisionError as e:
#     print("Не получилось")
#     print(e)


# class ValidationError(Exception):
#   pass

# name=input("Имя: ")
# def check_name(name):
#  if name=="" or not name.isalpha():
#   raise ValidationError("Wrong name")
# print(name)

# check_name(name)

import time
class Manager:
    def __enter__(self):
        self.start=time.time()
        print(self.start)


    def __exit__(self,*args):
        self.end=time.time()
        print(self.end-self.start)

with Manager():
    for i in range(100):
        print(i)








 
 