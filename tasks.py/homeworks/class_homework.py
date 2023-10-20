# Task1
class Notes:
    def __init__(self,uid,title,author,pages):
        self.uid=uid
        self.title=title
        self.author=author
        self.pages=pages

    def info_book (self):
        print(f"uid: {self.uid}")
        print(f"title: {self.title}")
        print(f"author: {self.author}")
        print(f"pages: {self.pages}")

note=Notes(1005435,"Шутка","И.С.Бах",2)
note.info_book()

# Task2
class MediaPlayer:
    def __init__(self,filename):
        self.filename=filename

    def open(self):
        print(f"Открыть {self.filename}")

#     def play(self):
#         print(f"Вопроизведение {self.filename}")

# filename1=MediaPlayer("VLC")
# filename2=MediaPlayer("KMPlayer")

# filename1.open()
# filename1.play()

# filename2.open()
# filename2.play()

# Task4
# class Money:  
#     def __init__(self, money ):  
#         self.money = money

#     def summa(self):
#         print(self.money)

# my_money = Money(100)
# your_money = Money(1000)

# my_money.summa()
# your_money.summa()

# Task5
# class Point:
#     def __init__(self,x,y,z="black"):
#         self.x=x
#         self.y=y
#         self.z=z

#     def info (self):
#         print(self.x, self.y, self.z)

# p1 = Point(10,20)
# p2 = Point(10,5,"red")

# p1.info()
# p2.info()
# Task6
class TriangleChecker: 
    def __init__(self, a, b, c): 
        self.a = a 
        self.b = b 
        self.c = c 
   
    def is_triangle(self): 
        if type(self.a) not in (int, float) or type(self.b) not in (int, float) or type(self.c) not in (int, float) or self.a <= 0 or self.b <= 0 or self.c <= 0: 
            return 1 
        elif self.a + self.b <= self.c or self.a + self.c <= self.b or self.b + self.c <= self.a: 
            return 2 
        else: 
            return 3 
 
 
a=int(input()) 
b=int(input())
c=int(input())
tr = TriangleChecker(a, b, c) 
print(tr.is_triangle())

