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