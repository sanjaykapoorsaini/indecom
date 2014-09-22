import csv

class TestCaseClass:
    """class for all the test cases which needs to be verified"""

    def __init__(self):
        # Sample Data
        self.sample_data = {'COMPANY A':'1', 'COMPANY B':'2', 'COMPANY C':'3', 'COMPANY N':'50'}  
		
    def test_TypeDictionary(self):
		# test each row of the csv file is a Dictionary
		csv_path = "/data_file.csv"
		with open(csv_path, 'rb') as csvfile: 
			reader = csv.DictReader(csvfile, delimiter=',')
			for row in reader: 
			    return str(type(row).__name__)
				
    def test_maxValue(self):
        # make sure the output value should be highest
        higest_share_price = max(map(int, self.sample_data.values()))
        return higest_share_price
   
    def test_keyWithHighestValue(self):
        # test to get the key of the Dictionary which have highest value
        list = []
        higest_share_price = max(map(int, self.sample_data.values()))
        [list.append(key) for key in self.sample_data if int(self.sample_data[key]) == higest_share_price]
        return list[0]
		

import unittest
class TestSequenceFunctions(unittest.TestCase):
    '''Unit test for testing the code with sample data'''
    
    def setUp(self):    
        '''Created the class object'''
        self.test = TestCaseClass()
	
    def test_functional(self):
	    '''Test the cases by changing the sample data and output'''
		
        self.assertEqual(self.test.test_TypeDictionary(), 'dict')
        self.assertEqual(self.test.test_maxValue(), 50)
        self.assertEqual(self.test.test_keyWithHighestValue(), 'COMPANY N')

if __name__ == '__main__':
    unittest.main()
