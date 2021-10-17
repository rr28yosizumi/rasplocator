from . import accele_controller
import FaBo9Axis_MPU9250
import time

class MPU9250Controller(accele_controller.AcceleController):
    def __init__(self):
        self.mpu9250 = FaBo9Axis_MPU9250.MPU9250()


    def check_vaital(self):
        pass

    def get_accele_data(self):
        
        accel  = self.mpu9250.readAccel()
        gyro = self.mpu9250.readGyro()

        return (
            accel['x'],
            accel['y'],
            accel['z'],
            gyro['x'],
            gyro['y'],
            gyro['z'],
        )
