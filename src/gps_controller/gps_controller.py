from abc import ABCMeta,abstractmethod
class GpsError(Exception):
    pass

class GpsController(metaclass = ABCMeta):
    def __init__(self):
        pass
    
    @abstractmethod
    def get_gps_data(self):
        return None
    
    @abstractmethod
    def is_enable_gps(self):
        return False
        
    @abstractmethod
    def check_vaital(self):
        raise GpsError('')