# Анонимные,
# lambda функции

# def f(x):
#  return x**2
# g = f #Переменная хранит ссылку на функцию
# print(f(2)) #ответ 4

# def calc(x):
#  return x+10
# print(calc(10))

# def mult(x):
#  return x**2

# def sum(x, y):
#     return x*y
# # f = sum
# sum = lambda x, y: x+y
# def mylt(x, y):
#     return x*y
# def calc(op, a, b):
#     print(op(a, b))
#     # return(op(a, b)) 
# calc(lambda x, y: x+y, 4, 5) #ответ 9
# # calc(sum, 4, 5) #ответ 9

# List Comprehension
# [exp for item in iterable]
# [exp for item in iterable (if conditional)]
# [exp <if conditional> for item in iterable (if conditional)]
# def f(x):
#     return x**3
# list =[(i, f(i)) for i in range(1, 10) if i i%2 == 0]
# for i in range(1, 101):
#     if(1%2 == 0):
#         list.append (i)
# print(list) #Список только из четных чисел


# В файле хранятся числа, нужно выбрать четные и
# составить список пар (число; квадрат числа).
# Пример:
# 1 2 3 5 8 15 23 38
# Получить:
# [(2, 4), (8, 64), (38, 1444)]
# f = open('file.txt', 'r')
# data = f.read() + ' '
# f.close()
# numbers = []
# while data != '':
#  space_pos = data.index(' ')
#  numbers.append(int(data[:space_pos]))
#  data = data[space_pos+1:]

# out = []
# for e in numbers:
#  if not e % 2:
#     out.append((e, e**2))
# print(out)
# Список четных чисел 
list = []
for i in range(1, 101):
    if(i%2 == 0):
        list.append(i)
print(list)

list = [i for i in range(1, 21) if i%2 == 0]
print(list)

# Картежи
list = [(i, i) for i in range(1, 11) if i%2 == 0]
print(list)

# В файле хранятся числа, нужно выбрать четные и
# составить список пар (число; квадрат числа).
# Пример:
# 1 2 3 5 8 15 23 38
# Получить:
# [(2, 4), (8, 64), (38, 1444)]
def select(f, col):
    return [f(x) for x in col]

def where(f, col):
    return [x for x in col if f(x)]
data = '1 2 3 5 8 15 23 38'.split()

res = select(int, data)
res = where(lambda x: not x % 2, res)
res = select(lambda x: (x, x**2), res)
print(res)

# Функция map() применяет указанную функцию к
# каждому элементу итерируемого объекта и
# возвращает итератор с новыми объектами.
# f(x) ⇒ x + 10
# map(f, [ 1, 2, 3, 4, 5])
#  ↓ ↓ ↓ ↓ ↓
#  [ 11, 12, 13, 14, 15]
# # Нельзя пройтись дважды
li = [x for x in range(1,20)]
li = list(map(lambda x:x+10, li))
print(li)

# Заводит числа через запятую при вводе
data = list(map(int, input().split()))
print(data)


Функция filter
# Функция filter() применяет указанную функцию к
# каждому элементу итерируемого объекта и
# возвращает итератор с теми объектами, для
# которых функция вернула True.
# f(x) ⇒ x - чётное
# filter(f, [ 1, 2, 3, 4,5])
#  ↓
#  [ 2, 4 ]
# Нельзя пройтись дважды
data = [x for x in range(10)]

res = list(filter(lambda x: x%2 == 0, data))
print(res)

# Функция zip
# Функция zip() применяется к набору итерируемых
# объектов и возвращает итератор с кортежами из
# элементов входных данных.
# Количество элементов в результате равно минимальному количеству элементов входного набора
# zip ([1, 2, 3], [ ‘о‘, ‘д‘, ‘т‘], [‘f’,’s’,’t’])
#  ↓
# [(1, 'о', 'f'), (2, 'д', 's'), (3, 'т', 't')]
# Нельзя пройтись дважды

users = [ 'user1','user2','user3','user4','user5']
ids = [4,5,9,14,7]
data = list(zip(users, ids))
print(data)

# Функция enumerate
# Функция enumerate() применяется к итерируемому
# объекту и возвращает новый итератор с кортежами
# из индекса и элементов входных данных.
# enumerate(['Казань', 'Смоленск', 'Рыбки', 'Чикаго'])
#  ↓
# [(0, 'Казань'), (1, 'Смоленск'), (2, 'Рыбки'), (3, 'Чикаго')]
# Нельзя пройтись дважды

users = [ 'user1','user2','user3','user4','user5']

data = list(enumerate(users))
print(data)
