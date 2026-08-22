class ListNode:
    def __init__(self, value: int) -> None:
        self.val = value
        self.next = None

class LinkedList:
    def __init__(self, value: int) -> None:
        node = ListNode(value)
        self.head = node
        self.tail = node
        self.length = 1

    def __repr__(self) -> str:
        nodes = []
        curr = self.head
        while curr:
            nodes.append(f'[{str(curr.val)}]')
            curr = curr.next
        return ' -> '.join(nodes)

    def append(self, value: int) -> None:
        new_node = ListNode(value)
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1

    def prepend(self, value: int) -> None:
        new_node = ListNode(value)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def insert(self, index: int, value: int) -> bool:
        if index > self.length:
            return False

        curr = self.head
        prev = None
        i = 0
        while i != index and curr:
            prev = curr
            i += 1
            curr = curr.next

        new_node = ListNode(value)
        if curr is self.head:
            new_node.next = self.head
            self.head = new_node
        elif curr is None:
            self.tail.next = new_node
            self.tail = new_node
        else:
            prev.next = new_node
            new_node.next = curr
        self.length += 1
        return True

if __name__ == '__main__':
    ll = LinkedList(2)
    ll.append(4)
    ll.prepend(1)
    ll.insert(0, 0)
    ll.insert(3, 3)
    ll.insert(ll.length, 5)
    print(ll)