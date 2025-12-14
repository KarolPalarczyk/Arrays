
array1 = [4, 36, 12, 28, 9, 44, 5]
array2 = [5, 1, 36]
numbers_not_in_second = []
print("--- Array Comparison Program ---")
print(f"First Array: {array1}")
print(f"Second Array: {array2}")
print("------------------------------")

for number in array1:
  if number not in array2:
    numbers_not_in_second.append(number)
print("Numbers from the first array that do not appear in the second array:")
print(numbers_not_in_second) 