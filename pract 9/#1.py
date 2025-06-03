from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("300x100+600+400")

str_var = StringVar()

def button_click(event=None):
    messagebox.showinfo("Привітання", "Вітаю " + str_var.get())

Label(text="Введіть ім'я:").pack()

entry = Entry(root, textvariable=str_var)
entry.pack()

btn = Button(root, text="ОК")
btn.pack()

btn.bind("<Button-1>", button_click)

entry.bind("<Return>", button_click)

root.mainloop()