#Write a program to take input from user and
# check the number is palindrome number or not.

num=int(input("Enter number to check whether number is palindrome or not:"))
temp=num
rev=0
while(num>0):
    dig=num%10
    rev=rev*10+dig
    num=num//10
if(temp==rev):
    print(f"{temp} The number is a palindrome!")
else:
    print("The number isn't a palindrome!")
