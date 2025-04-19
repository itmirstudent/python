import tkinter as tk
from tkinter import scrolledtext, filedialog
from AboutWindow import About

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self._modified = False
        self._filepath = ""
        self._version = "1.0"
        self._set_title()
        self.geometry("800x600")
        self.iconbitmap("title.ico")
        self.edit_text = scrolledtext.ScrolledText(width=96, height=37)
        self.edit_text.pack(fill=tk.BOTH, expand=1)
        self.edit_text.bind("<Key>", lambda key: self._set_modify(True))
        self._create_menu()

    def _create_menu(self):
        self._menu = tk.Menu(self, tearoff=0)

        # Файл
        file_menu = tk.Menu(self, tearoff=0)
        file_menu.add_command(label="Открыть файл", command=self._open_file)
        file_menu.add_command(label="Сохранить файл как", command=self._save_file_as)
        file_menu.add_command(label="Сохранить файл", command=self._save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Выход", command=self._exit)
        self._menu.add_cascade(label="Файл", menu=file_menu)

        # Справка
        help_menu = tk.Menu(self, tearoff=0)
        help_menu.add_command(label="О программе", command=self._open_about)
        self._menu.add_cascade(label="Справка", menu=help_menu)

        self.config(menu=self._menu)

    def _save_file(self):
        if self._filepath != "":
            with open(self._filepath, "w") as fl:
                text = self.edit_text.get("1.0", tk.END)
                fl.write(text[:-1])
            self._set_modify(False)
        else:
            self._save_file_as()

    def _save_file_as(self):
        self._filepath = filedialog.asksaveasfilename()
        if self._filepath != "":
            self._save_file()
            self._set_title()

    def _open_file(self):
        self._filepath = filedialog.askopenfilename()
        if self._filepath != "":
            with open(self._filepath, "r") as fl:
                text = fl.read()
                self.edit_text.delete("1.0", tk.END)
                self.edit_text.insert("1.0", text)
                self._set_title()

    def _exit(self):
        self.destroy()

    def _open_about(self):
        about = About(self)
        about.grab_set()

    def version(self):
        return self._version

    def _set_title(self):
        self.title(("*" if self._modified else "") + f"{"Безымянный" if self._filepath == "" else self._filepath} - Блокнот")

    def _set_modify(self, val = False):
        self._modified = val
        self._set_title()