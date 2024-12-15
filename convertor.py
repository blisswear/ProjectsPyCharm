import tkinter as tk
from tkinter import ttk
import requests


class CurrencyConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Currency Converter")

        self.amount_label = tk.Label(root, text="Amount:")
        self.amount_label.grid(row=0, column=0, padx=10, pady=10)

        self.amount_entry = tk.Entry(root)
        self.amount_entry.grid(row=0, column=1, padx=10, pady=10)

        self.from_currency_label = tk.Label(root, text="From Currency:")
        self.from_currency_label.grid(row=1, column=0, padx=10, pady=10)

        self.from_currency_combo = ttk.Combobox(root, values=self.get_currency_list())
        self.from_currency_combo.grid(row=1, column=1, padx=10, pady=10)

        self.to_currency_label = tk.Label(root, text="To Currency:")
        self.to_currency_label.grid(row=2, column=0, padx=10, pady=10)

        self.to_currency_combo = ttk.Combobox(root, values=self.get_currency_list())
        self.to_currency_combo.grid(row=2, column=1, padx=10, pady=10)

        self.convert_button = tk.Button(root, text="Convert", command=self.convert_currency)
        self.convert_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.result_label = tk.Label(root, text="")
        self.result_label.grid(row=4, column=0, columnspan=2, pady=10)

    def get_currency_list(self):
        response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
        data = response.json()
        return list(data['rates'].keys())

    def convert_currency(self):
        amount = float(self.amount_entry.get())
        from_currency = self.from_currency_combo.get()
        to_currency = self.to_currency_combo.get()

        response = requests.get(f"https://api.exchangerate-api.com/v4/latest/{from_currency}")
        data = response.json()

        rate = data['rates'][to_currency]
        converted_amount = amount * rate

        self.result_label.config(text=f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")


if __name__ == "__main__":
    root = tk.Tk()
    app = CurrencyConverter(root)
    root.mainloop()