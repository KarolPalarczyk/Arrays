
arr = [1, 2, 3, 4, 5]

print(f"Array: {arr}")
arr[0] = arr[0] - 1
print(f"Array: {arr}") 

arr[-1] = arr[-1] + 4
print(f"Array: {arr}") 

middle_index = len(arr) // 2 
arr[middle_index] = arr[middle_index] * 2
print(f"Array: {arr}") 