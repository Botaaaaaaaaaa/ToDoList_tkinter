# task1
# def add_music(genre,music):
#  if genre in lst:
#   lst[genre].append(music)
#  else:
#   lst[genre]=[music]
# add_music("qpop","Kairat Nurtas,ORDA")
# print(lst)

# lst:{
#     "music":{
#         "rap": ["Tyga,Travis Scott,50 CENT"],
#         "pop":["Selena,Ariana,The Weeknd"],
#         "opera":["Richard,Luna"]

#     }
# }
# task2
# students={
#     "Alim":[2,3,4,5],
#     "Tomi":[3,4,5,6],
#     "Islam":[4,5,6,7]
# }
# def students_gpa(students):
#  for k,v in students.items():
#   print(f"{k} = {sum(v)/len(v)}")
  
# students_gpa(students)
# task4
# book={
#     "first_book":{
#         "name":["Harry Potter"],
#   "genre":["fantasy"],
#   "author":["J.K.Rowling"]
#     },
#     "second_book":{
#         "name":["Rich Dad Poor Dad"],
#         "genre":["personal finance"],
#         "author":["Robert Kiyosaki"]
#     }
# }
# def find_author(author):
#     for k,v in book.items():
#      if v["author"]==author:
#         return v

# print(find_author(["J.K.Rowling"]))
# task5
coordinates = (2,3,4)
def return_sum(coordinates):
    return(sum(coordinates))

# print(return_sum(coordinates) +10)

