numbers = list(map(int, input("Enter numbers separated by space: ").split()))

print("Original List:", numbers)

print("Ascending Order:", sorted(numbers))
print("Descending Order:", sorted(numbers, reverse=True))

numbers.reverse()
print("Reversed List:", numbers)