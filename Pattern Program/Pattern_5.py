'''    Pattern 5
               *
            *    *
         *    *    *
      *    *    *    *
   *    *    *    *    *
'''
for row in range(5):
    for space in range(5,row,-1):
        print(" ",end='  ')
    for col in range(row+1):
        print("* ",end= '   ')
    print()