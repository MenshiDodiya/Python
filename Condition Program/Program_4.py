''' Write a program to take age from user and
check he/she is eligible for voting or not '''

age = int(input("Enter your age: "))
if age >= 18:
    print("you are eligible for voting")
else:
    print("you are not eligible for voting")