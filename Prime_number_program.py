#Write a program to check if the entered number is a prime number or not.
num = int(input("enter number:"))
if num > 1:
    for i in range(2, int(num/2)+1):
        if(num % 1 == 0):
            print(num, "is not prime number")
            break
        else:
            print(num, "is a prime number")
else:
    print(num, "is not prime number")
