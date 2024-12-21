import unittest

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = ''.join(c.lower() for c in s if c.isalpha() or c.isdigit())
            
        return s == s[::-1]
        


class TestSolution(unittest.TestCase):
    def test1(self):
        sol = Solution()
        self.assertEqual(sol.isPalindrome("A man, a plan, a canal: Panama"), True)
    
    def test2(self):
        sol = Solution()
        self.assertEqual(sol.isPalindrome("race a car"), False)
    
    def test3(self):
        sol = Solution()
        self.assertEqual(sol.isPalindrome(" "), True)

    def test4(self):
        sol = Solution()
        self.assertEqual(sol.isPalindrome("0P"), False)

if __name__ == '__main__':
    unittest.main()