import unittest

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        lowest, max_profit = float('inf'), 0

        for p in prices:
            if p < lowest:
                lowest = p
            profit = p - lowest
            if max_profit < profit:
                max_profit = profit
        return max_profit

        
        
class TestSolution(unittest.TestCase):
    def test1(self):
        sol = Solution()
        self.assertEqual(sol.maxProfit([7,1,5,3,6,4]), 5)

    def test2(self):
        sol = Solution()
        self.assertEqual(sol.maxProfit([7,6,4,3,1]), 0)

if __name__ == '__main__':
    unittest.main()