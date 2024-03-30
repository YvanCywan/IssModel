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
        self.assertEqual(torque, [0, 0, 0])
