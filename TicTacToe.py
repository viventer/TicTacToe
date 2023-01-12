# Tic tac toe game version: 1.0 (11.01.23).

# imports the tkinter module to create a GUI and the choice functions from the random module.
import tkinter as tk
from tkinter import messagebox
from random import choice


class TicTacToe:

    def start_game(self):
        # creates a window that can't be resized
        self.window = tk.Tk()
        self.window.title("TicTacToe")
        self.window.geometry("375x375")
        self.window.resizable(width=False, height=False)

        # Creation of buttons:
        # A list of buttons that can be clicked (to make a move).
        self.buttons = []
        r = 0
        c = 0
        for _ in range(9):
            button = tk.Button(self.window, width=1, height=1,
                               font=("Sans", 70, "bold"), text=" ")
            button.grid(row=r, column=c, ipadx=16)
            button.bind("<Button-1>", self.player_move)
            self.buttons.append(button)
            c += 1
            if c == 3:
                r += 1
                c = 0
        # A tuple that holds a copy of the list of created buttons needed to check the result.
        self.buttons_copy = tuple(self.buttons.copy())

        # Triggering the bot's first move and launching the window.
        self.window.after(0, self.bot_move)
        self.window.mainloop()

    # A function that handles the player's moves.
    def player_move(self, event):
        clicked_button = event.widget
        if clicked_button.cget("state") == "active":
            clicked_button.configure(
                text="O", disabledforeground="green", state="disabled")
            # Removes the clicked button from the list of possible moves.
            self.buttons.remove(clicked_button)
            self.check()
            self.window.after(0, self.bot_move)

    # A function that handles the bot's moves.
    def bot_move(self):
        # Randomizes a button from the pool of unused ones.
        drawn_button = choice(self.buttons)
        drawn_button.configure(
            text="X", disabledforeground="red", state="disabled")
        self.buttons.remove(drawn_button)
        self.check()

    # A function that checks whether the game should end.
    def check(self):
        winner = ""
        symbols = ""

        # Adds all the symbols on the board to the symbols variable.
        for button in self.buttons_copy:
            symbols += button.cget("text")

        # Checking the rows.
        if symbols[0:3] == "OOO" or symbols[3:6] == "OOO" or symbols[6:9] == "OOO":
            winner = "O"
        elif symbols[0:3] == "XXX" or symbols[3:6] == "XXX" or symbols[6:9] == "XXX":
            winner = "X"

        # Checking the columns.
        if symbols[0:7:3] == "OOO" or symbols[1:8:3] == "OOO" or symbols[2:9:3] == "OOO":
            winner = "O"
        elif symbols[0:7:3] == "XXX" or symbols[1:8:3] == "XXX" or symbols[2:9:3] == "XXX":
            winner = "X"

        # Diagonal checking.
        if symbols[0] == symbols[4] and symbols[4] == symbols[8]:
            if symbols[0] == "X":
                winner = "X"

            elif symbols[0] == "O":
                winner = "O"

        if symbols[2] == symbols[4] and symbols[4] == symbols[6]:
            if symbols[2] == "X":
                winner = "X"

            elif symbols[2] == "O":
                winner = "O"

        if winner == "X" or winner == "O":
            self.end(winner)
        elif " " not in symbols:
            self.end("draw")

    # The function that displays the result after the game is over.
    def end(self, winner):
        if winner == "O":
            messagebox.showinfo(
                title="Result", message="Congratulations, you won!")
            self.window.destroy()
        elif winner == "X":
            messagebox.showinfo(
                title="Result", message="Unfortunately you lost!")
            self.window.destroy()
        else:
            messagebox.showinfo(
                title="Result", message="The game ended in a draw!")
            self.window.destroy()


tic_tac_toe = TicTacToe()
tic_tac_toe.start_game()
