students = [
    {"id": 1, "name": "Alice", "marks": 85},
    {"id": 2, "name": "Bob", "marks": 78}
]

sid = int(input("Enter student ID to remove: "))

for student in students:
    if student["id"] == sid:
        students.remove(student)
        break

print("Updated Student List:")
print(students)