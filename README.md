# README – Wordly Game (Tkinter)

This is my Python project for making a simple word-guessing game, similar to Wordle.  
It uses **Tkinter** for the interface, and a text file with words for the secret word list.  

I will explain the code in parts, because I had to figure out each part step-by-step.  

---

## 1. Loading the Words

```python
def load_words_from_file(filename):
    with open(filename, 'r') as file:
        words = file.readlines()
    words = [word.strip() for word in words if len(word.strip()) == 5]
    return words
```

This function opens the file, reads all the lines, and keeps only the words that have exactly 5 letters.  
At first, I didn’t filter them and it made the game crash when a word had more or fewer letters.  
Using `.strip()` removes spaces and extra characters.  

---

## 2. Picking the Secret Word

```python
def get_random_word():
    return random.choice(word_list).upper()
```

This chooses a random word from the loaded list and makes it uppercase.  
I learned that uppercase is better because it matches the way the on-screen keyboard works.  

---

## 3. Checking the Guess

```python
def check_guess():
    ...
```

This is the main function for the game.  
- It takes the player’s guess and checks if it’s in the list of valid words.  
- If it is valid, it compares each letter to the secret word.  
- It gives three possible results for each letter:  
  - **green** → correct letter in correct position  
  - **yellow** → correct letter but wrong position  
  - **gray** → letter not in the word  

At first, I had problems because I forgot to handle lowercase vs uppercase, so no guesses matched.  

---

## 4. Showing the Results on the Grid

```python
grid_labels = [[...]]
```

This creates a 6×5 grid (6 attempts, each with 5 letters).  
Every guess updates the colors of the cells for that attempt.  
Before using loops, I tried to write each label one by one, which was very repetitive and harder to change.  

---

## 5. Resetting the Game

```python
def reset_game():
    ...
```

When the player wins or loses, this function:  
- Picks a new secret word  
- Clears the grid  
- Resets attempts to 0  
- Resets the keyboard colors  

Without this, I had to restart the whole program to play again.  

---

## 6. On-Screen Keyboard

```python
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
```

Each letter has its own button.  
When the player guesses, the keyboard buttons change color based on the result.  
I had to add a check so wrong letters disable themselves (gray).  

---

## 7. Adding and Removing Letters

```python
def add_letter(letter):
    ...
def remove_letter():
    ...
```

`add_letter()` puts a letter in the next empty cell of the current row.  
`remove_letter()` deletes the last letter in the current row.  
This part took me time because I wanted it to delete only the last letter, not the whole word.  

---

## 8. Main Interface

```python
root = tk.Tk()
...
root.mainloop()
```

- I used labels for the grid cells.  
- Buttons for letters, check, and delete.  
- A label for showing the attempt count.  

`root.mainloop()` keeps the window open until the user closes it.  