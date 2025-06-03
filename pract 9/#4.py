from tkinter import *

def kvadrat(event=None):
    try:
        a = int(edit1.get())
        edit2.delete(0, END)
        edit2.insert(0, str(a**2))
    except ValueError:
        edit2.delete(0, END)
        edit2.insert(0, "Помилка!")

def delete(event=None):
    edit1.delete(0, END)
    edit2.delete(0, END)

root = Tk()
root.geometry('300x200+600+200')

label1 = Label(text='a = ')
label1.grid(row=0, column=0, padx=20, pady=20)
edit1 = Entry(width=15)
edit1.grid(row=0, column=1, padx=10, pady=10)

label2 = Label(text='a**2 = ')
label2.grid(row=1, column=0, padx=10, pady=10)
edit2 = Entry(width=15)
edit2.grid(row=1, column=1, padx=10, pady=10)

button1 = Button(text='Обчислити', width=15)
button1.grid(row=2, column=1, pady=10)
button2 = Button(text='Очистити', width=15)
button2.grid(row=3, column=1, pady=10)


edit1.bind('<Return>', kvadrat)
button1.bind('<Button-1>', kvadrat)
button2.bind('<Button-1>', delete)
root.bind('<Escape>', delete)

root.mainloop()