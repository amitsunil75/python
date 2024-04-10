# for x in range(1,6):
#    for j in range(1,x+1):
#       print(j,end='')
#    print()

# for i in range(3):

#    for j in range(5):
#       if(i==0 and j==2) or(i==1 and j in(1,2,3)) or(i==2 and j in(0,4)):
#          print('*',end='')
#       else:
#          print(' ',end='')
#    print()      

for i in range(5):
   for j in range(4):
      if(i==0 and j in(0,1,2)) or (i==1 and j in(0,3)) or (i==2 and j in(0,1,2)) or (i==3 and j ==0) or   (i==4 and j ==0):
         print('*',end='')
      else:
         print(' ',end='')
   print()

# ltt='a23b56'
# if(ltt.isnumeric()):