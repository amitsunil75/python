from functools import reduce


x=0
y=1
for i in range(10):
    print(y)
    res= x+y
    x=y
    y=res
print(y)

# fib = lambda n:reduce(lambda x,_:x+[x[-2]]+x[-1],range(n-2),[0,1])


from functools import reduce

fib = lambda n: reduce(lambda x, _: x + [x[-2] + x[-1]], range(n-2), [0, 1])
print(fib(5))
