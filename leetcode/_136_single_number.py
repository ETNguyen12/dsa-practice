class Solution:
    def singleNumber(self, nums):
        hashset = set()
        for num in nums:
            if num in hashset:
                hashset.remove(num)
            else:
                hashset.add(num)
        return hashset.pop()