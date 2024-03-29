import unittest

from IssModel.IssModel import IssModel


class IssModelTest(unittest.TestCase):
    def test_get_mass(self):
        iss_model = IssModel()
        self.assertEqual(iss_model.get_mass(), 1000)

    def test_set_mass(self):
        iss_model = IssModel()
        iss_model.set_mass(2000)
        self.assertEqual(iss_model.get_mass(), 2000)

    def test_get_radius(self):
        iss_model = IssModel()
        self.assertEqual(iss_model.get_radius(), 1000)

    def test_set_radius(self):
        iss_model = IssModel()
        iss_model.set_radius(2000)
        self.assertEqual(iss_model.get_radius(), 2000)

    def test_get_height(self):
        iss_model = IssModel()
        self.assertEqual(iss_model.get_height(), 1000)

    def test_set_height(self):
        iss_model = IssModel()
        iss_model.set_height(2000)
        self.assertEqual(iss_model.get_height(), 500)