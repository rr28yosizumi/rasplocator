import time
from . import senser_data
from . import gps_controller
from . import acceleration_controller
from . import geo_helper

INTERBAL_DISTANCE = 0.0
INTERBAL_TIME= 0.1

class NOtLocatorSetupError(Exception):
    # セットアップができていない
    pass

class Locator():
    def __init__(self):
        self.setup()


    def setup(self):

        self._is_setup = False
        self._gps = gps_controller.create_gps_controller(gps_controller.GPS_TYPE_SERIAL)
        self._accel = acceleration_controller.create_accele_controller(acceleration_controller.ACCELE_TYPE_MPU9250)

        if self._gps == None or self._accel == None :
            return False

        self._is_setup = True
        return True

    def check_vital(self):
        if not self._is_setup :
            raise NOtLocatorSetupError('')
        self._gps.check_vaital()
        self._accel.check_vaital()


    def logging(self):

        self.check_vital()
        gps_data = self._gps.get_gps_data()
        lastpos = (gps_data[0],gps_data[1])

        while True:
            starttime = time.time()
            self.check_vital()

            gps_data = self._gps.get_gps_data()
            accele_data = self._accel.get_accele_data()
            distance = geo_helper.cal_distance(lastpos,(gps_data[0],gps_data[1]))

            if distance >= INTERBAL_DISTANCE:
                data = senser_data.SenserData()
                data.set_gps_data(*gps_data)
                data.set_accele_data(*accele_data)
                yield data
                lastpos = (gps_data[0],gps_data[1])

            # 一定時間が立っていたらスリープ時間を変更するといった工夫が必要
            endtime = time.time()
            if INTERBAL_DISTANCE > endtime - starttime :
                time.sleep(INTERBAL_TIME - (endtime - starttime))
    
    

