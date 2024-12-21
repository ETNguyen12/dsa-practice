import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from _268_missing_number import Solution

class TestSolution(unittest.TestCase):
    def test1(self):
        sol = Solution()
        self.assertEqual(sol.missingNumber([3, 0, 1]), 2)
    
    def test2(self):
        sol = Solution()
        self.assertEqual(sol.missingNumber([0, 1]), 2)

    def test3(self):
        sol = Solution()
        self.assertEqual(sol.missingNumber([9,6,4,2,3,5,7,0,1]), 8)

if __name__ == '__main__':
    unittest.main()