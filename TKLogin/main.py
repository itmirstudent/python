import tkinter as tk
from config import *

def printMessage(text=""):
    window = tk.Tk()
    window.title("Сообщение")
    window.geometry("200x100")
    lb = tk.Label(window, text=text)
    lb.pack(anchor=tk.CENTER, expand=1)
    bt = tk.Button(window, text="Ок", command=lambda: window.destroy())
    bt.pack(fill=tk.BOTH, anchor=tk.CENTER, expand=1)

main_window = tk.Tk()
main_window.title(TITLE)
main_window.geometry(f"{WIDTH}x{HEIGHT}")
main_window.iconbitmap(ICON)

# Создание поля ввода
textBox = tk.Text(main_window, width=15, height=1)
textBox.pack(anchor=tk.CENTER, expand=1)

# Создание кнопки
button = tk.Button(main_window, text="Сказать привет", command=lambda: printMessage(textBox.get(1.0, tk.END)))
button.pack(anchor=tk.CENTER, expand=1)

main_window.mainloop()