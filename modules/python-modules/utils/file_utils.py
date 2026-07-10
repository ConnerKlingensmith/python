"""
File operation utilities
"""

def count_lines(filename):
    """Count lines in a file"""
    try:
        with open(filename, 'r') as f:
            return len(f.readlines())
    except FileNotFoundError:
        return 0

def get_file_size(filename):
    """Get file size in bytes"""
    import os
    try:
        return os.path.getsize(filename)
    except FileNotFoundError:
        return 0
