"""Write a program to take two inputs from user and do
addition and multiplication of the between numbers of
that number.
#Ex: num1 = 5 Num2 = 10 / 5+6+7+8+9+10=45
#Then addition = 45, Multiplication = 151200"""
num1 = int(input("Enter number 1 = "))
num2 = int(input("Enter number 2 = "))
sum = 0
mul = 1
temp = num1

for num1 in range(num1,num2+1):
    mul = mul * num1
    sum = sum + num1

print(f"The addition between {temp} to {num2} are = {sum}")
print(f"The multiplication between {temp} to {num2} are = {mul}")