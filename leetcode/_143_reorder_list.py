import unittest

class ListNode:
    def __init__(self, x=0):
        self.val = x
        self.next = None

class Solution:
    def reorderList(self, head):
        """
        Do not return anything, modify head in-place instead.
        """
        