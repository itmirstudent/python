import tkinter as tk
from tkinter import scrolledtext, filedialog
from AboutWindow import About
from DialogWindow import Dialog
from functools import partial

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self._modified = False
        self._filepath = ""
        self._version = "1.0"
        self._encoding_list = ("UTF-8", "UTF-16", "UTF-32", "ANSI", "CP866", "CP1251", "KOI8_R")
        self._encoding = self._encoding_list[0]
        self._set_title()
        self.geometry("800x600")
        self.iconbitmap("title.ico")

        self.edit_text = scrolledtext.ScrolledText(width=96)
        self.edit_text.pack(fill=tk.BOTH, expand=1)
        self.edit_text.bind("<Key>", lambda key: self._set_modify(True))

        frame = tk.Frame(height=5, borderwidth=1)
        self.encoding_text = tk.Label(frame, text=self._encoding)
        self.encoding_text.pack(anchor=tk.E)
        frame.pack(fill=tk.X, expand=0)

        self.geometry("800x600")

        self.protocol("WM_DELETE_WINDOW", self._exit)
        self._create_menu()

    def _create_menu(self):
        self._menu = tk.Menu(self, tearoff=0)

        # Файл
        file_menu = tk.Menu(self, tearoff=0)
        file_menu.add_command(label="Открыть файл", command=self._open_file)
        file_menu.add_command(label="Сохранить файл как", command=self._save_file_as)
        file_menu.add_command(label="Сохранить файл", command=self._save_file)

        # encoding menu
        encoding_menu = tk.Menu(self, tearoff=0)
        for encoding_value in self._encoding_list:
            encoding_menu.add_command(label=encoding_value, command=partial(self._change_encoding, encoding_value))
        file_menu.add_separator()
        file_menu.add_cascade(label="Кодировка", menu=encoding_menu)

        file_menu.add_separator()
        file_menu.add_command(label="Выход", command=self._exit)
        self._menu.add_cascade(label="Файл", menu=file_menu)

        # Справка
        help_menu = tk.Menu(self, tearoff=0)
        help_menu.add_command(label="О программе", command=self._open_about)
        self._menu.add_cascade(label="Справка", menu=help_menu)

        self.config(menu=self._menu)

    def _change_encoding(self, encoding):
        self._encoding = encoding
        self.encoding_text.configure(text=self._encoding)

    def _save_file(self):
        if self._filepath != "":
            with open(self._filepath, "w", encoding=self._encoding) as fl:
                text = self.edit_text.get("1.0", tk.END)
                fl.write(text[:-1])
            self._set_modify(False)
        else:
            self._save_file_as()

    def _save_file_as(self):
        self._filepath = filedialog.asksaveasfilename(title="Сохранить файл", defaultextension="txt", \
                                                      filetypes=(("Текстовые документы", "*.txt"), ("Все файлы", "*.*")))
        if self._filepath != "":
            self._save_file()
            self._set_title()

    def _open_file(self, value=None):
        if self._if_modified(self._open_file, value) == False:
            return
        self._filepath = filedialog.askopenfilename(title="Открыть файл", defaultextension="txt", \
                                                    filetypes=(("Текстовые документы", "*.txt"), ("Все файлы", "*.*")))
        if self._filepath != "":
            with open(self._filepath, "r", encoding=self._encoding) as fl:
                text = fl.read()
                self.edit_text.delete("1.0", tk.END)
                self.edit_text.insert("1.0", text)
                self._set_title()
                self._set_modify(False)

    def _exit(self, value=None):
        if self._if_modified(self._exit, value) == False:
            return
        self.destroy()

    def _if_modified(self, action, value=None):
        if self._modified and value == None:
            dialog = Dialog(self, {"Да": 1, "Нет": 2, "Отменить": 3}, "Сохранить файл?", action)
            dialog.grab_set()
            return False
        elif value == 1:
            self._save_file()
        elif value == 3:
            return False
        return True

    def _open_about(self):
        # about = About(self)
        about = Dialog(self, {"OK": 0}, f"Версия: {self.version()}")
        about.grab_set()

    def version(self):
        return self._version

    def _set_title(self):
        self.title(("*" if self._modified else "") + f"{"Безымянный" if self._filepath == "" else self._filepath} - Блокнот")

    def _set_modify(self, val = False):
        self._modified = val
        self._set_title()