#WAP to calculate power using while & for loop.
num = int(input("Enter the number: "))
power = int(input("Enter the number to do power: "))
ans = 1
temp = power
while temp > 0:
    ans = num*ans
    temp -=1
print(f"The power of {num} ^ {power} = {ans}")