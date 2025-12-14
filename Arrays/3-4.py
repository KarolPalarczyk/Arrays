
numbers = [-15, 8, -31, 47, -2, 19]
maximum_number = numbers[0]
minimum_number = numbers[0]
for number in numbers[1:]:
    if number > maximum_number:
        maximum_number = number
    if number < minimum_number:
        minimum_number = number
print(f"Array: {numbers}")
print("---")
print(f"Maximum number found: {maximum_number}")
print(f"Minimum number found: {minimum_number}")