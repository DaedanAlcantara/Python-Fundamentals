# Data Types and Variables
# In Python, there are several built-in data types that you can use to store and manipulate data. Here are some of the most common ones:
# 1. **Numeric Types**:
# - `int`: Represents integer values (e.g., 1, 42, -5).
int = 42
# - `float`: Represents floating-point numbers (e.g., 3.14)
float = 3.14
# 2. **String Type**:
# - `str`: Represents a sequence of characters (e.g., "Hello, World!")
str = "Hello, World!"
# 3. **Boolean Type**:
# - `bool`: Represents a value that can be either `True` or `False`.
bool = True
# 4. **List Type**:
# - `list`: Represents an ordered collection of items (e.g., [1, 2, 3])
list = [1, 2, 3]
# 5. **Tuple Type**:
# - `tuple`: Represents an ordered, immutable collection of items (e.g., (1, 2, 3))
tuple = (1, 2, 3)
# 6. **Dictionary Type**:
# - `dict`: Represents a collection of key-value pairs (e.g., {"name":"Alice", "age": 30})
dict = {"name":"Alice", "age": 30}
# 7. **Set Type**:
# - `set`: Represents an unordered collection of unique items (e.g., {1, 2, 3})
set = {1, 2, 3}
# 8. **None Type**:
# - `None`: Represents the absence of a value or a null value.
none = None

# Naming Conventions for Variables:
# - Variable names should start with a letter (a-z, A-Z) or an underscore (_).
# - Variable names can contain letters, digits (0-9), and underscores.
# - Variable names are case-sensitive (e.g., `myVariable` and `myvariable` are different).
# - Variable names should not be a reserved keyword in Python (e.g., `if`, `else`, `for`, etc.).
# - Variable names should be descriptive and meaningful to improve code readability (e.g., `age` instead of `a`).   

# Example of variable naming:
age = 25
first_name = "John"
is_student = True

# Invalid variable names
9age = 25  # Cannot start with a digit
first-name = "John"  # Cannot contain hyphens
is student = True  # Cannot contain spaces
Variable = "This is valid, but not recommended"  # Valid but not recommended due to capitalization
class = "This is invalid because 'class' is a reserved keyword"  # Cannot use reserved keywords