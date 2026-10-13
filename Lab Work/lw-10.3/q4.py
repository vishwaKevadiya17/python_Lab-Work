students = [
    {"id": 1, "name": "Alice", "marks": 85},
    {"id": 2, "name": "Bob", "marks": 78}
]

sid = int(input("Enter student ID: "))
new_marks = int(input("Enter new marks: "))

for student in students:
    if student["id"] == sid:
        student["marks"] = new_marks
        break

print("Updated Student List:")
print(students)