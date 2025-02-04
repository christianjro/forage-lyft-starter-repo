import unittest

from tires.carrigan_tires import CarriganTires

class TestCarriganTires(unittest.TestCase):
    def test_needs_service_true(self):
        wear_sensors = [0.8, 0.8, 0,9, 0.7]
        tires = CarriganTires(wear_sensors) 
        self.assertTrue(tires.needs_service())

    def test_needs_service_false(self):
        wear_sensors = [0.7, 0.7, 0.7, 0.7]
        tires = CarriganTires(wear_sensors)
        self.assertFalse(tires.needs_service())
