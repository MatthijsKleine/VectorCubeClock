"""
The Cube Clock, also known as the board
"""


import copy
import random
import time
import anki_vector
from anki_vector.util import degrees
from anki_vector import lights


class CubeClock:
    def __init__(self, player1, player2, robot, cube):
        # Starting game positions (0 to 7 going clockwise)
        self.vector_spot = 0
        self.cube_spot = 3
        self.max_spot = 7
        self.cube_states = [(0, purple_light), (1, red_light), (2, green_light), (3, blue_light), (4, yellow_light)]
        self.current_cube_state = self.cube_states[3]
        self.human = player1
        self.vector = player2
        self.spots = (self.vector_spot, self.cube_spot)
        self.robot = robot
        self.cube = cube

    def place_move(self, player, move):
        if player == self.human:
            self.cube_spot = move
        elif player == self.vector:
            self.vector_spot = move
            if move > 0:
                self.robot.behavour.turn_in_place(degrees(45))
            else:
                self.robot.behavour.turn_in_place(degrees(-45))

        # Reset vector_spot for better memoisation
        self.cube_spot = (self.cube_spot - self.vector_spot) % (self.max_spot + 1)
        self.vector_spot = (self.vector_spot - self.vector_spot) % (self.max_spot + 1)
        self.spots = (self.vector_spot, self.cube_spot)

    def new_cube_state(self):
        self.current_cube_state = self.cube_states[random.randint(1, 4)]
        self.cube.set_lights(self.current_cube_state[1])
        time.sleep(3)
        self.cube.set_lights_off()

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
