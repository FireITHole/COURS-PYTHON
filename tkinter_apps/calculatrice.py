import tkinter as tk
from tkinter import ttk


class Calculatrice:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.geometry("300x400")
        self.root.title("Calculatrice Simple")

        s = ttk.Style()
        s.configure("TButton", font="Arial 14")

        self.entry_var = tk.StringVar()
        self.entry = ttk.Entry(self.root, font=("Arial", 14),
                               textvariable=self.entry_var, takefocus=0, state="readonly")
        self.entry.pack(fill="x", ipady=10)

        self.buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]

        self.row_val = 0
        self.col_val = 0

        self.button_frame = tk.Frame(self.root)

        for button in self.buttons:
            b = ttk.Button(self.button_frame, text=button,
                           style="TButton", command=lambda x=button: self.on_click(x))
            b.grid(row=self.row_val, column=self.col_val, sticky="nsew")
            self.col_val += 1
            if self.col_val > 3:
                self.col_val = 0
                self.row_val += 1

        for i in range(4):
            self.button_frame.rowconfigure(i, weight=1)
            self.button_frame.columnconfigure(i, weight=1)

        self.button_frame.pack(expand=True, fill="both")

        self.root.bind("<KeyPress>", lambda k: self.on_click(k.char)
                       if k.char in "0123456789+-*/=C" else None)
        self.root.bind("<Return>", lambda _: self.on_click("="))

        self.root.mainloop()

    def on_click(self, text: str) -> None:
        if text == "=":
            try:
                result = eval(self.entry_var.get())
                self.entry_var.set(result)
            except Exception:
                self.entry_var.set("Erreur")
        elif text == "C":
            self.entry_var.set("")
        else:
            if self.entry.get() == "Erreur":
                self.entry_var.set("")

            self.entry_var.set(self.entry_var.get() + text)


if __name__ == "__main__":
    Calculatrice()
