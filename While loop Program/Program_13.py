"""Write a program to take integer number from the user
and separate each number and check whether
it is even or odd number from that."""
num = int(input("Enter any number:"))
while num > 0:
    dig = num % 10
    num = num // 10
    if (dig % 2 == 0):
        print(f"{dig} is even")
    else:
        print(f"{dig} is odd")