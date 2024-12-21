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