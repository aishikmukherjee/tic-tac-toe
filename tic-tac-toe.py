"""This is the classic game of tic-tac-toe"""

from os import name, system


def clear_screen():
    """Clears the screen based on OS"""
    if name == "nt":  # For Windows
        system('cls')
    else:  # For Unix-like systems
        system('clear')


class Game:
    """This is the game class, it has all methods which are used to create the game logic."""
    def __init__(self):
        """Initialize game board, player turns, and state"""
        self.board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.chance_mapper = {7: (0, 0), 8: (0, 1), 9: (0, 2), 4: (1, 0),
                              5: (1, 1), 6: (1, 2), 1: (2, 0), 2: (2, 1),
                              3: (2, 2)}
        self.positions_available = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.positions_played_already = []
        self.current_player = 'X'
        self.winner = "Draw"

    def show_board(self):
        """Displays current board state"""
        for i in range(3):
            print(f" {self.board[i][0]} | {self.board[i][1]} | {self.board[i][2]} ")
            if i != 2:
                print("-----------")

    def swap_players(self):
        """Switches the current player"""
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def chance_handler(self):
        """Handles player's move and updates board"""
        choice = int(input("Enter chance: "))
        while choice in self.positions_played_already or choice not in self.positions_available:
            choice = int(input("Try again, position already used or not "
                               "within bound, Enter chance: "))

        self.positions_played_already.append(choice)
        self.positions_available.remove(choice)
        row, col = self.chance_mapper[choice]
        self.board[row][col] = self.current_player
        clear_screen()
        self.show_board()
        self.swap_players()

    def check_winner(self):
        """Checks for a winner, returns 'X', 'O' or 'Draw'"""
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] and self.board[i][0] != ' ':
                return self.board[i][0]
        for j in range(3):
            if self.board[0][j] == self.board[1][j] == self.board[2][j] and self.board[0][j] != ' ':
                return self.board[0][j]
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != ' ':
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] != ' ':
            return self.board[0][2]

        return "Draw"

    def let_start_the_game(self):
        """Starts the game and checks for the winner"""
        for _ in range(9):
            self.chance_handler()
            self.winner = self.check_winner()
            if self.winner != "Draw":
                break
        if self.winner == "Draw":
            print("\nRESULT: It's a draw")
        else:
            print(f"\nRESULT: The winner is: {self.winner}")


if __name__ == "__main__":
    while True:
        game = Game()
        game.let_start_the_game()
        if (input("Enter 0 to play again or anything else to exit: ")) != '0':
            break
        clear_screen()
