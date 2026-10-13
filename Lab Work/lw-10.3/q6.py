students = [
    {"id": 1, "name": "Alice", "marks": 85},
    {"id": 2, "name": "Bob", "marks": 78}
]

students.sort(key=lambda student: student["marks"], reverse=True)

print("Students sorted by marks:")
print(students)