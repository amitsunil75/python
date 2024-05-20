# ev=[]
# for i in range(100,400):
#     if i%2==0:
#         ev.append(i)
# print(ev)
# even_number_list=[]
def is_even_number(num):
    num = str(num)
    for i in num:
        if(int(i)%2==0):
            return num
        
l1=[]  
l2=[100,102,220]
for  i in range(100,400):
     c=is_even_number(i)
     l1.append(c)
    #  if(c == True):
    
print(l1)
