
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
# output:elephant@@@@
