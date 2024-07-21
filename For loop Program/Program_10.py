#WAP to calculate power using while & for loop.
num = int(input("Enter the number: "))
power = int(input("Enter the number to do power: "))
ans = 1
temp = power

for temp in range(1,temp+1):
        ans = num * ans

print(f"The power of {num} ^ {power} = {ans}")