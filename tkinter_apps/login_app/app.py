import tkinter as tk
from tkinter import ttk
import sqlite3
import os


class LoginPage:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title("Login Page")
        self.root.geometry("300x350")
        self.root.resizable(False, False)

        self.frame = ttk.Frame(
            self.root, padding="10 10 10 10", relief=tk.RAISED)
        self.frame.pack(expand=True, anchor="center")

        ttk.Label(self.frame, text="Connexion", font=(
            "Arial", 14), padding="10 10 10 10").pack()

        self.username_var = tk.StringVar(value="Username")
        self.username_entry = ttk.Entry(
            self.frame, width=30, textvariable=self.username_var)
        self.username_entry.pack(pady=10)

        self.username_entry.bind("<FocusIn>", lambda _: self.username_var.set(
            "") if self.username_var.get() == "Username" else None)

        self.password_var = tk.StringVar(value="Password")
        self.password_entry = ttk.Entry(
            self.frame, width=30, textvariable=self.password_var, show="*")
        self.password_entry.pack(pady=10)

        self.password_entry.bind("<FocusIn>", lambda _: self.password_var.set(
            "") if self.password_var.get() == "Password" else None)

        self.message_label = ttk.Label(self.frame, text="", foreground="red")
        self.message_label.pack(pady=10)

        self.login_button = ttk.Button(
            self.frame, text="Login", command=self.login)
        self.login_button.pack()

        self.root.bind("<Return>", lambda _: self.login())

        self.root.mainloop()

    def login(self):
        username = self.username_var.get()
        password = self.password_var.get()

        con = sqlite3.connect("app.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM users WHERE username = ? AND password = ?",
                    (username, password))
        user = cur.fetchone()
        con.close()

        if user:
            self.root.destroy()
            App()
        else:
            self.message_label["padding"] = "10 10 10 10"
            self.message_label["text"] = "Username or password is incorrect"


class App:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title("App")
        self.root.geometry("400x500")

        ttk.Label(self.root, text="Welcome", font=(
            "Arial", 14), padding="10 10 10 10").pack()

        self.root.mainloop()


if __name__ == "__main__":
    if not os.path.exists("app.db"):
        con = sqlite3.connect("app.db")
        cur = con.cursor()
        cur.execute(
            "CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)")
        con.commit()
        con.execute("INSERT INTO users VALUES ('admin', 'admin')")
        con.commit()
        con.close()

    LoginPage()
