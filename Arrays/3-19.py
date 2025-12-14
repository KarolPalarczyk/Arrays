
array_of_reals = [12.5, 5.0, 18.2, 3.1, 15.0, 9.9, 21.7]
print("--- Element Comparison Program ---")
print(f"Given Array: {array_of_reals}")
while True:
  try:
    user_input = input("Enter a value to compare against (e.g., 10.0): ")
    comparison_value = float(user_input)
    break
  except ValueError:
    print("Invalid input. Please enter a valid real number.")
count_greater = 0
for element in array_of_reals:
  if element > comparison_value:
    count_greater += 1
print(f"\nComparison Value: {comparison_value}")
print(f"Array: {array_of_reals}")
print(f"Result: {count_greater} elements are greater than {comparison_value}.")
print("------------------------------------")