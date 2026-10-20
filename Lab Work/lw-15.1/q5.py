arr = [10, 20, 30, 40, 50]

num = int(input("Enter element to delete: "))

if num in arr:
    arr.remove(num)
    print("Updated list =", arr)
else:
    print("Element not found")