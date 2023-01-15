import os
os.system('cls')

# Задача 26:  
# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

def PowerNum(num, pow):
    if pow == 0:
        return 1
    else:
        return PowerNum(num, pow - 1) * num


print ('***Решение задачи № 26***')
while True:
    try:
        A = int(input('Введите значение A >>> '))
        B = int(input('Введите значение B >>> '))

        if A == 0:
            print(f'{A} в степени {B} >>> 0\n')
            break
        elif B == 0:
            print(f'{A} в степени {B} >>> 1\n')  
            break
        elif B > 0:
            print(f'{A} в степени {B} >>> {PowerNum(A, B)}\n')  
            break
        elif B < 0:
            print(f'{A} в степени {B} >>> {1 / PowerNum(A, (-B))}\n')  
            break
    except:
        print('Некорректный ввод. Попробуйте еще раз!\n')


# Задача 28:
# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

def Sum (num1, num2):
    if num2 == 0:
        return num1
    else:
        return Sum (num1, num2 - 1) + 1


print ('***Решение задачи № 28***')
while True:
    try:
        a = int(input('Введите значение a >>> '))
        b = int(input('Введите значение b >>> '))

        if a >= 0 and b >= 0:
            print (f'Сумма чисел {a} и {b} >>> {Sum (a, b)}\n')
            break
        elif a < 0 and b >= 0: print(f'Число{a} не соответствует условию задачи. Попробуйте ещё раз!\n') 
        elif a >= 0 and b < 0: print(f'Число{b} не соответствует условию задачи. Попробуйте ещё раз!\n') 
        elif a < 0 and b < 0: print(f'Оба числа не соответствуют условию задачи. Попробуйте ещё раз!\n') 
    except:
        print('Некорректный ввод. Попробуйте еще раз!\n')