class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyCircularLinkedList:
    def __init__(self):
        self.head = None

    # Insert at the beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
            return
        tail = self.head.prev
        new_node.next = self.head
        new_node.prev = tail
        tail.next = new_node
        self.head.prev = new_node
        self.head = new_node

    # Insert at the end
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
            return
        tail = self.head.prev
        new_node.next = self.head
        new_node.prev = tail
        tail.next = new_node
        self.head.prev = new_node

    # Delete a node by value
    def delete_by_value(self, value):
        if not self.head:
            return
        temp = self.head
        while temp.data != value:
            temp = temp.next
            if temp == self.head:
                return  # Value not found
        if temp.next == temp:  # Only one node
            self.head = None
            return
        temp.prev.next = temp.next
        temp.next.prev = temp.prev
        if temp == self.head:
            self.head = temp.next

    # Print the linked list
    def print_list(self):
        if not self.head:
            print("List is empty")
            return
        temp = self.head
        while True:
            print(temp.data, end=" <-> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(head)")

# Example Usage
if __name__ == "__main__":
    dcll = DoublyCircularLinkedList()
    dcll.insert_at_beginning(3)
    dcll.insert_at_beginning(2)
    dcll.insert_at_beginning(1)
    dcll.print_list()

    dcll.insert_at_end(4)
    dcll.insert_at_end(5)
    dcll.print_list()

    dcll.delete_by_value(3)
    dcll.print_list()