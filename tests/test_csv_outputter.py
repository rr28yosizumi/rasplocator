import unittest
from datetime import datetime
import csv
import os

from src.outputter import csv_outputter
from src import senser_data

    
def write_test(testclass,testfile_path,testlimit):
    csvoutput = csv_outputter.CsvOutputter(testfile_path)
    testlist  = (
        senser_data.SenserData(datetime.now())
        for _ in range(testlimit)
    )
    for i in testlist:
        csvoutput.put_data(i)
    csvoutput.finish()

    testclass.assertTrue(os.path.isfile(testfile_path))

    with open(testfile_path) as f:
        reader = csv.DictReader(f)
        rlist = [row for row in reader]

    testclass.assertEqual(len(rlist),testlimit)

    os.remove(testfile_path)

class TestCaseCsvOutput(unittest.TestCase):
    def setUp(self) -> None:
        self.test_filepath = 'test.csv'
        return super().setUp()

    def tearDown(self) -> None:
        if os.path.isfile(self.test_filepath):
            os.remove(self.test_filepath)
        return super().tearDown()

    def test_case1(self):
        
        testlimit = 1000
        write_test(self,self.test_filepath,testlimit)

        testlimit = 2000
        write_test(self,self.test_filepath,testlimit)

        testlimit = 2500
        write_test(self,self.test_filepath,testlimit)

        
