""" Banking Interest Calculations """

from interest_calculations import simple_interest, compound_interest

prin = float(input("Enter the principal amount: "))
ny = float(input("Enter the number of years: "))
roi = float(input("Enter the rate of interest: "))

si, amount = simple_interest(prin=prin, ny=ny, roi=roi)
print(f'SI : {si} Amount : {amount}')

amount = compound_interest(prin=prin, t=ny, roi=roi)
print(f'Amount : {amount}')
