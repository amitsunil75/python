# ,2,4,5

sn = int(input('enter the range: start index:'))
en = int(input('enter the range: end index:'))
primeNumbers=[]

for i in range(max(2,sn),en):
    isPrime=True
    for j in range(2,i):
        if i%j==0:
            isPrime=False
            break
            
    if isPrime:
      primeNumbers.append(i)

print(primeNumbers)

