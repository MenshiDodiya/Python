''' Pattern 11
A
B C
D E F
G H I J
K L M N O
'''

num = 65
for row in range(0,5):
    for col in range(0,row+1):
        ch = chr(num)
        num = num + 1
        print(ch, end= ' ')
    print()
