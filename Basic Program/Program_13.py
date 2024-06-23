#WAP to swap a 2 number using 3rd variable

a = int(input("enter first number" ))
b = int(input("enter second numbers" ))
print(f"before swapping a = {a} and b = {b}")
temp = a
a = b
b = temp
print(f"after swapping a = {a} and b = {b}")