import tkinter as tk

class About(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.label = tk.Label(self, text=f"Версия: {parent.version()}")
        self.button = tk.Button(self, text="Ok", command=self.destroy)

        self.label.pack(padx=20, pady = 20)
        self.button.pack(pady=5, ipadx=2, ipady=2)