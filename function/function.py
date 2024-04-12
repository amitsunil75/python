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
n= int(input('enter your number to find factorial:'))
def fact(n):
    Fact=1
    for i in range(1,n+1):
        Fact*=i
    return Fact
result=fact(n)
print(f'Factorial of {n} is {result}')
# OUTPUT:
# enter your number to find factorial:6
# Factorial of 6 is 720



