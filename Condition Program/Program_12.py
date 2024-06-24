''' Write a program to take input of the age of 3 people
by user and determine oldest and youngest among them. '''

person1 = int(input("Enter the First person's age: "))
person2 = int(input("Enter the Second person's age: "))
person3 = int(input("Enter the Third person's age: "))

#this condition is to check who is oldest person
if person1 > person2 and person1 > person3:
    print("The first person is Oldest")
elif person2 > person3 and person2 > person1:
    print("The second person is Oldest")
else:
    print("The Third person is Oldest")

#this condition is to check who is youngest person
if person1 < person2 and person1 < person3:
    print("The first person is youngest")
elif person2 < person3 and person2 < person1:
    print("The second person is youngest")
else:
    print("The Third person is youngest")