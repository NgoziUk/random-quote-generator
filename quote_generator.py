import random
from tkinter import *

quotes = ["Stay positive", "Keep going", "You got this"]

def get_quote():
    return random.choice(quotes)

def show_quote():
    label.config(text=get_quote())

window = Tk()
window.title("Quote Generator")

button = Button(window, text="Generate Quote", command=show_quote)
button.pack()

label = Label(window, text="")
label.pack()

window.mainloop()
