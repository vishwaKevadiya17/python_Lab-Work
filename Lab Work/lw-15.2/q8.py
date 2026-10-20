arr = []

n = int(input("Enter array size: "))

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

print("First element:", arr[0])
print("Last element:", arr[n - 1])
print("Middle element:", arr[n // 2])