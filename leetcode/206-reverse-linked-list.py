import unittest

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        
        temp = current = ListNode()
        for num in nums[::-1]:
            current.next = ListNode(num)
            current = current.next
        
        return temp.next
    
def to_linked_list(nums):    
    temp = current = ListNode()
    for num in nums:
        current.next = ListNode(num)
        current = current.next
    return temp.next
        
def to_list(node):
    nums = []
    while node:
        nums.append(node.val)
        node = node.next
    return nums

class TestSolution(unittest.TestCase):
    def test1(self):
        sol = Solution()
        self.assertEqual(to_list(sol.reverseList(to_linked_list([1,2,3,4,5]))), [5,4,3,2,1])

    def test2(self):
        sol = Solution()
        self.assertEqual(to_list(sol.reverseList(to_linked_list([1,2]))), [2,1])

    def test3(self):
        sol = Solution()
        self.assertEqual(to_list(sol.reverseList(to_linked_list([]))), [])

if __name__ == '__main__':
    unittest.main()