import unittest
from src.gps_controller import serial_controller
import time

class TestCase(unittest.TestCase):
    def setUp(sefl):
        pass


    def test_case01(self):
        gps = serial_controller.SerialGPSController()

        while True:
            if gps.is_enable_gps() :
                break
            time.sleep(1)

        data = gps.get_gps_data()
        print(data)
