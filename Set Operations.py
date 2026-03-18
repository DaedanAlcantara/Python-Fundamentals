
set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1.union(set2))        # {1, 2, 3, 4, 5}
print(set1.intersection(set2)) # {3}
print(set1.difference(set2))   # {1, 2}
print(set2.difference(set1))   # {4, 5}


list1 = [1, 2, 3, 4]
list2 = [4, 5, 6, 9]
# Intersection using loops
print ()
print("Intersection: ", end="")
for i in range(len(list1)):
    for j in range(len(list2)):
        if list1[i] == list2[j]:
            print("{", end="")
            print(list1[i], end = " ")  
            print("\b}")

# Union using loops
print("Union: ", end="")
print("{", end="")
for i in range(len(list1)):
    print(list1[i], end = " ")
for j in range(len(list2)):
    if list2[j] not in list1:
        
        print(list2[j], end = " ")    
print("\b}")