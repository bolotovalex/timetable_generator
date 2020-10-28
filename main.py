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
    btn_exit = Button(window, text="Вход", width=20, command=exit_button)
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
    pass
def exit_button():
    exit()

if __name__ == '__main__':
    #dictionary = {1: ['ima', 'kab', 'pn', 'vt', 'sr', 'ct', 'pt'], 2: ['ima2', 'kab2', 'pn2', 'vt2', 'sr2', 'ct2', 'pt2']}
    dictionary={}
    file_path = 'index.html'
    row_position = 1
    result_list = []
    window = Tk()
    window.geometry('1280x768')
    window.title("Создание расписания")
    main_window()
    window.mainloop()



