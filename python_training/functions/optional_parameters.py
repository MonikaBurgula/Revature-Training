'''Date: 27-10-25
Author: Monika
Description: Optional parameters'''


def add(n1,n2,n3=0,n4=0):
    res=n1+n2+n3+n4
    return n1+n2+n3+n4
n1=int(input('Enter a number: '))
n2=int(input('Enter another number: '))
n3=int(input('Enter another number: '))
n4=int(input('Enter another number: '))
print(add(n1,n2,n3))
print(add(n1,n2,n3,n4))
print(add(n1,n2))


