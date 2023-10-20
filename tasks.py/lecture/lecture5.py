a=int(input())
for i in range(a):
    if i % 2==0:
     print(i)

a=int(input())
count = 0
while count<a:
   if count % 2==0:
     print(count)
   count +=1

a=int(input("Введите число: "))
count=0
sum_number = 0
while count<a:
   print(count)
   sum_number+=count
   count+=1
   print(sum_number)

a=int(input("Введите число: "))
sum_number = 0
for i in range(a):
    print(i)
    sum_number+=i
print(sum_number)

a= int(input())
for g in range(a+1):
    if g % 2==0:
     print(g)

n=int(input("Введите число: "))
for i in range(1,10):
 print(f"{n}x{i}={i*n}")

n=int(input("Введите число: "))
for i in range(1,10):
 print(f"{n}x{i}={i*n}")

n=int(input("Введите число: "))
count=1
while count<10:
    print(f"{n}x{count}={count*n}")
    count+=1

# способ1 # 
.
print(a[0])
for l in range(0,6):
    print(a[l])

# способ2
word = "Python"
for i in word:
   print(i)

count = 1
sum=0
while count<100:
    if count % 2 != 0:
        sum+=count
     
    print(count)
    count +=1

print(sum)
s="*"
for i in range(1,6):
 for h in range (i):
    print(s,end=" ")
 print()
15.09.2023
a=int(input("У Вас какая оценка?  "))
if a<=3:
      print("Плохо")  
elif a<=6 or a<=4:
    print("Удовлетворительно") 
elif a<=9 or a<=7:
    print("Хорошо")  
elif a<=10:
    print("Отлично")

a=int(input("Сколько время? "))
if a>=6 or a<12:
    print("Доброе утро!")
elif a>=12 or a<=18:
    print("Добрый день!")
elif a>=18 or a<=24:
    print("Добрый вечер!")
elif a>=0 and a<=6:
    print("Спокойной ночи!")

a=int(input("Введите число: "))
for i in range(1,a):
 if i%3==0:
  print(i)

list = [9,3,5,-3,7,8,-4]
num=0
count=0
for i in list:
    if i>0:
      num += i
      count+=1
print(num/count)

a=int(input())
b=int(input())
c=int(input())
if a+b>c and a+c>b and c+b>a:
    print("True")
else:
    print("False")
# 7
a= float(input())     
if 0<=a<=2 or 10<=a<=20:
    print("True")
else:
    print("False")
    


    
   

   
