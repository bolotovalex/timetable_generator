from tkinter import *

def main_window():
    #Buttons
    btn_add = Button(window, text="Добавить", width=20, command=add_button)
    btn_add.grid(column=2, row=0)
    btn_edit = Button(window, text="Реактировать", width=20, command=edit_button)
    btn_edit.grid(column=3, row=0)
    btn_delete = Button(window, text="Удалить", width=20, command=delete_button)
    btn_delete.grid(column=4, row=0)
    btn_save = Button(window, text="Сохранить", width=20, command=save_button)
    btn_save.grid(column=5, row=0)
    btn_exit = Button(window, text="Выход", width=20, command=exit_button)
    btn_exit.grid(column=6, row=0)

    #Head
    lbl = Label(window, text="Специалист", font=("Arial Bold", 14), width=20)
    lbl.grid(column=1, row=1)
    lbl = Label(window, text="Кабинет", font=("Arial Bold", 14), width=10)
    lbl.grid(column=2, row=1)
    lbl = Label(window, text="ПН", font=("Arial Bold", 14), width=10)
    lbl.grid(column=3, row=1)
    lbl = Label(window, text="ВТ", font=("Arial Bold", 14), width=10)
    lbl.grid(column=4, row=1)
    lbl = Label(window, text="СР", font=("Arial Bold", 14), width=10)
    lbl.grid(column=5, row=1)
    lbl = Label(window, text="ЧТ", font=("Arial Bold", 14), width=10)
    lbl.grid(column=6, row=1)
    lbl = Label(window, text="ПТ", font=("Arial Bold", 14), width=10)
    lbl.grid(column=7, row=1)

    create_timetable()

def create_timetable():
    global row_position, spec, kab, mon, tue, wed, thu, fri
    print(row_position)
    for key, value in dictionary.items():
        lbl = Label(window, text=key, font=("Arial Bold", 14), width=3)
        lbl.grid(column=0, row=key+1)
        lbl = Label(window, text=value[0], font=("Arial Bold", 14), width=20)
        lbl.grid(column=1, row=key+1)
        lbl = Label(window, text=value[1], font=("Arial Bold", 14), width=10)
        lbl.grid(column=2, row=key+1)
        lbl = Label(window, text=value[2], font=("Arial Bold", 14), width=10)
        lbl.grid(column=3, row=key+1)
        lbl = Label(window, text=value[3], font=("Arial Bold", 14), width=10)
        lbl.grid(column=4, row=key+1)
        lbl = Label(window, text=value[4], font=("Arial Bold", 14), width=10)
        lbl.grid(column=5, row=key+1)
        lbl = Label(window, text=value[5], font=("Arial Bold", 14), width=10)
        lbl.grid(column=6, row=key+1)
        lbl = Label(window, text=value[6], font=("Arial Bold", 14), width=10)
        lbl.grid(column=7, row=key+1)

    lenght = len(dictionary) + 1
    spec = Entry(window, width=20)
    spec.grid(column=1, row=row_position + 1)
    kab = Entry(window, width=12)
    kab.grid(column=2, row=row_position + 1)
    mon = Entry(window, width=12)
    mon.grid(column=3, row=row_position + 1)
    tue = Entry(window, width=12)
    tue.grid(column=4, row=row_position + 1)
    wed = Entry(window, width=12)
    wed.grid(column=5, row=row_position + 1)
    thu = Entry(window, width=12)
    thu.grid(column=6, row=row_position + 1)
    fri = Entry(window, width=12)
    fri.grid(column=7, row=row_position + 1)

def add_button():
    global row_position, spec, kab, mon, tue, wed, thu, fri
    dictionary[row_position] = [spec.get(), kab.get(), mon.get(), tue.get(), wed.get(), thu.get(), fri.get()]
    spec.destroy()
    kab.destroy()
    mon.destroy()
    tue.destroy()
    wed.destroy()
    thu.destroy()
    fri.destroy()
    row_position += 1
    create_timetable()
    print(dictionary)

def edit_button():
    pass
def delete_button():
    pass

def save_button():
    with open(file_txt, 'w', encoding='utf-8') as save_file:
        for key, value in dictionary.items():
            save_file.write(f"{key}%{value[0]}%{value[1]}%{value[2]}%{value[3]}%{value[4]}%{value[5]}%{value[6]}%\n")
        save_file.close()
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
<div class="header__name">Специалист</div>
<div class="header__cabinet">Кабинет</div>
<div class="header__day">Пн</div>
<div class="header__day">Вт</div>
<div class="header__day">Ср</div>
<div class="header__day">Чт</div>
<div class="header__day">Пт</div>
</div>
</header>

<div class="slideshow-container">"""
    raspisanie_section = ''
    result_list = []
    for key, value in dictionary.items():
        result_list.append(value)

    raspisanie_section = ''
    for i in range(len(result_list)):
        if i % 10 == 0:
            raspisanie_section += '<div class="mySlides fade">\n'
        raspisanie_section += (
            f'<div class="main__row">\n<div class="main__name">{result_list[i][0]}</div>\n<div class="main__cabinet">{result_list[i][1]}</div>\n<div class="main__time">{result_list[i][2]}</div>\n<div class="main__time">{result_list[i][3]}</div>\n<div class="main__time">{result_list[i][4]}</div>\n<div class="main__time">{result_list[i][5]}</div>\n<div class="main__time">{result_list[i][6]}</div>\n</div>\n')
        if i % 9 == 0 and i > 0:
            raspisanie_section += '</div>\n'
        elif i == len(result_list) - 1:
            raspisanie_section += '</div>\n'
    raspisanie_section += (f'</div>\n<br>\n<div style="text-align:center">\n')

    #Count slides
    for i in range(0,(len(result_list) // 10 + 1)):
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
dots[slideIndex - 1].className += " active";
setTimeout(showSlides, 3000); // Меняйте изображение каждые 2 секунды
}
</script>
</body>
</html>'''

    with open(file_index, 'w', encoding='utf-8') as project:
        project.write(first_part_file)
        project.write(raspisanie_section)
        project.write(last_part_file)
        project.close()

def exit_button():
    exit()

if __name__ == '__main__':
    file_txt = 'save.txt'
    file_index = 'index.html'
    dictionary = {}
    try:
        file = open(file_txt)
    except IOError as e:
        with open(file_txt, 'w', encoding='utf-8') as project:
            project.close()

    with open(file_txt, 'r', encoding='utf-8') as project:
        text = project.read().split('\n')

    for line in text:
        line = line.split('%')
        if len(line) > 1:
            dictionary[int(line[0])] = [line[1], line[2], line[3], line[4], line[5], line[6], line[7]]
    print(dictionary)
            #dictionary = {1: ['ima', 'kab', 'pn', 'vt', 'sr', 'ct', 'pt'], 2: ['ima2', 'kab2', 'pn2', 'vt2', 'sr2', 'ct2', 'pt2']}

    file_path = 'index.html'
    row_position = len(dictionary) + 1
    result_list = []
    window = Tk()
    window.geometry('1280x768')
    window.title("Создание расписания")
    main_window()
    window.mainloop()



