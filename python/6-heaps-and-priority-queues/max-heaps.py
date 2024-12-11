import heapq

class MaxHeap:
    def __init__(self):
        self.heap = []

    # Insert an element into the max-heap
    def insert(self, value):
        # Negate the value to simulate a max-heap using heapq (which is a min-heap)
        heapq.heappush(self.heap, -value)

    # Remove and return the largest element
    def extract_max(self):
        if not self.is_empty():
            return -heapq.heappop(self.heap)
        else:
            print("Heap is empty! Cannot extract.")
            return None

    # Get the largest element without removing it
    def get_max(self):
        if not self.is_empty():
            return -self.heap[0]
        else:
            print("Heap is empty! Nothing to get.")
            return None

    # Check if the heap is empty
    def is_empty(self):
        return len(self.heap) == 0

    # Print the max-heap
    def print_heap(self):
        # Convert negated values back to positive for display
        print("Max-Heap:", [-value for value in self.heap])

# Example Usage
if __name__ == "__main__":
    max_heap = MaxHeap()
    elements = [20, 15, 30, 10, 25, 5]

    for elem in elements:
        print(f"Inserting {elem} into the max-heap.")
        max_heap.insert(elem)
        max_heap.print_heap()

    print("Maximum element:", max_heap.get_max())

    print("Extracting elements from the max-heap:")
    while not max_heap.is_empty():
        print(max_heap.extract_max())
        max_heap.print_heap()