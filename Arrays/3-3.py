
original_array = [8, 2, 5, 1, 9]
squared_array = [x ** 2 for x in original_array]
print("Array:", end=" ")
print(*original_array)

print("2nd power:", end=" ")
print(*squared_array)