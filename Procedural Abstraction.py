"""
=============================================================
  CHAPTER 7 REVIEWER: Procedural Abstraction — Functions
  Batangas State University — ACP Final Exam Reviewer
=============================================================
  TOPICS COVERED:
    1. What are Functions & Why Use Them
       (Modularity, Reusability, Maintainability)
    2. Defining & Calling a Function
    3. Formal vs Actual Parameters
    4. The return Keyword
    5. Functions with No Parameters
    6. Functions with No Parameters but With Return Values
    7. Functions with Parameters and No Return Values (Void)
    8. Functions with Parameters AND Return Values
    9. Lambda Functions (anonymous functions)
       — map(), filter(), reduce()
   10. Recursive Functions

   DRY Rule = Don't Repeat Yourself
   If you find yourself writing the same code more than once,
    it's a sign you should use a function to avoid repetition.

  HOW TO USE:
    Run this file in IDLE, VS Code, or any Python interpreter.
    Each section prints its output to the console with
    clear labels so you can follow along easily.
=============================================================
"""

from functools import reduce


print("=" * 62)
print("  CHAPTER 7 REVIEWER: Procedural Abstraction — Functions")
print("=" * 62)


# ─────────────────────────────────────────────
# SECTION 1: WHY USE FUNCTIONS?
# Key ideas:
#   Modularity    → divide program into separate parts
#   Reusability   → same code used in different scenarios
#   Maintainability → easier to understand and modify
#   def keyword   → used to define a function
#   Function body must be INDENTED
# ─────────────────────────────────────────────
print("\n── SECTION 1: Why Use Functions? ──────────────────────")
print("""
  Functions let you:
    ✔ Modularity     → break code into separate, focused parts
    ✔ Reusability    → call the same function many times
    ✔ Maintainability→ fix or update one place instead of many

  Syntax:
    def function_name(parameters):
        # function body (indented)
        return value   # optional
""")


# ─────────────────────────────────────────────
# SECTION 2: DEFINING & CALLING A FUNCTION
# Key ideas:
#   def        → keyword to define a function
#   result     → function name (your choice)
#   (a, b)     → parameters (inputs)
#   return sum → sends the result back to the caller
#   result(1,1)→ calling the function (actual parameters)
# ─────────────────────────────────────────────
print("\n── SECTION 2: Defining & Calling a Function ───────────")

def result(a, b):
    """Returns the sum of a and b."""
    total = a + b
    return total

# Calling the function
sum_value = result(1, 1)
print(f"  result(1, 1)  → {sum_value}")
print(f"  result(5, 3)  → {result(5, 3)}")
print(f"  result(10, 20)→ {result(10, 20)}")

print("""
  Breakdown:
    def result(a, b):  ← def keyword + name + parameters
        total = a + b  ← function body (indented)
        return total   ← return sends value back

    sum_value = result(1, 1)  ← calling: 1 goes to a, 1 goes to b
""")


# ─────────────────────────────────────────────
# SECTION 3: FORMAL vs ACTUAL PARAMETERS
# Key ideas:
#   Formal parameters → variables in the function DEFINITION
#   Actual parameters → values passed during the function CALL
# ─────────────────────────────────────────────
print("\n── SECTION 3: Formal vs Actual Parameters ─────────────")

def greet(name, greeting):          # name, greeting = FORMAL parameters
    print(f"  {greeting}, {name}!")

greet("Juan", "Hello")              # "Juan", "Hello" = ACTUAL parameters
greet("Maria", "Good morning")
greet("Pedro", "Kamusta")

print("""
  FORMAL parameters → placeholders defined in the function header
  ACTUAL parameters → real values passed when calling the function
""")


# ─────────────────────────────────────────────
# SECTION 4: THE return KEYWORD
# Key ideas:
#   return sends a value back to the caller
#   Without return (or plain 'return'), function returns None
#   A function can only return ONE value
#   (but that value can be a tuple containing many things)
# ─────────────────────────────────────────────
print("\n── SECTION 4: The return Keyword ──────────────────────")

def add(x, y):
    return x + y        # returns the result

def say_hello():
    print("  Hello from say_hello()!")
    # No return statement → returns None

returned_value = add(4, 6)
print(f"  add(4, 6) returned: {returned_value}")

none_value = say_hello()
print(f"  say_hello() returned: {none_value}  (None = no return)")

