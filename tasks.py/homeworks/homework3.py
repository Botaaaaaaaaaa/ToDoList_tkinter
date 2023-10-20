# taskНОК
# def num(a, b):
#     m = a * b
#     while a != 0 and b != 0:
#         if a > b:
#             a %= b
#         else:
#             b %= a
#     return // (a + b)
# x = int(input())
# y = int(input())
# print('НОК:', num(x, y))
# task факториал
# def fac(n):
#     if n == 1:
#         return 1
#     return fac(n - 1) * n
# print(fac(10))
# task калькулятора
# def fac(k,p,s,c):
#  print(c)
# k=int(input("Введите сумму: "))
# p=k * 0.05
# s=int(input("На какой срок хоите? "))
# c= (k + p)/s
# fac(k,p,s,c)
# task палиндром
# def num(n,s,l):
#  for i in range(l//2):
#     if s[i] == s[-1-i]: 
#        print("Полиндром")
#        break
#  else:
#     print("Не полиндром")
# n = int(input(""))
# s = str(n) 
# l = len(s)
# num(n,s,l)
#  task11
# def num(m,n):
#  if m%n==0:
#   print(int(m/n))
#  else:
#   print(("{} на {} нацело не делится").format(m,n))
# m=int(input())
# n=int(input())
# num(m,n)
# task12
# def num(a):
#  if a[-1]=="7":
#     print("ДА")
#  else:
#     print("НЕТ")
# a=int(input())
# num(a)
# task13
# def num(m,n):
#     print((n + m-1) // n)
# n=int(input())
# m=int(input())
# num(m,n)
## task14
# def num(a):
#  a = a * 45 + (a // 2) * 5 + ((a + 1) // 2 - 1) * 15
#  print(a // 60 + 9, a % 60)
# a = int(input())
# num(a)
# task15
# def num(n):
#  print (hour % 24, min, sec)
# n = int(input())
# min1 = n // 60
# hour = min1 // 60
# min = min1 % 60
# sec = n % 60
# num(n)
 # task16
# def num(a):
#  print(a%10)
# a=int(input())
# num(a)
# task17
# def num(a,b,c):
#  if a + b <= c:
#     print('impossible')
#  else:
#     t = a * a + b * b - c * c
#     print(('right', 'obtuse', 'acute')[(t < 0) - (t > 0)])
# a=int(input())
# b=int(input())
# c=int(input())
# num(a,b,c)
# task18
# def num(n,i,s):
#  while i <= n:
#     s += i**2 
#     i += 1 
#  print(s)
# n = int(input())
# i = 1 
# s = 0
# num(n,i,s)
# task20
# def num(n,k):
#  for i in range(1,n+1):
#   k=k*i
#   print(k)
# n=int(input())
# k=1
# num(n,k)









   