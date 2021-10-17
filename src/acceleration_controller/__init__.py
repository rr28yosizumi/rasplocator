from . import accele_controller
from . import MPU9250_controller

ACCELE_TYPE_MPU9250 = 'MPU9250'

def create_accele_controller(type = ''):
    if type == 'MPU9250':
        controller = MPU9250_controller.MPU9250Controller()
    else:
        controller = accele_controller.AcceleController()

    return controller