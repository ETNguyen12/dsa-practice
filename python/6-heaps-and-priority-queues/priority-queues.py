import heapq

class PriorityQueue:
    def __init__(self):
        self.heap = []

    # Insert an element with priority into the priority queue
    def enqueue(self, priority, value):
        # Use (priority, value) tuples to store items in the heap
        heapq.heappush(self.heap, (priority, value))

    # Remove and return the element with the highest priority (lowest priority number)
    def dequeue(self):
        if not self.is_empty():
            return heapq.heappop(self.heap)[1]
        else:
            print("Priority Queue is empty! Cannot dequeue.")
            return None

    # Peek at the element with the highest priority
    def peek(self):
        if not self.is_empty():
            return self.heap[0][1]
        else:
            print("Priority Queue is empty! Nothing to peek.")
            return None

    # Check if the priority queue is empty
    def is_empty(self):
        return len(self.heap) == 0

    # Print the priority queue
    def print_queue(self):
        print("Priority Queue:", [(priority, value) for priority, value in self.heap])

# Example Usage
if __name__ == "__main__":
    # Initialize the priority queue
    pq = PriorityQueue()

    # Adding elements with varying priorities
    pq.enqueue(3, "Low Priority Task")
    pq.enqueue(1, "High Priority Task")
    pq.enqueue(2, "Medium Priority Task")

    # Peek at the highest priority task
    print("Peek at highest priority task:", pq.peek())

    # Display the entire priority queue
    pq.print_queue()

    # Process tasks based on priority
    print("Processing tasks in order of priority:")
    while not pq.is_empty():
        task = pq.dequeue()
        print(f"Processing: {task}")

    # Adding and removing more tasks
    pq.enqueue(0, "Critical Task")
    pq.enqueue(5, "Very Low Priority Task")
    pq.print_queue()

    print("Processing remaining tasks:")
    while not pq.is_empty():
        task = pq.dequeue()
        print(f"Processing: {task}")