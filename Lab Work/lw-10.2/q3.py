# Take a list of numbers as input
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

# Convert list into a set
unique_numbers = set(numbers)

# Display unique numbers
print("Unique numbers:", unique_numbers)