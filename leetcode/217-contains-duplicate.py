import unittest

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hashset = set()
        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
        return False
    


class TestSolution(unittest.TestCase):
    def test1(self):
        sol = Solution()
        self.assertEqual(sol.containsDuplicate([1,2,3,1]), True)

    def test2(self):
        sol = Solution()
        self.assertEqual(sol.containsDuplicate([1,2,3,4]), False)

    def test3(self):
        sol = Solution()
        self.assertEqual(sol.containsDuplicate([1,1,1,3,3,4,3,2,4,2]), True)

if __name__ == '__main__':
    unittest.main()