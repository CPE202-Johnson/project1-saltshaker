import unittest
from bears import *

class TestAssign1(unittest.TestCase):
    def test_bear1(self):
        self.assertTrue(bears(250))

    def test_bear2(self):
        self.assertTrue(bears(42))

    def test_bear3(self):
        self.assertFalse(bears(53))

    def test_bear4(self):
        self.assertFalse(bears(41))
        
    def test_bear5(self):
        self.assertFalse(bears(300))
    
    def test_bear6(self):
        self.assertTrue(bears(210))
        
    def test_bear7(self):
        self.assertTrue(bears(5280))

if __name__ == "__main__":
    unittest.main()
