
temperatures = [
    3, 7, 1, -2, 6, -4, 5, 1, 2, 3, 
    4, -1, 0, 2, -1, -2, 5, -2, 7, 2,
    -1, 4, 1, -4, 2, 3, 6, 7, 5, 7
]
number_of_measurements = len(temperatures)
temp_total = 0
for temp in temperatures:
    temp_total = temp_total + temp
avg_temp = temp_total / number_of_measurements
min_temp = min(temperatures)
max_temp = max(temperatures)
negative_temp_days = 0
i = 0
while i < number_of_measurements:
    if temperatures[i] < 0:
        negative_temp_days += 1
        
    i = i + 1

print('TEMPERATURE REPORT')
print('==================')
print('Month: March')
print(f"Number of measurements: {number_of_measurements}")
print(f"Average temperature in the month: {avg_temp:.2f}")

print(f"Minimum temperature: {min_temp}")
print(f"Maximum temperature: {max_temp}")
print(f"Number of days with negative temperature: {negative_temp_days}")