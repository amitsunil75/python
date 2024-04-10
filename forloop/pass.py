a=4
b=3
for i in range(10):
    if(a==b):
       a=-b
       pass
    else:
      a=b-a
      b=a-b
     
else:
   print(a,b)
# output:-1 -4