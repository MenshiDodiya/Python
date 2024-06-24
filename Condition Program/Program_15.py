""" Write a program to check whether an entered character is
lowercase (a to z) or uppercase (A to Z) """

txt = "abcdefghijklmnopqrstuvwxyz"
text = input("Enter any character: ")
if text in txt:
    print("The character is lowercase.")
else:
    print("The character is uppercase.")