import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from _136_single_number import Solution

class TestSolution(unittest.TestCase):
    def test1(self):
        sol = Solution()
        self.assertEqual(sol.singleNumber([2,2,1]), 1)

    def test2(self):
        sol = Solution()
        self.assertEqual(sol.singleNumber([4,1,2,1,2]), 4)

    def test3(self):
        sol = Solution()
        self.assertEqual(sol.singleNumber([1]), 1)

if __name__ == '__main__':
    unittest.main()