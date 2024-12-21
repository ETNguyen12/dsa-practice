import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from _217_contains_duplicate import Solution

class TestSolution(unittest.TestCase):
    def test1(self):
        sol = Solution()
        self.assertEqual(sol.containsDuplicate([1,2,3,1]), True)

    def test2(self):
        sol = Solution()
        self.assertEqual(sol.containsDuplicate([1,2,3,4]), False)

    def test3(self):
        sol = Solution()
        self.assertEqual(sol.containsDuplicate([1,1,1,3,3,4,3,2,4,2]), True)

if __name__ == '__main__':
    unittest.main()