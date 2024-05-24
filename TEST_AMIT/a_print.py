for i in range(4):
    for j in range(7):
        if(i==0 and j ==3) or(i==1 and j in(2,4)) or(i==2 and j in(1,2,3,4,5,6,7)) or (i==3 and j in(0,6))or(i==4 and j in(0,7)):
            print('*',end='')
        else:
            print(' ',end=' ')
    print()