# Take comma-separated numbers as input
numbers = input("Enter numbers separated by commas: ")

# Convert string into a list
number_list = [int(x.strip()) for x in numbers.split(',')]

# Convert list into a set and tuple
number_set = set(number_list)
number_tuple = tuple(number_list)

# Display results
print("List:", number_list)
print("Set:", number_set)
print("Tuple:", number_tuple)