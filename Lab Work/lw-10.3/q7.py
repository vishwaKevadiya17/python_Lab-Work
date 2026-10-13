students = [
    {"id": 1, "name": "Alice", "marks": 85},
    {"id": 2, "name": "Bob", "marks": 78}
]

print("Students scoring more than 80 marks:")

for student in students:
    if student["marks"] > 80:
        print(student)