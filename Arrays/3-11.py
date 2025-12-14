
def bubbleSort(arr):
  n = len(arr)
  for i in range(n):
    swapped = False
    for j in range(0, n - i - 1):
      if arr[j] > arr[j + 1]:
        temp = arr[j]
        arr[j] = arr[j + 1]
        arr[j + 1] = temp
        swapped = True
    if not swapped:
      break
      
  return arr
def sort_and_print(test_array):
  arr_to_sort = list(test_array) 
  
  print(f"Original Array: {arr_to_sort}")
  sorted_array = bubbleSort(arr_to_sort)
  
  print(f"Sorted Array:   {sorted_array}")
  print("-" * 30)
test_array1 = [64, 34, 25, 12, 22, 11, 90]
test_array2 = [5, 1, 4, 2, 8]
test_array3 = [10, 9, 8, 7, 6, 5]
print("--- Bubble Sort Demonstration ---")
sort_and_print(test_array1)
sort_and_print(test_array2)
sort_and_print(test_array3)