# Returning multiple values via tuple
def min_max(numbers):
    return min(numbers), max(numbers)   # returns a tuple

lo, hi = min_max([3, 1, 9, 5, 7])
print(f"\n  min_max([3,1,9,5,7]) → min={lo}, max={hi}")


# ─────────────────────────────────────────────
# SECTION 5: FUNCTIONS WITH NO PARAMETERS
# Key ideas:
#   Defined with empty parentheses: def func_name():
#   Performs a task without needing external data
#   Called with empty parentheses too: func_name()
# ─────────────────────────────────────────────
print("\n── SECTION 5: Functions with No Parameters ────────────")

def greet_user():
    """Displays a greeting — no input needed."""
    print("  Hello, user! Welcome to CodeChum!")

def show_menu():
    """Displays a menu."""
    print("  ┌─ MENU ────────────┐")
    print("  │ 1. Add record      │")
    print("  │ 2. View records    │")
    print("  │ 3. Exit            │")
    print("  └───────────────────┘")

def main_section5():
    greet_user()      # calling no-parameter function
    show_menu()

main_section5()


# ─────────────────────────────────────────────
# SECTION 6: FUNCTIONS WITH NO PARAMETERS BUT WITH RETURN VALUES
# Key ideas:
#   No input needed, but still computes and returns a value
#   Common use: generating data (random numbers, timestamps)
#   import random → lets you use randint()
# ─────────────────────────────────────────────
print("\n── SECTION 6: No Parameters but With Return Values ────")

import random

def generate_random_number():
    """Generates and returns a random number 0–99."""
    random_number = random.randint(0, 99)
    return random_number

def get_greeting():
    """Returns a greeting string."""
    return "Hello, World! Welcome to Python."

random_num = generate_random_number()
print(f"  generate_random_number() → {random_num}")
print(f"  get_greeting()           → {get_greeting()}")

print("""
  Note: The function does NOT need input, but it hands back
  a value using 'return' that the caller can store and use.
""")


# ─────────────────────────────────────────────
# SECTION 7: FUNCTIONS WITH PARAMETERS AND NO RETURN VALUES (VOID)
# Key ideas:
#   Accepts arguments but does NOT return a value
#   These are called "void functions"
#   No return statement — just performs an action (e.g. print)
#   Simple rule:
#     Just showing something? → use print()
#     Producing a value?      → use return
# ─────────────────────────────────────────────
print("\n── SECTION 7: Parameters but No Return Values (Void) ──")

def greet_user_by_name(name):
    """Prints a personalized greeting. Returns nothing."""
    print(f"  Hello, {name}! Welcome.")

def display_square(number):
    """Prints the square of a number. Returns nothing."""
    print(f"  The square of {number} is {number ** 2}")

def print_line(char="-", length=40):
    """Prints a separator line."""
    print("  " + char * length)

greet_user_by_name("Juan")
greet_user_by_name("Maria")
display_square(5)
display_square(9)
print_line()
print_line("=", 30)

print("""
  These functions TAKE INPUT but produce no return value.
  They perform an action (printing) and stop.
""")


# ─────────────────────────────────────────────
# SECTION 8: FUNCTIONS WITH PARAMETERS AND RETURN VALUES
# Key ideas:
#   The most common type of function in real programs
#   Takes input → processes it → sends a result back
# ─────────────────────────────────────────────
print("\n── SECTION 8: Parameters AND Return Values ────────────")

def calculate_area(length, width):
    """Returns the area of a rectangle."""
    return length * width

def is_passing(grade):
    """Returns True if grade is 75 or above."""
    return grade >= 75

def celsius_to_fahrenheit(celsius):
    """Converts Celsius to Fahrenheit."""
    return (celsius * 9 / 5) + 32

area = calculate_area(5, 3)
print(f"  calculate_area(5, 3)          → {area}")
print(f"  is_passing(80)                → {is_passing(80)}")
print(f"  is_passing(60)                → {is_passing(60)}")
print(f"  celsius_to_fahrenheit(100)    → {celsius_to_fahrenheit(100)}°F")


# ─────────────────────────────────────────────
# SECTION 9: LAMBDA FUNCTIONS
# Key ideas:
#   Also called ANONYMOUS FUNCTIONS
#   Defined with 'lambda' keyword — no def, no function name
#   Syntax:  lambda arguments: expression
#   Restricted to a SINGLE expression
#   Best for short, simple operations
#   Commonly used with map(), filter(), reduce()
# ─────────────────────────────────────────────
print("\n── SECTION 9: Lambda Functions ────────────────────────")

