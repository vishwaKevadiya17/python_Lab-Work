arr = [25, 10, 45, 5, 30]

maximum = arr[0]
minimum = arr[0]

for i in arr:
    if i > maximum:
        maximum = i

    if i < minimum:
        minimum = i

print("Maximum =", maximum)
print("Minimum =", minimum)