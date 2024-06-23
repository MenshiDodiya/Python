# print the ouput of this operation (!(!(45==67) && (45<89) && !(78>=45))

a = (not(not(45 == 67) and  (45 < 89) and  not(78 >= 45)))
#           T                   T               F
print(a)