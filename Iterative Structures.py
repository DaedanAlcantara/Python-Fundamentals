#Iterative Structures
# Pre-checking Loop (While Loop)
while True:
    print("This is a while loop.")
    break

# Post-checking Loop (Do-While Loop)
# Note: Python does not have a built-in do-while loop, but it can be simulated
count = 0
loop = True
while loop:
    print("This is a simulated do-while loop.")
    count += 1

    if (count == 3):
        loop = False
        break
    

# Conditioned Loop (For Loop)
for i in range(5, 10, 2):
    print(f"This is iteration number {i}.")

for item in ["apple", "banana", "cherry"]:
    print(f"This is a {item}.")

# Nested Loops 
for i in range(1, 4):
    for j in range(1, 4):
        print(f"Outer loop iteration: {i}, Inner loop iteration: {j}")

# Example Implementation: Diamond Pattern
size = 5
# Upper part of the diamond
for i in range(size):
    print(" " * (size - i - 1) + "*" * (2 * i + 1))
# Lower part of the diamond
for i in range(size - 2, -1, -1):
    print(" " * (size - i - 1) + "*" * (2 * i + 1))

# Example Implementation: Right Triangle Number Pattern
height = 5
for i in range(1, height + 1):
    for j in range (5, i - 1, -1):
        print(j, end=" ")
    print()  # Move to the next line after each row

# Example Implementation: Continuous Number Triangle
rows = 5
num = 1
for i in range(1, rows + 1): #is 1 inclusive or exclusive? inclusive
    for j in range(1, i + 1): #is 1 inclusive or exclusive? inclusive
        print(num, end=" ")
        num += 1
    print()  # Move to the next line after each row

