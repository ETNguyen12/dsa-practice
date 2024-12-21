import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from _21_merge_two_sorted_lists import Solution

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

class SolutionTest(unittest.TestCase):
    def test1(self):
        sol = Solution()
        self.assertEqual(to_list(sol.mergeTwoLists(to_linked_list([1, 2, 4]), to_linked_list([1, 3, 4]))), [1,1,2,3,4,4])

    def test2(self):
        sol = Solution()
        self.assertEqual(to_list(sol.mergeTwoLists(to_linked_list([]), to_linked_list([]))), [])

    def test3(self):
        sol = Solution()
        self.assertEqual(to_list(sol.mergeTwoLists(to_linked_list([]), to_linked_list([0]))), [0])

if __name__ == '__main__':
    unittest.main()