n = int(input("Enter array size: "))
a = []

for i in range(n):
    x = int(input("Enter element: "))
    a.append(x)

total = 0
for i in a:
    total = total + i

avg = total / n
print("Average of an Array:", avg)