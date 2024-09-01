import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        # Create main frame
        self.main_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.main_frame.pack(pady=20, padx=20)

        # Create title label
        self.title_label = tk.Label(self.main_frame, text="Password Generator", font=("Arial", 24), bg="#f0f0f0")
        self.title_label.pack(pady=10)

        # Create length label and entry
        self.length_frame = tk.Frame(self.main_frame, bg="#f0f0f0")
        self.length_frame.pack(pady=10)
        self.length_label = tk.Label(self.length_frame, text="Enter the desired length of the password:", bg="#f0f0f0")
        self.length_label.pack(side=tk.LEFT, padx=5)
        self.length_entry = tk.Entry(self.length_frame, width=10)
        self.length_entry.pack(side=tk.LEFT, padx=5)

        # Create options frame
        self.options_frame = tk.Frame(self.main_frame, bg="#f0f0f0")
        self.options_frame.pack(pady=10)
        self.uppercase_var = tk.BooleanVar()
        self.uppercase_checkbox = tk.Checkbutton(self.options_frame, text="Include uppercase letters", variable=self.uppercase_var, bg="#f0f0f0")
        self.uppercase_checkbox.pack(side=tk.LEFT, padx=5)
        self.numbers_var = tk.BooleanVar()
        self.numbers_checkbox = tk.Checkbutton(self.options_frame, text="Include numbers", variable=self.numbers_var, bg="#f0f0f0")
        self.numbers_checkbox.pack(side=tk.LEFT, padx=5)
        self.special_chars_var = tk.BooleanVar()
        self.special_chars_checkbox = tk.Checkbutton(self.options_frame, text="Include special characters", variable=self.special_chars_var, bg="#f0f0f0")
        self.special_chars_checkbox.pack(side=tk.LEFT, padx=5)

        # Create generate button
        self.generate_button = tk.Button(self.main_frame, text="Generate Password", command=self.generate_password)
        self.generate_button.pack(pady=10)

        # Create result label
        self.result_label = tk.Label(self.main_frame, text="Generated Password will appear here", bg="#f0f0f0")
        self.result_label.pack(pady=10)

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length < 1:
                self.result_label.config(text="Password length must be at least 1 character.")
                return

            # Define the character set for the password
            characters = string.ascii_lowercase
            if self.uppercase_var.get():
                characters += string.ascii_uppercase
            if self.numbers_var.get():
                characters += string.digits
            if self.special_chars_var.get():
                characters += string.punctuation

            # Generate a random password
            password = ''.join(random.choice(characters) for _ in range(length))
            self.result_label.config(text=f"Generated Password: {password}")
        except ValueError:
            self.result_label.config(text="Invalid input. Please enter a numeric value.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()