
def star(n):
  return '*' * n
array_numbers = [2, 6, 4, 9, 7]
print("--- Graphical Array Output ---")
for number in array_numbers:
  asterisks = star(number)
  print(f"{number}: {asterisks}")

print("----------------------------")