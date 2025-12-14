# --- Start of MyArrays Module Implementation ---

def get_second_largest(arr):
  """
  Returns the second largest element in the array.
  NOTE: This requires the array to be sorted first.
  """
  if len(arr) < 2:
    return None # Not enough elements
    
  # Create a copy and sort it (using Python's built-in sort for simplicity, 
  # as the task focuses on defining the array operations, not re-implementing sort).
  sorted_arr = sorted(arr, reverse=True)
  
  # The second largest element is at index 1 of the descending sorted array
  return sorted_arr[1]

def get_smallest_and_largest(arr):
  """
  Returns a two-element array [smallest, largest] value in an array.
  """
  if not arr:
    return []
    
  # Create a copy and sort it ascendingly
  sorted_arr = sorted(arr)
  
  # Smallest is at index 0, largest is at the last index
  return [sorted_arr[0], sorted_arr[-1]]

def get_median(arr):
  """
  Returns the median of the numbers in the array.
  The median is the middle value in the ordered sequence of numbers.
  NOTE: This requires the array to be sorted first.
  """
  if not arr:
    return None

  # Create a copy and sort it ascendingly
  sorted_arr = sorted(arr)
  n = len(sorted_arr)
  
  # Check if the number of elements (n) is odd or even
  if n % 2 != 0:
    # Odd length: Median is the middle element (e.g., index 2 for 5 elements)
    middle_index = n // 2
    return sorted_arr[middle_index]
  else:
    # Even length: Median is the average of the two middle elements
    # (e.g., indices 2 and 3 for 6 elements)
    mid1 = sorted_arr[n // 2 - 1]
    mid2 = sorted_arr[n // 2]
    # The result is cast to int to match the sample output format
    return int((mid1 + mid2) / 2)

def array_to_string_minus(arr):
  """
  Returns array elements as a string, separated by the minus sign.
  """
  # Convert all elements to strings and join them with '-'
  return "-".join(map(str, arr))

# --- End of MyArrays Module Implementation ---