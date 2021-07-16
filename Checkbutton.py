import tkinter as tk


def select_all():
    for check in [over_18, commerc, follow]:
        check.select()


def deselect_all():
    for check in [over_18, commerc, follow]:
        check.deselect()


def switch_all():
    for check in [over_18, commerc, follow]:
        check.toggle()


def show():
    print('Flag_18', over_18_value.get())
    print('Flag_comm', commerc_value.get())


win = tk.Tk()

over_18_value = tk.StringVar()
over_18_value.set('No')
commerc_value = tk.IntVar()
commerc_value.set(1)
win.geometry(f"300x400+100+200")
win.title('My first app')

over_18 = tk.Checkbutton(win, text='Вам есть 18 лет?',
                         variable=over_18_value,
                         offvalue='No',
                         onvalue='Yes')
commerc = tk.Checkbutton(win, text='Хотите получать рекламу?',
                         variable=commerc_value,
                         offvalue=0,
                         onvalue=1)
follow = tk.Checkbutton(win, text='Хотите подписаться на канал?', indicatoron=0)
over_18.pack()
commerc.pack()
follow.pack()
tk.Button(win, text='select all', command=select_all).pack()
tk.Button(win, text='deselect all', command=deselect_all).pack()
tk.Button(win, text='switch all', command=switch_all).pack()
tk.Button(win, text='Show', command=show).pack()


win.mainloop()