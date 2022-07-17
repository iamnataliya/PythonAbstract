Инструкция по синтаксису Pyhton
Вывод:  
```python
print("Hello World")
print("{0} {1}".format("Hello","World"))
print(f"{"Hello"} {"World"}")
print(f"{a:.2f}")
print(a , "+" , b , "=",c)
print("Hello World\n My name is Artiom\nI'm from Moldova")
```  
Ввод:
```python
a = input()
a = input("Enter number : ")
a = int(input())
```   
Арифметические операции:  
| символ | синтаксис | что делает |
| ----- | ----- | ----- |
| + | `a+b` | сложение |
| - | `a-b` | вычитание |
| * | `a*b` | умножение |
| / | `a/b` | деление |
| % | `a%b` | остаток от деления а на b |
| // | `a//b` | целая часть от деления a на b  |
| ** | `a**b` | возведение в степень a в степени b |  

Логические операции:  
| символ | синтаксис | что делает |
| ----- | ----- | ----- |
| == | `a == b` | равенство |
| != | `a != b` | Не равно |
| > | `a > b` | больше |
| >= | `a >= b` | больше или равно |
| < | `a < b` | меньше |
| <= | `a <= b` | меньше или равно |
| not | ` a not b` | a не b |
| and | `a>1 and b<1` | обязательное выполнение нескольких условий |
| or | `a>1 or b<1` | выполнение хотя бы одно из условий  |
| is | `a is b` | a это b |
| is not | `a is not b` | a это не b |
| in | `a in b` | a в b |
| not in | `a not in b` | a не в b |

Условия if, elif:
```python
if a>b:
    print(f"{a}>{b}")
elif a=b:
    print(f"{a}={b}")
else:
    print(f"{a}<{b}")
```   
**ВАЖНО!** после условия ставится `:` , полсе важны отсупы.

Выполнять пока выполняется условия While:
```python
while i<10:
    print(i)
    i+=1
while True:
    i+=1
    if i>10:
        break
    else:
        print("Hello World")
original = 23
inverted = 0
while original != 0:
    inverted = inverted * 10 + (original % 10)
    original //= 10
else:
    print('Пожалуй')
    print('хватит )')
print(inverted)
```   
**`while else`** - делай пока условие выполняется, когда не выполняется выполни `else`  
Структура for:
```python
for i in range(1,10):
    print(i)

list_of_numbers = [1,2,3,4,5,6,7,8]
for num in list_of_numbers:
    print(num)
for symbol in "Hello world"
    print(symbol)
```   
Если вкратце - `for` - это перебор каждого эллемента, в `C#` такая функция называется `foreach`  

Дополнительные функции:  
```python
range(5) # диапазон от 0 до 4
range(1,5) # диапазон от 1 до 4
range(1,100,5) # диапазон от 1 до 100 с шагом 5 : 1,6,11,16,21, ...
range(start_range,end_range,step_range)
```   
**ВНИМАНИЕ!** `range` - съедает последнюю цифру , то есть `rage(5)` - будет до `4`  

О строках:  
*Есть множество вариантов работы со строками, внизу будут описанны основные схемы*  
```python
text = "Hello world"
print(text[0]) # H - первый символ
print(text[-1]) # d - последний символ
print(text[:]) # печатает весь текст
print(text[:3]) # Hell - печатает от 0 до 3 символ
print(text[6:8]) # wor - печатает от 6 до 8 символы
print(text[0:len(text):3]) # l r добавляется шаг
print(text[start:end:step]) 
```   
Списки:  
*К сожалению - в python нет как таковых массивов, по этому всё делается через списки. Так-же **РЕККОМЕНДУЕТСЯ!** иметь в списках унифицированные данные*
```python
list_of_numbers = [1,2,3,4,5]
list_of_numbers = list(range(1,6))
list_of_number[0] = 10 # заменяет первое значение на 10
list_of_numbers.append(15) # добавляет в конец 15
list_of_number.remuve(10) # удаляет 10 из списка
```   
Функции:
```python
def print_text(text):
    print(f"You are printing - {text}")

def sum_of_numbers(a,b)
    return a+b

def minus_chek(number):
    if number > 0:
        return number
    elif number = 0:
        return "Zero"
    else:
        return -number
```   