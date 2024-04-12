# Positional Argument
def addName(firstname):
    print('hello'.capitalize()+' '+str(firstname).capitalize())

addName('amit')
addName('shifana')
# output:
# Hello Amit
# Hello Shifana

def add(a,b):
    result=a+b/a-b
    print(result)

add(2,3)
# output:0.5

# factorial
# n= int(input('enter your number to find factorial:'))
# def fact(n):
#     Fact=1
#     for i in range(1,n+1):
#         Fact*=i
#     return Fact
# result=fact(n)
# print(f'Factorial of {n} is {result}')
# OUTPUT:
# enter your number to find factorial:6
# Factorial of 6 is 720

# ARBITARY ARGUMENT
def arbitory(*args):
    print(args)

arbitory(2,3,4)
# output:(2, 3, 4)

# keyword argument
def keywd(a,b):
    print(a+b)
keywd(a=2,b=2)

# arbitory keyword Argument
def aka(**args):
    print(args)
aka(a=2,b=3,c=4)
# output:{'a': 2, 'b': 3, 'c': 4}
def infom(**info):
    print(f'roll no:{info['rollno']} ,age is {info['age']} and name is {info['name']}')
infom(rollno=2,age=3,name='amit')
infom(rollno=3,age=12,name='shifana')
# output:
# roll no:2 ,age is 3 and name is amit
# roll no:3 ,age is 12 and name is shifana

# default argument
def examStatus(isFailed=True):
    if isFailed:
        print('failed')
    else:
        print('passed')
examStatus()
examStatus(False)
# output:
# failed
# passed

def result(x):
    x=x/2
    x=x+9
    x=x*2
    x=x-2
    x=x+5
    x=x**2
    x=x*10
    x=x+11
    x=x+9
    x=x%25
    return 'finished' ,x
if('finished'==result(2)[0]):
    print(result(2))

# output:('finished', 10.0)