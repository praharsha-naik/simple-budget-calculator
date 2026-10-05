def get_valid_number(prompt):
    while True:
        try:
            user_input = input(prompt).strip()
            if not user_input:
                print("Input was empty. Please type a number.")
                continue
            value = float(user_input)
            if value < 0:
                print("Value cannot be negative. Please try again.")
                continue
            return value
        except Exception:
            print("Invalid input. Please enter a valid number.")

def run_budget_calculator():
    print("=== Simple Budget Calculator ===")
    
    income = get_valid_number("Enter your total monthly net income: ")
    rent = get_valid_number("Enter housing/rent expenses: ")
    groceries = get_valid_number("Enter grocery expenses: ")
    utilities = get_valid_number("Enter utility bills: ")
    transport = get_valid_number("Enter transport expenses: ")
    entertainment = get_valid_number("Enter entertainment expenses: ")
    
    total_expenses = rent + groceries + utilities + transport + entertainment
    remaining_savings = income - total_expenses
    savings_rate = (remaining_savings / income) * 100 if income > 0 else 0

    print("\n================ RESULTS ================")
    print(f"Total Income:   {income:,.2f}")
    print(f"Total Expenses: {total_expenses:,.2f}")
    print(f"Net Savings:    {remaining_savings:,.2f}")
    print(f"Savings Rate:   {savings_rate:.1f}%")
    print("=========================================")

    if savings_rate >= 20:
        print("Great job! You are hitting your savings target.")
    elif savings_rate > 0:
        print("You are saving money, but try to cut expenses.")
    else:
        print("Warning: Your expenses exceed your income!")

if __name__ == "__main__":
    run_budget_calculator()
