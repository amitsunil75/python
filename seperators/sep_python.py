
print("h","e","l","l","0",sep='*')
# output:h*e*l*l*0
print(12,"May",1997,sep="/")
# output:12/May/1997
print("h","e","l","l","0",end='*')
# output:h e l l 0*

tip=('05','04','2024')
sep='/'
tip= sep.join(tip)
print('\n'+tip)
# output:05/04/2024
print('elephant'.rjust(12,'@'))
# output:@@@@elephant
print('elephant'.ljust(12,'@'))
# output:elephant@@@@+

h='_____helo_____'
print(h.strip('_'))
# output:helo
print(h.rstrip('_'))
# output:_____helo
print(h.lstrip('_'))
# output:helo_____
print(h.partition('helo'))
# output:('_____', 'helo', '_____')
h='_____helo_____'
print(h.rpartition('helo'))
# output:('_____', 'helo', '_____')
print('hello'.replace('hello','hi'))
# output:hi
j='____helo___helo___'
print(j.replace('helo','hi',1))
# output:____hi___helo___
trans=h.maketrans('helo','hili')
print(trans)
# output:{104: 104, 101: 105, 108: 108, 111: 105}
print(h.translate(trans))
# output:_____hili_____
print('hel,lo'.split(','))
# output:['hel', 'lo']
print('hel,lo'.split('e',2))
# output:['h', 'l,lo']
print('helooo\nheloooo'.splitlines())
# output:['helooo', 'heloooo']
xyz='h34567'
yzf=xyz.zfill(20)
print(yzf)
# output:00000000000000h34567
