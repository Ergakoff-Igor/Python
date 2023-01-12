# Задача № 47:
# У вас есть код, который вы не можете менять (так часто бывает, когда код в глубине программы используется множество раз и вы не хотите ничего сломать):  transformation = <???> values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список transormed_values = list(map(transformation, values)) Единственный способ вашего взаимодействия с этим кодом - посредством задания функции transformation. Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать список значений, а нужно получить его как есть.
# Напишите такое лямбда-выражение transformation, чтобы transformed_values получился копией values.

# Ввод:
# values = [1, 23, 42, ‘asdfg’]
# transformed_values = list(map(trasformation, values))
# if values == transformed_values:
#     print(‘ok’)
# else:
#     print(‘fail’)

# Вывод: 
# ok

values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

transformation = lambda x: x

transformed_values = list(map(transformation, values))

values[1] = 1

print(values)

print(transformed_values)

# Задача № 49:
# Планеты вращаются вокруг звезд по эллиптическим орбитам. 
# Назовем самой далекой планетой ту, орбита которой имеет самую большую площадь. 
# Напишите функцию find_farthest_orbit(list_of_orbits), которая среди списка орбит планет найдет ту, по которой вращается самая далекая планета. 
# Круговые орбиты не учитывайте: вы знаете, что у вашей звезды таких планет нет, зато искусственные спутники были были запущены на круговые орбиты. 
# Результатом функции должен быть кортеж, содержащий длины полуосей эллипса орбиты самой далекой планеты. 
# Каждая орбита представляет из себя кортеж из пары чисел - полуосей ее эллипса. 
# Площадь эллипса вычисляется по формуле S = pi*a*b, где a и b - длины полуосей эллипса. 
# При решении задачи используйте списочные выражения. 
# Подсказка: проще всего будет найти эллипс в два шага: 
# сначала вычислить самую большую площадь эллипса, а затем найти и сам эллипс, имеющий такую  площадь. 
# Гарантируется, что самая далекая планета ровно одна

# Ввод:
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))

# Вывод: 
# 2.5 10

# Вариант 1:
orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

def find_farthest_orbit(orbits):
     s = [3.14*max(x)*min(x) if max(x) != min(x)
          else 0 for x in orbits]
     return(orbits[s.index(max(s))])

print(*find_farthest_orbit(orbits))

# Вариант 2:
orbits = [(3,6), (10,9), (2,2), (11,11)]

s = [3.14*max(x)*min(x) if max(x) != min(x) else 0 for x in orbits] 
print(orbits[s.index(max(s))])

# Вариант 3:
from math import pi

# S=pi*a*b
orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]



def find_farthest_orbit(list_of_orbits):
    s_max = 0
    index = 0
    list_s = []

    def sqare(a, b):
        return pi * a * b

    for i in range(len(list_of_orbits)):
        x = list_of_orbits[i][0]
        y = list_of_orbits[i][1]
        if x != y:
            if sqare(x, y) > s_max:
                s_max = sqare(x, y)
                index = i
    list_s.append(pi * list_of_orbits[i][0] * list_of_orbits[i][1])

    return [list_of_orbits[index], s_max]


print(find_farthest_orbit(orbits))

# Вариант 4:
def find_farthest_orbit(list_of_orbits):
	list_of_elliptical_orbits = [i for i in list_of_orbits if i[0] != i[1]]
	list_of_areas = [(pi * i[0] * i[1]) for i in list_of_elliptical_orbits]
	max_area_index = list_of_areas.index(max(list_of_areas))
	return list_of_elliptical_orbits[max_area_index]


# Задача № 51:
# Напишите функцию same_by(characteristic, objects), которая проверяет, все ли объекты имеют одинаковое значение некоторой характеристики, 
# и возвращают True, если это так. Если значение характеристики для разных объектов отличается - то False. 
# Для пустого набора объектов, функция должна возвращать True. Аргумент characteristic - это функция, 
# которая принимает объект и вычисляет его характеристику. 

# Ввод:		
# values = [0, 2, 10, 6]				
# if same_by(lambda x: x % 2, values):
# 	print(‘same’)
# else:
# # 	print(‘different’)

# Вывод: same

# Вариант 1:
values = [0, 2, 10, 6]				    

  #same
if filter(lambda x: x % 2, values):
	print('True')
else:
	print('False')

# Вариант 2
values = [0, 2, 10, 6]

def same_by(f, list_num):
    # return set(map(f, list_num))
    return True if len(set(map(f, list_num))) == 1 else False

print(values)
print(same_by(lambda x: x % 7, values))

