#Разница макс - мин  должно быть = средней цифре
number = int(input())

# Извлечение цифр
digit1 = number // 100          # Первая цифра
digit2 = (number // 10) % 10    # Вторая цифра
digit3 = number % 10            # Третья цифра

# Определяем максимальную, минимальную и среднюю цифры
maximum = max(digit1, digit2, digit3)
minimum = min(digit1, digit2, digit3)

# Находим среднюю цифру, используя сумму
middle = digit1 + digit2 + digit3 - maximum - minimum

# Проверка условия "интересного числа"
if (maximum - minimum) == middle:
    print("Число интересное")
else:
    print("Число неинтересное")
 
####Абсолютная сумма###
a1 = float(input())
a2 = float(input())
a3 = float(input())
a4 = float(input())
a5 = float(input())

# Вычисляем сумму модулей
absolute_sum = abs(a1) + abs(a2) + abs(a3) + abs(a4) + abs(a5)

# Вывод результата
print(absolute_sum)


###Манхэттенское расстояние###
# Считывание координат
p1 = int(input())  # координата x первой точки
p2 = int(input())  # координата y первой точки
q1 = int(input())  # координата x второй точки
q2 = int(input())  # координата y второй точки

# Вычисление манхэттенского расстояния
manhattan_distance = abs(p1 - q1) + abs(p2 - q2)

# Вывод результата
print(manhattan_distance)




