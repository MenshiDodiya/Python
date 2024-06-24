""" Write a program that a shopkeeper will give a discount of 10%
if the cost of the purchased quantity is more than 1000.
ask user for quantity suppose, one unit will cost 100
judge and print total cost for the user """

Quantity = int(input("Please enter how many item you have purchased: "))
price = Quantity * 100
if price >= 1000:
    print("you are eligible to take discount")
    price = price - (price * 0.1)
    print("you have to pay: ", price)
else:
    print("you are not eligible to take discount.")