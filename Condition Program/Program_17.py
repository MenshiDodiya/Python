""" Write a program to Ask user to enter age, gender ( M or F ),
( Y or N ) and then using following rules print their
place of service.
if employee is female, then she will work only in urban areas.
if employee is a male and age is in between 20 to 40
then he may work in anywhere
if employee is male and age is in between 40 to 60
then he will work in urban areas only.
And any other input of age should print "ERROR" """

name = input("Enter your name: ")
age = int(input("Enter your age: "))
gender = input("Enter your gender(F/M): ")
if gender == "f":
    print(f"The {name} will work in urban area only.")
else:
    if (age >= 20 and age <= 40):
        print(f"The {name} will work anywhere.")
    elif (age >= 40 and age <= 60):
        print(f"The {name} will work in urban area only.")
    else:
        print("Give a vaild age.")
print("Thank you")