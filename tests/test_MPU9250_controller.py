import unittest
from src.acceleration_controller import MPU9250_controller


class TestCase(unittest.TestCase):
    def setUp(sefl):
        pass

    def test_case1(self):
        mpu = MPU9250_controller.MPU9250Controller()
        accdata = mpu.get_accele_data()
        print(accdata)
        
