import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from _125_valid_palindrome import Solution

class TestSolution(unittest.TestCase):
    def test1(self):
        sol = Solution()
        self.assertEqual(sol.isPalindrome("A man, a plan, a canal: Panama"), True)
    
    def test2(self):
        sol = Solution()
        self.assertEqual(sol.isPalindrome("race a car"), False)
    
    def test3(self):
        sol = Solution()
        self.assertEqual(sol.isPalindrome(" "), True)

    def test4(self):
        sol = Solution()
        self.assertEqual(sol.isPalindrome("0P"), False)

if __name__ == '__main__':
    unittest.main()