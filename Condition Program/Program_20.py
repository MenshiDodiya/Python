""" Write a program to find max number from three number
using ternary operator. """

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
mx = (num1 if (num1 > num2 and num1 >num3) else
      (num2 if (num2 > num1 and num2 > num3) else num3))
print(f"Largest number among {num1}, {num2} and {num3} is: {mx}")