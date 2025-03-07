#Модуль math используется для проведения вычислений с действительными числами.
# нужно сперва запустить
import math

num1 = math.sqrt(2)     # вычисление квадратного корня из двух
num2 = math.ceil(3.8)   # округление числа вверх
num3 = math.floor(3.8)  # округление числа вниз
print(num1)
print(num2)
print(num3)  #выводит: 1.4142135623730951 /4 /3

###чтобы каждый раз не вызывать модуль и ставить точку можно:
from math import *

num1 = sqrt(2)     # вычисление корня квадратного из двух
num2 = ceil(3.8)   # округление числа вверх
num3 = floor(3.8)  # округление числа вниз

print(num1)
print(num2)
print(num3)

#Если нужно использовать только некоторые функции модуля, то мы можем импортировать только их следующим образом:
#from math import sqrt, ceil
from math import sqrt, ceil

print(sqrt(25))
print(ceil(34.7))
print(floor(12.8))  # приведет к ошибке, так как функция floor не подключена

##Евклидово расстояние:
from  math import *
x1=float(input())
x2=float(input())
y1=float(input())
y2=float(input())
num1=pow(x1-y1,2)       ##Возведение числа x в степень n
num2=pow(x2-y2,2)
num3=sqrt(num1 + num2)  ##Квадратный корень числа x
print(num3)

###программа определяющяя площадь круга и длину окружности по заданному радиусу R:
import math
R = float(input()) ##Ввести радиус R:
area = math.pi * R ** 2 # Вычисляем площадь круга
circumference = 2 * math.pi * R  # Вычисляем длину окружности
print(area)
print(circumference)

##Площадь круга вычисляется по формуле ( \pi R^2 ).
##Длина окружности вычисляется по формуле ( 2 \pi R ).

#####нахождение Средних значений:№№№№
from math import *  # Импортируем все функции из модуля math
a = float(input())
b = float(input())
# Вычисляем среднее арифметическое
arithmetic_mean = (a + b) / 2
# Вычисляем среднее геометрическое
geometric_mean = sqrt(a * b)  # теперь можем использовать sqrt() без префикса math.
# Вычисляем среднее гармоническое
harmonic_mean = (2 * a * b) / (a + b)
# Вычисляем среднее квадратичное
quadratic_mean = sqrt((a ** 2 + b ** 2) / 2)  # также используем sqrt() без префикса
print(arithmetic_mean)
print(geometric_mean)
print(harmonic_mean)
print(quadratic_mean)

##Тригонометрическое выражение:
from math import pi,sin,cos,tan,radians
x = radians(float(input()))
y = sin(x) + cos(x) + tan(x)**2
print(y)




