#Строковый тип данных
s = input()  # переменная s имеет строковый тип str
s1 = ''   # пустая строка
s2 = ' '  # строка состоящая из одного символа пробела

#Длиной строки называется количество символов из которых она состоит. Чтобы посчитать длину строки используем встроенную функцию len() (от слова length – длина).
s1 = 'abcdef'
length1 = len(s1)               # считаем длину строки из переменной s1
length2 = len('Python rocks!')  # считаем длину строкового литерала
print(length1)                  #считаются все символы, включая пробелы
print(length2)

#Преобразование чисел в строку
num1 = 1777    # целое число
num2 = 17.77   # число с плавающей точкой
s1 = str(num1) # преобразовали целое число в строку '1777'
s2 = str(num2) # преобразовали число с плавающей точкой в строку '17.77'

#Конкатенация строк/Строки, как и числа, можно складывать. Операция сложения строк называется конкатенацией или сцеплением.
s1 = 'ab' + 'bc'
s2 = 'bc' + 'ab'
s3 = s1 + s2 + '!!'
print(s1)
print(s2)
print(s3)
#решение-abbc/bcab/abbcbcab!!

#С помощью конкатенации строк можно эмулировать вывод данных
print('a', 'b', 'c', sep='*', end='!')
print()  # переход на новую строку
print('a' + '*' + 'b' + '*' + 'c' + '!')

