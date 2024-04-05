from typing import Any

import numpy as np


class ControlMomentGyroscope:
    max_momentum: float
    max_speed: float
    coordinates: list[float]

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

    def get_coordinates(self) -> list:
        return self.coordinates

    def set_coordinates(self, coordinates: list):
        self.coordinates = coordinates

    def calculate_torque(self, angular_velocity: float, axis: list) -> np.ndarray[Any, np.dtype]:
        if len(axis) != 3:
            raise ValueError("Axis must be a 3-element array-like object")

        axis = np.array(axis) / np.linalg.norm(axis)

        torque_magnitude = self.max_momentum * angular_velocity
        return np.cross(axis, torque_magnitude * axis)

    def calculate_angular_velocity(self, torque: list, axis: list) -> list[float]:
        return np.linalg.norm(torque) / self.max_momentum * np.array(axis)

    def calculate_axis(self, torque: list[float], angular_velocity: list[float]) -> np.array:
        return np.linalg.norm(torque) / self.max_momentum * np.array(angular_velocity)

    def calculate_coordinates(self, torque: list, angular_velocity: list[float], axis: list) -> np.array:
        return self.coordinates + self.calculate_axis(torque, angular_velocity)

    def __str__(self):
        return (
                f"ControlMomentGyroscope("
                f"max_momentum={self.max_momentum}, "
                f"max_speed={self.max_speed}, "
                f"coordinates={self.coordinates})"
        )
