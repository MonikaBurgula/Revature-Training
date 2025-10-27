"""Date: 27-10-25
Author: Monika
Description: arbitrary keyword arguments"""

def add(**nums) -> dict:
    res=nums['fn']+nums['sn']+nums['tn']
    return res

n1=int(input("enter first number: "))
n2=int(input("enter second number: "))
n3=int(input("enter third number: "))
print(add(fn=n1,sn=n2,tn=n3))

