# 1. Creating and Initializing Strings
basic_string = "Hello, World!"
multiline_string = """This is a 
multiline string."""
print("Basic String:", basic_string)
print("Multiline String:", multiline_string)

# 2. Accessing Characters in Strings
print("First Character:", basic_string[0])
print("Last Character:", basic_string[-1])

# 3. String Slicing
print("Substring (0:5):", basic_string[0:5])  # "Hello"
print("Substring (7:):", basic_string[7:])    # "World!"

# 4. String Concatenation and Repetition
concatenated = "Hello" + " " + "Python"
print("Concatenated String:", concatenated)

repeated = "Python " * 3
print("Repeated String:", repeated)

# 5. String Methods
print("Uppercase:", basic_string.upper())
print("Lowercase:", basic_string.lower())
print("Title Case:", basic_string.title())
print("Reversed String:", basic_string[::-1])

# 6. Checking String Properties
is_alpha = "Hello".isalpha()  # Only letters
is_digit = "12345".isdigit()  # Only digits
is_space = "   ".isspace()   # Only whitespace
print("Is Alphabetic:", is_alpha)
print("Is Numeric:", is_digit)
print("Is Whitespace:", is_space)

# 7. Searching and Replacing in Strings
search_result = basic_string.find("World")
print("'World' found at index:", search_result)

replaced_string = basic_string.replace("World", "Python")
print("Replaced String:", replaced_string)

# 8. Splitting and Joining Strings
split_string = basic_string.split(", ")
print("Split String:", split_string)

joined_string = "-".join(["Python", "is", "fun"])
print("Joined String:", joined_string)

# 9. Formatting Strings
name = "Alice"
age = 25
formatted = f"My name is {name} and I am {age} years old."
print("Formatted String:", formatted)

# 10. Iterating Through Strings
print("Characters in String:")
for char in basic_string:
    print(char, end=" ")
print()

# 11. Common String Algorithms
# Palindrome check
def is_palindrome(s):
    s = s.lower().replace(" ", "")  # Normalize
    return s == s[::-1]

print("Is 'racecar' a palindrome?:", is_palindrome("racecar"))
print("Is 'hello' a palindrome?:", is_palindrome("hello"))

# Counting Characters
from collections import Counter
char_count = Counter("abracadabra")
print("Character Count:", char_count)