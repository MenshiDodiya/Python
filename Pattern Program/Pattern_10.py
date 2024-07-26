''' Pattern 10
A
A B
A B C
A B C D
A B C D E
'''

for row in range(5):
    num = 65
    for col in range(row+1):
         print(chr(num), end=' ')
         num += 1
    print()
