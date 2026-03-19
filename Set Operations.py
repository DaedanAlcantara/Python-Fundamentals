
set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1.union(set2))     # {1, 2, 3, 4, 5}
print(set1.intersection(set2)) # {3}
print(set1.difference(set2))   # {1, 2}
print(set2.difference(set1))   # {4, 5}

print(set1 & set2) # Intersection
print(set1 | set2) # Union
print(set1 - set2) # One Sided Difference
print(set2 - set1) # One Sided Difference
print(set1 ^ set2) # Symmetrical Difference


setA = {1, 2, 3, 4}
setB = {4, 5, 6, 9}
# Intersection using loops
print ()
print("Intersection: ", end="")
for item in setA:
        if item in setB:
            print("{", end="")
            print(item, end = " ")  
            print("\b}")

# Union using loops
print("Union: ", end="")
print("{", end="")
for item in setA:
    print(item, end = " ")
for item in setB:
    if item not in setA:
        
        print(item, end = " ")    
print("\b}")

# Symmetrical Difference using Loops

print("Symmetrical Difference: ", end = "")
print("{", end = "")
for item in setA:
    if item in setB:
        continue
    else: print(item, end = " ")
for item in setB:
    if item in setA:
        continue
    else:
        print(item, end=" ")
print("\b}")

# One sided Difference
print("OSD -> setA - setB: ", end = "")
print("{", end = "")
for item in setA:
    if item not in setB:
        print(item, end = " ")
print("\b}")

print("OSD -> setB - setA: ", end= "")
print("{", end = "")
for item in setB:
    if item not in setA:
        print(item, end = " ")
print("\b}")
