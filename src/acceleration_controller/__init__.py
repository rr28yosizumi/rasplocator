from . import accele_controller
from . import MPU9250_controller
import sys

import logging

LOGGER = logging.getLogger(__name__)

ACCELE_TYPE_MPU9250 = 'MPU9250'

def create_accele_controller(type = ''):
    try:
        controller = None
        if type == 'MPU9250':
            controller = MPU9250_controller.MPU9250Controller()
        else:
            controller = accele_controller.AcceleController()
    except OSError as err:
        LOGGER.error("OS error: {0}".format(err))
    except ValueError:
        LOGGER.error("Could not convert data to an integer.")
    except:
        LOGGER.error("Unexpected error:", sys.exc_info()[0])
    finally:
        return controller