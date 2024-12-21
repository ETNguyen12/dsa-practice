import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from _1_two_sum import Solution

class TestSolution(unittest.TestCase):
    def test1(self):
        sol = Solution()
        self.assertEqual(sol.twoSum([2, 7, 11, 15], 9), [0, 1])

    def test2(self):
        sol = Solution()
        self.assertEqual(sol.twoSum([3, 2, 4], 6), [1, 2])

    def test3(self):
        sol = Solution()
        self.assertEqual(sol.twoSum([3, 3], 6), [0, 1])

if __name__ == '__main__':
    unittest.main()