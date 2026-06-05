from collections import Counter

# s = "banana"
# counts = Counter(s)
# letters = list(dict.fromkeys(s))
# print(letters)

# counts['b'] = counts.get('b', 0) + 1 

# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}

# a | b    # union: everything in either → {1, 2, 3, 4, 5, 6}
# a & b    # intersection: only in both → {3, 4}
# a - b    # difference: in a but not b → {1, 2}
# a ^ b    # symmetric difference: in exactly one, not both → {1, 2, 5, 6}

# a <= b   # a.issubset(b): is every element of a also in b?
# a >= b   # a.issuperset(b): does a contain all of b?
# a < b    # proper subset: subset AND not equal
# a > b    # proper superset
# a.isdisjoint(b) 

# a |= b   # a.update(b)             — add everything from b into a
# a &= b   # a.intersection_update(b)
# a -= b   # a.difference_update(b)
# a ^= b   # a.symmetric_difference_update(b)

# {1, 2, 3} & [2, 3, 4]          # TypeError
# {1, 2, 3}.intersection([2, 3, 4])   # works → {2, 3}

def capitalize(text: str) -> str:
    punctuation = '.?!'
    capitalized = False
    res = ''
    for i in range(len(text)):
        char = text[i] 
        if not capitalized and char.isalpha():
            res +=  char.upper()
            capitalized = True 
            continue
        elif char in punctuation:
            capitalized = False
        res += char 
    return res
    
print(capitalize('hello my name is Ethan! --123how are you doing today!'))