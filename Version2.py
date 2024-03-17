import tkinter as tk 
from tkinter import messagebox 
import random 
 
# List of words for the game 
words = { 
    "easy": ["python", "java", "ruby", "html", "css"], 
    "medium": ["hangman", "programming", "computer", "science", "algorithm"], 
    "hard": ["software", "developer", "javascript", "engineering", "database"] 
} 
 
# Stickman figures for Hangman 
hangman_stickman = [ 
    """ 
     ------ 
    |    | 
    | 
    | 
    | 
    | 
    """, 
    """ 
     ------ 
    |    | 
    |    O 
    | 
    | 
    | 
    """, 
    """ 
     ------ 
    |    | 
    |    O 
    |    | 
    | 
    | 
    """, 
    """ 
     ------ 
    |    | 
    |    O 
    |   /| 
    | 
    | 
    """, 
    """ 
     ------ 
    |    | 
    |    O 
    |   /|\\ 
    | 
    | 
    """, 
    """ 
     ------ 
    |    | 
    |    O 
    |   /|\\ 
    |   / 
    | 
    """, 
    """ 
     ------ 
    |    | 
    |    O 
    |   /|\\ 
    |   / \\ 
    | 
    """ 
] 
 
class HangmanGUI: 
    def __init__(self, root): 
        self.root = root 
        self.root.title("Hangman Game") 
 
        self.word = "" 
        self.guessed_letters = [] 
        self.attempts = 0 
 
        self.canvas = tk.Canvas(root, width=200, height=200) 
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
        self.guessed_letters = [] 
        self.attempts = 0 
 
        self.canvas.delete("all") 
        self.draw_hangman() 
 
        self.word_label = tk.Label(self.root, text=self.display_word()) 
        self.word_label.pack() 
 
        self.guess_label = tk.Label(self.root, text="Enter a letter:") 
        self.guess_label.pack() 
        self.guess_entry = tk.Entry(self.root) 
        self.guess_entry.pack() 
        self.guess_button = tk.Button(self.root, text="Guess", command=self.make_guess) 
        self.guess_button.pack() 
 
    def display_word(self): 
        displayed_word = "" 
        for letter in self.word: 
            if letter in self.guessed_letters: 
                displayed_word += letter 
            else: 
                displayed_word += "_" 
        return displayed_word 
 
    def draw_hangman(self): 
        self.canvas.create_text(100, 20, text=hangman_stickman[self.attempts], font=("Courier", 10)) 
 
    def make_guess(self): 
        guess = self.guess_entry.get().lower() 
 
        if len(guess) != 1 or not guess.isalpha(): 
            messagebox.showwarning("Invalid Guess", "Please enter a single letter.") 
            return 
 
        if guess in self.guessed_letters: 
            messagebox.showwarning("Repeated Guess", "You've already guessed that letter.") 
            return 
 
        self.guessed_letters.append(guess) 
 
        if guess not in self.word: 
            self.attempts += 1 
            if self.attempts == len(hangman_stickman) - 1: 
                messagebox.showinfo("Game Over", f"You've run out of attempts! The word was: {self.word}") 
                self.reset_game() 
                return 
 
        self.canvas.delete("all") 
        self.draw_hangman() 
 
        if self.check_win(): 
            messagebox.showinfo("Congratulations!", f"You've guessed the word: {self.word}") 
            self.reset_game() 
            return 
 
        self.word_label.config(text=self.display_word()) 
        self.guess_entry.delete(0, tk.END) 
 
    def check_win(self): 
        for letter in self.word:
             if letter not in self.guessed_letters: 
                return False 
        return True 
 
    def reset_game(self): 
        self.word_label.pack_forget() 
        self.guess_label.pack_forget() 
        self.guess_entry.pack_forget() 
        self.guess_button.pack_forget() 
        self.start_button.pack() 
 
 
def choose_word(difficulty): 
    return random.choice(words[difficulty]) 
 
if __name__ == "__main__": 
    root = tk.Tk() 
    hangman_gui = HangmanGUI(root) 
    root.mainloop()

    