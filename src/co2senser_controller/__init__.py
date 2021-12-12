import sys
from . import co2senser_controller
from . import MH_Z19_controller

import logging

LOGGER = logging.getLogger(__name__)

MH_Z19 = 'MH_Z19'

def create_co2senser_controller(type = ''):
    try:
        controller = None
        if type == 'MH_Z19':
            controller = MH_Z19_controller.MH_Z19Controller()
        else:
            controller = co2senser_controller.Co2senserController()
    except OSError as err:
        LOGGER.error("OS error: {0}".format(err))
    except ValueError:
        LOGGER.error("Could not convert data to an integer.")
    except:
        LOGGER.error("Unexpected error:", sys.exc_info()[0])
    finally:
        return controller