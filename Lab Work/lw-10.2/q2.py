# Create a dictionary
student = {
    'name': 'Alice',
    'age': 25,
    'city': 'New York'
}

print("Original dictionary:", student)

# Add a new key-value pair
student['course'] = 'Python'
print("After adding:", student)

# Update an existing value
student['age'] = 26
print("After updating:", student)

# Remove a key-value pair
del student['city']
print("After removing:", student)