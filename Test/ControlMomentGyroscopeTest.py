import unittest

import numpy as np

from ControlMomentGyroscope import ControlMomentGyroscope


class ControlMomentGyroscopeTest(unittest.TestCase):
    def test_torque(self):
        testCmg = ControlMomentGyroscope(max_momentum=1000, max_speed=1000)
        angular_velocity = 10
        axis = [1, 0, 0]
        torque = testCmg.calculate_torque(angular_velocity, axis)
        torque = np.linalg.norm(torque)
        self.assertEqual(torque, 0.0)

    def test_angular_velocity(self):
        testCmg = ControlMomentGyroscope(max_momentum=1000, max_speed=1000)
        angular_velocity: list[float] = testCmg.calculate_angular_velocity([100, 100, 100], [1000, 3000, 1000])
        expected_velocity = [173.20508076, 519.61524227, 173.20508076]
        self.assertEqual(all(angular_velocity), all(expected_velocity))

    def test_calculate_axis(self):
        testCmg = ControlMomentGyroscope(max_momentum=1000, max_speed=1000)
        axis = testCmg.calculate_axis([100, 100, 100], [1000, 3000, 1000])
        expected_axis = np.array([0.0, 0.0, 1.0])
        self.assertEqual(any(axis), any(expected_axis))

    def test_calculate_coordinates(self):
        testCmg = ControlMomentGyroscope(max_momentum=1000, max_speed=1000)
        testCmg.set_coordinates([1000, 3000, 1000])
        coordinates = testCmg.calculate_coordinates([100, 100, 100], [1000, 3000, 1000], [1000, 3000, 1000])
        expected_coordinates: np.array = np.array([1000.0, 3000.0, 1000.0])
        self.assertEqual(any(coordinates), any(expected_coordinates))
