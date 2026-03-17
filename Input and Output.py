# Standard Input and Output

print("Hello World!")
name = input("Please insert your name: ")
print("Welcome to Python Programming, " + name + "!\n")

# Stylized Output

print("Daily Records")
print("Entry No.", "Title", "Date Issued", sep = " | ")

print("No.0921", "Beans", "09-12-26", sep = " | ")
print("Today is Monday, ", end="")
print("I like string beans.") 
print("=" * 20, end="\n")


# String Formatting and Escape Sequences

name = "John"
age = 21
gwa = 1.75
amount = 1000000
percent = 0.75
print("\nRecord Tally \nMy name is %s, my age is %d, and my GWA is %.2f." % (name, age, gwa))
print(f"I have earned: Php {amount:,}")
print(f"Goal Achieved: {percent:.2%}")
print("\"The best view comes after the hardest climb\"")

# All formating specifiers:
# {:s} - String (or any object with a string representation, like numbers)
# {:d} - Integers
# {:f} - Floating point numbers
# {:b} - Format number as binary
# {:o} - Format number as octal
# {:.2f} - Floating point numbers with 2 decimal places
# {:,} - Format number with commas as thousands separators
# {:.2%} - Format number as percentage with 2 decimal places
# {:>10} - Right-align text in a field of width 10
# {:<10} - Left-align text in a field of width 10
# {:^10} - Center-align text in a field of width 10
# {:.2e} - Format number in scientific notation with 2 decimal places
# {:.2g} - Format number with 2 significant digits

# Escape Sequences:
# \n - New Line
# \t - Tab
# \\ - Backslash
# \r - Carriage Return
# \b - Backspace
# \' - Single Quote
# \" - Double Quote

