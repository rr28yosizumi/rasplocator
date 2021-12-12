from abc import ABCMeta,abstractmethod

class Co2senserError(Exception):
    pass

class Co2senserController(metaclass = ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def get_co2_data(self):
        pass

    @abstractmethod
    def check_vaital(self):
        raise Co2senserError('')
