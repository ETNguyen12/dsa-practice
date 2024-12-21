import unittest

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        for c in s:
            if c in mapping:
                popped = stack.pop() if stack else ' '
                if mapping[c] != popped:
                    return False
            else:
                stack.append(c)
        return not stack
            
        

class TestSolution(unittest.TestCase):
    def test1(self):
        sol = Solution()
        self.assertEqual(sol.isValid("()"), True)

    def test2(self):
        sol = Solution()
        self.assertEqual(sol.isValid("()[]{}"), True)

    def test3(self):
        sol = Solution()
        self.assertEqual(sol.isValid("(]"), False)

    def test4(self):
        sol = Solution()
        self.assertEqual(sol.isValid("([])"), True)

if __name__ == '__main__':
    unittest.main()