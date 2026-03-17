# Recursion Functions

def get_GCD_recursive (a, b):
    if b == 0:
        return a
    return get_GCD_recursive(b, a%b)

def factorial_recursive(n):
	if n == 0:
		return 1  
		# Base case: factorial of 0 is 1
	else:
		return n * factorial_recursive(n - 1)  
		# Recursive case: n! = n * (n-1)
		
# Iterative functions

def get_GCD_iterative(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i  
        # Multiply result by each integer from 1 to n
    return result

# Iterative vs Recursive functions
# Iterative functions use loops to repeat a block of code until a condition is met, while recursive functions call themselves with modified arguments until a base case is reached.
# Recursive functions can be more elegant and easier to read, especially for problems that have a natural
# recursive structure (like tree traversal, factorial, Fibonacci), while iterative functions can be more efficient in terms of memory usage and performance for certain problems.

print(get_GCD_iterative(48, 18))  # Output: 6
print(get_GCD_recursive(48, 18))  # Output: 6
print(factorial_iterative(5))     # Output: 120
print(factorial_recursive(5))     # Output: 120