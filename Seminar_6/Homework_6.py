import os
import time
'''
Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
Программа должна выводить данные
Программа должна сохранять данные в текстовом файле
Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
Использование функций. Ваша программа не должна быть линейной
'''
def clear_screen():
    os.system('cls')


# Найти запись по вхождению частей имени
def search_data():
    clear_screen()
    while(True):
        answer = input('Строка поиска(Для выхода нажмите "Enter") :>')
        if answer=="": return
        result=[]
        with open('phonebook.txt','r',encoding='utf8') as datafile:
            for line in datafile:
                result.append(line.strip('\n'))
            result = list(filter(lambda line:answer in line , result))
        for printdata in result:
            output_data_string(printdata)

    
# Вывод контакта
def output_data_string(printdata):
    parse_data = printdata.split(',')
    template = 'Фамилия: {0}\nИмя: {1}\nОтчество: {2}\nТелефон: {3}\n'
    print(template.format(parse_data[0],parse_data[1],parse_data[2],parse_data[3]))

# Сохранение контакта
def save_data_to_file(data_to_save):
    data_to_save = ",".join(data_to_save)+"\n"
    print(data_to_save)
    with open('phonebook.txt','a',encoding='utf8') as datafile:
        datafile.write(data_to_save)

# Счетчик контактов   
def print_data(enum=False):
    count=0
    with open('phonebook.txt','r',encoding='utf8') as datafile:
        for line in datafile:
            if enum:print(count+1)
            output_data_string(line)
            count+=1
    return count


# Показать все записи
def print_all_data():
    count = print_data()
    input('Всего {} Записей.  Нажмите Enter для выхода'.format(count))


# Добавить новый контакт
def add_data():
    while(True):
        print('Добавление записи(""-выход)')
        last_name = input("Фамилия: ")
        first_name = input("Имя: ")
        patronymic = input("Отчество: ")
        phone_number= input("Номер Телефона: ")
        data_to_save=[last_name,first_name,patronymic,phone_number]
        if "" in data_to_save: return
        save_data_to_file(data_to_save)


#основной длок
menu = '''Меню действий:\n
    1 - Показать все записи
    2 - Найти запись по вхождению частей имени
    3 - Найти запись по телефону
    4 - Добавить новый контакт
    5 - Удалить контакт
    6 - Изменить номер телефона у контакта
    7 - Выход'''
    
while (True):
    clear_screen()
    print(menu)
    answer = input('Введите номер действия>:')
    match answer:
        case "1":
            # Показать все записи
            print_all_data()
           
        case "2":
            # Найти запись по вхождению частей имени
            search_data()

        case "3":
            # Найти запись по телефону
            pass

        case "4":
            # Добавить новый контакт
            add_data()  

        case "5":
            # Удалить контакт
            pass

        case "6":   
            # Изменить номер телефона у контакта     
            pass              

        case "7":
            #выход
            exit(0)
            
        case _:
            print("неверный ввод")
            time.sleep(3)                  
