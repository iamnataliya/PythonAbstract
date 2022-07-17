# 1. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
from random import randint
list_d = []
# num = int(input("input simbol: " ))
for i in range(10):
    list_d.append(randint(1,15))
    print(list_d)
num = int(input("input simbol: "))
for i in list_d:    
    if i == num:
      print("YES")
else:
    print("NO")
# 2. Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.
import random
import string
random.seed(10)
for i in range(10):
    list_d = (random.choice(list('123456789qwertyuiopasdfgh')))
    print(list_d)
num = int(input("input simbol: "))
for i in list_d: 
    if i==num:
        print("YES")
    else:
        print("NO")

# Задать список из N элементов, заполненных числами из [-N, N]. Найти произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число
