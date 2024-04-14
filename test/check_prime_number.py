number = int(input('enter a number: '))

if(number==0 or number ==1):
    print('its neither prime or compposite')
else:
    isPrime=True
    for i in range(2,number):
      
      if number%i==0:
        isPrime=False
        break
    if isPrime:
       print('its is a prime number')
    else:
      print('its not prime')