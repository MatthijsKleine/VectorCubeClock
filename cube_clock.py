"""
The Cube Clock, also known as the board
"""
import copy
import random


class CubeClock:
    def __init__(self, player1, player2):
        # Starting game positions (0 to 7 going clockwise)
        self.vector_spot = 0
        self.cube_spot = 3
        self.max_spot = 7
        self.cube_states = [(0, "Black"), (1, "Red"), (2, "Green"), (3, "Blue"), (4, "Yellow")]
        self.current_cube_state = self.cube_states[3]
        self.human = player1
        self.vector = player2
        self.spots = (self.vector_spot, self.cube_spot)

    def place_move(self, player, move):
        if player == self.human:
            self.cube_spot = move
        elif player == self.vector:
            self.vector_spot = move
            # robot.behaviour turn 45 degrees TO BE ADDED

        # Reset vector_spot for better memoisation
        self.cube_spot = (self.vector_spot - self.vector_spot) % (self.max_spot + 1)
        self.vector_spot = (self.vector_spot - self.vector_spot) % (self.max_spot + 1)
        self.spots = (self.vector_spot, self.cube_spot)

    def new_cube_state(self):
        self.current_cube_state = self.cube_states[random.randint(1, 4)]
        # UPDATE CUBE LIGHTS

    def check_win(self):
        win = False
        if self.cube_spot == self.vector_spot:
            win = True
        return win

    def get_spots(self):
        spots = (self.cube_spot, self.vector_spot)
        return spots

    def get_possible_moves(self, player):
        moves = []
        if player == self.human:
            if self.current_cube_state[0] == 1:
                moves = [(self.cube_spot - 2) % (self.max_spot + 1), (self.cube_spot + 2) % (self.max_spot + 1)]
            if self.current_cube_state[0] == 2:
                moves = [(self.cube_spot - 1) % (self.max_spot + 1), (self.cube_spot + 1) % (self.max_spot + 1)]
            if self.current_cube_state[0] == 3:
                moves = [self.cube_spot, self.cube_spot]
            if self.current_cube_state[0] == 4:
                moves = [(self.cube_spot - 3) % (self.max_spot + 1), (self.cube_spot + 3) % (self.max_spot + 1)]
        elif player == self.vector:
            if self.current_cube_state[0] == 1:
                moves = [(self.vector_spot - 1) % (self.max_spot + 1), (self.vector_spot + 1) % (self.max_spot + 1)]
            if self.current_cube_state[0] == 2:
                moves = [(self.vector_spot - 2) % (self.max_spot + 1), (self.vector_spot + 2) % (self.max_spot + 1)]
            if self.current_cube_state[0] == 3:
                moves = [(self.vector_spot - 3) % (self.max_spot + 1), (self.vector_spot + 3) % (self.max_spot + 1)]
            if self.current_cube_state[0] == 4:
                moves = [self.vector_spot, self.vector_spot]
        return moves

    def deep_copy(self):
        return copy.deepcopy(self)
