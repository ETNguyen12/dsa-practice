import unittest

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t): return False
        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        return countS == countT



class TestSolution(unittest.TestCase):
    def test1(self):
        sol = Solution()
        self.assertEqual(sol.isAnagram("anagram", "nagaram"), True)
    
    def test2(self):
        sol = Solution()
        self.assertEqual(sol.isAnagram("rat", "car"), False)
    
if __name__ == '__main__':
    unittest.main()