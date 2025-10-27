'''Date : 25-10-25
Author : Monika
Description : Amstrong number'''


num = int(input('Enter a number: '))
original_num = num
sum = 0
digits = len(str(num))

while num > 0:
    rem = num % 10
    sum += rem ** digits
    num = num // 10

if sum == original_num:
    print(f'{original_num} is an Armstrong number')
else:
    print(f'{original_num} is not an Armstrong number')
