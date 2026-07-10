# Method 1: Import entire module
import math_utils
print(math_utils.add(1,2))

# Method 2: Import specific functions
from math_utils import add, multiply
print(add(3,4))
print(multiply(5,6))

# Method 3: Import with alias
import math_utils as mu
print(mu.power(3,3))

# Method 4: IMport everything (not recommended)
from math_utils import *
print(add(7,8))
