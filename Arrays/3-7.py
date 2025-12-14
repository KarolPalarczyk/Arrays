
polish_names = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]
longest_name = polish_names[0]
for name in polish_names[1:]:
    if len(name) > len(longest_name):
        longest_name = name
print("Names:", " ".join(polish_names))
print(f"Longest name: {longest_name}")