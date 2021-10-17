import unittest
from src import senser_data
from dataclasses import dataclass, field, asdict
import datetime


class TestCase(unittest.TestCase):
    """test class of tashizan.py
    """
    def setUp(self):
        pass


    def test_case1(self):
        data = senser_data.SenserData(datetime.datetime.now())

        diclist = []
        diclist.append(data.get_dict())
        print(diclist)


               


if __name__ == "__main__":
    unittest.main()