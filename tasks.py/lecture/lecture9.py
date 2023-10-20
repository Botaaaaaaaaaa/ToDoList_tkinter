# a={"name":"Arman", "age":"85","course":"2"}
# del a["name"]
# print(a)

# a={1,2,3,4,5}
# b={3,4,5,6,7}
# print(a|b)
# print(a&b)

# countries={}
# for i in range(4):
#     country,city=input().split()
#     countries[country]=city
# print(countries)

def find_a(title):
    for i in a:
     if title==i["title"]:
        print(i)
      
a= [
   {
    "title":"pen",
    "count":20,
    "price":2},

   { "title":"pencil",
    "count":15,
    "price":5},

    {"title": "table",
    "count": 10,
    "price": 100}
]
find_a("pen")

# a={1,2,3,4,5,6,7}
# b={5,6,7,8,9,10}
# print(a|b)
# print(a-b)
# print(a&b)
# print(a^b)

# a={3,4,5,6,7,8}
# b={7,8,9,10,11}
# print(a-b)
# print(a,b)

# a={3,4,5,6,7,8}
# b={7,8,9,10,11}
# print(a|b)
# task1
# a=[
#     {"5=":"отлично"},
#     {"4=":"хорошо"},
#     {"3=":"удовлетворительно"}
# ]
# print(a)
# task2
# d={}
# a=input().split()
# for i in a:
#    key,value=i.split("=")
#    d[key]=value
#    print(*sorted(d.items()))

# task3
# keys
# dict_1 = dict([value.split('=') 
# for value in input().split()])
# count = 0
# for key, value in dict_1.items():
#     if key == 'house' or key == 'True' or key == '5': 
#         count += 1
#     print('ДА')
# else:
#     print('НЕТ')
# task4
# keys=input().split()
# d={}
# for i in keys:
#     key,value=i.split('=')
#     d[key]=value
#     del d["True"]
#     del d["3"]
# print(*sorted(d.items()))

# task5
# a = list(input().split())
# d = dict() 
# for i in a:
#     if i[:2] in d:
#         d[i[:2]].append(i)
#     else:
#         d[i[:2]] = [i]
# print(*sorted(d.items()))
# task7
# a=input().split()
# print(len(set(a)))
# task8
# num = {int(value) for value in input() if value.isdigit()} 
# if sorted(num):
#  print(*sorted(num)) 
# else:
#  print('НЕТ')
# task9
# a = set(input().split())
# b = set(input().split())
# print(*(sorted(a & b)))
# task10
# a = set(input().split())
# b= set(input().split())
# print(*(sorted(a - b)))
# tASK11
# l = set((input().split()))
# m = set((input().split()))
# k = l|m
# n = l&m
# s = k-n
# print(*sorted(s))
# TASK12
# a = (int,input().split())
# if a !=2:
#     print("ДОПУЩЕН")
# else:
#     print("НЕ ДОПУЩЕН")





