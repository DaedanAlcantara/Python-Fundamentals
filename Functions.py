#Parts of a Function
def get_product (num1: int, num2: int) -> int:
    product = num1 * num2
    return product

# What does the -> int mean in function definition?
# It specifies the return type of the function, indicating that the function will return an integer.
# What does the : int mean in function definition?
# It specifies the type of the parameters, indicating that num1 and num2 should be integers.

# Types of Functions
# Function with Parameters but no Return Value
def greet(name: str) -> None:
    print(f"Hello, {name}! This function does not return any value but asks your name as parameter.")

#Function with no Parameters and no Return Value
def display_prompt() -> None:
    print("This is a prompt without parameters. This function only prints a message and does not return any value.")

# Function with Parameters and Return Value
def get_sum(num1: int, num2: int) -> int:
    print(f"This function asks for two integers as parameters. This function also returns the sum of {num1} and {num2} as return value as:", end=" ")
    return num1 + num2

# Function with no Parameters but Return Value
def get_current_year() -> int:
    import datetime
    print("This function does not ask for any parameters but returns the current year as return value as:", end=" ")    
    return datetime.datetime.now().year

print('\nFunctions with Parameters but no Return Value:')
greet("Alice")

print('\nFunctions with no Parameters and no Return Value:')
display_prompt()

print('\nFunctions with Parameters and Return Value:')
result = get_sum(5, 10)
print(result)

print('\nFunctions with no Parameters but Return Value:')
year = get_current_year()
print(year)

