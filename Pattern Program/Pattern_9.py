''' Pattern 9
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
'''

for row in range(5,-1,-1):
    for col in range(1,row+1):
        print(col,end=' ')
    print()
