import os
os.system('cls')

import random

# Задача 22:
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа.
# n - кол-во элементов первого набора.
# m - кол-во элементов второго набора.
# Значения генерируются случайным образом.
# Input: 11 6
# (значения сгенерированы случайным образом
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18)
# Output: 11 6
# 6 12

# Метод заполнения списка случайными натуральными числами:
def GetArray(N, min = 1, max = 10):
    array = []
    for _ in range(0, N):
        random_number = round(random.randint(min, max))
        array.append(random_number)
    return array
    

# Метод нахождения совпадений среди двух списков:
def FindMatches(arr1, arr2):
    resultSet = (set(arr1)).intersection(set(arr2))
    result = sorted(list(resultSet))
    if result:
        print (f'Среди данных спискаов имеются следующие совпадения: \n{result}')
    else:
        print (f'Среди данных спискаов нет совпадений')


print ('Решение задачи № 22')
while True:
    try:
        n = int(input('Введите длину первого списка >>> '))
        m = int(input('Введите длину второго списка >>> '))

        if n > 0 and m > 0:
            array1 = GetArray(n, max = 20)
            print (f'Первый список -> {array1}')
            array2 = GetArray(m, max = 20)
            print (f'Второй список -> {array2}')                       
            FindMatches(array1, array2)
            break
        else: print('Количество элементов списка не может быть отрицательным либо равным "0". Попробуйте ещё раз!')
    except:
        print('Некорректный ввод. Попробуйте еще раз!')

# Задача 24:
# В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов. 
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
# Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, 
# находясь перед некоторым кустом заданной во входном файле грядки.
# Input: 4
# (значения сгенерированы случайным образом
# 4 2 3 1)
# Output: 9

# Метод нахождения максимального количества ягод и номера позиции:
def PickBerries (arr):
    sum = 0
    maxSum = 0
    maxPos = 0
    for i in range(0, len(arr)):
        sum = arr[i-2] + arr[i-1] + arr[i]
        if sum > maxSum: 
            maxSum = sum
            maxPos = i
    if maxPos == 0: maxPos = len(arr)
    print (f'Максимальное количество ягод -> {maxSum} \n№ куста, возле которого нужно остановиться -> {maxPos}')


print ('Решение задачи № 24')
while True:
    try:
        N = int(input('Введите Количество кустов >>> '))

        if N > 3 :
            array = GetArray(N, max = 10)
            print (f'Количество ягод на кустах -> {array}')   
            PickBerries (array)              
            break
        elif N <= 0: print('Количество кустов не может быть отрицательным либо равным "0". Попробуйте ещё раз!')
        elif 0 < N < 4: print('Собирающий модуль за раз соберет все ягоды. Попробуйте ещё раз!')
    except:
        print('Некорректный ввод. Попробуйте еще раз!')