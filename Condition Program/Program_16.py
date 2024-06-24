""" Write a program to check if a year is leap year or not.
if a year is divisible by 4 then it is leap year but
if the year is century year like 2000, 1900, 2100 then
it must be divisible by 400. """

year = int(input("Enter the year:"))
#this condidtion is to check the year is century year or not
if year == 2000 or year == 1900 or year == 2100:
    print("The year is century year")
    if year % 400 == 0:
        print("The year is leap year and century year.")
    else:
        print("The year is not leap year and century year.")
else:
    print("The year is not century year.")
    if year % 4 == 0:
        print("The year is leap year.")
    else:
        print("The year is not leap year.")