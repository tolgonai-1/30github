#Строковый тип данных
s = input()  # переменная s имеет строковый тип str
s1 = ''   # пустая строка
s2 = ' '  # строка состоящая из одного символа пробела

#Длиной строки называется количество символов из которых она состоит. Чтобы посчитать длину строки используем встроенную функцию len() (от слова length – длина).
s1 = 'abcdef'
length1 =
# считаем длину строки из переменной s1
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

#Умножение строки на число:
s = 'Hi' * 4 #умножит строку
print(s)

#строку состоящяя из 75 символов - :
print('-' * 75)

#Тройные кавычки в Python используются для многострочного (multiline) текста:
text = '''Python is an interpreted, high-level, general-purpose programming language.
Created by Guido van Rossum and first released in 1991, Python design 
philosophy emphasizes code readability with its notable use of significant whitespace.'''

#сложенеи строк:
str1 = '1'
str2 = str1 + '2' + str1
str3 = str2 + '3' + str2
str4 = str3 + '4' + str3
print(str4)
#121312141213121

#сложение и умножение:
mystr = '123' * 3 + '456' * 2 + '789' * 1
print(mystr)  #123123123456456789

#чтобы вывести текст(можно использовать \)
s1 = '"Python is a great language!",'
s2 = 'said Fred.'
s3 = '"I don\'t ever remember having this much fun before."'
print(s1,s2,s3)


#Напишите программу, которая считывает с клавиатуры две строки – имя и фамилию пользователя – и выводит фразу:
a=input()
b=input()
print(f'Hello {a} {b}! You have just delved into Python')

#программa которая считывает с клавиатуры название футбольной команды и длину названия:
name=input()
length=len(name) # для счета количества символов
print(f'Футбольная команда {name} имеет длину {length} символов')


