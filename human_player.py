"""
The Human Player, also known as you
"""


class HumanPlayer:
    def __init__(self):
        self.next_move = 0

    def do_move(self):
        return self.next_move

    def set_move(self, move):
        self.next_move = move
