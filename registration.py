import tkinter as tk
from tkinter import messagebox
import sqlite3


# Создание базы данных SQLite
def create_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    )
    ''')
    conn.commit()
    conn.close()


# Регистрация пользователя
def register_user(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    try:
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
        conn.commit()
        messagebox.showinfo("Registration", "User registered successfully!")
    except sqlite3.IntegrityError:
        messagebox.showerror("Registration", "Username already exists.")
    conn.close()


# Авторизация пользователя
def authenticate_user(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
    user = cursor.fetchone()
    conn.close()
    return user is not None


# Окно регистрации
def open_registration_window():
    registration_window = tk.Toplevel(root)
    registration_window.title("Registration")

    tk.Label(registration_window, text="Username:").grid(row=0, column=0, padx=10, pady=10)
    username_entry = tk.Entry(registration_window)
    username_entry.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(registration_window, text="Password:").grid(row=1, column=0, padx=10, pady=10)
    password_entry = tk.Entry(registration_window, show='*')
    password_entry.grid(row=1, column=1, padx=10, pady=10)

    register_button = tk.Button(registration_window, text="Register",
                                command=lambda: register_user(username_entry.get(), password_entry.get()))
    register_button.grid(row=2, columnspan=2, pady=10)


# Основное окно авторизации
def open_auth_window():
    global root
    root = tk.Tk()
    root.title("Login")

    tk.Label(root, text="Username:").grid(row=0, column=0, padx=10, pady=10)
    username_entry = tk.Entry(root)
    username_entry.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(root, text="Password:").grid(row=1, column=0, padx=10, pady=10)
    password_entry = tk.Entry(root, show='*')
    password_entry.grid(row=1, column=1, padx=10, pady=10)

    login_button = tk.Button(root, text="Login", command=lambda: login(username_entry.get(), password_entry.get()))
    login_button.grid(row=2, columnspan=2, pady=10)

    register_button = tk.Button(root, text="Register", command=open_registration_window)
    register_button.grid(row=3, columnspan=2, pady=10)


def login(username, password):
    if authenticate_user(username, password):
        messagebox.showinfo("Login", "Login successful!")
    else:
        messagebox.showerror("Login", "Invalid username or password.")


if __name__ == "__main__":
    create_db()
    open_auth_window()
    root.mainloop()