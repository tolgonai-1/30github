print('Hello World')
print('5')
print(56, 87)
print(43.21)

### создание переменных  разных типов,типа snake_case. "=" - является оператором присваивания:

my_age = 27                    #integer (int)
my_mom_names = 'Gulnara'       #string (str)
my_friend_1 = 'Tolgonai'       ##string (str) может содержать числа,в середине или в конце,но не в начале
my_balans = 90.15              # число с плавающей запятой (float)
is_mom = False                  # булево значение (bool)


print(my_age)
print(my_mom_names)
print(my_balans)
print(is_mom)

## Изменение типа переменной:
my_age1 = 'twenty seven'
print(my_age)

#тип переменной NoneType:
apples = None
print('Go to the garden')
#apples =11

#узнать тип переменной
print(type(apples))

print(type(my_age))

print(my_balans, type(my_balans))

#смена типа переменной,перед ее выводом
print(float(my_age))

#сложение и вычитание
print(6+6)
print(9+float(32))
print(2+bool(is_mom))
print('6' + (my_age1))

###Ввод данных, команда input() - считывает данные,


print('What is your first name?')
print('Hello, my name is ', input())
print('What is your last name?')
print('My last name', input())
print('How old are you?')
print("I'm", input())

#задачка При использовании кавычек в команде print() будет выведен текст, заключённый в эти кавычки, а не содержимое переменных a и b.
#чтобы вывелось,то что на переменной =>убираем кавычки
a = "Don't worry"
b = 'Be happy'

print('a')
print('b')


##
print('Какой язык программирования ты изучаешь?')

language = input()

print(language, '- отличный выбор!')
print(language) #тут выводится та переменная,которую введет пользователь

##
a = '10'
b = '20'
c = '30'
# print(a b c) - это выдаст ошибку,так какк если  переменных несккколько -ихи нужно отделять запятыми
#Имя переменной может содержать буквы, цифры и символ нижнего подчеркивания (_). 😇
#Имя переменной не может начинаться с цифры. 😇
#Имя переменной не может содержать пробелы.







