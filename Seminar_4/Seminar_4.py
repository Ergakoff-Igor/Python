# Задание 25:
# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался. Количество повторов добавляется к символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2 

string = 'a a a b c a a d c d d'
res = ''
data = {}
array = string.split()
print(array)
for item in array:
    if item in data:
        data[item] += 1
        res += item + '_' + str(data[item]) + ' '
    else:
        data[item] = 0
        res += item + ' '
print(res)

# Задание 27:
# Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих подряд, слова разделены одним или большим числом пробелов или символами конца строки.Определите, сколько различных слов содержится в этом тексте.
# Input: She sells sea shells on the sea shore;The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore,I'm sure that the shells are sea shore shells.
# Output: 19

st = "She sells sea shells on the sea shore;\
The shells that she sells are sea shells I'm sure.\
So if she sells sea shells on the sea shore,\
I'm sure that the shells are sea shore shells."
print(st)
st = st.lower()
st = st.replace(',', " ")
st = st.replace('.', " ")
st = st.replace(';', " ")
st = st.replace('\'', " ")
words = set(st.split())
print(words)
print(len(words))


# Задание 29:
# Ваня и Петя поспорили, кто быстрее решит следующую задачу: “Задана последовательность неотрицательных целых чисел. 
# Требуется определить значение наибольшего элемента последовательности, которая завершается первым встретившимся нулем 
# (число 0 не входит в последовательность)”. Однако 2  друга оказались не такими смышлеными. Никто из ребят не смог до конца
# сделать это задание. Они решили так: у кого будет меньше ошибок в коде, тот и выиграл спор. За помощью товарищи обратились к Вам, студентам.


# Петя:
# n = int(input())
# max_number = 1000
# while n != 0:
#    n = int(input())
#    if max_number > n:
#        max_number = n
# print(max_number)

# # Ваня:
# n = int(input())
# max_number = -1
# while n < 0:
#    n = int(input())
#    if max_number < n:
#        n = max_number
# print(n)

n = int(input('введи число N:'))
if n!=0:
    max_number = n
    while n != 0:
        if max_number < n:
            max_number = n
        n = int(input('введи следуещее число N:'))
    print('максимальное число {}'.format(max_number))
else:
    print('чисел нет')
