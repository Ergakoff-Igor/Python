import os
import time
import menu as Menu

def clear_screen():
    os.system('cls')
    

main_menu = '''Главное меню:\n
1 - Действия с данными автобусов
2 - Действия с данными водителей
3 - Действия с данными маршрутов
4 - Выход\n'''

clear_screen()
print(main_menu)
answer = input('Введите номер действия>: ')
match answer:
    case "1":
        # Действия с данными автобусов
        Menu.Buses_menu()

    case "2":
        # Действия с данными водителей
        Menu.Dryvers_menu()

    case "3":
        # Действия с данными маршрутов
        Menu.Routes_menu()      

    case "4":
        #выход
        exit(0)
        
    case _:
        print("неверный ввод")
        time.sleep(1) 