import tkinter as tk
from tkinter import messagebox
import random

class GuessingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Guessing Game")

        self.target_number = random.randint(1, 20)
        self.attempts = 0

        self.label = tk.Label(master, text="Guess a number between 1 and 20:")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.button = tk.Button(master, text="Guess", command=self.check_guess)
        self.button.pack()

    def check_guess(self):
        guess = self.entry.get()
        self.attempts += 1
        try:
            guess = int(guess)
            if guess < 1 or guess > 20:
                messagebox.showwarning("Invalid Guess", "Please enter a number between 1 and 20.")
            else:
                if guess < self.target_number:
                    messagebox.showinfo("Result", "Too low! Try a higher number.")
                elif guess > self.target_number:
                    messagebox.showinfo("Result", "Too high! Try a lower number.")
                else:
                    messagebox.showinfo("Congratulations!", f"Correct! You've guessed the number {self.target_number}.\nIt took you {self.attempts} attempts.")
                    self.restart_game()
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid integer.")

    def restart_game(self):
        self.target_number = random.randint(1, 20)
        self.attempts = 0
        self.label.config(text="Guess a number between 1 and 20:")
        self.entry.delete(0, tk.END)

def main():
    root = tk.Tk()
    game = GuessingGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
