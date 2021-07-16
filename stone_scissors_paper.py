from tkinter import *
import random as rdm


root = Tk()
root.geometry(f'430x350+200+200')
root.title('Камень, ножницы, бумага')
root.resizable(False, False)
root['bg'] = 'grey'


class Main(Frame):
    def __init__(self, root):
        super(Main, self).__init__(root)
        self.startUI()

    def startUI(self):
        btn = Button(root, bg='coral', text="Камень", font=('bold', 14), relief=RAISED, bd=4, command=lambda x=1: self.btn_click(x))
        btn2 = Button(root, bg='green', text="Ножницы", font=('bold', 14), relief=RAISED, bd=4, command=lambda x=2: self.btn_click(x))
        btn3 = Button(root, text="Бумага", font=('bold', 14), relief=RAISED, bd=4, command=lambda x=3: self.btn_click(x))

        btn.place(x=10, y=100, width=120, height=50)
        btn2.place(x=155, y=100, width=120, height=50)
        btn3.place(x=300, y=100, width=120, height=50)

        self.win = self.drow = self.lose = 0

        self.lbl = Label(root, justify=CENTER, width=13, text='Начало игры', bg='yellow', fg='blue', font=('Times New Roman', 24, 'bold'))
        self.lbl.place(x=100, y=25)

        self.lbl3 = Label(root, justify=CENTER, width=13, text='Ход компьютера', bg='blue', fg='yellow', font=('Times New Roman', 24, 'bold'))
        self.lbl3.place(x=100, y=200)

        self.lbl2 = Label(
            root,
            justify=CENTER,
            font=('Times New Roman', 13),
            text=f"Побед: {self.win}  Поражений: {self.lose}  Ничьих: {self.drow}",
            bg='black',
            fg='white',
            width=30
        )
        self.lbl2.place(x=90, y=290)

    def btn_click(self, choise):
        comp_choise = rdm.randint(1, 3)
        if comp_choise == 1:
            self.lbl3.configure(text='Камень')
        elif comp_choise == 2:
            self.lbl3.configure(text='Ножницы')
        else:
            self.lbl3.configure(text='Бумага')

        if choise == comp_choise:
            self.drow += 1
            self.lbl.configure(text="Ничья", fg='blue')
        elif choise == 1 and comp_choise == 2 \
                or choise == 2 and comp_choise == 3 \
                or choise == 3 and comp_choise == 1:
            self.win += 1
            self.lbl.configure(text="Победа!", fg='red')
        else:
            self.lose += 1
            self.lbl.configure(text="Поражение", fg='black')

        self.lbl2.configure(text=f"Побед: {self.win}  Поражений:"
                                 f" {self.lose}  Ничьих: {self.drow}")

        del comp_choise


app = Main(root)
app.pack()


if __name__ == '__main__':
    root.mainloop()
