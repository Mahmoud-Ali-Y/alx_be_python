monthlyincome = int(input("Enter your monthly income: "))
monthlyexpenses = int(input("Enter your total monthly expenses: "))
MonthlySavings = monthlyincome - monthlyexpenses
ProjectedSavings = int((MonthlySavings * 12) + (MonthlySavings * 12 * 0.05))
print ("Your monthly savings are $", MonthlySavings, ".")
print ("Projected savings after one year, with interest, is: $", ProjectedSavings, ".")