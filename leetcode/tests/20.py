import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from _20_valid_parentheses import Solution

class TestSolution(unittest.TestCase):
    def test1(self):
        sol = Solution()
        self.assertEqual(sol.isValid("()"), True)

    def test2(self):
        sol = Solution()
        self.assertEqual(sol.isValid("()[]{}"), True)

    def test3(self):
        sol = Solution()
        self.assertEqual(sol.isValid("(]"), False)

    def test4(self):
        sol = Solution()
        self.assertEqual(sol.isValid("([])"), True)

if __name__ == '__main__':
    unittest.main()