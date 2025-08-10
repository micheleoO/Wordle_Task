import tkinter as tk
from tkinter import messagebox
import random

# List of 5-letter words (real words)
def load_words_from_file(filename):
    with open(filename, 'r') as file:
        words = file.readlines()
    # Remove spaces or extra characters
    words = [word.strip() for word in words if len(word.strip()) == 5]  # Only words that are exactly 5 letters
    return words

# Load words from txt file
word_list = load_words_from_file("words.txt")

# Pick a random word from the list
def get_random_word():
    return random.choice(word_list).upper()

secret_word = get_random_word()
max_attempts = 6
attempts = 0

# Store guesses
guesses = [["" for _ in range(5)] for _ in range(max_attempts)]  # 6 attempts, each attempt has 5 slots

# Function to handle input and update the UI
def check_guess():
    global attempts, secret_word
    guess = "".join(guesses[attempts]).upper()  # Convert the current guess into a word

    # Make sure the guess is a real word from the list
    if guess.lower() not in word_list:
        messagebox.showwarning("Error", "The word is not in the list! Try another one.")
        return
    
    if len(guess) != 5:
        messagebox.showwarning("Error", "The word must be 5 letters long!")
        return
    
    attempts += 1
    result = []
    
    # Letter feedback
    for i in range(5):
        if guess[i] == secret_word[i]:
            result.append(("green", guess[i]))  # Correct letter in the correct position
        elif guess[i] in secret_word:
            result.append(("yellow", guess[i]))  # Letter exists but in the wrong position
        else:
            result.append(("gray", guess[i]))  # Letter does not exist
    
    # Update UI (only for the current attempt)
    update_display(result)
    update_keyboard(result)  # Update the keyboard
    
    if guess == secret_word:
        messagebox.showinfo("Congratulations!", f"You guessed the correct word: {secret_word}")
        reset_game()
    elif attempts >= max_attempts:
        messagebox.showinfo("Game Over", f"You lost! The correct word was: {secret_word}")
        reset_game()

# Function to update the display after each attempt
def update_display(result):
    for j in range(5):
        # Update only the cells for the current attempt
        label = grid_labels[attempts-1][j]
        letter = guesses[attempts-1][j]
        color = result[j][0]
        label.config(text=letter, bg=color)

    label_attempts.config(text=f"Attempts: {attempts}/{max_attempts}")

# Function to reset the game
def reset_game():
    global attempts, secret_word, guesses
    secret_word = get_random_word()  # Pick a new random word
    attempts = 0
    guesses = [["" for _ in range(5)] for _ in range(max_attempts)]  # Reset guesses
    for i in range(6):
        for j in range(5):
            grid_labels[i][j].config(text="", bg="lightgray")
    label_attempts.config(text=f"Attempts: {attempts}/{max_attempts}")
    reset_keyboard()

# Function to reset the keyboard
def reset_keyboard():
    for button in keyboard_buttons:
        button.config(bg="lightgray", state="normal")  # Reset colors and enable all buttons

# Function to update the keyboard based on guess result
def update_keyboard(result):
    for i in range(5):
        letter = result[i][1]  # Letter
        color = result[i][0]  # Color
        
        # Change button color based on the result
        for button in keyboard_buttons:
            if button.cget("text") == letter:
                button.config(bg=color)
                
                # Disable button if it's wrong (gray)
                if color == "gray":
                    button.config(state="disabled")

# Function to add a letter to the current guess
def add_letter(letter):
    global attempts
    if attempts < max_attempts:
        row = attempts
        for col in range(5):
            if guesses[row][col] == "":
                guesses[row][col] = letter
                grid_labels[row][col].config(text=letter)
                break

# Function to remove the last letter
def remove_letter():
    global attempts
    if attempts < max_attempts:
        row = attempts
        for col in range(4, -1, -1):
            if guesses[row][col] != "":
                guesses[row][col] = ""
                grid_labels[row][col].config(text="")
                break

# Create the Tkinter UI
root = tk.Tk()
root.title("Wordly")
root.config(bg="white")

# Game instructions
instructions = tk.Label(root, text="Try to guess the 5-letter word!", font=("Arial", 14), bg="white")
instructions.grid(row=0, column=0, columnspan=5, pady=10)

# Create a grid of labels to show letters
grid_labels = [[tk.Label(root, text="", font=("Arial", 24), width=5, height=2, relief="solid", bg="lightgray") for _ in range(5)] for _ in range(6)]
for i in range(6):
    for j in range(5):
        grid_labels[i][j].grid(row=i+1, column=j, padx=5, pady=5)

# Show attempts
label_attempts = tk.Label(root, text=f"Attempts: {attempts}/{max_attempts}", font=("Arial", 12), bg="white")
label_attempts.grid(row=7, column=0, columnspan=5, pady=10)

# On-screen keyboard
keyboard_buttons = []
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i, letter in enumerate(alphabet):
    button = tk.Button(root, text=letter, font=("Arial", 14), width=4, height=2, command=lambda l=letter: add_letter(l))
    button.grid(row=8 + i // 10, column=i % 10, padx=20, pady=5)
    keyboard_buttons.append(button)

# Buttons for check and delete
check_button = tk.Button(root, text="Check", font=("Arial", 14), command=check_guess)
check_button.grid(row=10, column=5, columnspan=5, pady=10)

remove_button = tk.Button(root, text="Delete", font=("Arial", 14), command=remove_letter)
remove_button.grid(row=10, column=7, columnspan=5, pady=10)

# Run the Tkinter main loop
root.mainloop()