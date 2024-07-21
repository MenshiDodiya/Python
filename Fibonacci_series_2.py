'''Write a program to print Fibonacci series
0 1 1 2 4 7 13 24 44 81 149'''

num = int(input("Enter number to print fibonacci series: "))
n1, n2, n3 = 0, 1, 1
count = 0
print("Fibonacci sequence:")
while count < num:
       print(n1,end= ' ')
       sum = n1 + n2 +n3
       n1 = n2
       n2 = n3
       n3 = sum
       count += 1
