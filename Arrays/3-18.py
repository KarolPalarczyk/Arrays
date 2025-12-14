from MyArrays import get_second_largest 
from MyArrays import get_median 
from MyArrays import get_smallest_and_largest 
from MyArrays import array_to_string_minus

# --- Program Execution ---

# 1. Define the sequence of numbers
numbers = [7, 3, 8, 5, 2]

print("--- Array Operations Results ---")
print(f"Numbers: {', '.join(map(str, numbers))}")
print("-" * 30)

# i. Second largest element
second_largest = get_second_largest(numbers)
print(f"Second largest number: {second_largest}")

# iii. Median of numbers
median_value = get_median(numbers)
print(f"Median: {median_value}")

# i. (Alternative part) Smallest and largest number
smallest_largest = get_smallest_and_largest(numbers)
print(f"Smallest and largest number: {smallest_largest[0]}, {smallest_largest[1]}")

# ii. Array elements as a string with minus sign
numbers_as_string = array_to_string_minus(numbers)
print(f"Numbers as a string: {numbers_as_string}")

print("--------------------------------")