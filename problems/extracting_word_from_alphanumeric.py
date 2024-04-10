a='shetty123'
b=[]
for i in a:
    if(i.isalpha()):
        b.append(i)
        c=b[::-1]
print(''.join(c))

# output:yttehs

ad='d1pt1r2dd5'
nm=[]

for i in ad:
    if(i.isnumeric()):
        nm.append(i)
print(nm)
# output:['1', '1', '2', '5']
