"""take two integer inputs from the user.
first calculate the sum of two then product of two.
finally print the sum and product of both abtained results"""

num1 = int(input("Enter number 1:- "))
num2 = int(input("Enter number 2:- "))
add = num1 + num2
product = num1 * num2
print("The sum of 2 numbers is:- ",add)
print("The product of 2 number is:- ",product)
result1 = add + product
result2 = add * product
print("The sum of add and product is:- ",result1)
print("The product of add and product is:- ",result2)