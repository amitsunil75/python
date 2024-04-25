# class Triangle:
#     def trisides(self,side1=0,side2=0,side3=0):
        
#         if(side1==side2 and side2==side3 and side3==side1 ):
#             print('Equilateral Triangle')
#             print('Perimeter:{}'.format(3*side1))
#             print('area:{}'.format(0.433*side1*side1))
#         elif(side1==side2 and side2!=side3 and side3!=side1 ):
#             print('Isosceles Triangle')
#             print('Perimeter:{}'.format(side1+side2))
#         else:
#             print('Scalene Triangle:')
#             print('Perimeter:{}'.format(side1+side2+side3))

# t=Triangle()
# t.trisides(2,2,2)
# t.trisides(2,2,3)
# t.trisides(2,3,4)

class Triangle:
    def trisides(self,side1=0,side2=0,side3=None):
        
        if(side1==side2 and side3==None):
            print('Equilateral Triangle')
            print('Perimeter:{}'.format(3*side1))
            print('area:{}'.format(0.433*side1*side1))
        elif(side1==side2 and side2!=side3 and side3!=side1 ):
            print('Isosceles Triangle')
            print('Perimeter:{}'.format(side1+side2))
        else:
            print('Scalene Triangle:')
            print('Perimeter:{}'.format(side1+side2+side3))

t=Triangle()
t.trisides(2,2)
t.trisides(2,2,3)
t.trisides(2,3,4)


class ClosedGeomerticFigures:
    def Shape(self,length=None,breath=None):
        if(length is breath or breath==None):
            print('square')
            print('preimeter:{}'.format(4*length))
            print('Area:{}'.format(length*length))

        else:
            print('rectangle')
            print('preimeter:{}'.format(2*(length+breath)))
            print('area:{}'.format(length*breath))


c=ClosedGeomerticFigures()
c.Shape(2)
c.Shape(2,2)
c.Shape(2,3)