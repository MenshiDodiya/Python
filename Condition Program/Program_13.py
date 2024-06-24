""" Write a program that A student will not be allowed to sit
in an exam if his/her attendance is less than 75%.
Take following input from user
Number of classes held
Number of classes attended.
And print percentage of class attended
Is the student allowed to sit in the exam or not.

Modify the above question to allow a student to sit if
he/she has a medical cause.Ask the user if he/she has a
medical cause or not ( 'Y' or 'N' ) and print accordingly."""

class_held = int(input("Enter number of classes held: "))
attend_class = int(input("Enter how many number of class you have attend: "))
percentage = (attend_class * 100 )/ class_held
print(f"You have attend {percentage} % classes")
if percentage >= 75:
    print("You are allowed to attend the exam")
else:
    print("You are not allowed to attend the exam")

#this condition is for medical cause
ask = input("You have medical cause? -'yes'/'no'  ")
if ask == "yes":
    print("You are not allowed to sit in class due to medical cause.")
else:
    print("you are allowed to sit in class.")