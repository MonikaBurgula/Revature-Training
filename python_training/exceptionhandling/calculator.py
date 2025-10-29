from Calculations import Calculations
from AgeNotEnoughError import AgeNotEnoughError

n1 = int(input('Enter n1:'))
n2 = int(input('Enter n2:'))
age = int(input('Enter age:'))
calc = Calculations(n1,n2)

calc = Calculations(n1, n2)

print(f'{calc.add()}')
print(f'{calc.sub()}')
print(f'{calc.mul()}')
#print(f'{calc.div()}')

try:
    if n2==0 :
        raise ZeroDivisionError('n2 is zero')
    if age < 18:
        raise AgeNotEnoughError('You are minor')

except ZeroDivisionError as zde:
    print(f'{zde}')

except AgeNotEnoughError as anee:
    print(f'{anee}')

else:
    try:
        l1=[1,5,7,3]
        val=l1[2]
        res = calc.div()

    except ZeroDivisionError as zde:
        print(f' {zde} - Division by zero')

    except IndexError as ie:
        print(f' {ie} - Index out of range')

    except:
        print('Something went wrong')

    else:
        print(res)

    finally:
        print('done!!')
