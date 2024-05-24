
from functools import reduce


x=[1,2,3,4,5]
y= lambda x:x+1
res=list(filter(y,x))
print(res)
print(list(map(lambda x:x**2,x)))
z=reduce(lambda x,y:x+y,x)
print(z)
print(reduce(lambda x,y:x if x>y else y,x))