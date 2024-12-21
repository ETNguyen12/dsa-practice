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