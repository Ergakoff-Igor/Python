import os


def clear_screen():
    os.system('cls')


def read_data_from_file(file):
    result = []
    with open(file, 'r', encoding='utf8') as datafile:
        for line in datafile:
            result.append(line.strip('\n').split(', '))
    return result


def save_data_to_file(file, data_list):
    with open(file, 'a', encoding='utf8') as datafile:
        datafile.write(data_list +'\n')


def print_all_date(file):
    array = read_data_from_file(file)
    print_date(array)

def search_date(file, index, answer):
    line = read_data_from_file(file)
    result = list(filter(lambda line: answer == line[index], line))
    return result


def print_all_routes(buses_file, drivers_file, routes_file):  
    array_routes = read_data_from_file(routes_file)
    result = []
    for line in array_routes:  
        array_buses = search_date(buses_file, 0, line[2])
        array_drivers = search_date(drivers_file, 0, line[3])
        sum_array = line[:2] + array_buses[-1] + array_drivers[-1]
        del sum_array[2]
        del sum_array[3]
        result.append(sum_array)
    print_date(result)


def print_date(array):
    for line in array:
        delim = ' '
        new_line = delim.join (line)
        print(new_line)


def count_position(file):
    count = 0
    with open(file, "r", encoding="utf8") as datafile:
        for line in datafile:
            if '\n' in line: count += 1
    return count


def add_bus(file):
    clear_screen()
    print('Добавление автобуса:')
    number = input('Введите номер >>> ').upper()
    bus_id = "bus{}".format(count_position(file) + 1)
    bus = [bus_id, number]
    delim = ', '
    new_bus = delim.join (bus)
    save_data_to_file(file, new_bus)


def add_driver(file):
    clear_screen()
    print('Добавление Водителя:')
    surname = input('Введите фамилию >>> ').lower().title()
    first_name = input('Введите имя >>> ').lower().title()
    patronymic = input('Введите отчество >>> ').lower().title()
    phone_number = input('Введите номер телефона >>> ')
    driver_id = "D{}".format(count_position(file) + 1)
    driver = [driver_id, surname, first_name, patronymic,  phone_number]
    delim = ', '
    new_driver = delim.join (driver)
    save_data_to_file(file, new_driver)


def add_route(buses, drivers, routes_file):
    clear_screen()
    print('Добавление маршрута:') 
    route_id = "m{}".format(count_position(routes_file) + 1)

    route_number = input('Введите номер маршрута >>> ')

    print_all_date(buses)
    answer_bus = input('Укажите порядковый номер автобуса: ')
    bus_id = "bus{}".format(answer_bus)

    print_all_date(drivers)
    answer_driver = input('Укажите порядковый номер водителя: ')
    driver_id = "D{}".format(answer_driver)
   
    route = [route_id, route_number, bus_id, driver_id]
    delim = ', '
    new_route = delim.join (route)
    save_data_to_file(routes_file, new_route)
        

def dell_date(file, tipe_id):
    print_all_date(file)
    answer = input('Введите номер позиции, которую хотите удалить: ')
    id = tipe_id + answer

    with open(file, 'r', encoding='utf8') as datafile:
        lines = read_data_from_file(file)
    with open(file, "w", encoding='utf8') as datafile:
        for line in  lines:
            delim = ', '
            line = delim.join (line)            
            if  id not in line.strip("\n"):
                datafile.write(line + '\n')








