"""Date ; 27-10-25
Author : Monika
Description : Functions with multiple return values """


def calculate(num1, num2, num3):

    total_sum = num1 + num2 + num3
    average = total_sum / 3
    return total_sum, average

student_name = input("Enter a name: ")
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
num3 = int(input("Enter another number: "))

total_sum, average = calculate(num1, num2, num3)

print(f"Student Name: {student_name}")
print(f"Total: {total_sum}  Average: {average:.2f}")


