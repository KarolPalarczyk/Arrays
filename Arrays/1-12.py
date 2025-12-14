
categories = ["Food", "Transport", "Rent", "Entertainment"]
expenses = [500, 150, 1000, 200]
max_expense = max(expenses)
max_expense_index = expenses.index(max_expense)
most_expensive_category = categories[max_expense_index]
print(f"Expense categories: {categories}")
print(f"Monthly expenses: {expenses}")
print("------------------------------")
print(f"The most expensive category is: {most_expensive_category}")
print(f"The cost was: {max_expense}")