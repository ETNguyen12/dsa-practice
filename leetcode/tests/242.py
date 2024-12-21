import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from _242_valid_anagram import Solution

class TestSolution(unittest.TestCase):
    def test1(self):
        sol = Solution()
        self.assertEqual(sol.isAnagram("anagram", "nagaram"), True)
    
    def test2(self):
        sol = Solution()
        self.assertEqual(sol.isAnagram("rat", "car"), False)
    
if __name__ == '__main__':
    unittest.main()