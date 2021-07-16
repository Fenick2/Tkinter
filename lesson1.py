import tkinter as tk

window = tk.Tk()
photo = tk.PhotoImage(file='Baby-Tux-icon.png')
window.iconphoto(False, photo)
window['bg'] = 'white'
window.title('My first window')
window.geometry('400x600+100+100')
window.resizable(True, True)
window.minsize(200, 300)
window.maxsize(600, 900)

window.mainloop()
