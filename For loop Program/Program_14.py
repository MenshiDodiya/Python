"""Write a program to Calculate the sum of digits
of a number given by the user"""
num = input("Enter any number: ")
str = len(num)+1
num = int(num)
sum = 0
temp = num

for num in range(1,str):
    dig = num % 10
    num = num // 10
    sum = sum + dig

print(f"The sum of a number {temp} = {sum}")