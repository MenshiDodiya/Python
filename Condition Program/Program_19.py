""" Write a program to find number is even or odd using
ternary operator """

num = int(input("Enter any number: "))
num_type = 'even' if num % 2 == 0 else 'odd'
print(f"The number {num} is {num_type}")