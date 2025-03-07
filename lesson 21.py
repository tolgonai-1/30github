#Оператор in - проверяет что одна строка находится внутри другой:

s = 'https://pygen.ru/'
if 'a' in s:
    print('Введенная строка содержит символ а')
else:
    print('Введенная строка не содержит символ а')   #проверяет, содержится ли в переменной s символ 'a', и выводит:

#Мы можем использовать оператор in вместе с логическим оператором not, например:
s = input()
if '.' not in s:
    print('Введенная строка не содержит символа точки')
#С помощью оператора in мы можем упростить следующий код
if s == 'a' or s == 'e' or s == 'i' or s == 'o' or s == 'u':
    print('YES')
#до вида:

if len(s) == 1 and s in 'aeiou':
    print('YES')
#С помощью оператора in мы можем проверять наличие сразу нескольких символов в строке.

#Приведённый ниже код:

s = 'Sigma'
print('a' in s)
print('z' in s) #выводит:True/False

#Оператор in проверяет, содержится ли одна строка в другой строке как точная последовательность символов. В обеих строках символы должны находиться в том же порядке друг относительно друга и не должны быть разделены другими символами, чтобы выражение с оператором in вернуло значение True.
print('ab' in 'abc')
print('ac' in 'abc') #True/False

#Чувствительность к регистру:
#Проверка с использованием оператора in чувствительна к регистру.
s = 'Alpha'
print('p' in s)
print('P' in s)  #True/False

#####
language1 = 'JavaScript'
language2 = 'Java'

print(language1 in language2)
print(language2 in language1)

###
if s in 'abc123abc':
    print('YES')
else:
    print('NO')

###определить есть слово "синий" в вводимом тексте:
s=input()
if 'синий' in s:
    print('YES')
else:
    print('NO')


####проверяет есть ли суббота/воскресенье в инпуте:
s=input()
if 'суббота' in s or 'воскресенье' in s :
    print('YES')
else:
    print('NO')

#проверяет корректность почты:
email=input()
if '@' in email and '.' in email:
    print('YES')
else:
    print('NO')





