#WAP to swapping two numbers without using any other variable

a = int(input("enter first number" ))
b = int(input("enter second numbers" ))
print(f"before swapping a = {a} and b = {b}")
a = a + b
b = a - b
a = a - b
print(f"after swapping a = {a} and b = {b}")