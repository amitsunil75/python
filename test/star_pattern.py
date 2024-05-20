# for i in range(5,0,-1):
#     print('*'*i)


for i in range(5):
    for j in range(5):
        if (i==0 and j in (0,1,2,3,4)) or (i==1 and j==2) or (i==2 and j==2) or (i==3 and j==2) or (i==4 and j in(0,1,2,3,4)):
            print('*',end='')
        else:
            print(' ',end='')
    print()        