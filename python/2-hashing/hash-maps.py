# 1. Using Python Dictionaries as Hash Maps
hash_map = {}

# Adding key-value pairs
hash_map['name'] = 'Alice'
hash_map['age'] = 25
hash_map['city'] = 'New York'
print("Hash Map:", hash_map)

# Accessing values by key
print("Name:", hash_map['name'])

# Checking if a key exists
print("Is 'age' in hash_map?:", 'age' in hash_map)

# Removing a key-value pair
hash_map.pop('city')
print("After Removing 'city':", hash_map)

# Iterating through a hash map
for key, value in hash_map.items():
    print(f"{key}: {value}")

# 2. Hash Functions in Python
# Using Python's built-in hash function
key = "example"
hash_value = hash(key)
print(f"Hash Value for '{key}':", hash_value)

# Custom hashing function
# Hashing a tuple (immutable data structure)
data = ("Alice", 25, "New York")
hash_value = hash(data)
print(f"Hash Value for {data}: {hash_value}")

# 3. Handling Hash Collisions
# Demonstrating a simple hash collision
class SimpleHash:
    def __init__(self, value):
        self.value = value

    def __hash__(self):
        return len(self.value)  # Hash based on string length

    def __eq__(self, other):
        return self.value == other.value

obj1 = SimpleHash("cat")
obj2 = SimpleHash("dog")
hash_map = {}
hash_map[obj1] = "This is cat"
hash_map[obj2] = "This is dog"
print("Hash Map with Collisions:", hash_map)
print("Value for 'dog':", hash_map[obj2])

# 4. Applications of Hash Maps
# Counting character frequency using dictionaries
from collections import Counter
string = "abracadabra"
frequency = Counter(string)
print("Character Frequency:", frequency)

# Detecting duplicates in a list
nums = [1, 2, 3, 4, 1, 2]
unique_nums = set(nums)
print("Unique Elements:", unique_nums)

# 5. Advanced Hash Map Operations
# Default values using defaultdict
from collections import defaultdict
hash_map = defaultdict(int)
hash_map['a'] += 1
hash_map['b'] += 2
print("DefaultDict Hash Map:", hash_map)

# Grouping items using hash maps
data = ["apple", "banana", "cherry", "apricot", "blueberry"]
grouped = defaultdict(list)
for item in data:
    grouped[item[0]].append(item)
print("Grouped by First Letter:", dict(grouped))