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
    check_change_time()
    print(f"Частота смены экранов: {change_time} сек.")
    commands()

def make_table_from_list(inlist): 
    os.system(clear_command)
    No = int(1)
    table = PrettyTable()
    table.field_names = ["No", "ФИО", "Спец", "КАБ" ,"ПН", "ВТ", "СР", "ЧТ", "ПТ"]
    for line in inlist:
        line = line.rstrip()
        line = line.split('%')
        table.add_row([No, line[0], line[7], line[1], line[2], line[3], line[4], line[5], line[6]])
        No+=1
    print(table)

def commands():
    print()
    print("Действия:")
    print('д - добавить строку, р - редактировать строку, у - удалить строку, ч - изменить частоту смены экрана', )
    print('с - сохранить,       о - отправить,            в - выход')
    print('Введите букву команды: ', end='')
    choice = input()
    if choice == 'д' or choice == 'l':
        add_item()
    elif choice == 'р' or choice == 'h':
        edit_item()
    elif choice == 'у' or choice == 'e':
        remove_item()
    elif choice == 'с' or choice == 'c':
        make_html()
    elif choice == 'о' or choice == 'j':
        make_html()
        send_file()
    elif choice == 'в' or choice == 'd':
        exit()
    elif choice == 'ч' or choice == 'x':
        change_time_slide()
    else:
        os.system(clear_command)
        print('Неверная комманда. Нажмите ENTER.')
        input()
        main()

def add_item():
    os.system(clear_command)
    print('Введите ФИО(макс 17 символов): ', end='')
    fio = input().strip()
    while len(fio) > 17:
        os.system(clear_command)
        print('Недопустимое количество символов')
        print('Введите ФИО(макс 17 символов): ', end='')
        fio = input().strip()
        
    print('Введите специальность(макс 12 символов): ', end='')
    spec = input().strip()
    while len(spec) > 12:
        os.system(clear_command)
        print('Недопустимое количество символов')
        print('Введите спецальность(макс 12 символов): ', end='')
        spec = input().strip()

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
    

    item_list.append(fio + "%" + kab + "%" + mon + "%" + tue + "%" + wed + "%" + thu + "%" + fri + '%' + spec + '%' + '\n')
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
    
    print('Введите ФИО(макс 17 символов): ', end='')
    fio = input().strip()
    while len(fio) > 17:
        os.system(clear_command)
        print('Недопустимое количество символов')
        print('Введите ФИО(макс 17 символов): ', end='')
        fio = input().strip()
        
    print('Введите специальность(макс 12 символов): ', end='')
    spec = input().strip()
    while len(spec) > 12:
        os.system(clear_command)
        print('Недопустимое количество символов')
        print('Введите спецальность(макс 12 символов): ', end='')
        spec = input().strip()
    
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
    item_list[number_for_edit - 1] = fio + "%" + kab + "%" + mon + "%" + tue + "%" + wed + "%" + thu + "%" + fri + '%' + spec + '%' + '\n'
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

def change_time_slide():
    global change_time
    os.system(clear_command)
    print('Введите время смены экрана в секундах: ', end='')
    time_second = input()
    with open('time_change.txt', 'w') as project:
        project.write(time_second)
    project.close()
    main_menu()

def make_html():
    first_part_file = """<!DOCTYPE html>
<html>
<head>
<!--<meta name="viewport" content="width=device-width, initial-scale=1">-->
<meta charset="UTF-8">
<meta name="viewport"
content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
<meta http-equiv="X-UA-Compatible" content="ie=edge">
<link rel="stylesheet" href="style.css">
<title>Расписание работы</title>
</head>

<body>
<header>
<div class="header__row">
<div class="header__name">ФИО</div>
<div class="header__spec">Спец.</div>
<div class="header__cabinet">Каб</div>
<div class="header__day">Пн</div>
<div class="header__day">Вт</div>
<div class="header__day">Ср</div>
<div class="header__day">Чт</div>
<div class="header__day">Пт</div>
</div>
</header>

<div class="slideshow-container">"""
    raspisanie_section = ''
    item_list.clear()
    read_item_list()
    k=0
    for i in range(len(item_list)):
        line = item_list[i].split('%')
        if i % 10 == 0:
            raspisanie_section += '\n<div class="mySlides fade">\n'
        raspisanie_section += (f'<div class="main__row">\n<div class="main__name">{line[0]}</div>\n<div class="main__spec">{line[7]}</div>\n<div class="main__cabinet">{line[1]}</div>\n<div class="main__time">{line[2]}</div>\n<div class="main__time">{line[3]}</div>\n<div class="main__time">{line[4]}</div>\n<div class="main__time">{line[5]}</div>\n<div class="main__time">{line[6]}</div>\n</div>\n')
        
        if i-k == 9 and i > 0:
            raspisanie_section += '</div>\n'
            k+=10
       
        elif i == len(item_list) - 1:
            raspisanie_section += '</div>\n'
    raspisanie_section += (f'</div>\n<br>\n<div style="text-align:center">\n')


    #Count slides
    for i in range(0,(len(item_list) // 10 + 1)):
        raspisanie_section += (f'<span class="dot"></span>')
    last_part_file = '''<!--<span class="dot"></span> -->
</div>

<script>
var slideIndex = 0;
showSlides();
function showSlides() {
var i;
var slides = document.getElementsByClassName("mySlides");
var dots = document.getElementsByClassName("dot");
for (i = 0; i < slides.length; i++) {
slides[i].style.display = "none";
}
slideIndex++;
if (slideIndex > slides.length) { slideIndex = 1 }
for (i = 0; i < dots.length; i++) {
dots[i].className = dots[i].className.replace(" active", "");
}
slides[slideIndex - 1].style.display = "block";
dots[slideIndex - 1].className += " active";'''

    global time_slide
    last_part_file += (f'\nsetTimeout(showSlides, {int(change_time) * 1000}); // Меняйте изображение каждые 2 секунды\n')

    last_part_file += '''}
</script>
</body>
</html>'''
    with open('index.html', 'w', encoding='utf-8') as project:
        project.write(first_part_file)
        project.write(raspisanie_section)
        project.write(last_part_file)
        project.close()

def read_item_list():
    item_list.clear()
    with open(file_name, encoding='utf-8') as file:
        for line in file:
            item_list.append(line)

def save_file():
    print(item_list)
    with open(file_name, 'w', encoding='utf-8') as project:
        for i in item_list:
            project.write(i)
        project.close()


def check_change_time():
    global change_time
    try_file('time_change.txt')
    with open('time_change.txt') as project:
        for line in project:
            if len(line) != 0:
                change_time = int(line)
                               

if __name__ == '__main__':
    change_time = 12
    file_name = 'save.txt'
    try_file(file_name)
    number = 1
    item_list = []
    main_menu()