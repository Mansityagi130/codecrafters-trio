import tkinter as tk
from tkinter import messagebox
import random

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")
        
        self.words_easy = ['apple', 'banana', 'orange']
        self.words_medium = ['grape', 'peach', 'melon']
        self.words_hard = ['pineapple', 'strawberry', 'blueberry']
        
        self.difficulty_level = None
        self.secret_word = None
        self.guesses = ''
        self.remaining_attempts = 6
        
        self.create_widgets()

    def create_widgets(self):
        self.difficulty_label = tk.Label(self.root, text='Select Difficulty:', font=('Arial', 14))
        self.difficulty_label.pack(pady=5)

        self.difficulty_frame = tk.Frame(self.root)
        self.difficulty_frame.pack(pady=5)

        self.easy_button = tk.Button(self.difficulty_frame, text='Easy', command=lambda: self.start_game('easy'))
        self.easy_button.pack(side=tk.LEFT, padx=5)

        self.medium_button = tk.Button(self.difficulty_frame, text='Medium', command=lambda: self.start_game('medium'))
        self.medium_button.pack(side=tk.LEFT, padx=5)

        self.hard_button = tk.Button(self.difficulty_frame, text='Hard', command=lambda: self.start_game('hard'))
        self.hard_button.pack(side=tk.LEFT, padx=5)

    def start_game(self, difficulty):
        if difficulty == 'easy':
            self.secret_word = random.choice(self.words_easy)
        elif difficulty == 'medium':
            self.secret_word = random.choice(self.words_medium)
        elif difficulty == 'hard':
            self.secret_word = random.choice(self.words_hard)

        self.difficulty_level = difficulty
        self.guesses = ''
        self.remaining_attempts = 6

        self.create_game_widgets()

    def create_game_widgets(self):
        self.difficulty_label.pack_forget()
        self.difficulty_frame.pack_forget()

        self.secret_word_label = tk.Label(self.root, text='', font=('Arial', 18))
        self.secret_word_label.pack(pady=10)

        self.remaining_attempts_label = tk.Label(self.root, text='', font=('Arial', 14))
        self.remaining_attempts_label.pack(pady=5)

        self.input_label = tk.Label(self.root, text='Enter a letter:', font=('Arial', 14))
        self.input_label.pack(pady=5)

        self.input_entry = tk.Entry(self.root, font=('Arial', 14))
        self.input_entry.pack(pady=5)

        self.submit_button = tk.Button(self.root, text='Submit', command=self.check_guess)
        self.submit_button.pack(pady=5)

        self.update_display()

    def update_display(self):
        masked_word = ''.join([char if char in self.guesses else '_' for char in self.secret_word])
        self.secret_word_label.config(text=masked_word)
        self.remaining_attempts_label.config(text=f"Remaining attempts: {self.remaining_attempts}")

    def check_guess(self):
        guess = self.input_entry.get()
        if len(guess) != 1 or not guess.isalpha():
            messagebox.showwarning("Invalid Input", "Please enter a single letter.")
            return
        
        if guess in self.guesses:
            messagebox.showinfo("Already Guessed", "You already guessed this letter.")
            return

        self.guesses += guess
        self.input_entry.delete(0, tk.END)

        if guess not in self.secret_word:
            self.remaining_attempts -= 1
            if self.remaining_attempts == 0:
                messagebox.showinfo("Game Over", f"The word was '{self.secret_word}'. You lost!")
                self.restart_game()
                return

        self.update_display()

        if set(self.secret_word) == set(self.guesses):
            if self.difficulty_level == 'candidate':
                messagebox.showinfo("Congratulations", "You guessed the name correctly!")
            else:
                messagebox.showinfo("Congratulations", "You guessed the word correctly!")
            self.restart_game()

    def restart_game(self):
        self.secret_word_label.pack_forget()
        self.remaining_attempts_label.pack_forget()
        self.input_label.pack_forget()
        self.input_entry.pack_forget()
        self.submit_button.pack_forget()

        self.create_widgets()

def main():
    root = tk.Tk()
    hangman_game = HangmanGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
