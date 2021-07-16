import tkinter as tk


levels = {1: 'Easy', 2: 'Middle', 3: 'Hard'}
nations = {1: "Elve's", 2: "Humans", 3: "Orc's"}


def sel_lev():
    level = level_var.get()
    level_text.set(f'You are selected level {level}')
    print(levels[level])


def sel_nat():
    nation = nation_var.get()
    nation_text.set(f'You are selected nation {nation}')
    print(nations[nation])


win = tk.Tk()
win.geometry(f'300x400+100+200')
win.title('My first app')

level_var = tk.IntVar()
nation_var = tk.IntVar()
level_text = tk.StringVar()
nation_text = tk.StringVar()

tk.Label(win, text='Set difficulty level').pack()
for level in sorted(levels):
    tk.Radiobutton(win, text=levels[level], variable=level_var, value=level, command=sel_lev).pack()
tk.Label(win, textvariable=level_text).pack()

tk.Label(win, text='Set race').pack()
for race in sorted(nations):
    tk.Radiobutton(win, text=nations[race], variable=nation_var, value=race, command=sel_nat).pack()
tk.Label(win, textvariable=nation_text).pack()

win.mainloop()
