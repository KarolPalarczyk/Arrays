
monthly_expenses = [
    [200, 50, 100],  # Week 1
    [180, 60, 110],  # Week 2
    [220, 55, 105],  # Week 3
    [210, 65, 95]   # Week 4
]
food_total = 0
transport_total = 0
utilities_total = 0
monthly_total = 0

weekly_totals = []

for week_data in monthly_expenses:
    food_total += week_data[0]
    transport_total += week_data[1]
    utilities_total += week_data[2]

    week_sum = sum(week_data)
    weekly_totals.append(week_sum)

    monthly_total += week_sum

print('MONTHLY EXPENSES')
print('----------------')
print(f"Food: {food_total}")
print(f"Transport: {transport_total}")
print(f"Utilities: {utilities_total}")

print('----------------')
print(f"Week 1: {weekly_totals[0]}")
print(f"Week 2: {weekly_totals[1]}")
print(f"Week 3: {weekly_totals[2]}")
print(f"Week 4: {weekly_totals[3]}")

print('----------------')

print(f"TOTAL: {monthly_total}")