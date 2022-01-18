"""
CubeRunner, the file running the CubeClock, kind of
"""

import random
from cube_clock import CubeClock


class CubeRunner:
    def __init__(self, player1, player2):
        self.clock = CubeClock(player1, player2)
        self.players = [player1, player2]
        self.current_player = self.players[0]

    def do_move(self, steps):
        if not self.check_someone_won():
            move = self.current_player.do_move()
            self.clock.place_move(self.currrent_player, steps)
            self.change_player()

    def check_win(self):
        return self.clock.check_win()

    def change_player(self):
        self.current_player = (self.current_player + 1) % len(self.players)

    def reset(self):
        self.clock = CubeClock(self.players[0], self.players[1])

    def get_current_player(self):
        return self.current_player
