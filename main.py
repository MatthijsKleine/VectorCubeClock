"""
Cube Runner
Cube on a Clock Game with Anki Vector
By Just Baselmans & Matthijs Kleine
15/01/2022

This Python script allows the user to play an Expectiminimax game with Vector. In the game a cube is located on a
clock with 8 points to place it, with Vector in the middle. Vector start with the cube behind him, and tries to find
the cube as fast as possible. Each turn has 3 possible move sets, either Vector does 3 moves and the user can move
the cube 1 spot, both can move two spots, or Vector moves 1 and the user moves the cube 3 spots. All move sets have
equal probability, the user always moves first and the game ends when Vector sees the cube.

Anki Vector SDK Library Used: https://developer.anki.com/vector/docs
Code used from API Reference: https://developer.anki.com/vector/docs/api.html

Tutorials and referencing used from keith at Kinvert: https://www.kinvert.com/anki-vector-examples-tutorials-projects-python-sdk/

Expectiminimax algorithm heavily based on tutorial 09 and pseudocode from Wikipedia: https://en.wikipedia.org/wiki/Expectiminimax
"""
# Importing the required libraries
import anki_vector
from anki_vector import lights
from anki_vector.util import degrees, distance_mm, speed_mmps
import time
from cube_clock import CubeClock
from human_player import HumanPlayer
from expectiminimax_player import ExpectiMiniMaxPlayer


class Game:
    """
    Running the starting actions for Vector to set upp the game.
    """
    def __init__(self):
        # Initializing the classes
        self.player1 = HumanPlayer()
        self.player2 = ExpectiMiniMaxPlayer()
        self.game = CubeClock(self.player1, self.player2)

        # Referencing Vector as just "robot"
        self.args = anki_vector.util.parse_command_args()

        # Running the starting actions
        with anki_vector.Robot(self.args.serial) as robot:
            # Waking up Vector
            robot.behavior.set_eye_color(hue=0.16, saturation=1)
            robot.behavior.drive_off_charger()
            time.sleep(0.5)

            # Clearing his vision
            robot.behavior.set_head_angle(degrees(-5.0))
            robot.behavior.set_lift_height(0.0)

            # Connecting to the cube
            robot.behavior.say_text("Connecting to cube...")
            while not robot.world.connected_light_cube:
                print("No Cube Yet...")
                robot.world.connect_cube()
            print("Connected")
            time.sleep(0.1)
            cube = robot.world.connected_light_cube

            # Starting the game
            robot.behavior.say_text("Let's play a game!")
            time.sleep(0.2)
            robot.behavior.say_text("You can move first, put the cube behind me and tap it!")
            time.sleep(0.2)
            robot.behavior.say_text("Let's see how many moves we have!")

    """
    The loop of the game
    """
    def game_loop(self):




if __name__ == "__main__":
    game = Game()
    while True:
        game.game_loop()

    # Left over but maybe reusable code from the initial idea
    # noinspection PyUnreachableCode
    """
        mode_chosen = False
        ask_left = True
        while mode_chosen is False:
            robot.behavior.set_eye_color(hue=0, saturation=0)
            time.sleep(1.0)
            if ask_left:
                robot.behavior.say_text("Pet me now for Left Depth First Search")
            else:
                robot.behavior.say_text("Pet me now for Right Depth First Search")
            time.sleep(1.0)
            touch_data = robot.touch.last_sensor_reading
            if touch_data is not None:
                is_being_touched = touch_data.is_being_touched
            if is_being_touched and ask_left:
                LeftSearch = True
                mode_chosen = True
                eye_color = (0.66, 1)
                cube_color = lights.blue_light
            elif is_being_touched and not ask_left:
                LeftSearch = False
                mode_chosen = True
                eye_color = (1, 1)
                cube_color = lights.red_light
            ask_left = not ask_left
        robot.behavior.set_eye_color(hue=eye_color[0], saturation=eye_color[1])
        cube.set_lights(cube_color)
        found_cube = False
        robot.behavior.say_text("Thank you i will be on my way")
        cube.set_lights_off()
        # robot.events.subscribe(get_cube(robot), Events.object_appeared)
        while not found_cube:
            proximity_data = robot.proximity.last_sensor_reading
            closest_proximity = None
            for degrees_turned in range(360):
                if proximity_data < closest_proximity:
                    closest_proximity = proximity_data
                    angle_closest = degrees_turned
                robot.behavior.turn_in_place(degrees(1))
                proximity_data = robot.proximity.last_sensor_reading
            robot.behavior.turn_in_place(degrees(90 + angle_closest))
            while proximity_data > closest_proximity:
                robot.behavior.drive_straight(distance_mm(100), speed_mmps(100))
                proximity_data = robot.proximity.last_sensor_reading
        """