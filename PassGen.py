from random import choice
import tkinter as tk
import pyperclip
from AlphaConfirm import AlphaConfirm as ac
def passwordgen(length):
    code = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "{", "}", '"', "'", "[", "]", ",", ".", "<", ">", "/", "?", "#", "~", "\\", "*", "-", "=", "+", "_", ")", "(", "&", "^", "%", "@", "!", "`", "¬", "¦"]
    password = ""
    try:
        length = int(length)
    except:
        raise ValueError
    for x in range(length):
        x = choice(["low", "upp"])
        add = choice(code)
        if x == "low":
            if not ac(add):
                password += add
            else:
                add = add.lower()
                password += add
        if x == "upp":
            if not ac(add):
                password += add
            else:
                add = add.upper()
                password += add
    return password
def copy():
    global enter
    length = enter.get()
    pyperclip.copy(passwordgen(length))
    return
root = tk.Tk()
text = tk.Label(root, text = "Input Password Length")
text.pack()
enter = tk.Entry(root)
enter.pack()
button = tk.Button(root, text = "Submit", command = copy)
button.pack()
root.mainloop()
