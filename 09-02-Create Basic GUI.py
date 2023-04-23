#Demo 09-02
from tkinter import *

window = Tk()
window.geometry('200x120')

Label(text='User').grid(row=0, column=0, padx=5)
Entry().grid(row=0, column=1, columnspan=2, pady=5)

Label(text='Pswd').grid(row=1, column=0, padx=5)
Entry().grid(row=1, column=1, columnspan=2, pady=5)

Button(text='OK').grid(row=2, column=1, pady=5)
Button(text='Cancel').grid(row=2, column=2, pady=5)

window.mainloop()

