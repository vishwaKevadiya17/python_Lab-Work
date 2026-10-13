students = [
    {"id": 1, "name": "Alice", "marks": 85},
    {"id": 2, "name": "Bob", "marks": 78}
]

sid = int(input("Enter student ID to search: "))

for student in students:
    if student["id"] == sid:
        print("Student Details:", student)
        break
else:
    print("Student not found")