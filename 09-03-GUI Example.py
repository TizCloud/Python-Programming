from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox
import csv

window = Tk()
window.geometry('350x300')
window.title('Items Management System')
window.resizable(0, 0)
window.config(padx=5, pady=20)
window.option_add('*font', 'tahoma 10')
window.option_add('*Button.background', 'lightgray')

Label(text='Item').grid(row=1, column=0, pady=3, ipadx=5, sticky=W)
ent_name = Entry(width=30)
ent_name.grid(row=1, column=1, sticky=W)

Label(text='Price').grid(row=2, column=0, pady=3, ipadx=5, sticky=W)
ent_price = Entry(width=15)
ent_price.grid(row=2, column=1, sticky=W)

Label(text='Total').grid(row=3, column=0, pady=3, ipadx=5, sticky=W)
ent_remain = Entry(width=15)
ent_remain.grid(row=3, column=1, sticky=W)

Label(text='Description').grid(row=4, column=0, ipadx=5, ipady=3, sticky=NW)
text_dscr = ScrolledText(width=30, height=3)
text_dscr.grid(row=4, column=1, pady=6, sticky=W)

frame1 = Frame(window)
frame1.grid(row=5, column=0, columnspan=2)

btn_first = Button(frame1, text='|<', command=lambda: btn_first_click())
btn_first.pack(side=LEFT, pady=10, padx=3, ipadx=5)

btn_prev = Button(frame1, text='<', command=lambda: btn_prev_click())
btn_prev.pack(side=LEFT, padx=3, ipadx=5)

lbl_row = Label(frame1, text='No.: 0 / 0')
lbl_row.pack(side=LEFT, padx=3, ipadx=5)

btn_next = Button(frame1, text='>', command=lambda: btn_next_click())
btn_next.pack(side=LEFT, padx=3, ipadx=5)

btn_last = Button(frame1, text='>|', command=lambda: btn_last_click())
btn_last.pack(side=LEFT, padx=3, ipadx=5)

frame2 = Frame(window)
frame2.grid(row=6, column=0, columnspan=2)

btn_add = Button(frame2, text='Add', command=lambda: btn_add_click())
btn_add.pack(side=LEFT, pady=15, padx=5, ipadx=5)

btn_save = Button(frame2, text='Save', command=lambda: btn_save_click())
btn_save.pack(side=LEFT, padx=5, ipadx=5)

btn_delete = Button(frame2, text='Delete', command=lambda: btn_delete_click())
btn_delete.pack(side=LEFT, padx=5, ipadx=5)

dataset = []
row_index = -1
num_rows = 0
first_add = True


def read_file():
    global dataset, num_rows
    try:
        with open('product.csv', mode='r', encoding='utf-8', newline='') as file:
            reader = csv.reader(file)
            dataset = list(reader)
            num_rows = len(dataset)
    except IOError as err:
        print(err)


def show_data(index=0):
    global dataset, row_index
    row_index = index
    row = dataset[index]

    name = StringVar(value=row[0])
    ent_name.config(textvariable=name)
    ent_price.config(textvariable=StringVar(value=row[1]))
    ent_remain.config(textvariable=StringVar(value=row[2]))
    text_dscr.delete(1.0, END)
    text_dscr.insert(END, row[3])

    lbl_row.config(text=f'No.: {row_index + 1} / {num_rows}')


def btn_next_click():
    global row_index, num_rows
    if (row_index + 1) >= num_rows:
        return

    row_index += 1
    show_data(row_index)


def btn_last_click():
    global num_rows
    show_data(num_rows - 1)


def btn_prev_click():
    global row_index, num_rows
    if (row_index - 1) < 0:
        return

    row_index -= 1
    show_data(row_index)


def btn_first_click():
    show_data(0)

def btn_add_click():
    global row_index, first_add
    ent_name.delete(0, END)
    ent_price.delete(0, END)
    ent_remain.delete(0, END)
    text_dscr.delete(1.0, END)
    row_index = -1
    lbl_row.config(text='No.: ? / ?')
    if first_add:
        messagebox.showinfo(message='Please Insert Information.')
        first_add = False

def btn_save_click():
    global dataset, row_index

    new_dataset = [
        ent_name.get(), ent_price.get(),
        ent_remain.get(), text_dscr.get(1.0, END).strip()
    ]

    if row_index == -1:
        dataset.append(new_dataset)
    else:
        mb = messagebox.askokcancel(title='Edit', message='Confrim')
        if mb == True:
            dataset[row_index] = new_dataset
        else:
            return

    edit_data(dataset)


def btn_delete_click():
    global row_index
    if row_index == -1:
        return

    mb = messagebox.askokcancel(title='Delete', message='Confrim')
    if mb == True:
        del dataset[row_index]
        edit_data(dataset)
    else:
        return


def edit_data(data):
    try:
        with open('product.csv', mode='w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)
            messagebox.showinfo(message='Information Success.')
    except IOError as err:
        messagebox.showerror(message=err)
    finally:
        renew()


def renew():
    read_file()
    show_data(0)


renew()
window.mainloop()
