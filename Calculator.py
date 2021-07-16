import tkinter as tk
from tkinter import messagebox


def add_digit(digit):
    val = calc.get()
    if val == '0' and len(val) == 1:
        val = val[1:]
    calc['state'] = tk.NORMAL
    calc.delete(0, tk.END)
    calc.insert(0, val + digit)
    calc['state'] = tk.DISABLED


def add_operation(operation):
    value = calc.get()
    if value[-1] in '+-*/':
        value = value[:-1]
    elif '+' in value or '-' in value or '*' in value or '/' in value:
        calculate()
        value = calc.get()
    calc['state'] = tk.NORMAL
    calc.delete(0, tk.END)
    calc.insert(0, value + operation)
    calc['state'] = tk.DISABLED


def add_clear():
    calc['state'] = tk.NORMAL
    calc.delete(0, tk.END)
    calc.insert(0, '0')
    calc['state'] = tk.DISABLED


def calculate():
    value = calc.get()
    if value[-1] in '+-*/':
        value = value + value[:-1]
    calc['state'] = tk.NORMAL
    calc.delete(0, tk.END)
    try:
        calc.insert(0, eval(value))
    except (NameError, SyntaxError):
        messagebox.showinfo('Ошибка!', 'Вводите только цифры!')
        calc.insert(0, 0)
    except ZeroDivisionError:
        messagebox.showinfo('Ошибка!', 'На ноль делить нельзя!')
        calc.insert(0, 0)
    calc['state'] = tk.DISABLED


def make_digit_button(digit):
    return tk.Button(text=digit, bd=3, font=('Arial', 12), command=lambda: add_digit(digit))


def make_oper_button(oper):
    return tk.Button(text=oper, bd=3, font=('Arial', 12), bg='lightblue', command=lambda: add_operation(oper))


def make_clear_button(cl):
    return tk.Button(text=cl, bd=3, font=('Arial', 14), bg='lightblue', fg='red', command=lambda: add_clear())


def make_calc_button(calc):
    return tk.Button(text=calc, bd=3, font=('Arial', 12), bg='salmon', command=lambda: calculate())


def press_key(event):
    if event.char.isdigit():
        add_digit(event.char)
    elif event.char in '+-*/':
        add_operation(event.char)
    elif event.char == '\r':
        calculate()


win = tk.Tk()
win.geometry(f'305x275+100+200')
win['bg'] = 'cornflowerblue'  # 6495ED
win.title('Калькулятор')
win.resizable(False, True)
win.minsize(0, 275)
win.maxsize(640, 560)

win.bind('<Key>', press_key)

tk.Label(win, text='CASIO', font=('Arial', 11, 'bold'),
         bg='yellow').grid(row=0, column=0, sticky='w')

calc = tk.Entry(win, justify=tk.RIGHT, font=('Arial', 16), width=15)
calc.insert(0, '0')
calc['state'] = tk.DISABLED
calc.grid(row=0, column=1, columnspan=4, sticky='we', padx=3)

make_digit_button('1').grid(row=1, column=0, sticky='wens', padx=3, pady=3)
make_digit_button('2').grid(row=1, column=1, sticky='wens', padx=3, pady=3)
make_digit_button('3').grid(row=1, column=2, sticky='wens', padx=3, pady=3)
make_digit_button('4').grid(row=2, column=0, sticky='wens', padx=3, pady=3)
make_digit_button('5').grid(row=2, column=1, sticky='wens', padx=3, pady=3)
make_digit_button('6').grid(row=2, column=2, sticky='wens', padx=3, pady=3)
make_digit_button('7').grid(row=3, column=0, sticky='wens', padx=3, pady=3)
make_digit_button('8').grid(row=3, column=1, sticky='wens', padx=3, pady=3)
make_digit_button('9').grid(row=3, column=2, sticky='wens', padx=3, pady=3)
make_digit_button('0').grid(row=4, column=0, columnspan=3, sticky='wens', padx=3, pady=3)

make_oper_button('+').grid(row=3, column=3, rowspan=2, sticky='wens', padx=3, pady=3)
make_oper_button('-').grid(row=1, column=4, sticky='wens', padx=3, pady=3)
make_oper_button('*').grid(row=2, column=3, sticky='wens', padx=3, pady=3)
make_oper_button('/').grid(row=2, column=4, sticky='wens', padx=3, pady=3)

make_clear_button('C').grid(row=1, column=3, sticky='wens', padx=3, pady=3)

make_calc_button('=').grid(row=3, column=4, rowspan=2, sticky='wens', padx=3, pady=3)

win.grid_columnconfigure(0, minsize=60)
win.grid_columnconfigure(1, minsize=60)
win.grid_columnconfigure(2, minsize=60)
win.grid_columnconfigure(3, minsize=60)
win.grid_columnconfigure(4, minsize=60)

win.grid_rowconfigure(1, minsize=60)
win.grid_rowconfigure(2, minsize=60)
win.grid_rowconfigure(3, minsize=60)
win.grid_rowconfigure(4, minsize=60)

win.mainloop()
