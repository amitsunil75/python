prm=int(input('enter a number'))

if(prm ==1 or prm==0):
    print('its niether prime or composite')
else:
    isprime=True
    for i in range(2,prm):
        if(prm%i==0):
             isprime=False
             break

    if(isprime):
        print('the number is prime')
    else:
        print('Not A prime number')