''' Write a program that a company decided to give a bonus
of 5% to an employee if his/her year service is more than
5 years. Ask users for their salary and year of service and
print the net bonus amount. '''

name = (input("Enter your name: "))
salary = int(input("Enter your salary: "))
year = int(input("Enter how many year you have worked: "))
if year >= 5:
    bonus = salary * 0.05
    print(f"{name} Congratulation!! you will get bonus of ",bonus)
else:
    print(f"{name} you will not get the bonus.")