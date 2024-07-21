"""Write a program to take any one number from user
and print its table"""
print("------ Table ------")
num = int(input("Enter any number to get the table: "))
mul = 1
ans = 0
for mul in range(1,11):
    ans = num * mul
    print(f"{num} * {mul} = {ans}")