import tkinter as tk
import random

# Function to define the computer's choice
def computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

# Function to update the result label
def update_result(result):
    result_label.config(text=result)

# Function to handle button clicks
def button_click(choice):
    user_choice = choice
    computer_option = computer_choice()

    # Determine the winner
    if (user_choice == 'rock' and computer_option == 'scissors') or \
       (user_choice == 'scissors' and computer_option == 'paper') or \
       (user_choice == 'paper' and computer_option == 'rock'):
        result = f"User wins! {user_choice} beats {computer_option}."
    elif user_choice == computer_option:
        result = "It's a tie!"
    else:
        result = f"Computer wins! {computer_option} beats {user_choice}."

    # Update the result label
    update_result(result)

root = tk.Tk()
root.title("Rock, Paper, Scissors")

# Create labels, buttons, and images
user_choice_label = tk.Label(root, text="User turn:")
user_choice_label.grid(row=0, column=0)
computer_choice_label = tk.Label(root, text="Computer's turn:")
computer_choice_label.grid(row=1, column=0)
result_label = tk.Label(root, text="")
result_label.grid(row=2, column=0)

rock_button = tk.Button(root, text="Rock", command=lambda: button_click('rock'))
rock_button.grid(row=3, column=0)
paper_button = tk.Button(root, text="Paper", command=lambda: button_click('paper'))
paper_button.grid(row=4, column=0)
scissors_button = tk.Button(root, text="Scissors", command=lambda: button_click('scissors'))
scissors_button.grid(row=5, column=0)

root.mainloop()