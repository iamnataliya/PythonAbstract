# Лекция 1
print("Hello World")
print("{0} {1}".format("Hello","World"))
# print(f"{"Hello"} {"World"}")
# print(f"{a:.2f}")
# print(a , "+" , b , "=",c)
print("Hello World\nMy name is Natalia\nI'm from Msk")  # переход на другую строку

# Типы данных и переменная
# int, float, boolean, str, list, None
a = 123
b = 1.23
print(b) 
print(type(a))

s = 'hellow tata'
print(s)  #вывод строки

f = True

# Списки
list = []
print(list)
list = ['1', '2', '3', 'Hi']
print(list)

# Ввод данных
# input, print
# Целые числа сумма
print('Input A')
a = int(input())
print('Input B')
b = int(input())
print(a, ' + ', b, ' = ', a+b)
# Вещественные числа сумма
print('Input A')
a = float(input())
print('Input B')
b = float(input())
print(a, ' + ', b, ' = ', a+b)

# Арифметические операции
a = 2
b = 8
c = a//b #Деление без остатка
c = a/b #Деление
c = round(a*b, 5) #Округление
print(c)

#Логические операции
# not, and, or, 
# is, is not, in, not in
a = 1 < 4 and 3 < 6
print(a)

f = 1 > 2 or 4 < 6
print(f)

f = [1,2,3,4,5]
print(f)
print(not 2 in f) #есть ли 2 в списке?

is_odd = f[0] % 2 == 0
print(is_odd)

# Управляющие конструкции
# if, if-else
a = int(input('a ='))
b = int(input('b ='))
if a>b:
    print(a)
else:
    print(b)

# Управляющие конструкции (цикл)
#while, for
original = 23
inverted = 0
while original !=0: #Не равен 0
    inverted = inverted * 10 + (original % 10) #целочисленное
    original //= 10
print(inverted)

original = 23
inverted = 0
while original !=0: #Не равен 0
    inverted = inverted * 10 + (original % 10) #целочисленное
    original //= 10
else:
    print('Plese stop')
print(inverted)

list = [1,2,3,4]
for i in list:
   print(i**2)  #Квадрат чисел

r = range(10) #Итератор от 0 до 9
for i in r:
   print(i)

#Немного о строках
text = 'съешь ещё этих мягких французских булок'
print(len(text)) # 39
print('ещё' in text) # True
print(text.isdigit()) # False
print(text.islower()) # True
print(text.replace('ещё','ЕЩЁ')) #
print(text[0]) # c
print(text[1]) # ъ
print(text[len(text)-1]) # к
print(text[-5]) # б
print(text[:]) # print(text)
print(text[:2]) # съ
print(text[len(text)-2:]) # ок
print(text[2:9]) # ешь ещё
print(text[6:-18]) # ещё этих мягких
print(text[0:len(text):6]) # сеикакл
print(text[::6]) # сеикакл
text = text[2:9] + text[-5] + text[:2] # ...

#Списки: введение
numbers = [1, 2, 3, 4, 5]
print(numbers) # [1, 2, 3, 4, 5]
numbers = list(range(1, 6))
print(numbers) # [1, 2, 3, 4, 5]
numbers[0] = 10
print(len(numbers)) # Вывод индексов
print(numbers) # [10, 2, 3, 4, 5]
for i in numbers:
 i *= 2
 print(i) # [20, 4, 6, 8, 10]
print(numbers) # [10, 2, 3, 4, 5]
colors = ['red', 'green', 'blue']
for e in colors:
 print(e) # red green blue
for e in colors:
 print(e*2) # redred greengreen blueblue
colors.append('gray') # добавить в конец
print(colors == ['red', 'green', 'blue', 'gray']) # True
colors.remove('red') #del colors[0] # удалить элемент

# Функции
# Это фрагмент программы, используемый многократно
def f(x):
 return x**2
def f(x):
 if x == 1:
    return 'Целое'
 elif x == 2.3:
    return 23
 else:
   return
print(f(1)) # Целое
print(f(2.3)) # 23
print(f(28)) # None
print(type(f(1))) # str
print(type(f(2.3))) # int
print(type(f(28))) # NoneType