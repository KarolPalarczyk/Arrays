
def weekday(n):
    weekdays = ["Monday", "Tuesday", "Wednesday",
                "Thursday", "Friday", "Saturday", "Sunday"]
    if 1 <= n <= 7:
        return weekdays[n - 1]
    else:
        return "Invalid day number"
print(f"Day 1: {weekday(1)}")
print(f"Day 4: {weekday(4)}")
print(f"Day 7: {weekday(7)}")