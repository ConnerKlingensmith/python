# Import modules from package
from utils import string_utils
from utils import file_utils

# Use string utilities
text = "hello world"
print(f"Original: {text}")
print(f"Reversed: {string_utils.reverse_string(text)}")
print(f"Capitalized: {string_utils.capitalize_words(text)}")
print(f"Vowel count: {string_utils.count_vowels(text)}")

# Use file utilities
print(f"\nLines in math_utils.py: {file_utils.count_lines('math_utils.py')}")
print(f"Size: {file_utils.get_file_size('math_utils.py')} bytes")
