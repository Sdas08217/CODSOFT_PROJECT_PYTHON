import tkinter as tk
from tkinter import messagebox

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        
        self.create_widgets()

    def create_widgets(self):
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10)

        tk.Label(self.frame, text="Number 1:").grid(row=0, column=0, padx=5, pady=5)
        self.num1_entry = tk.Entry(self.frame, width=15)
        self.num1_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.frame, text="Number 2:").grid(row=1, column=0, padx=5, pady=5)
        self.num2_entry = tk.Entry(self.frame, width=15)
        self.num2_entry.grid(row=1, column=1, padx=5, pady=5)

        self.add_button = tk.Button(self.frame, text="+", command=lambda: self.calculate('add'))
        self.add_button.grid(row=2, column=0, padx=5, pady=5)

        self.subtract_button = tk.Button(self.frame, text="-", command=lambda: self.calculate('subtract'))
        self.subtract_button.grid(row=2, column=1, padx=5, pady=5)

        self.multiply_button = tk.Button(self.frame, text="×", command=lambda: self.calculate('multiply'))
        self.multiply_button.grid(row=2, column=2, padx=5, pady=5)

        self.divide_button = tk.Button(self.frame, text="÷", command=lambda: self.calculate('divide'))
        self.divide_button.grid(row=2, column=3, padx=5, pady=5)

        self.result_label = tk.Label(self.frame, text="Result: ")
        self.result_label.grid(row=3, columnspan=4, pady=5)

    def calculate(self, operation):
        try:
            num1 = float(self.num1_entry.get())
            num2 = float(self.num2_entry.get())
        except ValueError:
            messagebox.showwarning("Invalid Input", "Please enter numeric values.")
            return

        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            if num2 != 0:
                result = num1 / num2
            else:
                messagebox.showerror("Error", "Division by zero is not allowed.")
                return
        else:
            messagebox.showerror("Error", "Invalid operation.")
            return
        
        self.result_label.config(text=f"Result: {result}")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()