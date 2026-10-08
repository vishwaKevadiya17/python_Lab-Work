# Create a list
numbers = [10, 20, 30, 20, 40]
print("Original list:", numbers)

# Convert list into a set and tuple
number_set = set(numbers)
number_tuple = tuple(numbers)

print("List to set:", number_set)
print("List to tuple:", number_tuple)

# Convert tuple into a list
new_list = list(number_tuple)
print("Tuple to list:", new_list)

# Convert set into a list and tuple
set_list = list(number_set)
set_tuple = tuple(number_set)

print("Set to list:", set_list)
print("Set to tuple:", set_tuple)