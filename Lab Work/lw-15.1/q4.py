arr = [10, 20, 30, 40, 50]

num = int(input("Enter new element: "))
pos = int(input("Enter position: "))

arr.insert(pos - 1, num)

print("Updated list =", arr)