import tkinter as tk
from tkinter import ttk, messagebox


class Calculator:
    def __init__(self):
        self.history = []

    def add(self, num1, num2):
        result = num1 + num2
        self.history.append(f"{num1} + {num2} = {result}")
        return result

    def subtract(self, num1, num2):
        result = num1 - num2
        self.history.append(f"{num1} - {num2} = {result}")
        return result

    def multiply(self, num1, num2):
        result = num1 * num2
        self.history.append(f"{num1} * {num2} = {result}")
        return result

    def divide(self, num1, num2):
        if num2 == 0:
            raise ZeroDivisionError("Деление на ноль!")
        result = num1 / num2
        self.history.append(f"{num1} / {num2} = {result}")
        return result

    def power(self, num1, num2):
        result = num1 ** num2
        self.history.append(f"{num1} ** {num2} = {result}")
        return result

    def get_history(self):
        return self.history


class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Калькулятор")
        self.root.geometry("400x500")
        self.calculator = Calculator()

        self.create_widgets()

    def create_widgets(self):
        self.entry = ttk.Entry(self.root, font=('Arial', 14), justify='right')
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='ew')

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 5, 0), ('**', 5, 1), ('H', 5, 2)
        ]

        for (text, row, col) in buttons:
            btn = ttk.Button(
                self.root,
                text=text,
                command=lambda t=text: self.on_button_click(t)
            )
            btn.grid(row=row, column=col, padx=5, pady=5, sticky='nsew')

        self.history_label = ttk.Label(self.root, text="История:")
        self.history_label.grid(row=6, column=0, columnspan=4, sticky='w', padx=10)
        self.history_text = tk.Text(self.root, height=5, state='disabled')
        self.history_text.grid(row=7, column=0, columnspan=4, padx=10, pady=5, sticky='nsew')

    def on_button_click(self, char):
        if char == '=':
            self.calculate()
        elif char == 'C':
            self.entry.delete(0, tk.END)
        elif char == 'H':
            self.show_history()
        else:
            self.entry.insert(tk.END, char)

    def calculate(self):
        try:
            expression = self.entry.get()
            if '**' in expression:
                num1, num2 = map(float, expression.split('**'))
                result = self.calculator.power(num1, num2)
            elif '+' in expression:
                num1, num2 = map(float, expression.split('+'))
                result = self.calculator.add(num1, num2)
            elif '-' in expression:
                num1, num2 = map(float, expression.split('-'))
                result = self.calculator.subtract(num1, num2)
            elif '*' in expression:
                num1, num2 = map(float, expression.split('*'))
                result = self.calculator.multiply(num1, num2)
            elif '/' in expression:
                num1, num2 = map(float, expression.split('/'))
                result = self.calculator.divide(num1, num2)
            else:
                raise ValueError("Неверная операция!")

            self.entry.delete(0, tk.END)
            self.entry.insert(0, str(result))

        except ZeroDivisionError:
            messagebox.showerror("Ошибка", "Деление на ноль!")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Некорректный ввод: {e}")

    def show_history(self):
        history = self.calculator.get_history()
        self.history_text.config(state='normal')
        self.history_text.delete(1.0, tk.END)
        self.history_text.insert(tk.END, "\n".join(history))
        self.history_text.config(state='disabled')


if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()