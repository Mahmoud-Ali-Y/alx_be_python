monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))
monthly_Savings = monthly_income - monthly_expenses
ProjectedSavings = int((monthly_Savings * 12) + (monthly_Savings * 12 * 0.05))
print ("Your monthly savings are $", monthly_Savings, ".")
print ("Projected savings after one year, with interest, is: $", ProjectedSavings, ".")