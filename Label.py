import tkinter as tk

win = tk.Tk()
win.geometry(f'300x400-100-200')
win.title('My 1 app')

label_1 = tk.Label(win, text='Hello!',
                   bg='blue',
                   fg='yellow',
                   font=('Arial', 16, 'bold', 'italic'),
                   padx=15,
                   pady=40,
                   width=15,
                   height=8,
                   anchor='s',  # n,s,e,w
                   relief=tk.RAISED,
                   bd=4,
                   justify=tk.CENTER
                   )

label_1.pack()
win.mainloop()
