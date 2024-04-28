class AddNumbers:
    def sum_Numbers(self,a=None,b=None,c=None):
        s=0
        if(a!=None and b!=None and c!=None):
            s=a+b+c
            return s
        elif(a!=None and b!=None):
            s=a+b
            return s
        else:
            return a
        

addNumbers=AddNumbers()
s=addNumbers.sum_Numbers(1,2,3)
print(s)
s=addNumbers.sum_Numbers(1,2)
print(s)
s=addNumbers.sum_Numbers(1)
print(s)
