
data_tuple = ("Seven", [10, 20, 30], (5, 15, 25))
value_i = data_tuple[0]

print("--- Accessing Nested Elements ---")
print(f"Original Tuple: {data_tuple}")
print("-" * 35)

print(f"i. Value \"Seven\" (Index 0 of the tuple): {value_i}")
list_element = data_tuple[1] 
value_ii = list_element[2]
print(f"ii. Value 30 (Index 1 of the tuple, then Index 2 of the list): {value_ii}")
print("---------------------------------")