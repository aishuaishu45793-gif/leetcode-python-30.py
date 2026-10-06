# 100 Remove duplicates

numbers = [1, 2, 2, 3, 4, 4, 5, 5]

result = []

for number in numbers:
    if number not in result:
        result.append(number)

print("Without duplicates:", result)