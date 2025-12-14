
numbers = [15, 8, 31, 47, 2, 19]

total_sum = 0
for number in numbers:
    total_sum = total_sum + number
array_count = len(numbers)
if array_count > 0:
    arithmetic_mean = total_sum / array_count
else:
    arithmetic_mean = 0

print(f"Array: {numbers}")
print("---")
print(f"Total Sum: {total_sum}")
print(f"Number of Elements: {array_count}")
print(f"Arithmetic Mean: {arithmetic_mean}")