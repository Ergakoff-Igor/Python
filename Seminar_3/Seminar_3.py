# Задание 17:
# Дан список чисел. Определите, сколько в нем встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

import random

n = int(input('Введите длину списка >>> '))
l = []
for num in range(0,n):
    
    random_number = round(random.randint(0,5))
    l.append(random_number)

a = set(l)

print(l)
print(len(a))

# Задание 19:
# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо,  K – положительное число.
# Input:   [1, 2, 3, 4, 5] k = 2
# Output:  [4, 5, 1, 2, 3]

# Решение 1:
import random

n = int(input('Введите длину списка >>> '))
l = []
for num in range(0,n):
    
    random_number = round(random.randint(-10,10))
    l.append(random_number)
print(l)

k = int(input('Введите на сколько индексов сдвигать >>> '))
for i in range(k):
    p = l.pop(-1)
    l.insert(0, p)

print(l)

# Решение 2:
K = 2
m = [1, 2, 3, 4, 5]
result = []
for i in range(0, K):
    m.insert(0, m[-1])
    m.pop(-1)
    print(m)

# метод который двигает в обе стороны 

def shiftList(myList, k):
    t = k if k>0 else -k
    if k > 0: myList.reverse()
    for _ in range(t):
        myList.append(myList.pop(0))
    if k > 0: myList.reverse()
    return myList

# Задание 21:
# Напишите программу для печати всех уникальных значений в словаре. 
# Input:  [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}] 
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

dictionary = \
    {
        "I": "S001", 
        "II": "S002", 
        "III": "S001", 
        "IV": "S005", 
        "V": "S005", 
        "VI ": "S009", 
        "VII": "S007"
    }
print(dictionary)

print(set(dictionary.values()))

# Задание 23:
# Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает количество элементов массива, больших предыдущего (элемента с предыдущим номером) 
# Input: [0, -1, 5, 2, 3]
# Output: 2 
# пояснение
# (-1 < 5, 2 < 3)

import random

l = []
for num in range(0,10):
    random_number = round(random.randint(0,5))
    l.append(random_number)

print(l)

count = 0

for i in range(1, len(l)):
    if l[i-1]<l[i]:
        count+=1

print(count)
