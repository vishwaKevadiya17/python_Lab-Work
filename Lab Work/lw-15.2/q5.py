a = [10, 20, 30, 40, 50]

n = int(input("Enter a number: "))
found = -1

for i in range(len(a)):
    if a[i] == n:
        found = i
        break

if found != -1:
    print("Number found at index:", found)
else:
    print("Not Found")