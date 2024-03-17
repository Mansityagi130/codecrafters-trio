import tkinter as tk
from tkinter import messagebox
import random

# List of words for the game
words = {
    "easy": ["python", "java", "ruby", "html", "css"],
    "medium": ["hangman", "programming", "computer", "science", "algorithm"],
    "hard": ["software", "developer", "javascript", "engineering", "database"]
}

class HangmanGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")

        self.word = ""
        self.guessed_letters = set()
        self.remaining_attempts = 6

        self.canvas = tk.Canvas(root, width=400, height=400)
        self.canvas.pack()

        self.difficulty_frame = tk.Frame(root)
        self.difficulty_frame.pack(pady=10)
        self.difficulty_label = tk.Label(self.difficulty_frame, text="Choose difficulty level:")
        self.difficulty_label.pack(side=tk.LEFT)
        self.difficulty_var = tk.StringVar()
        self.difficulty_var.set("easy")
        self.difficulty_menu = tk.OptionMenu(self.difficulty_frame, self.difficulty_var, "easy", "medium", "hard")
        self.difficulty_menu.pack(side=tk.LEFT)

        self.start_button = tk.Button(root, text="Start Game", command=self.start_game)
        self.start_button.pack()

    def start_game(self):
        difficulty = self.difficulty_var.get()
        self.word = choose_word(difficulty)
        self.guessed_letters = set()
        self.remaining_attempts = 6

        self.canvas.delete("all")
        self.draw_hangman()

        self.display_word()

        self.letters_frame = tk.Frame(self.root)
        self.letters_frame.pack(pady=10)
        for letter in "abcdefghijklmnopqrstuvwxyz":
            btn = tk.Button(self.letters_frame, text=letter.upper(), width=4, height=2, command=lambda l=letter: self.guess_letter(l))
            btn.grid(row=(ord(letter) - ord('a')) // 7, column=(ord(letter) - ord('a')) % 7)

    def draw_hangman(self):
        # Draw the scaffold
        self.canvas.create_line(50, 350, 150, 350, width=3)  # Horizontal
        self.canvas.create_line(100, 350, 100, 50, width=3)  # Vertical
        self.canvas.create_line(100, 50, 250, 50, width=3)   # Top

        if self.remaining_attempts < 6:
            # Draw head
            if self.remaining_attempts < 6:
                self.canvas.create_oval(225, 75, 275, 125, width=3)

        if self.remaining_attempts < 5:
            # Draw body
            self.canvas.create_line(250, 125, 250, 250, width=3)

        if self.remaining_attempts < 4:
            # Draw left arm
            self.canvas.create_line(250, 150, 220, 175, width=3)

        if self.remaining_attempts < 3:
            # Draw right arm
            self.canvas.create_line(250, 150, 280, 175, width=3)

        if self.remaining_attempts < 2:
            # Draw left leg
            self.canvas.create_line(250, 250, 220, 300, width=3)

        if self.remaining_attempts < 1:
            # Draw right leg
            self.canvas.create_line(250, 250, 280, 300, width=3)

    def display_word(self):
        displayed_word = ""
        for letter in self.word:
            if letter in self.guessed_letters:
                displayed_word += letter + " "
            else:
                displayed_word += "_ "
        self.word_label = tk.Label(self.root, text=displayed_word, font=("Helvetica", 20))
        self.word_label.pack()

    def guess_letter(self, letter):
        if letter in self.guessed_letters:
            messagebox.showwarning("Repeated Guess", "You've already guessed that letter.")
            return

        self.guessed_letters.add(letter)
        if letter not in self.word:
            self.remaining_attempts -= 1

        self.canvas.delete("all")
        self.draw_hangman()
        self.display_word()

        if self.check_win():
            messagebox.showinfo("Congratulations!", f"You've guessed the word: {self.word}")
            self.reset_game()
        elif self.remaining_attempts == 0:
            messagebox.showinfo("Game Over", f"You've run out of attempts! The word was: {self.word}")
            self.reset_game()

    def check_win(self):
        return all(letter in self.guessed_letters for letter in self.word)

    def reset_game(self):
        self.word_label.pack_forget()
        self.letters_frame.destroy()
        self.start_button.pack()


def choose_word(difficulty):
    return random.choice(words[difficulty])

if __name__ == "__main__":
    root = tk.Tk()
    hangman_gui = HangmanGUI(root)
    root.mainloop()