# Basic lambda
add_lambda = lambda x, y: x + y

square     = lambda x: x ** 2
is_even    = lambda x: x % 2 == 0
#lamda vs def: lambda is for simple, one-line functions; def is for anything complex or reused


print(f"  add_lambda(5, 3)  → {add_lambda(5, 3)}")
print(f"  square(7)         → {square(7)}")
print(f"  is_even(4)        → {is_even(4)}")
print(f"  is_even(7)        → {is_even(7)}")

# --- map() ---
# Applies a lambda to EACH item in an iterable
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(f"\n  map()  — square each: {numbers} → {squared}")



# --- filter() ---
# Creates a new list of items where lambda returns True
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"  filter() — keep evens: {numbers} → {evens}")

# --- reduce() ---
# Applies a rolling computation across the list
product = reduce(lambda x, y: x * y, numbers)
print(f"  reduce() — multiply all: {numbers} → {product}")

print("""
  Lambda Limitations:
    ✘ Cannot contain multiple statements or complex logic
    ✘ Can only have ONE expression
    ✘ Overuse makes code harder to read
    ✔ Use def for anything complex or reused
""")


# ─────────────────────────────────────────────
# SECTION 10: RECURSIVE FUNCTIONS
# Key ideas:
#   A function that CALLS ITSELF during execution
#   Must have a BASE CASE — a condition that STOPS recursion
#   Without a base case → infinite recursion (runtime error!)
#   Useful for self-similar or repetitive problems
#     e.g. factorial, Fibonacci, tree traversal
# ─────────────────────────────────────────────
print("\n── SECTION 10: Recursive Functions ────────────────────")

def factorial(n):
    """
    Calculates n! (n factorial) recursively.
    Base case:      n == 0 → return 1
    Recursive case: n * factorial(n - 1)
    """
    if n == 0:
        return 1            # BASE CASE — stops recursion
    else:
        return n * factorial(n - 1)  # RECURSIVE CASE

def fibonacci(n):
    """
    Returns the nth Fibonacci number recursively.
    Base cases:      n==0 → 0,  n==1 → 1
    Recursive case:  fibonacci(n-1) + fibonacci(n-2)
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Factorial demos
print("  Factorial:")
for i in range(7):
    print(f"    factorial({i}) = {factorial(i)}")

# Fibonacci demos
print("\n  Fibonacci sequence (first 8 terms):")
fib_seq = [fibonacci(i) for i in range(8)]
print(f"    {fib_seq}")

print("""
  IMPORTANT:
    Every recursive function MUST have a base case.
    Without it → infinite recursion → RuntimeError!

  Trace of factorial(3):
    factorial(3)
      → 3 * factorial(2)
           → 2 * factorial(1)
                → 1 * factorial(0)
                     → 1  (BASE CASE)
    Result: 3 * 2 * 1 * 1 = 6
""")


# ─────────────────────────────────────────────
# QUICK REFERENCE CHEAT SHEET
# ─────────────────────────────────────────────
print("""
╔══════════════════════════════════════════════════════════════╗
║      CHAPTER 7 CHEAT SHEET — Functions Quick Reference       ║
╠══════════════════════════════════════════════════════════════╣
║  TYPE                     PARAMETERS    RETURN VALUE         ║
║  No param, no return         ( )           None              ║
║  No param, with return       ( )           value             ║
║  With param, no return    (a, b, ...)      None  (void)      ║
║  With param, with return  (a, b, ...)      value             ║
╠══════════════════════════════════════════════════════════════╣
║  LAMBDA  →  lambda args: expression                          ║
║    map()    → applies lambda to EACH item                    ║
║    filter() → keeps items where lambda is True               ║
║    reduce() → rolling computation across all items           ║
╠══════════════════════════════════════════════════════════════╣
║  RECURSION                                                   ║
║    Must have a BASE CASE to stop calling itself              ║
║    Without base case → infinite recursion → ERROR            ║
╠══════════════════════════════════════════════════════════════╣
║  SIMPLE RULE:                                                ║
║    Just showing something? → print() inside, no return       ║
║    Producing a value?      → use return                      ║
╚══════════════════════════════════════════════════════════════╝
""")

print("✅ Chapter 7 Reviewer Complete! Good luck on your exam!")