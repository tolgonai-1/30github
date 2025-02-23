#Решение задач:
#Даны три целых числа. Определите, сколько среди них совпадающих. Программа должна вывести одно из чисел: 3 (если все совпадают),2 (если два совпадает) или 0  (если все числа различны).
#1 способ. Использование вложенного условного оператора.
a, b, c = int(input()), int(input()), int(input())

if a == b:
    if b == c:
        print(3)
    else:
        print(2)
else:
    if a == c:
        print(2)
    else:
        if b == c:
            print(2)
        else:
            print(0)
#2 способ. Использование каскадного условного оператора.

a, b, c = int(input()), int(input()), int(input())

if a == b == c:
    print(3)
elif a == b:
    print(2)
elif b == c:
    print(2)
elif a == c:
    print(2)
else:
    print(0)

#3 способ. Использование каскадного условного оператора и логического оператора or.

a, b, c = int(input()), int(input()), int(input())

if a == b == c:
    print(3)
elif a == b or b == c or a == c:
    print(2)
else:
    print(0)
