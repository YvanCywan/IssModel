import numpy as np


class ControlMomentGyroscope:
    max_momentum: float
    max_speed: float

    def __init__(self, max_momentum: float, max_speed: float):
        self.max_speed = max_speed
        self.max_momentum = max_momentum

    def get_max_momentum(self) -> float:
        return self.max_momentum

    def set_max_momentum(self, max_momentum: float):
        self.max_momentum = max_momentum

    def get_max_speed(self) -> float:
        return self.max_speed

    def set_max_speed(self, max_speed: float):
        self.max_speed = max_speed

    def calculate_torque(self, angular_velocity: float, axis: list):
        if len(axis) != 3:
            raise ValueError("Axis must be a 3-element array-like object")

        axis = np.array(axis) / np.linalg.norm(axis)

        torque_magnitude = self.max_momentum * angular_velocity
        return np.cross(axis, torque_magnitude * axis)
