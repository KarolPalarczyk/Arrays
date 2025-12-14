
def occurs(number, array):
  return number in array
target_array = [15, 38, 7, 23, 14]
array_display = " ".join(map(str, target_array))
print("--- Number Presence Check Program ---")
print(f"Array: {array_display}")
while True:
  try:
    user_input = input("Enter a number to check: ")
    number_to_check = int(user_input)
    break
  except ValueError:
    print("Invalid input. Please enter an integer number.")
is_present = occurs(number_to_check, target_array)
print(f"Number: {number_to_check}")
print(f"Array: {array_display}")

if is_present:
  print(f"Result: number {number_to_check} appears in the array")
else:
  print(f"Result: number {number_to_check} does NOT appear in the array")
  
print("-------------------------------------")