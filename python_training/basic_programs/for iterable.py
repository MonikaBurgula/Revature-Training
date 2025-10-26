'''Date : 25-10-25
Author : Monika
Description : for each '''


# for iterable

square=[]
numbers=[10,20,30,40,50]
for num in numbers:
    print(num)
    square.append(num*num)
print(f'list : {square}')

tupsq=tuple(square)
print(f'tuple : {tupsq}')

setsq=set(square)
print(f'set : {setsq}')

