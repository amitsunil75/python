for i in range(0,5):
    print(' '*(5-i)+'* '*i)
row1= int(input('enter row'))
for i in range(1,row1+1):
   for j in range(row1,i,-1):
       print(' ',end='')
   for  k in range(0,i):
       print(i,end='')
   print()