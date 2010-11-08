import unittest
import worldbank

class TestWorldBank(unittest.TestCase):
    def setUp(self):
        self.wb = worldbank.WorldBank()
        
    def test_get_country(self):
        data = self.wb.get_country(code='all')
        
        #checks that there are between 200 and 1000 countries (sanity check)
        self.assertTrue(data[0]['total'] > 200 and data[0]['total'] < 1000)
        
        self.assertEqual(data[0]['per_page'], str(self.wb.per_page))
        
    def test_get_indicators(self):
        data = self.wb.get_indicators(code='NY.GDP.MKTP.CD')
        self.assertEqual(data[1][0]['id'], 'NY.GDP.MKTP.CD')
        
if __name__ == '__main__':
    unittest.main()