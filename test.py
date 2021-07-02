import unittest
from badStyle import dec, add


class TestBadStyle(unittest.TestCase):
    def test_dec(self):
        self.assertEqual(dec(1), 0)
        self.assertEqual(dec(0), -1)
        self.assertEqual(dec(2.1), 1.1)
    
    def test_add(self):
        self.assertEqual(add(2,1), 3)
        self.assertEqual(add(2.1, 1.2), 3.3)
    
    
if __name__ == '__main__':
    unittest.main()