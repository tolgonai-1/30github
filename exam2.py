#определить заканчивается ли год на 00:
if year % 100 == 0:
    print("YES")
else:
    print("NO")


#Шахматная доска-определение цвета клеток:
col1 = int(input())
row1 = int(input())
col2 = int(input())
row2 = int(input())

# Определяем цвета клеток по чётности суммы координат
color1 = (col1 + row1) % 2  # Чётный - чёрный (0), Нечётный - белый (1)
color2 = (col2 + row2) % 2  # Чётный - чёрный (0), Нечётный - белый (1)

# Сравниваем цвета и выводим результат
if color1 == color2:
    print("YES")
else:
    print("NO")


#определение возраста и пола девочек,где принимают только девочек от 10-15 лет:
year=int(input())
gender=input()
if 10 <= year <=15 and gender == 'f':
    print('YES')
else:
    print('NO')

#программa, которая считывает целое число и выводит соответствующую ему римскую цифру.
num=int(input())
if num == 1:
    print('I')
elif num == 2:
    print('II')
elif num == 3:
    print('III')
elif num == 4:
    print('IV')
elif num == 5:
    print('V')
elif num == 6:
    print('VI')
elif num == 7:
    print('VII')
elif num == 8:
    print('VIII')
elif num == 9:
    print('IX')
elif num == 10:
    print('X')
else:
    print('ошибка')


#YES or NO – вот в чём вопрос:

num = int(input())

if num % 2 != 0:
    print("YES")
elif 2 <= num <= 5:
    if num % 2 == 0:
        print('NO')
elif 6 <= num <= 20:
    if num % 2 == 0:
        print('YES')
else:  # просто else без условия
    if num > 20 and num % 2 == 0:
        print('NO')



#Даны две различные клетки шахматной доски. Напишите программу, которая определяет, может ли слон попасть с первой клетки на вторую одним ходом
# Считываем четыре числа по отдельности
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

# Проверяем, может ли слон попасть на вторую клетку
if (x1 - x2 == y1 - y2) or (x1 - x2 == -(y1 - y2)):
    print("YES")
else:
    print("NO"


#Даны две различные клетки шахматной доски. Напишите программу, которая определяет, может ли конь попасть с первой клетки на вторую одним ходом

# Считываем четыре числа
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

# Проверяем, может ли конь попасть на вторую клетку
if (x1 + 2 == x2 and (y1 + 1 == y2 or y1 - 1 == y2)) or \
   (x1 - 2 == x2 and (y1 + 1 == y2 or y1 - 1 == y2)) or \
   (x1 + 1 == x2 and (y1 + 2 == y2 or y1 - 2 == y2)) or \
   (x1 - 1 == x2 and (y1 + 2 == y2 or y1 - 2 == y2)):
    print("YES")
else:
    print("NO")

#Даны две различные клетки шахматной доски. Напишите программу, которая определяет, может ли ферзь попасть с первой клетки на вторую одним ходом
# Считываем четыре числа
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

# Проверяем, может ли ферзь попасть на вторую клетку
if x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2):
    print("YES")
else:
    print("NO")

