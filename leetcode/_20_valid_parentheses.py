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