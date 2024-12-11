from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    # Enqueue an element into the queue
    def enqueue(self, data):
        self.queue.append(data)

    # Dequeue an element from the queue
    def dequeue(self):
        if not self.is_empty():
            return self.queue.popleft()
        else:
            print("Queue is empty! Cannot dequeue.")
            return None

    # Peek at the front element of the queue
    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            print("Queue is empty! Nothing to peek.")
            return None

    # Check if the queue is empty
    def is_empty(self):
        return len(self.queue) == 0

    # Get the size of the queue
    def size(self):
        return len(self.queue)

    # Print the queue
    def print_queue(self):
        print("Queue (front to back):", list(self.queue))

# Example Usage
if __name__ == "__main__":
    queue = Queue()

    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.print_queue()

    print("Dequeued element:", queue.dequeue())
    queue.print_queue()

    print("Front element:", queue.peek())
    print("Queue size:", queue.size())

    queue.dequeue()
    queue.dequeue()
    queue.dequeue()  # Attempt to dequeue from an empty queue