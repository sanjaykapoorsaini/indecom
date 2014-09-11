import unittest
import csv

class TestSequenceFunctions(unittest.TestCase):
    '''Unit test for testing the code with sample data'''
    
    def setUp(self):    
        '''Sample data'''
        self.sample_data = {'COMPANY A':'1', 'COMPANY B':'2', 'COMPANY C':'3', 'COMPANY N':'50'}
    
    def testTypeDictionary(self):
        # test each row of the csv file is a Dictionary
        csv_path = "D:/Desktop/data_file.csv"
        with open(csv_path, 'rb') as csvfile: 
            reader = csv.DictReader(csvfile, delimiter=',')
            for row in reader: 
                self.assertTrue(str(type(row).__name__) == 'dict')   

    def test_maxValue(self):
        # make sure the output value should be highest
        higest_share_price = max(map(int, self.sample_data.values()))
        self.assertTrue(higest_share_price == 50) 
   
    def test_keyWithHighestValue(self):
        # test to get the key of the Dictionary which have highest value
        list = []
        higest_share_price = max(map(int, self.sample_data.values()))
        [list.append(key) for key in self.sample_data if int(self.sample_data[key]) == higest_share_price]
        self.assertTrue(list[0] == 'COMPANY N') 

if __name__ == '__main__':
    unittest.main()
