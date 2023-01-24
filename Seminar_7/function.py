import os

def clear_screen():
    os.system('cls')

def read_data_from_file(file):
    result = []
    with open(file, 'r', encoding='utf8') as datafile:
        for line in datafile:
            result.append(line.strip('\n').split(','))
    return result


def save_data_to_file(file, data_list):
    with open(file, 'a', encoding='utf8') as datafile:
        datafile.write(data_list +'\n')

def print_all_date(file):
    contact = read_data_from_file(file)
    print_date(contact)


def print_date(contact):
    for line in contact:
            print(line)


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
    delim = ','
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
    delim = ','
    new_driver = delim.join (driver)
    save_data_to_file(file, new_driver)







