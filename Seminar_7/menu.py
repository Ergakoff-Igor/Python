import os
import time
import function as fn

BUSES = 'bus.txt'
DRIVERS = 'driver.txt'
ROUTES = 'route.txt'


def clear_screen():
    os.system('cls')
    
def Buses_menu():
    bus_menu = '''Действия с данными автобусов:\n
1 - Вывод всех автобусов
2 - Добавление автобуса
3 - Удаление автобуса
4 - Выход\n'''

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
            # Удаление автобуса
            fn.dell_date(BUSES, 'bus')

        case "4":
            #выход
            exit(0)
            
        case _:
            print("неверный ввод")
            time.sleep(1) 


def Dryvers_menu():
    dryver_menu = '''Действия с данными водителей:\n
1 - Вывод всех водителей
2 - Добавление водителя
3 - Удаление водителя
4 - Выход\n'''

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
            # Удаление водителя
            fn.dell_date(DRIVERS, 'D')

        case "4":
            #выход
            exit(0)
            
        case _:
            print("неверный ввод")
            time.sleep(1) 


def Routes_menu():
    route_menu = '''Действия с данными маршрутов:\n
1 - Вывод всех маршрутов
2 - Добавление маршрута
3 - Удаление маршрута
3 - Выход\n'''

    clear_screen()
    print(route_menu)
    answer = input('Введите номер действия>: ')
    match answer:
        case "1":
            # Вывод всех маршрутов
            fn.print_all_routes(BUSES, DRIVERS, ROUTES)

        case "2":
            # Добавление маршрута
            fn.add_route(BUSES, DRIVERS, ROUTES)

        case "3":
            # Удаление маршрута
            fn.dell_date(ROUTES, 'm')

        case "4":
            #выход
            exit(0)
            
        case _:
            print("неверный ввод")
            time.sleep(1) 

