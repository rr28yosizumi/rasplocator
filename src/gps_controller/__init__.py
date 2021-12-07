from . import gps_controller
from . import serial_controller
import logging
import sys

LOGGER = logging.getLogger(__name__)


GPS_TYPE_SERIAL='serial'

def create_gps_controller(gps_type):
    try:
        controller = None
        if gps_type == 'serial':
            controller = serial_controller.SerialGPSController()
        else:
            controller = gps_controller.GpsController()
    except OSError as err:
        LOGGER.error("OS error: {0}".format(err))
    except ValueError:
        LOGGER.error("Could not convert data to an integer.")
    except:
        LOGGER.error("Unexpected error:", sys.exc_info()[0])
    finally:
        return controller