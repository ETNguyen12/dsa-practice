import heapq

class MinHeap:
    def __init__(self):
        self.heap = []

    # Insert an element into the heap
    def insert(self, value):
        heapq.heappush(self.heap, value)

    # Remove and return the smallest element
    def extract_min(self):
        if not self.is_empty():
            return heapq.heappop(self.heap)
        else:
            print("Heap is empty! Cannot extract.")
            return None

    # Get the smallest element without removing it
    def get_min(self):
        if not self.is_empty():
            return self.heap[0]
        else:
            print("Heap is empty! Nothing to get.")
            return None

    # Check if the heap is empty
    def is_empty(self):
        return len(self.heap) == 0

    # Print the heap
    def print_heap(self):
        print("Heap:", self.heap)

# Example Usage
if __name__ == "__main__":
    min_heap = MinHeap()
    elements = [20, 15, 30, 10, 25, 5]

    for elem in elements:
        print(f"Inserting {elem} into the heap.")
        min_heap.insert(elem)
        min_heap.print_heap()

    print("Minimum element:", min_heap.get_min())

    print("Extracting elements from the heap:")
    while not min_heap.is_empty():
        print(min_heap.extract_min())
        min_heap.print_heap()