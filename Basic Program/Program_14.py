#WAP to swap a 3 number using other variable

a = int(input("enter first number" ))
b = int(input("enter second numbers" ))
c = int(input("enter third number" ))
print(f"before swapping a = {a}, b = {b} and c = {c}")
temp = a
a = b
b = c
c = temp
print(f"after swapping a = {a}, b = {b} and c = {c}")