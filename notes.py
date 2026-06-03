from collections import Counter

s = "banana"
counts = Counter(s)
letters = list(dict.fromkeys(s))
print(letters)

counts['b'] = counts.get('b', 0) + 1 