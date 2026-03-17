# Basic Operators

# Unary Operators
x = 5
print(-x)  # Negation
print(+x)  # Identity

# Binary Operators
# Math Operators
a = 10
b = 3
print(a + b)  # Addition
print(a - b)  # Subtraction
print(a * b)  # Multiplication
print(a / b)  # Division
print(a % b)  # Modulus
print(a ** b)  # Exponentiation
print(a // b)  # Floor Division

# Logic Operators
p = True
q = False
print(p and q)  # Logical AND
print(p or q)   # Logical OR
print(not p)    # Logical NOT

# Relational Operators
x = 5
y = 10
print(x == y)  # Equal to
print(x != y)  # Not equal to
print(x > y)   # Greater than
print(x < y)   # Less than
print(x >= y)  # Greater than or equal to
print(x <= y)  # Less than or equal to

# Assignment Operators
x = 5
x += 3  # Equivalent to x = x + 3
print(x)
x -= 2  # Equivalent to x = x - 2
print(x)
x *= 4  # Equivalent to x = x * 4
print(x)
x /= 2  # Equivalent to x = x / 2
print(x)
x %= 3  # Equivalent to x = x % 3
print(x)
x **= 2  # Equivalent to x = x ** 2
print(x)
x //= 2  # Equivalent to x = x // 2
print(x)

# Guess the Output
ans = not(not(not(not(not(not(not(not(not(not(not(True)))))))))))
print(ans)  # Output: False