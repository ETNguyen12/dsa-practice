import unittest

class Solution():
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for i, num in enumerate(nums):
            if target - num in hashmap:
                return [hashmap[target - num], i]
            hashmap[num] = i



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