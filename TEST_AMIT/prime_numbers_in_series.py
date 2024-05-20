startIndex=int(input('enter the start index'))
endIndex=int(input('enter the end index'))
primeNumbers=[]
for i in range(max(2,startIndex),endIndex):
    isPrime=True
    for j in range(2,i):
        if(i%j==0):
            isPrime=False
            break
    if isPrime:
        primeNumbers.append(i)
    else:
        pass

print(primeNumbers)