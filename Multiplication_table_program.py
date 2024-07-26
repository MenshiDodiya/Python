'''Write a program to take 2 integer input from user and
print all number of table's
eg:- num1 = 3 num2 = 7 print table of 3 4 5 6 7'''

num1 = int(input("Enter any number:"))
num2 = int(input("Enter any number:"))
for row in range(num1, num2+1):
    print(f"multiplication table for:{num1} ")
    for col in range(1,11):
        print(f"{num1} * {col} = {num1 * col}")
    num1 +=1
    print()