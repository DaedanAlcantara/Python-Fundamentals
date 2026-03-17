# Selection Structures
# If Statements for Simple Decision Making
age = 18
if age >= 18:
    print("You are an adult.")
# If-Else Statements for Decision Making
# Note: Python uses indentation to define blocks of code
age = 18
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# Elif (Else-If) for Multiple Conditions
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")


# Guess the Output. Where would the compiler go through?
number = 90
if number < 50:
    print("The number is less than 50.")
elif number % 10 == 0:
    print("The number is divisible by 10.")
elif number % 5 == 0:
    print("The number is divisible by 5.")
else:
    print("The number is not less than 50 or divisible by 10.")

# Explanation: The compiler will first check if the number is less than 50, which is false. Then it will check if the number is divisible by 10, which is true. Therefore, it will print "The number is divisible by 10." and skip the remaining conditions.

# Example Implementation: Simple Calculator
num1 = 10
num2 = 5
operation = input("Choose an operation (add, subtract, multiply, divide): ")
if operation == "add":
    result = num1 + num2
    print(f"The result of adding {num1} and {num2} is: {result}")
elif operation == "subtract":
    result = num1 - num2
    print(f"The result of subtracting {num2} from {num1} is: {result}")
elif operation == "multiply":
    result = num1 * num2
    print(f"The result of multiplying {num1} and {num2} is: {result}")
elif operation == "divide":
    if num2 != 0:
        result = num1 / num2
        print(f"The result of dividing {num1} by {num2} is: {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation. Please choose add, subtract, multiply, or divide.")

# Example Implementation: FizzBuzz
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
