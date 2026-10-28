n = int(input("Enter array size: "))
a = []

for i in range(n):
    x = int(input("Enter element: "))
    a.append(x)

count = 0
for i in a:
    count = count + 1

print("Length of an Array:", count)