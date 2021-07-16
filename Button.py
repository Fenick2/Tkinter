import tkinter as tk


def say_hello():
    print('Hello!')


def add_label():
    label = tk.Label(win, text='new label')
    label.pack()


def counter():
    global count
    count += 1
    btn4['text'] = f'Нажато {count} раз'


count = 0

win = tk.Tk()
win.geometry(f'400x600+200+100')
win.title('My first app')
win['bg'] = 'grey'

btn1 = tk.Button(win, text='Say!', command=say_hello)

btn2 = tk.Button(win, text='Add new lbl', command=add_label)

btn3 = tk.Button(win, text='Add new lbl Lambda',
                 command=lambda: tk.Label(win, text='lambda lbl').pack())

btn4 = tk.Button(win, text=f'Счетчик нажатий',
                 command=counter, bg='yellow',
                 activebackground='blue',
                 activeforeground='yellow')

btn1.pack()
btn2.pack()
btn3.pack()
btn4.pack()

win.mainloop()
