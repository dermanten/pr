from tkinter import *

def Suma(event=None):
    try:
        s = int(edit1.get()) + int(edit2.get())
        res.set(s)
    except ValueError:
        res.set("Помилка!")

root = Tk()
root.title("Сума")
root.geometry('500x100')

res = StringVar()

Label(root, text="Введіть a:").grid(row=0, sticky=W)
Label(root, text="Введіть b:").grid(row=1, sticky=W)
Label(root, text="Сума:").grid(row=3, sticky=W)
Label(root, text="", textvariable=res).grid(row=3, column=1, sticky=W)

edit1 = Entry(root)
edit2 = Entry(root)

edit1.grid(row=0, column=1)
edit2.grid(row=1, column=1)

edit2.bind('<Return>', Suma)

button1 = Button(root, text="Обчислити")
button1.grid(row=0, column=2, columnspan=2, rowspan=2, sticky=W+E+N+S, padx=5, pady=5)

button1.bind('<Button-1>', Suma)

mainloop()