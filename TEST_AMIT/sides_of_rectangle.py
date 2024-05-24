
import math


side1= int(input('input 1:'))
side2= int(input('input 2:'))
side3= int(input('input 3:'))
li=[side1,side2,side3]
li.sort()
if(math.pow(li[2],2) ==(math.pow(li[1],2)+math.pow(li[0],2))):
    print('its side of right angle')
else:
    print('not a side')