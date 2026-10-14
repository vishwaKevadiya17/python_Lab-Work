import random

numbers = []

for i in range(5):
    num = random.randint(1, 100)
    numbers.append(num)

print("List:", numbers)
print("Minimum Value:", min(numbers))
print("Maximum Value:", max(numbers))
print("Sum:", sum(numbers))