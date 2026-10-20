arr = [10, 20, 30, 40, 50]

num = int(input("Enter element to search: "))

if num in arr:
    index = arr.index(num)
    print("Element found at index", index)
else:
    print("Element not found")