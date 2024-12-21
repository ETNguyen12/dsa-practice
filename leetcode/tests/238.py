import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from _238_product_array_except_self import Solution
    
class TestSolution(unittest.TestCase):
    def test1(self):
        sol = Solution()
        self.assertEqual(sol.productExceptSelf([1,2,3,4]), [24,12,8,6])

    def test2(self):
        sol = Solution()
        self.assertEqual(sol.productExceptSelf([-1,1,0,-3,3]), [0,0,9,0,0])

if __name__ == '__main__':
    unittest.main()