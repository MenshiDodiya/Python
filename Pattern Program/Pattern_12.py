''' Pattern 12
E D C B A
E D C B
E D C
E D
E
'''

for row in range(5,-1,-1):
    num = 69
    for col in range(1,row+1):
         print(chr(num), end=' ')
         num -= 1
    print()
