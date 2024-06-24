""" Write a program to check whether a character is
alphabet, digit or special character. """

alpha = 'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ'
symbol = '!@#$%^&*?'
ch = chr(ord(input("Enter any character = ")))
if ch in alpha:
    print("The character is Alphabet")
elif ch in symbol:
    print("The character is Special character")
else:
    print("The character is Number")