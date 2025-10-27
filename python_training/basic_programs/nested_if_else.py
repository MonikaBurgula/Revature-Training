'''Date : 25-10-25
Author : Monika
Description : nested if else'''

# Largest of 3

num1 = int(input('Enter a number: '))
num2 = int(input('Enter second number: '))
num3 = int(input('Enter third number: '))


if num1 == num2 == num3:
    print('All numbers are equal')

else :
    if num1 > num2 and num1 > num3:
        print(f'{num1} is greater than {num2} and {num3}')

    elif num2 > num1 and num2 > num3:
        print(f'{num2} is greater than {num1} and {num3}')

    else:
        print(f'{num3} is greater than {num1} and {num2}')
