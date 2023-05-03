# import Tkinter library
import tkinter as tk

# themed widgets
from tkinter import ttk

#messagebox module
import tkinter.messagebox as mb

# import my module
from packaging_tutorial.example import find_answer
# create a window
window = tk.Tk()
window.title("(a+b)^2 Kalkulaator")


# create a style object to customize the widgets
style = ttk.Style()
style.configure("TLabel", font=("Arial", 12), foreground="yellow")
style.configure("TButton", font=("Arial", 12), foreground="yellow")


label_a = ttk.Label(window, text="Sisesta a:")
label_a.grid(row=0, column=0, padx=10, pady=10, sticky="w")


entry_a = ttk.Entry(window)
entry_a.grid(row=0, column=1, padx=10, pady=10)


label_b = ttk.Label(window, text="Sisesta b:")
label_b.grid(row=1, column=0, padx=10, pady=10, sticky="w")


entry_b = ttk.Entry(window)
entry_b.grid(row=1, column=1, padx=10, pady=10)

button = ttk.Button(window, text="Arvuta")


def calculate():
    try:
        a = int(entry_a.get())
        b = int(entry_b.get())
    except ValueError:
        mb.showerror("Error", "Kirjuta numbrid!")
        return  # exit the function

    answer = find_answer(a, b)

    label_answer.config(text=f"Vastus: {answer}")


button.config(command=calculate)
button.grid(row=2, column=0, columnspan=2)

label_answer = ttk.Label(window)
label_answer.grid(row=3, column=0, columnspan=2)

window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(1, weight=1)
window.grid_rowconfigure(2, weight=1)
window.grid_rowconfigure(3, weight=1)
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)

window.mainloop()
