
array_elements = [2, 3, 2, 5, 8, 1, 9, 8]
frequency_map = {}
for element in array_elements:
  frequency_map[element] = frequency_map.get(element, 0) + 1
unique_elements = []
for element, count in frequency_map.items():
  if count == 1:
    unique_elements.append(element)

print("--- Unique Elements Program ---")
print(f"Array: {array_elements}")
print(f"Unique elements: {unique_elements}")
print("-------------------------------")