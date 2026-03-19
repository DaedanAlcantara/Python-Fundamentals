#Triangle Pattern
height = 5
for i in range(1, height + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()  # Move to the next line after each row

# Diamond Pattern
height = 5
for i in range(1, height + 1):
    print(" " * (height - i) + "*" * (2 * i - 1))
for i in range(height - 1, 0, -1):
    print(" " * (height - i) + "*" * (2 * i - 1))

