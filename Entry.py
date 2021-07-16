import tkinter as tk


def get_entry():
    value = name.get()
    print(value if value else 'Empty Entry')


def del_entry():
    name.delete(0, tk.END)


def submit():
    print(name.get())
    print(password.get())
    del_entry()
    password.delete(0, tk.END)


win = tk.Tk()
win.geometry(f'400x500+100+200')
win.title('My first app')
tk.Label(win, text='Name').grid(row=0, column=0, sticky='w')
tk.Label(win, text='Password').grid(row=1, column=0, sticky='w')

name = tk.Entry(win)
password = tk.Entry(win, show='*')
name.grid(row=0, column=1)
password.grid(row=1, column=1)

tk.Button(win, text='get', command=get_entry).grid(row=2, column=0, sticky='we')
tk.Button(win, text='delete', command=del_entry).grid(row=2, column=1, sticky='we')
tk.Button(win, text='submit', command=submit).grid(row=3, column=1, sticky='we')
tk.Button(win, text='insert', command=lambda: name.insert(0, 'hello'))\
    .grid(row=2, column=2, sticky='we')
tk.Button(win,)

win.grid_columnconfigure(0, minsize=100)
win.grid_columnconfigure(1, minsize=100)

win.mainloop()
