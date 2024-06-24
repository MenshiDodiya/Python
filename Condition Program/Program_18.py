''' Write a program if the entered alphabet is in uppercase
then convert it into lowercase and if the entered alphabet
is in lower case than convert it into uppercase '''

ch = chr(ord(input("Enter any alphabet: ")))
if ch.isupper():
    print("Convert it into lower case: ", ch.lower())
elif ch.islower():
    print("convert it into upper case: ", ch.upper())
else:
    print("not an alphabet")