import tkinter as tk
from functools import partial

class Dialog(tk.Toplevel):
    def __init__(self, parent, buttons, text, notification = None):
        super().__init__(parent)
        self.parent = parent
        self._notification = notification
        self.resizable(False, False)
        self.transient(parent)

        self.label = tk.Label(self, text=text)
        self.label.pack(padx=20, pady=10)

        button_frame = tk.Frame(self)
        for caption, value in buttons.items():
            new_button = tk.Button(button_frame, width=10, text=caption, command=partial(self._click, value))
            new_button.pack(side=tk.LEFT, padx=5, pady=5, ipadx=5, ipady=5)
        button_frame.pack(fill=tk.BOTH, pady=10)

        self.protocol("WM_DELETE_WINDOW", partial(self._click, -1))
        self._center_over_parent()

    def _center_over_parent(self):
        self.update_idletasks()
        px, py = self.parent.winfo_rootx(), self.parent.winfo_rooty()
        sw, sh = self.parent.winfo_width(), self.parent.winfo_height()
        w, h = self.winfo_width(), self.winfo_height()
        self.geometry(f"{w}x{h}+{px + (sw - w) // 2}+{py + (sh - h) // 2}")

    def _click(self, value):
        self.destroy()
        if self._notification != None:
            self._notification(value)
