# 99 Second largest number

numbers = [10, 25, 8, 40, 30]

unique_numbers = list(set(numbers))
unique_numbers.sort()

print("Second largest:", unique_numbers[-2])