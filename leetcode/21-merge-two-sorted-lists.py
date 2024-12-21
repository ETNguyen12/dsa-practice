import unittest

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        temp = current = ListNode()

        while list1 != None and list2 != None:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        current.next = list1 or list2
        return temp.next
        


def to_linked_list(list):
    temp = current = ListNode()
    for item in list:
        current.next = ListNode(item)
        current = current.next
    return temp.next

def to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

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