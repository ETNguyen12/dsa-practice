class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        hashset = set()

        while head:
            if head in hashset:
                return True
            hashset.add(head)
            head = head.next
        return False