import random

print(random.randint(0,100))
print(random.randrange(2,30,2))
mylist=[2,4,56,8]
print(random.choices(mylist))
print(random.choice(mylist))
x = 2
rate_parameter = lambda: x + 1
print(random.expovariate(rate_parameter()))
print(random.random())
print(random.gauss())

random_value=random.randint(1,5)
print(random_value)

i=1
while i<4:
    user_input=int(input(f'enter any random variable b/w 1 and 5 : '))
    if user_input is random_value:
        print('you has won the game')
        break
    else:
        print('try gain')
        i+=1
        continue
else:
    print('you have lost the game')    
        
