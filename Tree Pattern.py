# Christmas Tree Pattern

n = 5
for i in range (1, 3):
    print(' ' * (n - i) + '*' * (2 * i - 1))
for i in range (1, 4):
    print(' ' * (n - i) + '*' * (2 * i - 1))
for i in range (1, 5):
    print(' ' * (n - i) + '*' * (2 * i - 1))

# Number Row Pattern

rows = 4
for i in range (1, rows+1):
    for j in range(1, 5):
        print(i-1, end = " ")
    print()