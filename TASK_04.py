import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock, Paper, Scissors")
        self.root.configure(bg="#f0f0f0")
        
        self.user_score = 0
        self.computer_score = 0

        self.create_widgets()

    def create_widgets(self):
        self.frame = tk.Frame(self.root, bg="#f0f0f0")
        self.frame.pack(pady=10)
        
        self.instruction_label = tk.Label(self.frame, text="Choose Rock, Paper, or Scissors:", font=("Arial", 14), bg="#f0f0f0", fg="#007bff")
        self.instruction_label.pack(pady=5)
        
        self.button_frame = tk.Frame(self.frame, bg="#f0f0f0")
        self.button_frame.pack()
        
        self.rock_button = tk.Button(self.button_frame, text="Rock", command=lambda: self.play('rock'), width=10, height=2, font=("Arial", 12), bg="#4CAF50", fg="#ffffff")
        self.rock_button.pack(side=tk.LEFT, padx=5, pady=5)
        
        self.paper_button = tk.Button(self.button_frame, text="Paper", command=lambda: self.play('paper'), width=10, height=2, font=("Arial", 12), bg="#4CAF50", fg="#ffffff")
        self.paper_button.pack(side=tk.LEFT, padx=5, pady=5)
        
        self.scissors_button = tk.Button(self.button_frame, text="Scissors", command=lambda: self.play('scissors'), width=10, height=2, font=("Arial", 12), bg="#4CAF50", fg="#ffffff")
        self.scissors_button.pack(side=tk.LEFT, padx=5, pady=5)
        
        self.result_label = tk.Label(self.frame, text="", font=("Arial", 12), bg="#f0f0f0", fg="#000000")
        self.result_label.pack(pady=5)
        
        self.score_label = tk.Label(self.frame, text=f"Score: You {self.user_score} - Computer {self.computer_score}", font=("Arial", 12), bg="#f0f0f0", fg="#000000")
        self.score_label.pack(pady=5)

    def get_computer_choice(self):
        return random.choice(['rock', 'paper', 'scissors'])

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return 'tie'
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'scissors' and computer_choice == 'paper') or \
             (user_choice == 'paper' and computer_choice == 'rock'):
            return 'win'
        else:
            return 'lose'

    def play(self, user_choice):
        computer_choice = self.get_computer_choice()
        result = self.determine_winner(user_choice, computer_choice)
        
        result_text = f"Computer chose: {computer_choice}\n"
        
        if result == 'win':
            result_text += "You win!"
            self.user_score += 1
            self.result_label.config(text=result_text, fg="#008000")
        elif result == 'lose':
            result_text += "You lose!"
            self.computer_score += 1
            self.result_label.config(text=result_text, fg="#ff0000")
        else:
            result_text += "It's a tie!"
            self.result_label.config(text=result_text, fg="#000000")
        
        self.score_label.config(text=f"Score: You {self.user_score} - Computer {self.computer_score}")

if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissorsApp(root)
    root.mainloop()