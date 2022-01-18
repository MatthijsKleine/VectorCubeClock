"""
The Cube Clock, also known as the board
"""
import copy


class CubeClock:
    def __init__(self, player1, player2):
        # Starting game positions (0 to 8 going clockwise)
        self.vector_spot = 0
        self.cube_spot = 4
        self.max_spot = 8
        self.human = player1
        self.vector = player2
        self.spots = (self.vector_spot, self.cube_spot)

    def place_move(self, player, steps):
        if player == self.human:
            self.cube_spot = (self.cube_spot + steps) % (self.max_spot + 1)
        elif player == self.vector:
            self.vector_spot = (self.vector_spot + steps) % (self.max_spot + 1)
            # robot.behaviour turn 45 degrees TO BE ADDED

        # Reset vector_spot for better memoisation
        self.cube_spot = (self.vector_spot - self.vector_spot) % (self.max_spot + 1)
        self.vector_spot = (self.vector_spot - self.vector_spot) % (self.max_spot + 1)
        self.spots = (self.vector_spot, self.cube_spot)

    def check_win(self, player):
        win = False
        if self.cube_spot == self.vector_spot:
            win = True
        if player == self.human:
            win = not win
        return win

    def get_spots(self):
        spots = (self.cube_spot, self.vector_spot)
        return spots

    def deep_copy(self):
        return copy.deepcopy(self)
