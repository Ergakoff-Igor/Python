import os
os.system('cls')

# Задача 16:
# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь вводит натуральное число N – количество элементов в массиве и число, которое необходимо проверить - X.
# Заполните массив случайными натуральными числами от 1 до N/2.
# Выведите, сколько раз X встречается в массиве.
# Ввод: 5
# Ввод: 1
# 1 2 1 2 2
# # Вывод: 2

print ('Решение задачи № 16')
while True:
    try:
        import random

        N = int(input('Введите длину списка >>> '))
        if N > 3:
            array = []
            for num in range(0, N):

                random_number = round(random.randint(1, N // 2))
                array.append(random_number)
            print(array)
            
            X = int(input('Введите искомое число >>> '))
            count = 0
            if X in array:
                for item in array:
                    if item == X: count +=1
                print(f' Число {X} в списке {array} встречается {count} раз')
                break
            else:
                print (f'Числа {X} нет в списке {array}')
                break

        elif N == 0: print ('В списке не может быть "0" элементов. Попробуйте ещё раз!')
        elif N == 1: print ('Нет смысла искать элементы в списке, т.к. элемент всего один и это "1". Попробуйте ещё раз!')
        elif N == 2 or N == 3: print ('В списке только элементы "1", других быть не может. Попробуйте ещё раз!')
        elif N < 0: print ('Количество элементов списка не может быть отрицательным. Попробуйте ещё раз!')
    except:
        print('Некорректный ввод. Попробуйте еще раз!')

# # Задача 18:
# # Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# # Пользователь вводит натуральное число N – количество элементов в массиве и число, которое необходимо проверить - X.
# # Заполните массив случайными натуральными числами от 1 до N.
# # Выведите, ближайший к X элемент. Если есть несколько элементов, которые равноудалены от X, выведите наименьший по величине.
# # Ввод: 10
# # Ввод: 7
# # 1 2 1 8 9 6 5 4 3 4
# # Вывод: 6
print ('Решение задачи № 18')
while True:
    try:
        import random

        N = int(input('Введите длину списка >>> '))
        if N > 1:
            array = []
            for num in range(0, N):
                random_number = round(random.randint(1, N))
                array.append(random_number)
            print(array)

            X = int(input('Введите натуральное число >>> '))
            if X in array:
                print (f'Число {X} присутствует в списке {array}')
                break
            elif X < min(array): 
                print (f'Ближайший элемент в массиве {array} к числу {X} -> {min(array)}')
                break
            elif X > max(array): 
                print (f'Ближайший элемент в массиве {array} к числу {X} -> {max(array)}')
                break
            else:
                litle =[]
                big =[]
                for item in array:
                    if item < X: litle.insert(0, item)
                    elif item > X: big.insert(0, item)

            if (X - max(litle)) <= (min(big) - X): 
                print (f'Ближайший элемент в массиве {array} к числу {X} -> {max(litle)}')
                break
            elif (X - max(litle)) > (min(big) - X): 
                print (f'Ближайший элемент в массиве {array} к числу {X} -> {min(big)}')
                break

        elif N == 0: print ('В списке не может быть "0" элементов. Попробуйте ещё раз!')
        elif N == 1: print ('Нет смысла искать элементы в списке, т.к. элемент всего один и это "1". Попробуйте ещё раз!')
        elif N < 0: print ('Количество элементов списка не может быть отрицательным. Попробуйте ещё раз!')
    except:
        print('Некорректный ввод. Попробуйте еще раз!')    

# Задача 20:
# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.

# А русские буквы оцениваются так:
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.

# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

# Ввод: ноутбук
# Вывод: 12

print ('Решение задачи № 20')
while True:
    try:
        word = input ('Введите слово >>> ')
        
        EnLetter = \
            {
                "A": 1, "E": 1, "I": 1, "O": 1, "U": 1, "L": 1, "N": 1, "S": 1, "T": 1, "R": 1,
                "D": 2, "G": 2,
                "B": 3, "C": 3, "M": 3, "P": 3,
                "F": 4, "H": 4, "V": 4, "W": 4, "Y": 4,
                "K": 5,
                "J": 8, "X": 8,
                "Q": 10, "Z": 10
            }

        RuLetter = \
            {
                "А": 1, "В": 1, "Е": 1, "И": 1, "Н": 1, "О": 1, "Р": 1, "С": 1, "Т": 1,
                "Д": 2, "К": 2, "Л": 2, "М": 2, "П": 2, "У": 2,
                "Б": 3, "Г": 3, "Ё": 3, "Ь": 3, "Я": 3,
                "Й": 4, "Ы": 4,
                "Ж": 5, "З": 5, "Х": 5, "Ц": 5, "Ч": 5,
                "Ш": 8, "Э": 9, "Ю": 10,
                "Ф": 10, "Щ": 10, "Ъ": 10
            }


        word = word.upper()
        result = 0
        count =0

        if word[0] in EnLetter:
            for item in word:
                result += EnLetter.get(item)
                count += 1
        elif word[0] in RuLetter:
            for item in word:
                result += RuLetter.get(item)
                count += 1
        if result > 0 and count == len(word):            
            print (result)
            break
      
        else: print('Некорректный ввод. Попробуйте еще раз!')
    except:
        print('Некорректный ввод. Попробуйте еще раз!')

        