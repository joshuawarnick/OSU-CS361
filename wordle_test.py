import tkinter as tk
from tkinter import messagebox
import random

class WordleGame(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Wordle Game")
        self.geometry("400x500")  # Adjusted height to 500 pixels
        self.word = self.generate_word()
        self.max_attempts = 6
        self.current_attempt = 0
        self.guesses = []

        self.button_rules = tk.Button(self, text="Rules", command=self.display_rules)
        self.button_rules.pack(pady=10)

        self.label_instruction = tk.Label(self, text="Guess the word (5-letter word)")
        self.label_instruction.pack(pady=10)

        self.entry_guess = tk.Entry(self)
        self.entry_guess.pack(pady=5)

        self.button_submit = tk.Button(self, text="Submit", command=self.check_guess)
        self.button_submit.pack(pady=5)

        self.canvas = tk.Canvas(self, width=250, height=400)  # Adjusted canvas height to 400 pixels
        self.canvas.pack(pady=10)

        self.status_label = tk.Label(self, text="")
        self.status_label.pack()

        self.display_board()

    def generate_word(self):
        words = ["apple", "table", "chair", "house", "zebra"]
        return random.choice(words)

    def display_board(self):
        for row in range(6):
            for col in range(5):
                x0 = col * 50
                y0 = row * 50
                x1 = x0 + 50
                y1 = y0 + 50
                self.canvas.create_rectangle(x0, y0, x1, y1, outline='black', width=2)

    def check_guess(self):
        guess = self.entry_guess.get().lower()
        if len(guess) != 5:
            messagebox.showerror("Error", "Please enter a 5-letter word.")
        else:
            self.current_attempt += 1
            self.guesses.append(guess)
            self.update_board(guess)
            if guess == self.word:
                messagebox.showinfo("Congratulations", f"You've guessed the word '{self.word}'! It took you {self.current_attempt} attempts.")
                self.destroy()
            elif self.current_attempt >= self.max_attempts:
                messagebox.showinfo("Game Over", f"Sorry, you've reached the maximum number of attempts. The word was '{self.word}'.")
                self.destroy()

    def update_board(self, guess):
        row = self.current_attempt - 1
        for col, letter in enumerate(guess):
            x0 = col * 50
            y0 = row * 50
            x1 = x0 + 50
            y1 = y0 + 50

            if letter == self.word[col]:
                color = 'green'
            elif letter in self.word:
                color = 'yellow'
            else:
                color = '#d3d3d3'  # Light gray color

            self.canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline='black', width=2)
            self.canvas.create_text((x0 + x1) / 2, (y0 + y1) / 2, text=letter, fill='black', font=("Helvetica", 12, "bold"))

        self.status_label.config(text=f"Attempt: {self.current_attempt}/{self.max_attempts}")

    def display_rules(self):
        rules_text = ("How to Play Wordle\n\n"
                      "Each guess must be a valid five-letter word.\n\n"
                      "The color of a tile will change to show you how close your guess was.\n\n"
                      "If the tile turns green, the letter is in the word, and it is in the correct spot.\n\n"
                      "If the tile turns yellow, the letter is in the word, but it is not in the correct spot.\n\n"
                      "If the tile turns gray, the letter is not in the word.")

        messagebox.showinfo("Wordle Rules", rules_text)

class Page(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("My Page")

        self.label_title = tk.Label(self, text="Josh's CS 361 Arcade", font=("Helvetica", 20))
        self.label_title.pack(pady=20)

        self.label_whats_new = tk.Label(self, text="What's New:", font=("Helvetica", 14))
        self.label_whats_new.pack()

        self.text_whats_new = tk.Text(self, width=50, height=5)
        self.text_whats_new.insert(tk.END, "Here are the latest updates...\n\n"
                                             "The Homepage GUI\n"
                                             "The Wordle, Tic Tac Toe, and Snake Buttons\n"
                                             "The Wordle Game Implementation\n"
                                             "    - Rules button to popup the game rules\n"
                                             "    - The word submit text box and submit button\n"
                                             "    - The wordle board which displays word guesses and letter status\n")
        self.text_whats_new.pack(pady=10)

        self.label_disclaimer_title = tk.Label(self, text="Disclaimer:", font=("Helvetica", 14))
        self.label_disclaimer_title.pack()

        self.label_disclaimer = tk.Label(self, text="You can play these games for as long as you like, but each should be able to be finished in under 10 minutes.", font=("Helvetica", 10))
        self.label_disclaimer.pack()

        button_frame = tk.Frame(self)
        button_frame.pack(pady=20)

        self.button_wordle = tk.Button(button_frame, text="Play Wordle", command=self.play_wordle_game)
        self.button_wordle.pack(side="left", padx=10, pady=10)

        self.button_tic_tac_toe = tk.Button(button_frame, text="Play Tic Tac Toe", command=self.open_tic_tac_toe_game)
        self.button_tic_tac_toe.pack(side="left", padx=10, pady=10)

        self.button_snake = tk.Button(button_frame, text="Play Snake", command=self.open_snake_game)
        self.button_snake.pack(side="left", padx=10, pady=10)

        button_frame.place(relx=0.5, rely=1.0, anchor=tk.S)

    def play_wordle_game(self):
        wordle_game = WordleGame(self)
        wordle_game.mainloop()

    def open_tic_tac_toe_game(self):
        # Insert code to open Tic Tac Toe game here
        pass

    def open_snake_game(self):
        # Insert code to open Snake game here
        pass

if __name__ == "__main__":
    app = Page()
    app.mainloop()
