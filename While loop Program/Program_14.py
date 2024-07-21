"""Write a program to Calculate the sum of digits
of a number given by the user"""
num = int(input("Enter any number: "))
sum = 0
temp = num
while num > 0:
    dig = num % 10
    num = num // 10
    sum = sum + dig
print(f"The sum of a number {temp} = {sum}")