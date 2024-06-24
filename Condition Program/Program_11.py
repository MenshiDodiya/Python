''' Write a program that A school have following rules for
grading system:
take 5 subjects marks from user and calculate its average
below 25 - F
25  to 45 - E
45 to 50 - D
50 to 60 - C
60 to 80 - B
above 80 - A '''

print("Enter marks of subjects")
maths = int(input("Maths: "))
science = int(input("Science: "))
english = int(input("English: "))
hindi = int(input("Hindi: "))
gujarati = int(input("Gujarati: "))
total = maths+science+english+hindi+gujarati
print("Total: ",total)
average = total/5
print("Percentage: ",average)
if average >= 80:
    print("Congratulation!! you have got A Grade")
elif average >= 60 or average <= 79:
    print("Congratualation!! you have got B Grade")
elif average >= 50 or average <= 59:
    print("Congratualation!! you have got C Grade")
elif average >= 45 or average <= 49:
    print(" you have got D Grade")
elif average >= 25 or average <= 44:
    print("you have got E Grade")
elif average <= 25:
    print("you have got F Grade. you have failed in exam")
else:
    print("Enter valid marks")