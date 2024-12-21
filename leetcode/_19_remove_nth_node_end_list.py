class ListNode:
    def __init__(self, x = 0, nxt = None):
        self.val = x
        self.next = nxt

class Solution:
    def removeNthFromEnd(self, head, n):
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        nums.pop(len(nums) - n)

        temp = current = ListNode()
        for num in nums:
            current.next = ListNode(num)
            current = current.next
        return temp.next
