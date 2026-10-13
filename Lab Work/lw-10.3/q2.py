students = [
    {"id": 1, "name": "Alice", "marks": 85},
    {"id": 2, "name": "Bob", "marks": 78}
]

sid = int(input("Enter student ID: "))
name = input("Enter student name: ")
marks = int(input("Enter student marks: "))

new_student = {"id": sid, "name": name, "marks": marks}
students.append(new_student)

print("Updated Student List:")
print(students)