
li=[2,3,4,5,5,55,100,200]
ab=[i for i in li]
print(ab)
ab=[i for i in li if i%2==0 ]
print(ab)
ab=[i for i in li if i%2!=0 ]
print(ab)
name='nija amit'
aj=[i.upper() for i in name ]
print(''.join(map(str,aj)))
