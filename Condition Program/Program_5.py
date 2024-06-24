''' Write a program to check if the entered alphabet
is vowel or consonant '''

vowel ="aAeEiIoOuU"
ch = chr(ord(input("Enter any alphabet: ")))
if ch in vowel:
    print("The alphabet is vowel")
else:
    print("The alphabet is consonant")