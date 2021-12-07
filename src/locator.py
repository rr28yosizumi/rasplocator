import time
from . import senser_data
from . import gps_controller
from . import acceleration_controller
from . import geo_helper

INTERVAL_DISTANCE = 0.0
INTERVAL_TIME= 0.1

class NotLocatorSetupError(Exception):
    # セットアップができていない
    pass

class Locator():
    def __init__(self):
        self.setup()


    def setup(self):

        self._is_setup = False
        self._gps = gps_controller.create_gps_controller(gps_controller.GPS_TYPE_SERIAL)
        self._accel = acceleration_controller.create_accele_controller(acceleration_controller.ACCELE_TYPE_MPU9250)
        self._is_setup = True
        return True

    def check_vital(self):
        if not self._is_setup :
            raise NotLocatorSetupError('')

        if self._gps is not None:
            self._gps.check_vaital()
        else:
            raise NotLocatorSetupError('')
        
        if self._accel is not None:
            self._accel.check_vaital()
        else:
            raise NotLocatorSetupError('')


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

            if distance >= INTERVAL_DISTANCE:
                data = senser_data.SenserData()
                data.set_gps_data(*gps_data)
                data.set_accele_data(*accele_data)
                yield data
                lastpos = (gps_data[0],gps_data[1])

            # 一定時間が立っていたらスリープ時間を変更するといった工夫が必要
            endtime = time.time()
            if INTERVAL_DISTANCE > endtime - starttime :
                time.sleep(INTERVAL_TIME - (endtime - starttime))
    
class Distance_Locator(Locator):

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

            if distance >= INTERVAL_DISTANCE:
                data = senser_data.SenserData()
                data.set_gps_data(*gps_data)
                data.set_accele_data(*accele_data)
                yield data
                lastpos = (gps_data[0],gps_data[1])

            # 一定時間が立っていたらスリープ時間を変更するといった工夫が必要
            endtime = time.time()
            if INTERVAL_DISTANCE > endtime - starttime :
                time.sleep(INTERVAL_TIME - (endtime - starttime))

class Timeinterval_Locator(Locator):

    def check_vital(self):
        if not self._is_setup :
            raise NotLocatorSetupError('')

    def logging(self):
        while True:
            starttime = time.time()
            self.check_vital()
            data = senser_data.SenserData()

            if self._gps is not None:
                gps_data = self._gps.get_gps_data()
                data.set_gps_data(*gps_data)

            if self._accel is not None:
                accele_data = self._accel.get_accele_data()
                data.set_accele_data(*accele_data)
                
            yield data

            # 一定時間が立っていたらスリープ時間を変更するといった工夫が必要
            endtime = time.time()
            time.sleep(INTERVAL_TIME - (endtime - starttime))
            
