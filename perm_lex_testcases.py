import unittest
from perm_lex import *

class TestAssign1(unittest.TestCase):

    # Tests input with two letters
    def test_perm_gen_lex1(self):
        self.assertEqual(perm_gen_lex('ab'),['ab','ba'])
        
    # Tests for blank input
    def test_perm_gen_lex2(self):
        self.assertEqual(perm_gen_lex(''),[])
        
    # Tests for input with three letters
    def test_perm_gen_lex3(self):
        self.assertEqual(perm_gen_lex('abc'),['abc','acb','bac','bca','cab','cba'])

if __name__ == "__main__":
        unittest.main()
