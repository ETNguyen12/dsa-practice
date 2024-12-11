class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at the beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node

    # Insert at the end
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    # Delete a node by value
    def delete_by_value(self, value):
        if not self.head:
            return
        temp = self.head
        while temp and temp.data != value:
            temp = temp.next
        if temp:
            if temp.prev:
                temp.prev.next = temp.next
            if temp.next:
                temp.next.prev = temp.prev
            if temp == self.head:
                self.head = temp.next

    # Print the linked list
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")

# Example Usage
if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.insert_at_beginning(3)
    dll.insert_at_beginning(2)
    dll.insert_at_beginning(1)
    dll.print_list()

    dll.insert_at_end(4)
    dll.insert_at_end(5)
    dll.print_list()

    dll.delete_by_value(3)
    dll.print_list()