from tkinter import *

root = Tk()
root.geometry('300x300+500+200')
val = StringVar()
val.set("blue")

colors = ["blue", "yellow", "green", "red"]

def color(*args):
    label1.config(bg=val.get())

val.trace("w", color)

i = 0
for color_name in colors:
    rb = Radiobutton(root, text=color_name.capitalize(), variable=val, value=color_name)
    rb.place(x=50, y=50 + i * 30)
    i += 1

label1 = Label(root, text="Моя мітка", width=20)
label1.place(x=120, y=180)

root.mainloop()