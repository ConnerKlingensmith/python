"""
String manipulation utilities
"""
def reverse_string(text):
    """Reverse a string"""
    return text[::-1]

def capitalize_words(text):
    """Capitalize each word"""
    return text.title()

def count_vowels(text):
    """Count vowels in text"""
    vowels = 'aeiouAEIOU'
    return sum(1 for char in text if char in vowels)
