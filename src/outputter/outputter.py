from abc import ABCMeta,abstractmethod

class OutPut(metaclass = ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def put_data(self,data):
        pass

    @abstractmethod
    def finish(self):
        pass

    
