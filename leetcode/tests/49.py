import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from _49_group_anagrams import Solution

class TestSolution(unittest.TestCase):
    def test1(self):
        sol = Solution()
        self.assertEqual(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]), [["eat","tea","ate"],["tan","nat"],["bat"]])
    
    def test2(self):
        sol = Solution()
        self.assertEqual(sol.groupAnagrams([""]), [[""]])

    def test3(self):
        sol = Solution()
        self.assertEqual(sol.groupAnagrams(["a"]), [["a"]])

if __name__ == '__main__':
    unittest.main()