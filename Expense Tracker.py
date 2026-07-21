# Project 2: Expense Tracker
# DecodeLabs Python Internship

def main():
    total = 0  # Accumulator - starts at zero, outside the loop

    print("Expense Tracker")
    print("Enter an expense amount, or type 'quit' to stop.\n")

    while True:
        user_input = input("Enter expense (or 'quit' to finish): ")

        # Sentinel value check - user wants to stop
        if user_input.lower() == "quit":
            break

        # Defensive coding - handle invalid (non-numeric) input
        try:
            expense = int(user_input)
            total += expense   # Accumulator pattern: total = total + expense
            print(f"Added: {expense}. Running total: {total}\n")
        except ValueError:
            print("Invalid input. Please enter a number.\n")

    print(f"\nFINAL TOTAL: ${total}")

if __name__ == "__main__":
    main()