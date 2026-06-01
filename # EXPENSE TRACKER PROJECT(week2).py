# EXPENSE TRACKER PROJECT

# Initialize total expense
total = 0

print("===== EXPENSE TRACKER =====")
print("Type 'quit' to stop entering expenses.\n")

# Infinite loop
while True:

    expense = input("Enter expense amount: ")

    # Sentinel value to stop loop
    if expense.lower() == "quit":
        break

    # Defensive coding
    try:
        expense = int(expense)

        # Accumulator logic
        total += expense

        print("Expense added successfully!")
        print("Current Total:", total, "\n")

    except ValueError:
        print("Invalid input! Please enter numbers only.\n")

# Final output
print("\n===== FINAL REPORT =====")
print("Total Expenses =", total)
print("Thank you!")
