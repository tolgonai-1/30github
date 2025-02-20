#Условный оператор if-else:
answer = input('Какой язык программирования мы изучаем?')
if answer == 'Python':
    print('Верно! Мы ботаем Python =)')
    print('Python - отличный язык!')


answer = input('Какой язык программирования мы изучаем?')

if answer == 'Python':
    print('Верно! Мы ботаем Python =)')
    print('Python - отличный язык!')
else:
    print('Не совсем так!')


word = input()
if word == 'Python':
    print('Да')
    print('Нет')


#задача,которая проверяет состоит ли 2 значное число из одинаковых цифр:
num = int(input())
last_digit = num % 10 #последняя цифра числа
first_digit = num // 10 #первая цифра числа
if last_digit == first_digit:
    print('Yes')
else:
    print('No')

#Операторы сравнения:
#оператор присваивания (=)  - присваивает значения переменным.
# условный оператор (==) - проверка элементов на равенство

num1 = int(input())
num2 = int(input())

if num1 < num2:
    print(num1, 'меньше чем', num2)
if num1 > num2:
    print(num1, 'больше чем', num2)

if num1 == num2:  # используем двойное равенство
    print(num1, 'равно', num2)
if num1 != num2:
    print(num1, 'не равно', num2)

#Цепочки сравнений:
age = int(input())
if 3 <= age <= 6:
    print('Вы ребёнок') #проверяет, находится ли значение переменной age в диапазоне от 3-6

#проверяет равенство трех переменных:
if a == b == c:
    print('числа равны')
else:
    print('числа не равны')

#Kоторая считывает три числа и подсчитывает количество чётных чисел:
num1, num2, num3 = int(input()), int(input()), int(input())

counter = 0  # переменная счётчик
if num1 % 2 == 0:
    counter = counter + 1  # увеличиваем счётчик на 1
if num2 % 2 == 0:
    counter = counter + 1  # увеличиваем счётчик на 1
if num3 % 2 == 0:
    counter = counter + 1  # увеличиваем счётчик на 1

print(counter)    #counter, которое показывает, сколько из трех введенных чисел являются четными.


#оператор сравнения
#двоеточие после if/else
#отступ
#if/else - должны быть на одном уровне
#операторов сравнения только так :>=, <=, !=












