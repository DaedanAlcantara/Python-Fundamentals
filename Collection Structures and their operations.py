# Collection Structures
# Operations

# List
my_list = [1, 2, 3, 4, 5]

# Slicing
print(my_list[1:4])

# Adding
my_list.append(90)
my_list.insert(2, 99)

# Removal
my_list.remove(3) # removes value 3
my_list.pop() # removes last element

# Counting
my_list.count(5) # counts occurences of value 5
my_list.index(90) # finds index of value 90

# Sorting
my_list.sort() #sort in ascending
my_list.reverse() # reverses list

#Tuples
my_tuple = (1, 2, 3, 4)
single_element_tuple = (24)

# Slicing
print(my_tuple[1:3])
print(my_tuple[-1])

# Counting
my_tuple.count(2)
my_tuple.index(3)

# Unpacking
a, b, c = (1, 2, 3)
print(a, b, c)

# Dictionaries
my_dict = {"name": "Alice", "age": 25, "city": "New York"}
empty_dict = {}

# Accessing
print(my_dict["name"])  # Alice
print(my_dict.get("age"))  # 25

# Modifying
my_dict["age"] = 26  # Update value
my_dict["job"] = "Engineer"  # Add new key-value pair
print(my_dict.keys())   # Get all keys
print(my_dict.values()) # Get all values
print(my_dict.items())  # Get key-value pairs

# Removing
del my_dict["city"]  # Delete key
removed_value = my_dict.pop("age")  # Remove and return value

