import os
import time
import function as fn

BUSES = 'bus.txt'
DRIVERS = 'driver.txt'
ROUTES = 'rout.txt'


def clear_screen():
    os.system('cls')
    
def Buses_menu():
    bus_menu = '''Действия с данными автобусов:\n
    1 - Вывод всех автобусов
    2 - Добавление автобуса
    3 - Выход\n'''

    clear_screen()
    print(bus_menu)
    answer = input('Введите номер действия>: ')
    match answer:
        case "1":
            # Вывод всех автобусов
            fn.print_all_date(BUSES)

        case "2":
            # Добавление автобуса
            fn.add_bus(BUSES)

        case "3":
            #выход
            exit(0)
            
        case _:
            print("неверный ввод")
            time.sleep(1) 


def Dryvers_menu():
    dryver_menu = '''Действия с данными Водителей:\n
    1 - Вывод всех водителей
    2 - Добавление водителя
    3 - Выход\n'''

    clear_screen()
    print(dryver_menu)
    answer = input('Введите номер действия>: ')
    match answer:
        case "1":
            # Вывод всех водителей
            fn.print_all_date(DRIVERS)

        case "2":
            # Добавление водителя
            fn.add_driver(DRIVERS)

        case "3":
            #выход
            exit(0)
            
        case _:
            print("неверный ввод")
            time.sleep(1) 


def Routes_menu():
    route_menu = '''Действия с данными Водителей:\n
    1 - Вывод всех маршрутов
    2 - Добавление маршрута
    3 - Выход\n'''

    clear_screen()
    print(route_menu)
    answer = input('Введите номер действия>: ')
    match answer:
        case "1":
            # Вывод всех маршрутов
            fn.print_all_date(ROUTES)

        case "2":
            # Добавление маршрута
            pass

        case "3":
            #выход
            exit(0)
            
        case _:
            print("неверный ввод")
            time.sleep(1) 

