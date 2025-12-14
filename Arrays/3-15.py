# 1. Define the tuple
input_tuple = (10, 20, 30, 40, 50)

# 2. Reverse the tuple
# In Python, slicing with a step of -1 (e.g., [::-1]) reverses an iterable.
# This creates a new reversed tuple.
reversed_tuple = input_tuple[::-1]

# 3. Print the results
print("--- Tuple Reversal Program ---")
print(f"Tuple: {input_tuple}")
print(f"Reverse order: {reversed_tuple}")
print("------------------------------")