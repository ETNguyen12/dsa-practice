# 1. Creating and Initializing a Hash Set
hash_set = set()

# Adding elements to the hash set
hash_set.add(1)
hash_set.add(2)
hash_set.add(3)
print("Hash Set:", hash_set)

# Attempting to add duplicate elements
hash_set.add(2)  # No effect, as sets do not allow duplicates
print("After Adding Duplicate 2:", hash_set)

# 2. Accessing Elements in a Hash Set
# Checking membership
print("Is 1 in hash_set?:", 1 in hash_set)
print("Is 4 in hash_set?:", 4 in hash_set)

# Removing elements
hash_set.remove(2)
print("After Removing 2:", hash_set)

# Using discard (does not throw an error if the element is absent)
hash_set.discard(4)
print("After Discarding 4:", hash_set)

# 3. Iterating Over a Hash Set
print("Iterating through hash_set:")
for element in hash_set:
    print(element)

# 4. Set Operations
set_a = {1, 2, 3}
set_b = {3, 4, 5}

# Union
print("Union:", set_a | set_b)

# Intersection
print("Intersection:", set_a & set_b)

# Difference
print("Difference (A - B):", set_a - set_b)

# Symmetric Difference
print("Symmetric Difference:", set_a ^ set_b)

# 5. Practical Applications of Hash Sets
# Detecting duplicates in a list
nums = [1, 2, 3, 4, 1, 2]
hash_set = set(nums)
print("Unique Elements:", hash_set)

# Finding common elements in two lists
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
common_elements = set(list1) & set(list2)
print("Common Elements:", common_elements)

# 6. Advanced Usage with Frozensets
# Frozensets are immutable sets
frozen_set = frozenset([1, 2, 3])
print("Frozenset:", frozen_set)

# Frozensets can be used as keys in a dictionary
hash_map = {frozen_set: "immutable set"}
print("Hash Map with Frozenset Key:", hash_map)