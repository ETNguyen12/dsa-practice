import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from _121_best_time_stock import Solution

class TestSolution(unittest.TestCase):
    def test1(self):
        sol = Solution()
        self.assertEqual(sol.maxProfit([7,1,5,3,6,4]), 5)

    def test2(self):
        sol = Solution()
        self.assertEqual(sol.maxProfit([7,6,4,3,1]), 0)

if __name__ == '__main__':
    unittest.main()