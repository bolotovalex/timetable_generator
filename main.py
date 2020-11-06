#!/usr/bin/python3
import os
import platform

if platform.system() == "Windows":
    clear_command = 'cls'
    pip_v = 'pip'
else:
    clear_command = 'clear'
    pip_v = 'pip3'


try:
    import prettytable
except ModuleNotFoundError:
    os.system(f"{pip_v} install prettytable")

from prettytable import PrettyTable

def try_file(filename):
    try:
        file = open(filename)
    except IOError as e:
        with open(filename, 'w', encoding='utf-8') as project:
            project.close()

def main_menu():
    print(item_list)
    os.system(clear_command)
    read_item_list()
    make_table_from_list(item_list)
    commands()

def make_table_from_list(inlist): 
    os.system(clear_command)
    No = int(1)
    table = PrettyTable()
    table.field_names = ["No", "ФИО", "КАБ" ,"ПН", "ВТ", "СР", "ЧТ", "ПТ"]
    for line in inlist:
        line = line.rstrip()
        line = line.split('%')
        table.add_row([No, line[0], line[1], line[2], line[3], line[4], line[5], line[6]])
        No+=1
    print(table)

def commands():
    print()
    print("Действия:")
    print('д - добавить строку, р - редактировать строку, у - удалить строку')
    print('с - сохранить,       о - отправить,            в - выход')
    print('Введите букву команды: ', end='')
    choice = input()
    if choice == 'д':
        add_item()
    elif choice == 'р':
        edit_item()
    elif choice == 'у':
        remove_item()
    elif choice == 'с':
        make_html()
    elif choice == 'о':
        make_html()
        send_file()
    elif choice == 'в':
        exit()
    else:
        os.system(clear_command)
        print('Неверная комманда. Нажмите ENTER.')
        input()
        main()

def add_item():
    os.system(clear_command)
    print('Введите ФИО: ', end='')
    fio = input().strip()
    print('Введите номер кабинета: ', end='')
    kab = input().strip()
    print('Введите время работы специалиста в ПОНЕДЕЛЬНИК(например 8:00-12:00): ', end='')
    mon = input().strip()
    print('Введите время работы специалиста во ВТОРНИК(например 8:00-12:00): ', end='')
    tue = input().strip()
    print('Введите время работы специалиста в СРЕДУ(например 8:00-12:00): ', end='')
    wed = input().strip()
    print('Введите время работы специалиста в ЧЕТВЕРГ(например 8:00-12:00): ', end='')
    thu = input().strip()
    print('Введите время работы специалиста в ПЯТНИЦУ(например 8:00-12:00): ', end='')
    fri = input().strip()
    item_list.append(fio + "%" + kab + "%" + mon + "%" + tue + "%" + wed + "%" + thu + "%" + fri + '%' + '\n')
    save_file()
    main_menu()

def edit_item():
    os.system(clear_command)
    read_item_list()
    make_table_from_list(item_list)
    print()  
    print('Введите номер для редактирования: ', end='')
    number_for_edit = int(input())
    os.system(clear_command)
    print('Введите ФИО: ', end='')
    fio = input().strip()
    print('Введите номер кабинета: ', end='')
    kab = input().strip()
    print('Введите время работы специалиста в ПОНЕДЕЛЬНИК(например 8:00-12:00): ', end='')
    mon = input().strip()
    print('Введите время работы специалиста во ВТОРНИК(например 8:00-12:00): ', end='')
    tue = input().strip()
    print('Введите время работы специалиста в СРЕДУ(например 8:00-12:00): ', end='')
    wed = input().strip()
    print('Введите время работы специалиста в ЧЕТВЕРГ(например 8:00-12:00): ', end='')
    thu = input().strip()
    print('Введите время работы специалиста в ПЯТНИЦУ(например 8:00-12:00): ', end='')
    fri = input().strip()
    item_list[number_for_edit - 1] = fio + "%" + kab + "%" + mon + "%" + tue + "%" + wed + "%" + thu + "%" + fri + '%' + '\n'
    #item_list.append(fio + "%" + kab + "%" + mon + "%" + tue + "%" + wed + "%" + thu + "%" + fri + '%' + '\n')
    save_file()
    main_menu()

def remove_item():
    os.system(clear_command)
    read_item_list()
    make_table_from_list(item_list)
    print()  
    print('Введите номер для удаления: ', end='')
    number_for_delete = int(input())
    os.system(clear_command)
    print(item_list[number_for_delete - 1].split('%'))
    print()
    print('Вы действительно хотите удалить эту строку Д/Н?: ', end='')
    choice = input()
    if choice == 'Д' or choice == 'д' or choice == 'Y' or choice == 'y':
        item_list.pop(number_for_delete - 1)
    save_file()
    main_menu()

def make_html():
    pass

def read_item_list():
    item_list.clear()
    with open(file_name, encoding='utf-8') as file:
        for line in file:
            item_list.append(line)

def save_file():
    print(item_list)
    with open(file_name, 'w', encoding='utf-l8') as project:
        for i in item_list:
            project.write(i)
        project.close()



if __name__ == '__main__':

    file_name = 'save.txt'
    try_file(file_name)
    number = 1
    item_list = []
    main_menu()