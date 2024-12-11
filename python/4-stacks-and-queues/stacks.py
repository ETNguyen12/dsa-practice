class Stack:
    def __init__(self):
        self.stack = []

    # Push an element onto the stack
    def push(self, data):
        self.stack.append(data)

    # Pop an element from the stack
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            print("Stack is empty! Cannot pop.")
            return None

    # Peek at the top element of the stack
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            print("Stack is empty! Nothing to peek.")
            return None

    # Check if the stack is empty
    def is_empty(self):
        return len(self.stack) == 0

    # Get the size of the stack
    def size(self):
        return len(self.stack)

    # Print the stack
    def print_stack(self):
        print("Stack (top to bottom):", self.stack[::-1])

# Example Usage
if __name__ == "__main__":
    stack = Stack()

    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.print_stack()

    print("Popped element:", stack.pop())
    stack.print_stack()

    print("Top element:", stack.peek())
    print("Stack size:", stack.size())

    stack.pop()
    stack.pop()
    stack.pop()  # Attempt to pop from an empty stack