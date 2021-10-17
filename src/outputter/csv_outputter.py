from dataclasses import dataclass, field, asdict
from . import outputter
import csv
import os

DEFAULT_LIMIT = 1000

class CsvOutputter(outputter.OutPut):
    def __init__(self,filepath):
        self._path = filepath
        self._data_list = []
        self._limit = DEFAULT_LIMIT

    def put_data(self,data):
        self._data_list.append(data.get_dict())

        if len(self._data_list) >= self._limit :
            self.save(self._data_list)
            self._data_list = []
    
    def finish(self):
        if len(self._data_list) != 0:
            self.save(self._data_list)
            self._datalist = []

    def save(self,data_list):
        
        if os.path.isfile(self._path) :
            openmode = 'a'
        else:
            openmode = 'w'

        with open(self._path,mode = openmode,newline="") as f:
            writer = csv.DictWriter(f,data_list[0].keys())
            if openmode == 'w':
                writer.writeheader()
            writer.writerows(data_list)
        