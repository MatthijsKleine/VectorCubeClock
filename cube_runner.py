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

    def do_move(self):
        if not self.clock.check_win():
            move = self.current_player.do_move()
            self.clock.place_move(self.current_player, move)
            self.change_player()

    def change_player(self):
        if self.current_player == self.players[0]:
            self.current_player = self.players[1]
        else:
            self.current_player = self.players[0]

    def reset(self):
        self.clock = CubeClock(self.players[0], self.players[1])

    def get_current_player(self):
        return self.current_player
