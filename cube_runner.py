"""
CubeRunner, the file running the CubeClock, kind of
"""


import random
import anki_vector
import time
from cube_clock import CubeClock


class CubeRunner:
    def __init__(self, player1, player2, robot, cube):
        self.clock = CubeClock(player1, player2, robot, cube)
        self.players = [player1, player2]
        self.current_player = self.players[0]
        self.robot = robot
        self.cube = cube

        touch_data = self.robot.touch.last_sensor_reading
        untouched = 0
        self.robot.behavior.say_text("Don't touch me I am setting up in this environment")
        for i in range(20):
            untouched += touch_data.raw_touch_value
        untouched = untouched / 20
        print(untouched)
        time.sleep(1.0)
        self.robot.behavior.say_text("Now touch my whole back")
        while touch_data.raw_touch_value + 50 < untouched:
            time.sleep(0.1)
        time.sleep(1.0)
        touched = 0
        for i in range(20):
            touched += touch_data.raw_touch_value
        touched = touched / 20.0
        print(touched)
        diff = touched - untouched
        self.threshold = untouched + diff / 4

    def do_move(self):
        if not self.clock.check_win():
            move = 0
            if self.current_player == self.players[0]:
                moves = self.clock.get_possible_moves(self.current_player)
                self.robot.behavior.say_text("Touch me if you moved the cube clockwise, otherwise wait 3 seconds.")
                clockwise = 1
                touchTimer = 0
                while not self.robot.touch.last_sensor_reading.is_being_touched and touchTimer < 30:
                    time.sleep(0.1)
                    touchTimer = touchTimer + 1
                if touchTimer >= 30:
                    clockwise = 0
                move = self.clock.get_possible_moves(self.current_player)[clockwise]
            else:
                move = self.current_player.do_move()
            self.clock.place_move(self.current_player, move)
            if self.current_player == self.players[0]:
                self.clock.new_cube_state()
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

    def turn_cycle(self):
        if self.clock.check_win():
            self.robot.behavior.say_text("I win!")
        if self.players[1].depth > self.players[1].max_depth:
            self.robot.behavior.say_text("You win!")

    def is_running(self):
        active = True
        if self.clock.check_win():
            active = False
        if self.players[1].depth > self.players[1].max_depth:
            active = False
        return active


