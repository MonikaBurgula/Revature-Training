'''Date : 25-10-25# for range
Author : Monika
Description : for range'''

# for range:


for x in range(1,10):
    print(x)

# sum of squares:


terms = int(input('Enter a number: '))
sum=0
for num in range(1,terms+1):
    sum+=num*num
print(f'The sum is: {sum}')