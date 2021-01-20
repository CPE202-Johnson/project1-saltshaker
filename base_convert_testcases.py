import unittest
from  base_convert import *

class TestBaseConvert(unittest.TestCase):

    def test_base2(self):
        self.assertEqual(convert(45,2),"101101")
        
    def test_base3(self):
        self.assertEqual(convert(100,3),"10201")

    def test_base4(self):
        self.assertEqual(convert(30,4),"132")
        
    def test_base5(self):
        self.assertEqual(convert(4,5),"4")

    def test_base12(self):
        self.assertEqual(convert(263,12),"19B")

    def test_base15(self):
        self.assertEqual(convert(850,15),"3BA")

    def test_base16(self):
        self.assertEqual(convert(316,16),"13C")

if __name__ == "__main__":
        unittest.main()