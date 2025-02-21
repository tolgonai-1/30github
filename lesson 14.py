#####логические операторы   #Оператор and#####

#программа для учеников от двенадцати лет, которые учатся минимум в  7 классе.
age = int(input('Сколько вам лет?: '))
grade = int(input('В каком классе вы учитесь?: '))
if age >= 12 and grade >= 7: #выполняется  при выполнении обоих условий одновременно
    print('Доступ разрешен.')
else:
    print('Доступ запрещен.')

#Оператор and может объединять произвольное количество условий:
age = int(input('Сколько вам лет?: '))
grade = int(input('В каком классе вы учитесь?: '))
city = input('В каком городе вы живете?: ')
if age >= 12 and grade >= 7 and city == 'Москва':
    print('Доступ разрешен.')
else:
    print('Доступ запрещен.')



#####логические операторы   #Оператор or#####
age = int(input('Сколько вам лет?: '))
grade = int(input('В каком классе вы учитесь?: '))
city = input('В каком городе вы живете?: ')
if age >= 12 and grade >= 7 and (city == 'Москва' or city == 'Санкт-Петербург'): # код выполняется если хотя бы одно из условий истинно.
    print('Доступ разрешен.')
else:
    print('Доступ запрещен.')


#####логические операторы   #Оператор not#####
age = int(input('Сколько вам лет?: '))
if not (age < 12):
    print('Доступ разрешен.')
else:
    print('Доступ запрещен.')


#1. в первую очередь выполняется логическое отрицание not;
#2. далее выполняется логическое умножение and;
#3. далее выполняется логическое сложение or.

#программа которая определяет, является ли заданное натуральное число трёхзначным:
num = int(input())
if 100 <= num <= 999:
    print('Число является трёхзначным')
else:
    print('Число не является трёхзначным')

#программа проверяет, что все три цифры натурального трёхзначного числа различны:
num = int(input())
d3 = num % 10
d2 = num % 100 // 10
d1 = num // 100
if d3 != d2 and d3 != d1 and d2 != d1:
    print('Цифры различны')
else:
    print('Цифры не различны')


#программа которая по координатам точки, не лежащей на осях координат, определяет номер координатной четверти, в которой она находится.
x = int(input())
y = int(input())

if x > 0 and y > 0:
    print('1 четверть')
if x < 0 and y > 0:
    print('2 четверть')
if x < 0 and y < 0:
    print('3 четверть')
if x > 0 and y < 0:
    print('4 четверть')


#задача
a = int(input())

if a >= 2 and a <= 17: #цифры от 2 до 17
    b = 3
    p = a * a + b * b #(7*2=14) + (3*3=9)=21
else:
    b = 5

p = (a + b) * (a + b) #(10)*(10)=100
print(p)














