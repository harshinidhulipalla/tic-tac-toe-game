import random
import random
import random

# Example: Get a random number between 1 and 10
random_number = random.randint(1, 10)
print(random_number)
import tkinter as tk
import random
from tkinter import messagebox

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe - Human vs AI")
        self.master.geometry("500x650")
        self.master.resizable(0, 0)

        # Game board
        self.board = {i: " " for i in range(1, 17)}  # 16 cells for a 4x4 grid
        self.turn_order = ["x", "o"]  # 'x' is human, 'o' is AI
        self.turn_index = 0
        self.game_end = False

        # Title label
        self.titleLabel = tk.Label(self.master, text="Tic Tac Toe - Human vs AI", font=("Arial", 26), bg="orange", width=16)
        self.titleLabel.pack()

        # Frame for the board
        self.board_frame = tk.Frame(self.master)
        self.board_frame.pack()

        # Create buttons for the board
        self.buttons = []
for i in range(16):
            button = tk.Button(self.board_frame, text=" ", width=6, height=3, font=("Arial", 20), bg="yellow", relief="raised", borderwidth=5)
            button.grid(row=i // 4, column=i % 4)  # 4 columns in each row
            button.config(command=lambda i=i: self.player_move(i + 1))  # Pass the button index (1-based)
            self.buttons.append(button)

        # Restart button
        self.restartButton = tk.Button(self.master, text="Restart Game", width=19, height=1, font=("Arial", 20), bg="green", relief="raised", borderwidth=5, command=self.restart_game)
        self.restartButton.pack()

    def update_board(self):
        """Update the buttons to reflect the current game state."""
        for i in range(16):
            self.buttons[i]["text"] = self.board[i + 1]
def check_for_win(self, player):
        """Check if the given player has won the game."""
        # Check rows
        for row in range(0, 16, 4):  # Start each row (index 0, 4, 8, 12)
            if self.board[row + 1] == self.board[row + 2] == self.board[row + 3] == self.board[row + 4] == player:
                return True

        # Check columns
        for col in range(1, 5):  # Check each column (1-4)
            if self.board[col] == self.board[col + 4] == self.board[col + 8] == self.board[col + 12] == player:
                return True

        # Check diagonals
        if self.board[1] == self.board[6] == self.board[11] == self.board[16] == player:
            return True
        if self.board[4] == self.board[7] == self.board[10] == self.board[13] == player:
            return True

        return False

    def check_for_draw(self):
        """Check if the game is a draw (i.e., no empty spaces left)."""
        return all(self.board[i] != " " for i in self.board)

    def player_move(self, position):
        """Handle the human player's move."""
        if self.game_end:
             return

        if self.board[position] == " " and self.turn_order[self.turn_index] == "x":
            # Human's turn
            self.board[position] = "x"
            self.update_board()

            if self.check_for_win("x"):
                self.end_game("You win!")
            elif self.check_for_draw():
                self.end_game("Game Draw!")
            else:
                # Switch to AI
                self.turn_index = 1
                self.ai_move()

    def ai_move(self):
        """AI makes a random move."""
        if self.game_end:
            return

        available_moves = [pos for pos in self.board if self.board[pos] == " "]
        if available_moves:
            ai_position = random.choice(available_moves)
            self.board[ai_position] = "o"
            self.update_board()

            if self.check_for_win("o"):
                self.end_game("AI wins!")
                 elif self.check_for_draw():
                self.end_game("Game Draw!")
            else:
                # Switch back to human
                self.turn_index = 0

    def end_game(self, message):
        """End the game and show a message."""
        self.game_end = True
        messagebox.showinfo("Game Over", message)

    def restart_game(self):
        """Restart the game."""
        self.board = {i: " " for i in range(1, 17)}  # Reset the board
        self.update_board()
        self.game_end = False
        self.turn_index = 0  # Reset turn to human ('x')
        self.titleLabel.config(text="Tic Tac Toe - Human vs AI")

# Run the game in Jupyter Notebook
def run_game():
    root = tk.Tk()
    game = TicTacToe(root)
     root.mainloop()

run_game()
