from tkinter import *
from tkinter import ttk

def Miss(event=None):
    n = combo.current()
    if n == 0:
        label2.config(text="Лондон")
    elif n == 1:
        label2.config(text="Київ")
    elif n == 2:
        label2.config(text="Париж")
    elif n == 3:
        label2.config(text="Прага")
    elif n == 4:
        label2.config(text="Варшава")

root = Tk()
root.title("Країни та столиці")
root.geometry("350x200")

countries = ["Велика Британія", "Україна", "Франція", "Чехія", "Польща"]

label1 = Label(root, text="Виберіть країну:")
label1.grid(column=0, row=0)

combo = ttk.Combobox(root, values=countries, width=30)
combo.grid(column=0, row=1)
combo.current(0)

btn = Button(root, text="Столиця")
btn.grid(column=0, row=2)

label2 = Label(root, text="")
label2.grid(column=0, row=3)

btn.bind("<Return>", Miss)
combo.bind("<Return>", Miss)
btn.focus_set()

root.mainloop()