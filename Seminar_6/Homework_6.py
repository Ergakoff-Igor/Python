import os
import time

FILENAME = 'phonebook.txt'

'''
Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
Программа должна выводить данные
Программа должна сохранять данные в текстовом файле
Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
Использование функций. Ваша программа не должна быть линейной
'''
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
    for list in contact:
        template = "{0:<30} Тел.: {1:<13}"
        print(template.format(
            list[0]+' ' + list[1]+' '+list[2], list[3]))


def search_menu(file):
    menu = '''Меню поиска:\n
    1 - Найти контакт по имени
    2 - Найти контакт по фамилии
    3 - Найти контакт по номеру телефона
    4 - Выход\n'''

    clear_screen()
    print(menu)
    answer = input('Введите номер действия>: ')
    match answer:
        case "1":
            answer = input('Введите имя: ').lower().title()
            print_date (search_date(file, 1, answer))
            
        case "2":
            answer = input('Введите фамилию: ').lower().title()
            print_date (search_date(file, 0, answer))
            
        case "3":
            answer = input('Введите номер телефона: ')
            print_date (search_date(file, 3, answer))
            
        case "4":
            #выход
            exit(0)
            
        case _:
            print("неверный ввод")
            time.sleep(1) 

def search_date(file, index, answer):
    line = read_data_from_file(file)
    result = list(filter(lambda line: answer == line[index], line))
    return result


def add_data(file):
    print('Добавление контакта:')
    surname = input('Введите фамилию >>> ').lower().title()
    first_name = input('Введите имя >>> ').lower().title()
    patronymic = input('Введите отчество >>> ').lower().title()
    phone_number = input('Введите номер телефона >>> ')
    contact = [surname, first_name, patronymic,  phone_number]
    delim = ','
    new_contact = delim.join (contact)
    save_data_to_file(file, new_contact)


def dell_contact(file):
    print('Удаление контакта:')   
    answer = input ('Введите данные контакта >>> ').lower().title()
    with open(file, 'r', encoding='utf8') as datafile:
        lines = read_data_from_file(file)
    with open(file, "w", encoding='utf8') as datafile:
        for line in  lines:
            delim = ','
            line = delim.join (line)            
            if  answer not in line.strip("\n"):
                datafile.write(line + '\n')


def replace_phone_number(file):
    print('Изменение номера телефона:')    
    answer = input ('Введите искомое значение >>> ').lower().title()
    lines = read_data_from_file(file)
    with open(file, "w", encoding='utf8') as datafile:
        for line in  lines:
            if  answer in line:
                new_number = input (f'{line}\n Введите новый номер')
                line[3] = new_number
            delim = ','
            datafile.write(delim.join (line) + '\n')
    

# Меню:

menu = '''Меню действий:\n
1 - Показать все записи
2 - Найти запись
3 - Добавить новый контакт
4 - Удалить контакт
5 - Изменить номер телефона у контакта
6 - Выход\n'''
    
clear_screen()
print(menu)
answer = input('Введите номер действия>: ')
match answer:
    case "1":
        # Показать все записи
        print_all_date(FILENAME)

    case "2":
        # Найти запись
        search_menu(FILENAME)

    case "3":
        # Добавить новый контакт
        add_data(FILENAME)  

    case "4":
        # Удалить контакт
        dell_contact(FILENAME)

    case "5":   
        # Изменить номер телефона у контакта     
        replace_phone_number(FILENAME)       

    case "6":
        #выход
        exit(0)
        
    case _:
        print("неверный ввод")
        time.sleep(1)                  
