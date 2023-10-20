# def task2(z):
#     for i in range(1,z):
#         if z%i==0:
#          print(i)
 
# z=int(input())
# task2(z)

# def temp(z):
#  a=273
#  print("Градус в Фаренгейте:",z+a,"F")

# z=int(input())
# temp(z)

def num(s,d):
    for i in range(1,d):
        if s%i==0 or d%i==0:
            print(i)
    
s=int(input())
d=int(input())
num(s,d)



