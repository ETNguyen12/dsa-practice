import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from _206_reverse_linked_list import Solution

class ListNode:
    def __init__(self, x=0, next=None):
        self.val = x
        self.next = next

def to_linked_list(nums): 
    temp = current = ListNode()
    for num in nums:
        current.next = ListNode(num)
        current = current.next
    return temp.next

def to_list(head):
    ls = []
    while head:
        ls.append(head.val)
        head = head.next
    return ls

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