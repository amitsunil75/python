myage=int(input('enter the age'))
if(myage<=18 or myage>=90):
    print('you wont  be able to vote')
else:
    print('you are elegible to vote')



number=int(input('enter a number'))
if(number%5==0):
    print('hello')
else:print('bye')
li=[]
for i in range(4):
    age=int(input('enter the age'))
    li.append(age)
li.sort(reverse=True)
print('oldest one ',li[0])

