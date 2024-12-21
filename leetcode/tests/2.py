import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from _2_add_two_numbers import Solution

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
       self.assertEqual(to_list(sol.addTwoNumbers(to_linked_list([2,4,3]), to_linked_list([5,6,4]))), [7,0,8])

    def test2(self):
        sol = Solution()
        self.assertEqual(to_list(sol.addTwoNumbers(to_linked_list([0]), to_linked_list([0]))), [0])

    def test3(self):
        sol = Solution()
        self.assertEqual(to_list(sol.addTwoNumbers(to_linked_list([9,9,9,9,9,9,9]), to_linked_list([9,9,9,9]))), [8,9,9,9,0,0,0,1])

if __name__ == '__main__':
    unittest.main()