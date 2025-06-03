from tkinter import *

def factorial(event=None):
    try:
        n = int(entry.get())
        f = 1
        for i in range(1, n + 1):
            f *= i
        label_result.config(text=f"Факторіал числа {n}! = {f}")
    except ValueError:
        label_result.config(text="Введіть ціле число!")

root = Tk()
root.title("Факторіал")
root.geometry("400x150")

label_prompt = Label(root, text="Введіть число N:")
label_prompt.place(x=30, y=20)

entry = Entry(root)
entry.place(x=200, y=20, width=150)

label_result = Label(root, text="")
label_result.place(x=30, y=60)

button = Button(root, text="Обчислити")
button.place(x=200, y=90, width=150)

entry.bind("<Return>", factorial)
button.bind("<Button-1>", factorial)

entry.focus_set()

root.mainloop()