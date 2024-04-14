
startIndex= int(input('enter the start index : '))
endIndex= int(input('enter the start index: '))
primeNumber=[]
nonPrimeNumber=[]
if (startIndex and endIndex >0 and startIndex !=endIndex):
    for i in range(max(2,startIndex),endIndex):
        isPrime=True
        for j in range(2,i):
            if i%j==0:
                isPrime=False
                break
                
        if(isPrime):
          primeNumber.append(i)
       
    print(f'these are prime number :{primeNumber}',end=',')
    # print(f'these are non  prime number :{primeNumber}',end=',')

else:
    print('improper range should be index should be graeter than zero and should not be similar')

