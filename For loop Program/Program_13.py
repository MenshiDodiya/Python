"""Write a program to take integer number from the user
and separate each number and check whether
it is even or odd number from that."""
num = input("Enter any number:")
str = len(num)+1
num = int(num)

for num in range(1,str):
    dig = num % 10
    num = num // 10
    if (dig % 2 == 0):
        print(f"{dig} is even")
    else:
        print(f"{dig} is odd")