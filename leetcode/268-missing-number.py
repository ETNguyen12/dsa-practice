import unittest

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashset = set(range(len(nums) + 1))
        for num in nums:
            hashset.discard(num)
        return hashset.pop()



class TestSolution(unittest.TestCase):
    def test1(self):
        sol = Solution()
        self.assertEqual(sol.missingNumber([3, 0, 1]), 2)
    
    def test2(self):
        sol = Solution()
        self.assertEqual(sol.missingNumber([0, 1]), 2)

    def test3(self):
        sol = Solution()
        self.assertEqual(sol.missingNumber([9,6,4,2,3,5,7,0,1]), 8)

if __name__ == '__main__':
    unittest.main()