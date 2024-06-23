#WAP to swapping three numbers without using any other variable

a = int(input("enter first number" ))
b = int(input("enter second number" ))
c = int(input("enter third number"))
print(f"before swapping a = {a}, b = {b} and c = {c}")
a = a + b + c
c = a - b -c
b = a - b -c
a= a - b - c
print(f"after swapping a = {a}, b = {b} and c = {c}")