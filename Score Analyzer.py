"""
Student Score Analyzer
Calculates average of 5 quiz scores and determines pass/fail
"""

# Create an empty list
scores = [] #Array contains null value; it can be modified to store values later on

# Ask the user to enter 5 scores
for i in range(1, 6):
    score = int(input(f"Enter score {i}: "))
    scores.append(score)

print("\nScores:")
total = 0

# Display scores and compute total
for score in scores:
    print(score)
    total += score

# Compute average
average = total / len(scores)

print(f"\nAverage: {average:.2f}")

# Determine pass or fail
if average >= 75:
    print("Passed")
else:
    print("Failed")