from . import gps_controller
from . import serial_controller

GPS_TYPE_SERIAL='serial'

def create_gps_controller(gps_type):

    if gps_type == 'serial':
        controller = serial_controller.SerialGPSController()
    else:
        controller = gps_controller.GpsController()

    return controller