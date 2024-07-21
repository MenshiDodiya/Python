# Write a program to take number from the user and
# check if the number is an Armstrong number or not.

num = int(input("Enter a number to check whether number is armstrong number or not: "))
sum = 0
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")
