
a=int(input('enter a number'))
if(a>0):
   if (a >= 10 and a<=20):print('is betwnn 10 and 20')
   elif(a>20 and a<=50):print(f'{a} between 20 and 50')
   elif(a>50 and a<=100):print(f'{a} between 20 and 100')
   else:
      print(' please enter number betwwen 10 and 100')
else:
  print('invalid input')

