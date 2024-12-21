class Node:
    def __init__(self, x, nxt = None, random = None):
        self.val = x
        self.next = nxt
        self.random = random

class Solution:
    def __init__(self):
        self.hashmap = {}

    def copyRandomList(self, head):
        if not head:
            return None
        if head in self.hashmap:
            return self.hashmap[head]

        copy = Node(head.val)
        self.hashmap[head] = copy
        copy.next = self.copyRandomList(head.next)
        copy.random = self.hashmap.get(head.random)
        return copy