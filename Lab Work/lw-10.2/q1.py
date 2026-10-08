# Create a set of unique integers
numbers = {10, 20, 30, 40}
print("Original set:", numbers)

# Add a new element
numbers.add(50)
print("After adding:", numbers)

# Remove an element
numbers.remove(20)
print("After removing:", numbers)

# Duplicate elements are not allowed
numbers.add(10)
print("After adding duplicate:", numbers)