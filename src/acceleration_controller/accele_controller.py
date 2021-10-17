from abc import ABCMeta,abstractmethod

class AcceleError(Exception):
    pass

class AcceleController(metaClass = ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def get_accele_data(self):
        pass

    @abstractmethod
    def check_vaital(self):
        raise AcceleError('')

