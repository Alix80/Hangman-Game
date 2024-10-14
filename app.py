
import tkinter as tk
from tkinter import messagebox
import random
def select_random_word():
    words = ["python", "hangman", "computer", "programming", "algorithm", "random", "variable"]
    return random.choice(words)
def update_display():
    display_word.set(" ".join([letter if letter in guessed_letters else "_" for letter in word]))
def process_guess():
    guess = guess_entry.get().lower()
    
    if guess in guessed_letters:
        messagebox.showinfo("Hangman", "You've already guessed that letter.")
    elif guess in word:
        guessed_letters.add(guess)
        messagebox.showinfo("Hangman", f"Good guess! '{guess}' is in the word.")
        update_display()
    else:
        incorrect_guesses[0] += 1
        messagebox.showinfo("Hangman", f"Incorrect! You have {max_incorrect_guesses - incorrect_guesses[0]} guesses left.")
        wrong_guesses_label.config(text=f"Incorrect guesses: {incorrect_guesses[0]}")
    if all(letter in guessed_letters for letter in word):
        messagebox.showinfo("Hangman", f"Congratulations! You guessed the word: {word}")
        root.quit()  # End the game
    elif incorrect_guesses[0] >= max_incorrect_guesses:
        messagebox.showinfo("Hangman", f"You've run out of guesses! The word was: {word}")
        root.quit()

    guess_entry.delete(0, tk.END)  
word = select_random_word()
guessed_letters = set()
incorrect_guesses = [0]
max_incorrect_guesses = 6

# Create the main window
root = tk.Tk()
root.title("Hangman Game")
display_word = tk.StringVar()
display_word.set(" ".join("_" for _ in word))
word_label = tk.Label(root, textvariable=display_word, font=("Helvetica", 20))
word_label.pack(pady=20)
guess_label = tk.Label(root, text="Guess a letter:")
guess_label.pack()
guess_entry = tk.Entry(root, font=("Helvetica", 14))
guess_entry.pack(pady=10)

# Button to submit the guess
guess_button = tk.Button(root, text="Submit Guess", command=process_guess)
guess_button.pack(pady=10)
wrong_guesses_label = tk.Label(root, text=f"Incorrect guesses: {incorrect_guesses[0]}", font=("Helvetica", 14))
wrong_guesses_label.pack(pady=10)
root.mainloop()
