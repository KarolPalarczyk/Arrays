# 1. Define the compare_arrays function
def compare_arrays(array1, array2):
  if len(array1) != len(array2):
    return False
  for i in range(len(array1)):
    if array1[i] != array2[i]:
      return False # Found a mismatch, so they are not the same
  return True

def run_comparison(arr1, arr2):
  """Prints the arrays and the result of the comparison."""
  result = compare_arrays(arr1, arr2)
  arr1_str = " ".join(map(str, arr1))
  arr2_str = " ".join(map(str, arr2))
  comparison_msg = "arrays are the same" if result else "arrays are different"

  print(f"\nArray1: {arr1_str}")
  print(f"Array2: {arr2_str}")
  print(f"Comparison: {comparison_msg}")
  print("-" * 30)
print("--- Array Comparison Tests ---")
run_comparison(["water", "book", "sky"], ["water", "book", "sky"])
run_comparison([True, False], [True, False, True]) # Different length
run_comparison([5, 3, 1], [5, 3, 1])
run_comparison([3, 2, 1], [3, 2]) # Different length
run_comparison([1, 2, 3], [1, 2, 4]) 
run_comparison([1, 2, 3], [3, 2, 1])