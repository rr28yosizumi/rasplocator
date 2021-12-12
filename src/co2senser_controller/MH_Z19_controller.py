from . import co2senser_controller
import mh_z19


class MH_Z19Controller(co2senser_controller.Co2senserController):
    
    def __init__(self):
        self._mh_z19 = None


    def check_vaital(self):
        pass

    def get_co2_data(self):
        data =  mh_z19.read_all()
        if 'co2' not in data.keys() :
            data['co2']=0.0
        
        if 'temperature' not in data.keys():
            data['temperature'] = -274

        return {
            'co2':data['co2'],
            'temp':data['temperature']
        }
