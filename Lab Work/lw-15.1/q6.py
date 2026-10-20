arr = [10, 20, 30, 40, 50]

index = int(input("Enter index: "))
num = int(input("Enter new value: "))

if index >= 0 and index < len(arr):
    arr[index] = num
    print("Updated list =", arr)
else:
    print("Invalid index")