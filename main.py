#!/usr/bin/python3
from tkinter import *

def add_row():
    global row_position, spec, kab, mon, tue, wed, thu, fri, result_list, lbl_spec, lbl_kab, lbl_mon, lbl_tue, lbl_wed, lbl_thu, lbl_fri
    row_position += 1
    lbl_spec = Label(window, text=spec.get(), font=("Arial Bold", 14), width=20)
    lbl_spec.grid(column=0, row=row_position)
    lbl_kab = Label(window, text=kab.get(), font=("Arial Bold", 14), width=10)
    lbl_kab.grid(column=1, row=row_position)
    lbl_mon = Label(window, text=mon.get(), font=("Arial Bold", 14), width=10)
    lbl_mon.grid(column=2, row=row_position)
    lbl_tue = Label(window, text=tue.get(), font=("Arial Bold", 14), width=10)
    lbl_tue.grid(column=3, row=row_position)
    lbl_wed = Label(window, text=wed.get(), font=("Arial Bold", 14), width=10)
    lbl_wed.grid(column=4, row=row_position)
    lbl_thu = Label(window, text=thu.get(), font=("Arial Bold", 14), width=10)
    lbl_thu.grid(column=5, row=row_position)
    lbl_fri = Label(window, text=fri.get(), font=("Arial Bold", 14), width=10)
    lbl_fri.grid(column=6, row=row_position)
    list_for_add = [spec.get(), kab.get(), mon.get(), tue.get(), wed.get(), thu.get(), fri.get()]
    result_list.append(list_for_add)
    print(result_list)

def remove_row():
    global row_position, result_list, lbl_spec, lbl_kab, lbl_mon, lbl_tue, lbl_wed, lbl_thu, lbl_fri
    if row_position > 4:
        row_position = row_position - 1
        result_list.pop(-1)
        lbl_spec.destroy()
        lbl_kab.destroy()
        lbl_mon.destroy()
        lbl_tue.destroy()
        lbl_wed.destroy()
        lbl_thu.destroy()
        lbl_fri.destroy()
    print(result_list)


def save_result():
    global row_position, spec, kab, mon, tue, wed, thu, fri, result_list
    '''result_list = [[[] for j in range(0,7)] for i in range(0,row_position - 1)]
    for i in result_list:
        print(i)'''
    print(spec.get())


def head_program():
    global row_position, spec, kab, mon, tue, wed, thu, fri, result_list

    lbl = Label(window, text="Добавление значений поля:", font=("Arial Bold", 14), width=30)
    lbl.grid(column=0, row=0)
    lbl = Label(window, text="Специалист", font=("Arial Bold", 14), width=20)
    lbl.grid(column=0, row=1)
    lbl = Label(window, text="Кабинет", font=("Arial Bold", 14), width=10)
    lbl.grid(column=1, row=1)
    lbl = Label(window, text="ПН", font=("Arial Bold", 14), width=10)
    lbl.grid(column=2, row=1)
    lbl = Label(window, text="ВТ", font=("Arial Bold", 14), width=10)
    lbl.grid(column=3, row=1)
    lbl = Label(window, text="СР", font=("Arial Bold", 14), width=10)
    lbl.grid(column=4, row=1)
    lbl = Label(window, text="ЧТ", font=("Arial Bold", 14), width=10)
    lbl.grid(column=5, row=1)
    lbl = Label(window, text="ПТ", font=("Arial Bold", 14), width=10)
    lbl.grid(column=6, row=1)


    spec = Entry(window, width=20)
    spec.grid(column=0, row=2)
    kab = Entry(window, width=12)
    kab.grid(column=1, row=2)
    mon = Entry(window, width=12)
    mon.grid(column=2, row=2)
    tue = Entry(window, width=12)
    tue.grid(column=3, row=2)
    wed = Entry(window, width=12)
    wed.grid(column=4, row=2)
    thu = Entry(window, width=12)
    thu.grid(column=5, row=2)
    fri = Entry(window, width=12)
    fri.grid(column=6, row=2)
    lbl = Label(window, text="Расписание:", font=("Arial Bold", 14), width=20)
    lbl.grid(column=0, row=3)
    btn_add = Button(window, text="Добавить строку", width=20, command=add_row)
    btn_add.grid(column=7, row=1)
    #btn_copy = Button(window, text="Скопировать строку", width=20, command=copy_row)
    #btn_copy.grid(column=7, row=2)
    btn_del = Button(window, text="Удалить строку", width=20, command=remove_row)
    btn_del.grid(column=7, row=3)
    btn_save = Button(window, text="Сохранить", width=20, command=save_result)
    btn_save.grid(column=7, row=4)

    global row_position
    row_position = 4

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    row_position = 0
    result_list = []
    window = Tk()
    window.geometry('1200x768')
    window.title("Создание расписания")
    head_program()
    window.mainloop()


