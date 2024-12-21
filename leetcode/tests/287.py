import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from _287_find_duplicate_number import Solution
    
class TestSolution(unittest.TestCase):
    def test1(self):
        sol = Solution()
        self.assertEqual(sol.findDuplicate([1,3,4,2,2]), 2)

    def test2(self):
        sol = Solution()
        self.assertEqual(sol.findDuplicate([3,1,3,4,2]), 3)

    def test3(self):
        sol = Solution()
        self.assertEqual(sol.findDuplicate([3,3,3,3,3]), 3)

if __name__ == '__main__':
    unittest.main()