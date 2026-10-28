n = int(input("Enter array size: "))

a = []
b = []
c = []

print("Enter array A's elements:")
for i in range(n):
    a.append(int(input()))

print("Enter array B's elements:")
for i in range(n):
    b.append(int(input()))

for i in range(n):
    c.append(a[i] + b[i])

print("Array C is:", c)