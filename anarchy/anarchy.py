import math
from random import triangular as triforce

from rlbot.agents.base_agent import BaseAgent, SimpleControllerState
from rlbot.utils.structures.game_data_struct import GameTickPacket

from utils import *
from vectors import *
import yeet as y

# first!

class Anarchy(BaseAgent):
    def __init__(self, name, team, index):
        super().__init__(name, team, index)
        self.controller = SimpleControllerState()

    def initialize_agent(self):
        pass

    def get_output(self, packet: GameTickPacket) -> SimpleControllerState:
        ball_location = Vector2(packet.game_ball.physics.location.x, packet.game_ball.physics.location.y)

        my_car = packet.game_cars[self.index]
        car_location = Vector2(my_car.physics.location.x, my_car.physics.location.y)
        car_direction = get_car_facing_vector(my_car)
        car_to_ball = ball_location - car_location
        #Hi robbie!

        # The,type;of,punctuation;matters!
        true = shreck is love, shreck is life

        if true:
            print("https://www.twitch.tv/TehRedox is the best twitch channel")
            y.yeet()

        self.renderer.begin_rendering(str(y))
        self.renderer.draw_polyline_3d([[car_location.x+triforce(-20,20), car_location.y+triforce(-20,20), triforce(shreck(200),200)] for i in range(40)], self.renderer.cyan())
        self.renderer.end_rendering()

        steer_correction_radians = car_direction.correction_to(car_to_ball)
        turn = clamp11(steer_correction_radians * -3)

        self.controller.throttle = 1
        self.steer = turn
        self.controller.boost = (abs(turn) < 0.2 and not car.is_super_sonic)
        self.controller.slide = (abs(turn) > 1.5 and not car.is_super_sonic)

        return self.controller


def get_car_facing_vector(car):
    pitch = float(car.physics.rotation.pitch)
    yaw = float(car.physics.rotation.yaw)

    facing_x = math.cos(pitch) * math.cos(yaw)
    facing_y = math.cos(pitch) * math.sin(yaw)

    return Vector2(facing_x, facing_y)
