import math

# Display to the user to choose which calculation they want to do
print("Investment - to calculate the amount of interest you'll earn onyour investment.")
print("Bond - to calculate the amount you'll have to pay on a home loan.")

# Ask for user choice
user_selection = input("either “investment” or “bond” from the menu above to proceed: ").lower()

# When user chooses investment 
if user_selection == "investment":
    # Ask for the investment details from the user
    deposit = float(input("Enter the amount of money your depositing: "))
    interest_rate = float(input("Enter the interest rate as a percentage: ")) /100
    years = float(input("Enter the number of years you plan on investing for: "))
    interest = input("Do you want 'simple' or 'compound' interest? ").lower()

    # Interest rate types and thier calculations
    if interest == "simple":
       # Simple interest formula 𝐴 = 𝑃(1 + 𝑟 × 𝑡)
       total_amount = deposit * (1 + interest_rate * years)
       print(f"Your investment will grow to {total_amount} after {years} years.")
    elif interest == "compound":
       # Compound interest formula 𝐴 = 𝑃(1 + 𝑟)𝑡
       total_amount = deposit * math.pow((1 + interest_rate), years)
       print(f"Your investment will grow to {total_amount} after {years} years.")
    else:
       print("Invalid interest type selected. Please enter 'simple' or 'compound'.")

# When user chooses investment 
if user_selection == "bond":
    # Ask for the investment details from the user
    present_value = float(input("Enter the present value of the house: "))
    interest_rate = float(input("Enter the interest rate as a percentage: ")) /100
    months = int(input("Enter the number of months you plan to take to repay the bond: "))

    monthly_interest_rate = interest_rate / months
    
    #Bond repayment formula repayment = (i * P)/(1 - (1 + i)**(-n))
    monthly_repayments = (monthly_interest_rate * present_value) / (1 - (1 + monthly_interest_rate)**(-months))
    print(f"Your monthly repayment will be {monthly_repayments}")