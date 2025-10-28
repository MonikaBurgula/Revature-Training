""" Calculations """

from mypackage.interest_calculations import simple_interest
from mypackage.shape_calculations import area_of_rect, area_of_circle

prin= float(input("Enter principal amount: "))
ny= float(input("Enter number of years: "))
roi = float(input("Enter rate of interest: "))

print(f'Simple Interest: {simple_interest(prin=prin, ny=ny, roi=roi)[0]}  '
      f'Amount :{simple_interest(prin=prin, ny=ny, roi=roi)[1]}')

radius= float(input("Enter radius of circle: "))
length= float(input("Enter length of rectangle: "))
brd= float(input("Enter breadth of rectangle: "))

print(f'Area of circle: {area_of_circle(radius=radius)} \n'
      f'Area of rectangle: {area_of_rect(length=length, brd=brd)}')
