class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    # Insert at the beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = new_node
        new_node.next = self.head
        self.head = new_node

    # Insert at the end
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = new_node
        new_node.next = self.head

    # Delete a node by value
    def delete_by_value(self, value):
        if not self.head:
            return
        if self.head.data == value and self.head.next == self.head:
            self.head = None
            return
        temp = self.head
        prev = None
        while temp.data != value:
            prev = temp
            temp = temp.next
            if temp == self.head:
                return
        if temp == self.head:
            prev = self.head
            while prev.next != self.head:
                prev = prev.next
            self.head = self.head.next
            prev.next = self.head
        else:
            prev.next = temp.next

    # Print the linked list
    def print_list(self):
        if not self.head:
            print("List is empty")
            return
        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(head)")

# Example Usage
if __name__ == "__main__":
    cll = CircularLinkedList()
    cll.insert_at_beginning(3)
    cll.insert_at_beginning(2)
    cll.insert_at_beginning(1)
    cll.print_list()

    cll.insert_at_end(4)
    cll.insert_at_end(5)
    cll.print_list()

    cll.delete_by_value(3)
    cll.print_list()