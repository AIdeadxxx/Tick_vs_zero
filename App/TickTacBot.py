import random

class TicTacBot:
    def __init__(self, symbol="O"):
        self.symbol = symbol
    
    def make_move(self, board):
        available_moves = [i for i in range(9) if board[i] == " "]
        return random.choice(available_moves) if available_moves else None