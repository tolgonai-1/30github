#Работа с целыми числами:
num1 = 7                # num1 - это число
num2 = 10               # num2 - это число
num3 = num1 + num2      # num3 - это число

print(num3)
#пример:
a = 3
b = 2

print(a + b)
print(a - b)
print(a * b)
print(a / b)

#Запомни: первым делом выполняется умножение или деление, затем сложение и вычитание. Для изменения порядка выполнения операций понадобятся скобки.

num1 = 2 + 3 * 4
num2 = (2 + 3) * 4

print(num1)
print(num2)
                       #Преобразование типов:
s = '1992'
year = int(s)
print(year)  #str ====> int

#Чтобы команда input() работала с переменными целого типа, надо написать так:

num1 = int(input())
num2 = int(input())

print(num1 + num2)

#Преобразование int ====> str
num = 17
s = str(num)



