''' Pattern 8
1
2 3
4 5 6
7 8 9 10
'''

num = 1
for row in range(0,4):
    for col in range(0,row+1):
        print(num, end=' ')
        num += 1
    print()
