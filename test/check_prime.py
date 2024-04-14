number = int(input('enter a number: '))

if number==0 or number==1:
    print('prime nor comaposite')           
else :
 isprime=True
 for i in range(2,number):
    if number%i==0:
        isprime=False
        break

 if isprime:
    print('its prime')
 else:print('not prime')






