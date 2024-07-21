'''Write a program to print Fibonacci series
0 1 1 2 3 5 8 13 21 34 55 89'''

num = int(input("Enter number to print fibonacci series: "))
n1, n2, = 0, 1
count = 0

print("Fibonacci sequence:")
while count < num:
       print(n1,end= ' ')
       sum = n1 + n2
       n1 = n2
       n2 = sum
       count += 1