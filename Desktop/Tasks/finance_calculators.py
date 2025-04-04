import math

# Display the menu to the user
print("Investment - to calculate the amount of interest you'll earn on your investment.")
print("Bond - to calculate the amount you'll have to pay on a home loan.")
choice = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()

# Process the user's choice
if choice == "investment":
    # Investment calculator
    print("\nYou have selected the investment calculator.")

    # Get user inputs
    deposit = float(input("Enter the amount of money you are depositing: "))
    interest_rate = float(input("Enter the interest rate (as a percentage, e.g., enter 8 for 8%): "))
    years = int(input("Enter the number of years you plan to invest: "))
    interest_type = input("Enter 'simple' or 'compound' interest: ").lower()

    # Calculate the total amount based on the interest type
    if interest_type == "simple":
        total_amount = deposit * (1 + (interest_rate / 100) * years)
    elif interest_type == "compound":
        total_amount = deposit * math.pow((1 + (interest_rate / 100)), years)
    else:
        print("Invalid interest type entered. Please restart the program.")
        exit()

    # Output the result
    print(f"\nAfter {years} years, your investment will be worth: R{total_amount:.2f}")

elif choice == "bond":
    # Bond repayment calculator
    print("\nYou have selected the bond repayment calculator.")

    # Get user inputs
    present_value = float(input("Enter the present value of the house: "))
    interest_rate = float(input("Enter the interest rate (as a percentage, e.g., enter 8 for 8%): "))
    months = int(input("Enter the number of months you plan to repay the bond: "))

    # Calculate the monthly repayment
    monthly_interest_rate = (interest_rate / 100) / 12
    repayment = (monthly_interest_rate * present_value) / (1 - math.pow((1 + monthly_interest_rate), -months))

    # Output the result
    print(f"\nYour monthly bond repayment will be: R{repayment:.2f}")

else:
    # Handle invalid input
    print("Invalid choice entered. Please restart the program and enter either 'investment' or 'bond'.")


