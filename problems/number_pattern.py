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
print('\n')
for i in range(5):
   for j in range(4):
      if(i==0 and j in(0,1,2)) or (i==1 and j in(0,3)) or (i==2 and j in(0,1,2)) or (i==3 and j ==0) or   (i==4 and j ==0):
         print('*',end='')
      else:
         print(' ',end='')
   print()

# ltt='a23b56'
# if(ltt.isnumeric()):

print('\n its is P \n\n ')
for i in range(5):
   for j in range(5):
      if(i==0 and j in (0,4)) or (i==1 and j in (1,3)) or (i==2 and j==2) or ((i==3 and j==2)) or (i==4 and j==2):
         print('*',end='')
      else:
         print(' ',end='')
   print()

print('\n its is Y \n\n ')
for i in range(5):
   for j in range(5):
      if(i==0 and j==2) or (i==1 and j in(1,3)) or (i==1 and j in(1,3)) or(i==2 and j in(0,1,2,3,4)) or (i==3 and j in(0,4)) or (i==4 and j in(0,4)):
          print('*',end='')
      else:
         print(' ',end='')
   print()

print('\n its is A \n\n ')
for i in range(7):
   for j in range(7):
      if(i==0 and j in (0,6)) or (i==1 and j in (0,1,5,6)) or (i==2 and j in (0,2,4,6)) or (i==3 and j in (0,3,6)) or (i==4 and j in (0,6))  :
          print('*',end='')
      else:
         print(' ',end='')
   print()
print('\n its is M \n\n ')
for i in range(5):
   for j in range(5):
      if(i==0 and j in (0,1,2,3,4)) or (i==1 and j==2) or (i==2 and j==2)  or (i==3 and j==2) or(i==4 and j in(0,1,2,3,4)) :
          print('*',end='')
      else:
         print(' ',end='')
   print()


print('\n\n')
for i in range(5):
   for j in range(5):
      if(i==0 and j in (0,1,2,3,4)) or (i==1 and j==2) or (i==2 and j==2)  or (i==3 and j==2)  :
          print('*',end='')
      else:
         print(' ',end='')
   print()