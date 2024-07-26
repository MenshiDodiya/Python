''' Pattern 3
* * * * *
* * * *
* * *
* *
*
'''
for row in range(4,-1,-1):
    for col in range(0,row+1):
        print("*",end=' ')
    print()
