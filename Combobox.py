import tkinter as tk
from tkinter import ttk


def show_day():
    print(combo.get())  # возвращает строку


def set_day():
    print(combo.set('Sunday'))


weekDays = 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'

win = tk.Tk()
win.geometry(f'300x400+800+150')
win.title('My first app')

combo = ttk.Combobox(win, values=weekDays)
combo.current(0)
ttk.Button(win, text='show_day', command=show_day).pack()
ttk.Button(win, text='set_day', command=set_day).pack()
combo.pack()


win.mainloop()
